import { reactive } from 'vue';

const notificationStore = reactive({
    notifications: [],
    addNotification(notification) {
        notification.id = Date.now() + Math.random(); // 生成唯一ID
        this.notifications.push(notification);
    },
    removeNotification(id) {
        const index = this.notifications.findIndex(notif => notif.id === id);
        if (index !== -1) {
            this.notifications.splice(index, 1);
        }
    },
});

export default notificationStore;
