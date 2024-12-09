import api from '@/utils/api';

const TOKEN_KEY = 'authToken';
const REFRESH_TOKEN_KEY = 'refreshToken';
const USERNAME_KEY = 'username';

export const getAccessToken = () => {
    return localStorage.getItem(TOKEN_KEY);
};

export const getRefreshToken = () => {
    return localStorage.getItem(REFRESH_TOKEN_KEY);
};

export const setTokens = ({ access, refresh }) => {
    localStorage.setItem(TOKEN_KEY, access);
    localStorage.setItem(REFRESH_TOKEN_KEY, refresh);
};

export const clearTokens = () => {
    localStorage.removeItem(TOKEN_KEY);
    localStorage.removeItem(REFRESH_TOKEN_KEY);
};

export const isAdmin = () => {
    const userType = localStorage.getItem('userType');
    return !!getAccessToken() && userType === 'admin';
};

export const getUsername = () => {
    return localStorage.getItem(USERNAME_KEY);
};


