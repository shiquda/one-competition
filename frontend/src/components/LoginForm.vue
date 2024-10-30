<template>
  <div class="max-w-md mx-auto p-6 bg-gray-100 rounded-lg shadow">
    <h1 class="text-2xl font-bold mb-4 text-center">登录</h1>
    <form>
      <div class="mb-4">
        <label for="username" class="block text-sm font-medium text-gray-700"
          >用户名/邮箱</label
        >
        <input
          type="text"
          id="username"
          placeholder="请输入用户名或邮箱"
          v-model="username"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        />
      </div>

      <div class="mb-4">
        <label for="password" class="block text-sm font-medium text-gray-700"
          >密码</label
        >
        <input
          type="password"
          id="password"
          placeholder="请输入密码"
          v-model="password"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        />
        <span class="text-red-500 text-sm mt-1 block" v-if="passwordError">{{
          passwordError
        }}</span>
      </div>

      <button
        type="submit"
        @click.prevent="login"
        class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition-colors"
      >
        登录
      </button>
      <p class="mt-4 text-center text-sm">
        还没有账号？<router-link
          to="/register"
          class="text-blue-500 hover:underline"
          >注册</router-link
        >
      </p>
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import showNotification from '@/utils/showNotification';
  import { useRouter } from 'vue-router';

  const router = useRouter();

  const username = ref('');
  const password = ref('');

  const passwordError = ref('');

  const login = () => {
    console.log(username.value, password.value);

    // test
    const success = true;
    if (success) {
      showNotification({
        message: '登录成功！将自动跳转至首页',
        type: 'success',
        duration: 2000,
      });
      setTimeout(() => {
        router.push('/'); // 使用 router 实例进行路由跳转
      }, 2500);
    } else {
      showNotification({
        message: '登录失败！请稍后再试',
        type: 'error',
        duration: 3000,
      });
    }
  };
</script>
