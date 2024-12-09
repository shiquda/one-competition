<template>
  <div class="ml-auto">
    <template v-if="authStore.isLoggedIn">
      <!-- 用户已登录,显示一些功能按钮 -->
      <UserOptionsWidget />
    </template>
    <template v-else>
      <!-- 用户未登录,显示登录按钮 -->
      <button
        @click="login"
        class="flex items-center space-x-2 bg-gray-500 text-white px-3 py-2 rounded-md hover:bg-blue-600 transition-colors"
      >
        <i class="fa-solid fa-user"></i>
        <span>登录</span>
      </button>
    </template>
  </div>
</template>

<script setup>
  import { useRouter } from 'vue-router';
  import UserOptionsWidget from '@/components/UserOptionsWidget.vue';
  import { useAuthStore } from '@/store/authStore.js';

  const router = useRouter();
  const authStore = useAuthStore();

  const login = () => {
    router.push('/login');
  };
</script>

<style scoped>
  /* 样式通过 Tailwind CSS 完成，无需额外样式 */
</style>
