import { createRouter, createWebHistory } from 'vue-router';
import About from '@/views/About.vue';
import Submit from '@/views/Submit.vue';
import Home from '@/views/Home.vue';
import CompetitionDetail from '@/views/CompetitionDetail.vue';

const routes = [
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
        path: '/competition/:id',
        name: 'CompetitionDetail',
        component: CompetitionDetail
    },
    {
        path: '/index.html',
        redirect: '/'
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;