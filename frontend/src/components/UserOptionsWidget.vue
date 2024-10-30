<template>
  <div class="user-options">
    <i class="fa-solid fa-user"></i>
    <button @click="toggleDropdown" class="user-button">
      {{ username }} ▼
    </button>
    <div v-if="isDropdownVisible" class="dropdown-menu">
      <i class="fa-solid fa-user"></i>
      <a href="/personal-center" class="dropdown-item">个人中心</a>
      <i class="fa-solid fa-right-from-bracket"></i>
      <a href="#" @click.prevent="logout" class="dropdown-item">退出登录</a>
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
    beforeDestroy() {
      document.removeEventListener('click', this.handleClickOutside);
    },
  };
</script>

<style scoped>
  .user-options {
    position: relative;
    display: inline-block;
  }

  .user-button {
    background-color: #fff;
    border: 1px solid #ccc;
    padding: 8px 12px;
    cursor: pointer;
  }

  .dropdown-menu {
    position: absolute;
    top: 100%;
    right: 0;
    background-color: #fff;
    border: 1px solid #ccc;
    min-width: 150px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    z-index: 1000;
  }

  .dropdown-item {
    display: block;
    padding: 10px 15px;
    color: #333;
    text-decoration: none;
  }

  .dropdown-item:hover {
    background-color: #f5f5f5;
  }
</style>
