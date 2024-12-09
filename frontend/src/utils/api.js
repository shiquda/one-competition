import axios from 'axios';
import { getAccessToken, getRefreshToken, setTokens, clearTokens } from './auth';
import router from '@/router';
import showNotification from '@/utils/showNotification';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || '/api',
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
    },
});

// 请求拦截器，添加 Authorization 头
api.interceptors.request.use(
    (config) => {
        const token = getAccessToken();
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// 响应拦截器，处理 401 错误（令牌过期）
api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        if (error.response && error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            const refreshToken = getRefreshToken();
            if (refreshToken) {
                try {
                    const response = await axios.post('/auth/refresh/', {
                        refresh: refreshToken,
                    });
                    const newAccessToken = response.data.access;
                    setTokens({ access: newAccessToken, refresh: refreshToken });
                    originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;
                    return api(originalRequest);
                } catch (refreshError) {
                    clearTokens();
                    router.push('/login');
                    showNotification({
                        message: '登录已过期，请重新登录。',
                        type: 'error',
                        duration: 3000,
                    });
                    return Promise.reject(refreshError);
                }
            } else {
                clearTokens();
                router.push('/login');
                showNotification({
                    message: '请先登录。',
                    type: 'error',
                    duration: 3000,
                });
            }
        }
        return Promise.reject(error);
    }
);

export default api;