<script setup>
  import HeaderButton from './HeaderButton.vue';
</script>

<template>
  <nav class="navigator">
    <ul>
      <div class="logo">
        <router-link to="/" class="header-button">
          <img
            src="@/assets/imgs/logo.png"
            alt="One 竞赛"
            width="20"
            height="20"
          />
          <span class="logo-text">One 竞赛</span>
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
    </ul>
  </nav>
  <div class="navigator-placeholder"></div>
</template>

<style scoped>
  .navigator {
    position: fixed;
    top: 0;
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

  .logo {
    display: flex;
    align-items: center;
    margin-right: 20px;
  }

  .logo .header-button {
    display: flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
  }

  .logo .header-button:hover {
    background-color: transparent;
    color: #007bff;
  }

  .logo-text {
    font-size: 18px;
    font-weight: bold;
    color: #007bff;
    transition: color 0.3s;
  }

  .navigator-placeholder {
    height: 60px; /* 与导航栏高度相同 */
  }
</style>
