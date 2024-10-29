<template>
  <div class="not-found">
    <h1>404</h1>
    <p>页面未找到</p>
    <router-link to="/">↩️返回首页</router-link>
  </div>
</template>

<style scoped>
  .not-found {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 400px;
    text-align: center;
  }

  h1 {
    font-size: 6rem;
    margin-bottom: 1rem;
  }

  p {
    font-size: 2rem;
    margin-bottom: 2rem;
  }

  a {
    font-size: 1.5rem;
    color: #1890ff;
    text-decoration: none;
  }
</style>

<script setup></script>
