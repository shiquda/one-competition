<template>
  <form class="max-w-4xl w-full mx-auto p-6 bg-gray-100 rounded-lg shadow" @submit.prevent="register">
    <h1 class="text-2xl font-bold mb-4 text-center">注册</h1>

    <div class="mb-4">
      <label for="username" class="block text-sm font-medium text-gray-700">用户名</label>
      <input
        type="text"
        id="username"
        placeholder="请输入用户名"
        v-model="username"
        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        required
      />
    </div>

    <div class="mb-4">
      <label for="email" class="block text-sm font-medium text-gray-700">邮箱</label>
      <input
        type="email"
        id="email"
        placeholder="请输入邮箱"
        v-model="email"
        @input="validateEmail"
        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        required
      />
      <span class="text-red-500 text-sm mt-1 block" v-if="emailError">{{ emailError }}</span>
    </div>

    <div class="mb-4">
      <label for="password" class="block text-sm font-medium text-gray-700">密码</label>
      <input
        type="password"
        id="password"
        placeholder="密码位数为8-32位，且包含大小写字母和数字"
        v-model="password"
        @input="validatePassword"
        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        required
      />
      <span class="text-red-500 text-sm mt-1 block" v-if="passwordError">{{ passwordError }}</span>
    </div>

    <button
      type="submit"
      :disabled="hasErrors"
      class="mt-6 w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
    >
      提交
    </button>
    <p class="mt-4 text-center text-sm">
      已经有账号？
      <router-link to="/login" class="text-blue-500 hover:underline">登录</router-link>
    </p>
  </form>
</template>

<script setup>
import { ref, computed } from 'vue';
import api from '@/utils/api';
import { setTokens } from '@/utils/auth';
import showNotification from '@/utils/showNotification';
import { useRouter } from 'vue-router';

const router = useRouter();

const username = ref('');
const email = ref('');
const password = ref('');
const emailError = ref('');
const passwordError = ref('');

const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,32}$/;
const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

const validatePassword = () => {
  if (!passwordRegex.test(password.value)) {
    passwordError.value = '密码位数为8-32位，且包含大小写字母和数字';
  } else {
    passwordError.value = '';
  }
};

const validateEmail = () => {
  if (!emailRegex.test(email.value)) {
    emailError.value = '请输入正确的邮箱';
  } else {
    emailError.value = '';
  }
};

const hasErrors = computed(() => {
  return (
    passwordError.value ||
    emailError.value ||
    !username.value ||
    !password.value ||
    !email.value
  );
});

const register = async () => {
  validatePassword();
  validateEmail();
  if (passwordError.value || emailError.value) return;

  try {
    const response = await api.post(`/auth/register/`, {
      username: username.value,
      password: password.value,
      email: email.value,
    });

    console.log(response.data);

    const { message, refresh, token, user_type, username: returnedUsername } = response.data;
    setTokens({ access: token, refresh });
    localStorage.setItem('username', returnedUsername);
    localStorage.setItem('userType', user_type);
    // 打印localStorage中的内容
    console.log(localStorage);

    showNotification({
      message: '注册成功！将自动跳转至首页',
      type: 'success',
      duration: 2000,
    });

    setTimeout(() => {
      router.push('/');
    }, 2000);
  } catch (error) {
    console.log(error);
    const errorMessage = error.response?.data?.error || '注册失败，请稍后重试';
    showNotification({
      message: errorMessage,
      type: 'error',
      duration: 3000,
    });
  }
};
</script>