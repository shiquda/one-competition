<script setup>
  import Footer from '@/components/Footer.vue';
  import Header from '@/components/Header.vue';
  import NotificationContainer from '@/components/NotificationContainer.vue';
</script>

<template>
  <div id="app" class="min-h-screen flex flex-col">
    <Header />

    <main class="flex-grow mt-16 overflow-y-auto">
      <router-view></router-view>
      <!-- 路由出口，动态渲染不同页面 -->
    </main>

    <NotificationContainer />
    <Footer />
  </div>
</template>

<style>
  /* 可以在此处添加全局样式 */
  body,
  html {
    height: 100%;
  }
</style>
