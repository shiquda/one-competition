<!-- TODO: 修复进出动画与间隔不一致问题 -->
<template>
  <transition
    enter-active-class="transition ease-out duration-300 transform"
    enter-from-class="opacity-0 translate-y-4"
    enter-to-class="opacity-100 translate-y-0"
    leave-active-class="transition ease-in duration-300 transform"
    leave-from-class="opacity-100 translate-y-0"
    leave-to-class="opacity-0 translate-y-4"
  >
    <div :class="notificationClasses" class="mb-4 w-full max-w-sm">
      <div class="flex items-center mr-3">
        <i v-if="type === 'info'" class="fas fa-info-circle text-blue-500"></i>
        <i
          v-else-if="type === 'success'"
          class="fas fa-check-circle text-green-500"
        ></i>
        <i
          v-else-if="type === 'error'"
          class="fas fa-times-circle text-red-500"
        ></i>
        <i
          v-else-if="type === 'warning'"
          class="fas fa-exclamation-triangle text-yellow-500"
        ></i>
      </div>
      <span class="flex-1 break-words">{{ message }}</span>
      <button @click="close" class="ml-4 text-white font-bold">
        <i class="fas fa-times"></i>
      </button>
    </div>
  </transition>
</template>

<script setup>
  import { defineProps, defineEmits, ref, watch } from 'vue';

  const props = defineProps({
    message: {
      type: String,
      required: true,
    },
    type: {
      type: String,
      default: 'info',
    },
  });

  const emits = defineEmits(['close']);

  const notificationClasses = ref('');

  watch(
    () => props.type,
    newType => {
      notificationClasses.value = `flex items-center p-4 rounded shadow-lg ${
        newType === 'info'
          ? 'bg-blue-700 text-white'
          : newType === 'success'
          ? 'bg-green-700 text-white'
          : newType === 'error'
          ? 'bg-red-700 text-white'
          : newType === 'warning'
          ? 'bg-yellow-700 text-white'
          : 'bg-gray-700 text-white'
      }`;
    },
    { immediate: true }
  );

  const close = () => {
    emits('close');
  };
</script>

<style scoped>
  /* 确保文本不会影响通知的宽度 */
  span {
    word-wrap: break-word;
  }
</style>
