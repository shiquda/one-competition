<template>
  <div class="max-w-md mx-auto p-6 bg-white rounded-lg shadow">
    <form @submit.prevent="login">
      <h2 class="text-2xl font-bold mb-4 text-center">登录</h2>
      <div class="mb-4">
        <label for="identifier" class="block text-gray-700">用户名或邮箱</label>
        <input
          type="text"
          id="identifier"
          v-model.trim="identifier"
          @input="validateIdentifier"
          class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
          required
        />
        <span class="text-red-500 text-sm mt-1 block" v-if="identifierError">{{
          identifierError
        }}</span>
      </div>

      <div class="mb-4">
        <label for="password" class="block text-gray-700">密码</label>
        <input
          type="password"
          id="password"
          v-model="password"
          class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
          required
        />
        <span class="text-red-500 text-sm mt-1 block" v-if="passwordError">{{
          passwordError
        }}</span>
      </div>

      <button
        type="submit"
        :disabled="hasErrors || isLoading"
        class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        {{ isLoading ? '登录中...' : '登录' }}
      </button>
      <p class="mt-4 text-center text-sm">
        还没有账号？
        <router-link to="/register" class="text-blue-500 hover:underline"
          >注册</router-link
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
  const isLoading = ref(false);

  const identifier = ref('');
  const password = ref('');
  const identifierError = ref('');
  const passwordError = ref('');

  // 正则表达式用于密码验证
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,32}$/;
  // 正则表达式用于邮箱验证
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

  const validateIdentifier = () => {
    if (!identifier.value) {
      identifierError.value = '用户名或邮箱不能为空';
    } else if (emailRegex.test(identifier.value)) {
      identifierError.value = '';
    } else {
      // 假设用户名至少为3个字符
      if (identifier.value.length < 3) {
        identifierError.value = '用户名至少需3个字符';
      } else {
        identifierError.value = '';
      }
    }
  };

  const validatePassword = () => {
    if (!password.value) {
      passwordError.value = '密码不能为空';
    } else if (!passwordRegex.test(password.value)) {
      passwordError.value = '密码位数为8-32位，且包含大小写字母和数字';
    } else {
      passwordError.value = '';
    }
  };

  const hasErrors = computed(() => {
    return (
      !identifier.value.trim() ||
      !password.value ||
      identifierError.value !== '' ||
      passwordError.value !== ''
    );
  });

  const login = async () => {
    validateIdentifier();
    // validatePassword();
    if (hasErrors.value) return;

    isLoading.value = true;
    try {
      const response = await api.post(`/auth/login/`, {
        username: identifier.value, // 后端使用 'username' 字段接收，可以根据后端逻辑处理
        password: password.value,
      });
      // 假设后端返回的是 token 和 refresh 令牌
      setTokens({
        access: response.data.token,
        refresh: response.data.refresh,
      });
      showNotification({
        message: '登录成功',
        type: 'success',
        duration: 2000,
      });
      authStore.login();
      // 更新存储的用户名和用户类型
      localStorage.setItem('username', response.data.username);
      localStorage.setItem('userType', response.data.user_type);
      router.push('/'); // 登录后跳转到首页或其他页面
    } catch (error) {
      console.error('登录失败:', error);
      showNotification({
        message: error.response?.data?.error || '登录失败',
        type: 'error',
        duration: 3000,
      });
    } finally {
      isLoading.value = false;
    }
  };
</script>

<style scoped></style>
