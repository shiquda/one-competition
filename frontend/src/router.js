import { createRouter, createWebHistory } from 'vue-router';
import About from '@/views/About.vue';
import Submit from '@/views/Submit.vue';

const routes = [
    {
        path: '/',
        name: 'About',
        component: About
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
        path: '/index.html',
        redirect: '/'
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;