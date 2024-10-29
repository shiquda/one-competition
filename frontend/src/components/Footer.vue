<script setup>
  import License from '@/components/License.vue';
</script>

<template>
  <footer>
    <License />
  </footer>
</template>

<style scoped>
  footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 2px;
    background-color: #f5f5f5;
    text-align: center;
  }
</style>
