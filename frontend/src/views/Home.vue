<!-- frontend/src/views/Home.vue -->
<script setup>
  import { ref } from 'vue';
  import CompetitionViewSwitcher from '@/components/CompetitionViewSwitcher.vue';
  import CompetitionLists from '@/components/CompetitionLists.vue';
  import CompetitionCalendar from '@/components/CompetitionCalendar.vue';

  const currentView = ref('list'); // 默认视图

  const handleViewChange = view => {
    currentView.value = view;
  };
</script>

<template>
  <h1 class="text-3xl font-bold text-center mb-3 text-gray-800">竞赛信息</h1>
  <CompetitionViewSwitcher @viewChanged="handleViewChange" />

  <CompetitionLists v-if="currentView === 'list'" />
  <CompetitionCalendar v-else-if="currentView === 'calendar'" />
</template>

<style scoped></style>
