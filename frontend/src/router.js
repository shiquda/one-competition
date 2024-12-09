import { createRouter, createWebHistory } from 'vue-router';
import About from '@/views/About.vue';
import Submit from '@/views/Submit.vue';
import Home from '@/views/Home.vue';
import CompetitionDetail from '@/views/CompetitionDetail.vue';
import NotFound from '@/views/NotFound.vue';
import Login from '@/views/Login.vue';
import Register from '@/views/Register.vue';
import UserCenter from '@/views/UserCenter.vue';
import Admin from '@/views/Admin.vue';
import { getAccessToken } from '@/utils/auth';
import { useAuthStore } from '@/store/authStore.js';
import showNotification from '@/utils/showNotification';

const routes = [
    {
        path: '/index.html',
        redirect: '/'
    },
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        component: About
    },
    {
        path: '/admin',
        name: 'Admin',
        component: Admin,
        meta: { requiresAuth: true, isAdmin: true }
    },
    {
        path: '/submit',
        name: 'Submit',
        component: Submit,
        meta: { requiresAuth: true }
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/personal-center',
        name: 'UserCenter',
        component: UserCenter,
        meta: { requiresAuth: true }
    },
    {
        path: '/competition/:id',
        name: 'CompetitionDetail',
        component: CompetitionDetail
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: NotFound
    }
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
});

// 路由守卫
router.beforeEach((to, from, next) => {
    const authStore = useAuthStore();
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
    const isAdmin = to.matched.some(record => record.meta.isAdmin);
    const token = getAccessToken();
    const isLoggedIn = authStore.isLoggedIn;

    if (requiresAuth && !token) {
        next('/login');
    } else if (isAdmin) {
        const userType = localStorage.getItem('userType');
        if (userType === 'admin') {
            next();
        } else {
            next('/');
            showNotification({
                message: '您没有访问该页面的权限。',
                type: 'error',
                duration: 3000,
            });
        }
    } else if (requiresAuth && !isLoggedIn) {
        next('/login');
    } else {
        next();
    }
});

export default router;
