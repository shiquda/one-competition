<script setup>
  import HeaderButton from './HeaderButton.vue';
</script>

<template>
  <nav class="navigator">
    <ul>
      <HeaderButton title="首页" to="/"></HeaderButton>
      <HeaderButton title="投稿" to="/submit"></HeaderButton>
      <HeaderButton title="关于" to="/about"></HeaderButton>
    </ul>
  </nav>
</template>

<style scoped>
  .navigator {
    position: relative;
    left: 0;
    right: 0;
    z-index: 1000;
    border-bottom: 1px solid #e0e0e0;
    background-color: #f5f5f5;
  }

  .navigator ul {
    display: flex;
    justify-content: flex-start;
    list-style: none;
    padding: 0 20px;
    height: 60px;
    margin: 0;
  }

  .navigator ul li {
    margin-right: 20px;
    display: flex;
    align-items: center;
  }

  .navigator ul li:last-child {
    margin-right: 0;
  }
</style>

<script>
  export default {
    name: 'Header',
  };
</script>
