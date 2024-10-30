<template>
  <div class="max-w-lg mx-auto p-6 bg-gray-100 rounded-lg shadow">
    <h1 class="text-2xl font-bold mb-4 text-center">注册</h1>
    <form>
      <div class="mb-4">
        <label for="username" class="block text-sm font-medium text-gray-700"
          >用户名</label
        >
        <input
          type="text"
          id="username"
          placeholder="请输入用户名"
          v-model="username"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        />
      </div>

      <div class="mb-4">
        <label for="email" class="block text-sm font-medium text-gray-700"
          >邮箱</label
        >
        <input
          type="email"
          id="email"
          placeholder="请输入邮箱"
          v-model="email"
          @input="validateEmail"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        />
        <span class="text-red-500 text-sm mt-1 block" v-if="emailError">{{
          emailError
        }}</span>
      </div>

      <div class="mb-4">
        <label for="password" class="block text-sm font-medium text-gray-700"
          >密码</label
        >
        <input
          type="password"
          id="password"
          placeholder="密码位数为8-32位，且包含大小写字母和数字"
          v-model="password"
          @input="validatePassword"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        />
        <span class="text-red-500 text-sm mt-1 block" v-if="passwordError">{{
          passwordError
        }}</span>
      </div>

      <button
        type="submit"
        @click.prevent="register"
        :disabled="hasErrors"
        class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        注册
      </button>
      <p class="mt-4 text-center text-sm">
        已经有账号？<router-link
          to="/login"
          class="text-blue-500 hover:underline"
          >登录</router-link
        >
      </p>
    </form>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue';
  import showNotification from '@/utils/showNotification';
  import { useRouter } from 'vue-router';

  const router = useRouter(); // 获取 router 实例

  const username = ref('');
  const email = ref('');
  const password = ref('');

  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,32}$/;
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  const passwordError = ref('');
  const emailError = ref('');

  const validatePassword = () => {
    if (!passwordRegex.test(password.value)) {
      passwordError.value = '密码位数为8-32位，且包含大小写字母和数字';
    } else {
      passwordError.value = ''; // 清空错误提示
    }
  };

  const validateEmail = () => {
    if (!emailRegex.test(email.value)) {
      emailError.value = '请输入正确的邮箱';
    } else {
      emailError.value = ''; // 清空错误提示
    }
  };

  const register = async () => {
    validatePassword();
    validateEmail();
    if (passwordError.value || emailError.value) return;
    // TODO: 注册请求
    console.log(username.value, email.value, password.value);
    // test
    const success = true;
    if (success) {
      showNotification({
        message: '注册成功！将自动跳转至登录页面',
        type: 'success',
        duration: 2000,
      });
      setTimeout(() => {
        router.push('/login'); // 使用 router 实例进行路由跳转
      }, 2500);
    } else {
      showNotification({
        message: '注册失败！请稍后再试',
        type: 'error',
        duration: 2000,
      });
    }
  };
</script>
