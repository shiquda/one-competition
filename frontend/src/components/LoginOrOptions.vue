<template>
  <div class="ml-auto">
    <template v-if="isLoggedIn">
      <!-- 用户已登录,显示一些功能按钮 -->
      <UserOptionsWidget />
    </template>
    <template v-else>
      <!-- 用户未登录,显示登录按钮 -->
      <button
        @click="login"
        class="flex items-center space-x-2 bg-blue-500 text-white px-3 py-2 rounded-md hover:bg-blue-600 transition-colors"
      >
        <i class="fa-solid fa-user"></i>
        <span>登录</span>
      </button>
    </template>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import UserOptionsWidget from '@/components/UserOptionsWidget.vue';

  const router = useRouter();

  // 用一个响应式变量来跟踪登录状态
  const isLoggedIn = ref(false);

  // 检查用户登录状态的函数
  const checkLoginStatus = () => {
    // TODO: 发送请求检查用户登录状态,根据响应设置 isLoggedIn 的值
    // 这里暂时写死,假设用户已登录
    isLoggedIn.value = true;
  };

  // 组件挂载时检查登录状态
  onMounted(() => {
    checkLoginStatus();
  });

  const login = () => {
    router.push('/login');
  };
</script>

<style scoped>
  /* 样式通过 Tailwind CSS 完成，无需额外样式 */
</style>
