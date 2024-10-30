<template>
  <div class="relative inline-block text-left">
    <button
      @click="toggleDropdown"
      class="flex items-center space-x-2 bg-white border border-gray-300 rounded-md px-3 py-2 hover:bg-gray-50 focus:outline-none"
    >
      <i class="fa-solid fa-user"></i>
      <span>{{ username }}</span>
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
        <router-link
          to="/personal-center"
          class="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
        >
          <i class="fa-solid fa-user mr-2"></i>个人中心
        </router-link>
        <button
          @click="logout"
          class="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
        >
          <i class="fa-solid fa-right-from-bracket mr-2"></i>退出登录
        </button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'UserOptionsWidget',
    data() {
      // TODO: 获取用户名
      return {
        username: 'User', // 可以通过props或从store中获取
        isDropdownVisible: false,
      };
    },
    methods: {
      toggleDropdown() {
        this.isDropdownVisible = !this.isDropdownVisible;
      },
      logout() {
        // TODO: 发送退出登录请求
        // 示例：
        localStorage.removeItem('authToken');
        this.$router.push('/login');
      },
      handleClickOutside(event) {
        if (!this.$el.contains(event.target)) {
          this.isDropdownVisible = false;
        }
      },
    },
    mounted() {
      document.addEventListener('click', this.handleClickOutside);
    },
    beforeUnmount() {
      document.removeEventListener('click', this.handleClickOutside);
    },
  };
</script>

<style scoped>
  /* 样式通过 Tailwind CSS 完成，无需额外样式 */
</style>
