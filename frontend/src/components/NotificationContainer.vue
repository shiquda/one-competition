<template>
  <div
    class="fixed top-5 right-5 flex flex-col space-y-2 z-50"
    id="notification-container"
  >
    <Notification
      v-for="notif in notificationStore.notifications"
      :key="notif.id"
      :message="notif.message"
      :type="notif.type"
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
