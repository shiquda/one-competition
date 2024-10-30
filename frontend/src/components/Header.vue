<script setup>
  import HeaderButton from './HeaderButton.vue';
  import LoginOrOptions from './LoginOrOptions.vue';
</script>

<template>
  <nav
    class="fixed top-0 left-0 right-0 z-50 border-b border-gray-200 bg-white shadow"
  >
    <ul class="flex items-center h-16 px-5">
      <div class="flex items-center mr-5">
        <router-link
          to="/"
          class="flex items-center space-x-2 text-blue-500 hover:text-blue-700"
        >
          <img
            src="@/assets/imgs/logo.png"
            alt="One 竞赛"
            width="20"
            height="20"
          />
          <span class="text-lg font-bold">One 竞赛</span>
        </router-link>
      </div>
      <HeaderButton
        title="投稿"
        to="/submit"
        awesomeIcon="fa-solid fa-pen"
      ></HeaderButton>
      <HeaderButton
        title="关于"
        to="/about"
        awesomeIcon="fa-solid fa-circle-info"
      ></HeaderButton>
      <LoginOrOptions class="ml-auto" />
    </ul>
  </nav>
  <div class="h-16"></div>
  <!-- 导航栏占位 -->
</template>
