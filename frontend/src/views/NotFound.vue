<template>
  <div class="flex flex-col items-center justify-center h-[404px] text-center">
    <h1 class="text-8xl font-bold mb-4">404</h1>
    <p class="text-3xl mb-6">页面未找到</p>
    <div class="flex gap-4">
      <router-link
        to="/"
        class="flex items-center px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition"
      >
        <i class="fas fa-home mr-2"></i>
        返回首页
      </router-link>
      <button
        @click="goBack"
        class="flex items-center px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600 transition"
      >
        <i class="fas fa-arrow-left mr-2"></i>
        返回上一页
      </button>
    </div>
  </div>
</template>

<style scoped>
  /* 样式通过 Tailwind CSS 完成，无需额外样式 */
</style>

<script setup>
  import { useRouter } from 'vue-router';
  const router = useRouter();
  const goBack = () => router.go(-1);
</script>
