import { createRouter, createWebHistory } from 'vue-router';
import About from '@/views/About.vue';
import Submit from '@/views/Submit.vue';
import Home from '@/views/Home.vue';
import CompetitionDetail from '@/views/CompetitionDetail.vue';
import NotFound from '@/views/NotFound.vue';
import Login from '@/views/Login.vue';
import Register from '@/views/Register.vue';
import UserCenter from '@/views/UserCenter.vue'; // 新增


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
        path: '/submit',
        name: 'Submit',
        component: Submit
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
        component: UserCenter // 新增的个人中心页面
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
    history: createWebHistory(),
    routes
});

export default router;
