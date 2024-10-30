<template>
  <div class="user-options-widget">
    <template v-if="isLoggedIn">
      <!-- 用户已登录,显示一些功能按钮 -->
      <UserOptionsWidget />
    </template>
    <template v-else>
      <!-- 用户未登录,显示登录按钮 -->
      <i class="fa-solid fa-user"></i>
      <HeaderButton @click="login">登录</HeaderButton>
    </template>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import UserOptionsWidget from '@/components/UserOptionsWidget.vue';
  import HeaderButton from '@/components/HeaderButton.vue';

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
  .user-options-widget {
    display: flex;
    align-items: center;
    margin-left: auto;
  }
</style>
