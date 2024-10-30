<template>
  <li>
    <router-link
      :to="to"
      class="flex items-center space-x-2 px-3 py-2 text-gray-700 hover:text-blue-500"
    >
      <i :class="awesomeIcon"></i>
      <span>{{ title }}</span>
    </router-link>
  </li>
</template>

<script setup>
  // 绑定属性
  defineProps({
    title: String,
    to: String,
    awesomeIcon: String,
  });
</script>
