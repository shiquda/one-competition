<template>
  <div v-if="isLoggedIn" class="max-w-screen-lg mx-auto p-6 space-y-8">
    <!-- Header -->
    <header class="text-center">
      <h1 class="text-4xl font-bold">个人中心</h1>
    </header>

    <!-- 用户信息卡 -->
    <div class="card bg-gray-800 text-white rounded-lg p-6 shadow-md">
      <h2 class="text-2xl font-semibold mb-4">用户信息</h2>
      <p><strong>用户名：</strong> {{ username }}</p>

      <p><strong>用户类型：</strong> {{ userType }}</p>
    </div>

    <!-- 重置密码组件 -->
    <div class="card bg-gray-800 text-white rounded-lg p-6 shadow-md">
      <h2 class="text-2xl font-semibold mb-4">重置密码</h2>
      <form @submit.prevent="resetPassword" class="space-y-4">
        <div>
          <label for="current-password" class="block text-sm font-medium"
            >当前密码：</label
          >
          <input
            type="password"
            id="current-password"
            v-model="passwords.current"
            class="w-full p-2 mt-1 border rounded-lg bg-gray-900 border-gray-600 focus:outline-none focus:ring focus:ring-blue-500"
            required
          />
        </div>

        <div>
          <label for="new-password" class="block text-sm font-medium"
            >新密码：</label
          >
          <input
            type="password"
            id="new-password"
            v-model="passwords.new"
            @input="validateNewPassword"
            class="w-full p-2 mt-1 border rounded-lg bg-gray-900 border-gray-600 focus:outline-none focus:ring focus:ring-blue-500"
            required
          />
          <span class="text-red-500 text-sm mt-1 block" v-if="passwordError">{{
            passwordError
          }}</span>
        </div>

        <div>
          <label for="confirm-password" class="block text-sm font-medium"
            >确认新密码：</label
          >
          <input
            type="password"
            id="confirm-password"
            v-model="passwords.confirm"
            @input="validateConfirmPassword"
            class="w-full p-2 mt-1 border rounded-lg bg-gray-900 border-gray-600 focus:outline-none focus:ring focus:ring-blue-500"
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
          :disabled="hasErrors"
          class="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-500 disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          提交
        </button>
      </form>
    </div>
  </div>

  <!-- 未登录时显示提示信息 -->
  <div v-else class="max-w-screen-lg mx-auto p-6 text-center">
    <p class="text-lg">请先登录以查看个人中心。</p>
    <router-link
      to="/login"
      class="mt-4 inline-block bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 transition-colors"
    >
      登录
    </router-link>
  </div>
</template>

<script>
  import { ref, computed, onMounted } from 'vue';
  import api from '@/utils/api';
  import showNotification from '@/utils/showNotification';
  import { useAuthStore } from '@/store/authStore.js';

  export default {
    setup() {
      const authStore = useAuthStore();
      const username = ref('');
      const email = ref('');
      const userType = ref('');
      const passwords = ref({
        current: '',
        new: '',
        confirm: '',
      });
      const passwordError = ref('');
      const confirmPasswordError = ref('');

      const hasErrors = computed(() => {
        return (
          !passwords.value.current ||
          !passwords.value.new ||
          !passwords.value.confirm ||
          passwordError.value ||
          confirmPasswordError.value
        );
      });

      const validateNewPassword = () => {
        const passwordRegex =
          /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,32}$/;
        if (!passwordRegex.test(passwords.value.new)) {
          passwordError.value = '密码位数为8-32位，且包含大小写字母和数字';
        } else {
          passwordError.value = '';
        }
      };

      const validateConfirmPassword = () => {
        if (passwords.value.new !== passwords.value.confirm) {
          confirmPasswordError.value = '新密码和确认密码不匹配';
        } else {
          confirmPasswordError.value = '';
        }
      };

      const resetPassword = async () => {
        validateNewPassword();
        validateConfirmPassword();

        if (passwordError.value || confirmPasswordError.value) {
          showNotification({
            message: '请修正表单中的错误',
            type: 'error',
            duration: 3000,
          });
          return;
        }

        try {
          const response = await api.post('/auth/change_password/', {
            old_password: passwords.value.current,
            new_password: passwords.value.new,
            confirm_password: passwords.value.confirm,
          });

          showNotification({
            message: response.data.message || '密码修改成功',
            type: 'success',
            duration: 2000,
          });

          // 清空输入框
          passwords.value.current = '';
          passwords.value.new = '';
          passwords.value.confirm = '';
        } catch (error) {
          console.log(error);
          const errorMessage =
            error.response?.data?.error || '密码修改失败，请稍后重试';
          showNotification({
            message: errorMessage,
            type: 'error',
            duration: 3000,
          });
        }
      };

      onMounted(() => {
        if (authStore.isLoggedIn) {
          // 假设有获取用户信息的 API 调用
          // 这里可以根据实际情况调用 API 获取详细的用户信息
          username.value = localStorage.getItem('username') || '';
          email.value = localStorage.getItem('email') || '';
          userType.value = localStorage.getItem('userType') || '';
        }
      });

      return {
        isLoggedIn: authStore.isLoggedIn,
        username,
        email,
        userType,
        passwords,
        passwordError,
        confirmPasswordError,
        hasErrors,
        resetPassword,
        validateNewPassword,
        validateConfirmPassword,
      };
    },
  };
</script>

<style scoped>
  /* 样式通过 Tailwind CSS 完成，无需额外样式 */
</style>
