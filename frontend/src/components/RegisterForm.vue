<template>
  <div class="max-w-md mx-auto p-6 bg-white rounded-lg shadow">
    <form @submit.prevent="register">
      <h2 class="text-2xl font-bold mb-4 text-center">注册</h2>

      <div class="mb-4">
        <label for="username" class="block text-gray-700">用户名</label>
        <input
          type="text"
          id="username"
          v-model.trim="username"
          @input="validateUsername"
          class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
          required
        />
        <span class="text-red-500 text-sm mt-1 block" v-if="usernameError">{{
          usernameError
        }}</span>
      </div>

      <div class="mb-4">
        <label for="email" class="block text-gray-700">邮箱</label>
        <input
          type="email"
          id="email"
          v-model.trim="email"
          @input="validateEmail"
          class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
          required
        />
        <span class="text-red-500 text-sm mt-1 block" v-if="emailError">{{
          emailError
        }}</span>
      </div>

      <div class="mb-4">
        <label for="password" class="block text-gray-700">密码</label>
        <input
          type="password"
          id="password"
          v-model="password"
          @input="validatePassword"
          class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
          required
        />
        <span class="text-red-500 text-sm mt-1 block" v-if="passwordError">{{
          passwordError
        }}</span>
      </div>

      <div class="mb-4">
        <label for="confirm-password" class="block text-gray-700"
          >确认密码</label
        >
        <input
          type="password"
          id="confirm-password"
          v-model="confirmPassword"
          @input="validateConfirmPassword"
          class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
          required
        />
        <span
          class="text-red-500 text-sm mt-1 block"
          v-if="confirmPasswordError"
          >{{ confirmPasswordError }}</span
        >
      </div>

      <button
        type="submit"
        :disabled="isRegistering"
        class="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-500 disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        {{ isRegistering ? '注册中...' : '注册' }}
      </button>

      <p class="mt-4 text-center text-sm">
        已有账号？
        <router-link to="/login" class="text-blue-500 hover:underline"
          >登录</router-link
        >
      </p>
    </form>
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue';
  import api from '@/utils/api';
  import { setTokens } from '@/utils/auth';
  import showNotification from '@/utils/showNotification';
  import { useRouter } from 'vue-router';
  import { useAuthStore } from '@/store/authStore.js';

  const router = useRouter();
  const authStore = useAuthStore();
  const isRegistering = ref(false);

  const username = ref('');
  const email = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  const usernameError = ref('');
  const emailError = ref('');
  const passwordError = ref('');
  const confirmPasswordError = ref('');

  const usernameRegex = /^[a-zA-Z0-9_-]{3,16}$/;
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,32}$/;

  const validateUsername = () => {
    if (!username.value) {
      usernameError.value = '用户名不能为空';
    } else if (!usernameRegex.test(username.value)) {
      usernameError.value =
        '用户名3-16个字符，可包含字母、数字、下划线和短横线';
    } else {
      usernameError.value = '';
    }
  };

  const validateEmail = () => {
    if (!email.value) {
      emailError.value = '邮箱不能为空';
    } else if (!emailRegex.test(email.value)) {
      emailError.value = '请输入有效的邮箱地址';
    } else {
      emailError.value = '';
    }
  };

  const validatePassword = () => {
    if (!password.value) {
      passwordError.value = '密码不能为空';
    } else if (!passwordRegex.test(password.value)) {
      passwordError.value = '密码8-32位，包含大小写字母和数字';
    } else {
      passwordError.value = '';
    }
  };

  const validateConfirmPassword = () => {
    if (!confirmPassword.value) {
      confirmPasswordError.value = '请确认您的密码';
    } else if (password.value !== confirmPassword.value) {
      confirmPasswordError.value = '密码不匹配';
    } else {
      confirmPasswordError.value = '';
    }
  };

  const hasErrors = computed(() => {
    return (
      !username.value ||
      !email.value ||
      !password.value ||
      !confirmPassword.value ||
      usernameError.value ||
      emailError.value ||
      passwordError.value ||
      confirmPasswordError.value
    );
  });

  const register = async () => {
    validateUsername();
    validateEmail();
    validatePassword();
    validateConfirmPassword();

    if (hasErrors.value) {
      showNotification({
        message: '请修正表单中的错误',
        type: 'error',
        duration: 3000,
      });
      return;
    }

    isRegistering.value = true;

    try {
      const response = await api.post('/auth/register/', {
        username: username.value,
        email: email.value,
        password: password.value,
        confirm_password: confirmPassword.value,
      });

      const {
        message,
        refresh,
        token,
        user_type,
        username: returnedUsername,
      } = response.data;
      setTokens({ access: token, refresh });
      localStorage.setItem('username', returnedUsername);
      localStorage.setItem('userType', user_type);

      showNotification({
        message: '注册成功！即将跳转至首页',
        type: 'success',
        duration: 2000,
      });

      authStore.login();

      setTimeout(() => {
        router.push('/');
      }, 2000);
    } catch (error) {
      console.error('注册失败:', error);
      const errorMessage =
        error.response?.data?.error || '注册失败，请稍后重试';
      showNotification({
        message: errorMessage,
        type: 'error',
        duration: 3000,
      });
    } finally {
      isRegistering.value = false;
    }
  };
</script>

<style scoped>
  /* 样式通过 Tailwind CSS 完成，无需额外样式 */
</style>
