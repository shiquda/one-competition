import notificationStore from '@/store/notificationStore.js';

const showNotification = ({ message, type = 'info', duration = 3000, autoDismiss = true }) => {
    notificationStore.addNotification({ message, type, duration, autoDismiss });
};

export default showNotification;