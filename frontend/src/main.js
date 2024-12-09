import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia';

// 引入 Tailwind CSS
import '@/assets/tailwind.css'

// 引入 Font Awesome CSS
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/js/all.js';

// 引入 vue-cal 的样式文件
import 'vue-cal/dist/vuecal.css';

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);
app.mount('#app');