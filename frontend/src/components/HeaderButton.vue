<template>
  <li>
    <router-link :to="to" class="header-button">{{ title }}</router-link>
  </li>
</template>

<script>
  export default {
    props: {
      title: String,
      to: String,
    },
  };
</script>

<style scoped>
  .header-button {
    background-color: transparent;
    border: none;
    border-right: 1px solid #e0e0e0;
    border-radius: 0;
    padding: 0 15px;
    font-size: 14px;
    transition: color 0.3s;
    text-decoration: none;
    color: inherit;
  }

  .header-button:hover {
    background-color: transparent;
    color: #007bff;
  }

  li:last-child .header-button {
    border-right: none;
  }
</style>
