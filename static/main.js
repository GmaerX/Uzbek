import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { autoAnimatePlugin } from '@formkit/auto-animate/vue'
import './assets/index.css';

createApp(App).use(store).use(router).use(autoAnimatePlugin).mount('#app')
