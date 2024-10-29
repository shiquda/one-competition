<template>
  <transition name="slide-fade">
    <div v-if="visible" class="notification" :class="type">
      <div class="icon">
        <i v-if="type === 'info'" class="fas fa-info-circle"></i>
        <i v-else-if="type === 'success'" class="fas fa-check-circle"></i>
        <i v-else-if="type === 'error'" class="fas fa-times-circle"></i>
        <i
          v-else-if="type === 'warning'"
          class="fas fa-exclamation-triangle"
        ></i>
      </div>
      <span class="message">{{ message }}</span>
      <button @click="close">×</button>
    </div>
  </transition>
</template>

<script setup>
  import { ref, watch } from 'vue';

  const props = defineProps({
    message: {
      type: String,
      required: true,
    },
    duration: {
      type: Number,
      default: 3000, // 默认消失时间为 3000 毫秒
    },
    autoDismiss: {
      type: Boolean,
      default: true, // 默认自动消失
    },
    type: {
      type: String,
      default: 'info', // 通知类型（info, success, error, warning等）
    },
  });

  const emits = defineEmits(['close']);

  const visible = ref(true);

  // 关闭通知
  const close = () => {
    visible.value = false;
    emits('close');
  };

  // 自动消失处理
  watch(
    () => props.autoDismiss,
    newValue => {
      if (newValue && visible.value) {
        setTimeout(close, props.duration);
      }
    },
    { immediate: true }
  );
</script>

<style scoped>
  .notification {
    display: flex;
    align-items: center;
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 16px 24px;
    border-radius: 4px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    z-index: 1000;
    transition: opacity 0.5s ease, transform 0.5s ease;
    min-width: 300px;
  }

  .icon {
    margin-right: 12px;
    flex-shrink: 0;
    font-size: 20px;
  }

  .icon i {
    /* 图标颜色继承父元素颜色 */
    color: inherit;
  }

  .message {
    flex: 1;
    color: white;
    font-size: 14px;
  }

  button {
    background: none;
    border: 1px solid white;
    color: white;
    cursor: pointer;
    margin-left: 12px;
    font-size: 16px;
    flex-shrink: 0;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0;
  }

  .notification.info {
    background-color: #2196f3;
  }

  .notification.success {
    background-color: #4caf50;
  }

  .notification.error {
    background-color: #f44336;
  }

  .notification.warning {
    background-color: #ff9800;
  }
</style>
