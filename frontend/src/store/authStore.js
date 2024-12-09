import { defineStore } from 'pinia';
import { getAccessToken, clearTokens, isAdmin, getUsername } from '@/utils/auth.js';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        isLoggedIn: !!getAccessToken(),
        isAdmin: isAdmin(),
        username: getUsername(),
    }),
    actions: {
        login() {
            this.isLoggedIn = true;
            this.isAdmin = isAdmin();
            this.username = getUsername();
        },
        logout() {
            this.isLoggedIn = false;
            this.isAdmin = false;
            this.username = '';
            clearTokens();
        },
    },
}); 