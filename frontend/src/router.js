import { createRouter, createWebHistory } from 'vue-router';
import About from '@/views/About.vue';
import Submit from '@/views/Submit.vue';
import Home from '@/views/Home.vue';
import CompetitionDetail from '@/views/CompetitionDetail.vue';
import NotFound from '@/views/NotFound.vue';
import Login from '@/views/Login.vue';

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