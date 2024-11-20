<script setup>
  import { ref, onMounted } from 'vue';
  import CompetitionViewSwitcher from '@/components/CompetitionViewSwitcher.vue';
  import CompetitionLists from '@/components/CompetitionLists.vue';
  import CompetitionCalendar from '@/components/CompetitionCalendar.vue';

  const currentView = ref('list'); // 默认视图
  const competitions = ref([]); // 存储竞赛数据
  const loading = ref(true); // 数据加载状态
  const error = ref(null); // 错误信息

  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

  const handleViewChange = view => {
    currentView.value = view;
  };

  // 获取竞赛数据的函数
  const fetchCompetitions = async () => {
    try {
      const url = `${API_BASE_URL}/competitions/`;
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error('Failed to fetch competitions');
      }
      competitions.value = await response.json();
      console.log(competitions.value);
      competitions.value.forEach(competition => {
        console.log(competition.timeline);
        competition.startTime = competition.timeline.find(
          node => node.node_name === 'start_time'
        ).date;
        competition.endTime = competition.timeline.find(
          node => node.node_name === 'end_time'
        ).date;
      });
    } catch (err) {
      error.value = err.message;
    } finally {
      loading.value = false;
    }
  };

  onMounted(() => {
    fetchCompetitions();
  });
</script>

<template>
  <h1 class="text-3xl font-bold text-center mb-3 text-gray-800">竞赛信息</h1>
  <CompetitionViewSwitcher @viewChanged="handleViewChange" />

  <div v-if="loading" class="text-center text-gray-500">加载中...</div>
  <div v-else-if="error" class="text-center text-red-500">
    错误: {{ error }}
  </div>
  <div v-else>
    <CompetitionLists
      v-if="currentView === 'list'"
      :competitions="competitions"
    />
    <CompetitionCalendar
      v-else-if="currentView === 'calendar'"
      :competitions="competitions"
    />
  </div>
</template>

<style scoped></style>
