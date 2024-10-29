<template>
  <div class="notification-container">
    <Notification
      v-for="notif in notificationStore.notifications"
      :key="notif.id"
      :message="notif.message"
      :type="notif.type"
      :duration="notif.duration"
      :autoDismiss="notif.autoDismiss"
      @close="removeNotification(notif.id)"
    />
  </div>
</template>

<script setup>
  import Notification from './Notification.vue';
  import notificationStore from '@/store/notificationStore.js';

  const removeNotification = id => {
    notificationStore.removeNotification(id);
  };
</script>

<style scoped>
  .notification-container {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
    display: flex;
  }
</style>
