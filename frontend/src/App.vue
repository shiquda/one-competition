<script setup>
  import Footer from '@/components/Footer.vue';
  import Header from '@/components/Header.vue';
  import NotificationContainer from '@/components/NotificationContainer.vue';
</script>

<template>
  <div id="app">
    <Header />

    <main>
      <router-view></router-view>
      <!-- 路由出口，动态渲染不同页面 -->
    </main>

    <NotificationContainer />
    <Footer />
  </div>
</template>

<style>
  /* 可以定义一些全局样式 */
  #app {
    text-align: center;
  }
</style>
