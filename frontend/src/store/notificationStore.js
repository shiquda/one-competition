import { reactive } from 'vue';

const notificationStore = reactive({
    notifications: [],
    addNotification({ message, type = 'info', duration = 3000, autoDismiss = true }) {
        const notification = {
            id: Date.now() + Math.random(), // 生成唯一ID
            message,
            type,
            duration,
            autoDismiss,
        };
        this.notifications.push(notification);
        if (autoDismiss) {
            setTimeout(() => {
                this.removeNotification(notification.id);
            }, duration);
        }
    },
    removeNotification(id) {
        const index = this.notifications.findIndex(notif => notif.id === id);
        if (index !== -1) {
            this.notifications.splice(index, 1);
        }
    },
});

export default notificationStore;
