<template>
  <div class="relative inline-block text-left">
    <button
      @click="toggleDropdown"
      class="flex items-center space-x-2 bg-white border border-gray-300 rounded-md px-3 py-2 hover:bg-gray-50 focus:outline-none"
    >
      <i class="fa-solid fa-user"></i>
      <span>{{ authStore.username }}</span>
      <svg
        class="w-4 h-4"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M19 9l-7 7-7-7"
        />
      </svg>
    </button>
    <div
      v-if="isDropdownVisible"
      class="origin-top-right absolute right-0 mt-2 w-40 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5"
    >
      <div class="py-1">
        <div>
          <router-link
            to="/personal-center"
            class="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
          >
            <i class="fa-solid fa-user mr-2"></i>个人中心
          </router-link>
        </div>
        <div v-if="authStore.isAdmin">
          <router-link
            to="/admin"
            class="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
          >
            <i class="fa-solid fa-magnifying-glass mr-2"></i>审核竞赛
          </router-link>
        </div>
        <div>
          <button
            @click="logout"
            class="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
          >
            <i class="fa-solid fa-right-from-bracket mr-2"></i>退出登录
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import { useAuthStore } from '@/store/authStore.js';
  import { useRouter } from 'vue-router';

  const authStore = useAuthStore();
  const router = useRouter();
  const isDropdownVisible = ref(false);

  const toggleDropdown = () => {
    isDropdownVisible.value = !isDropdownVisible.value;
  };

  const logout = () => {
    authStore.logout();
    router.push('/login');
  };
</script>

<style scoped>
  /* 样式通过 Tailwind CSS 完成，无需额外样式 */
</style>
