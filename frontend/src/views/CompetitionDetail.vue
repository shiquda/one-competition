<template>
  <div class="competition-detail">
    <h1>{{ competition.name }}</h1>
    <p>{{ competition.description }}</p>
    <p>开始时间: {{ formatDate(competition.startTime) }}</p>
    <p>结束时间: {{ formatDate(competition.endTime) }}</p>
    <a :href="competition.url" target="_blank">竞赛官网</a>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';

  const route = useRoute();
  const competition = ref({});

  const fetchCompetitionDetail = async () => {
    try {
      //   const response = await fetch(
      //     `http://127.0.0.1:8000/competitions/${route.params.id}`
      //   );
      //   const data = await response.json();
      //   competition.value = data;
      competition.value = {
        id: 1,
        name: '竞赛1',
        startTime: '2024-01-01',
        endTime: '2024-01-02',
      };
    } catch (error) {
      console.error('获取竞赛详情失败:', error);
    }
  };

  onMounted(() => {
    fetchCompetitionDetail();
  });

  const formatDate = dateStr => {
    const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
    return new Date(dateStr).toLocaleDateString('zh-CN', options);
  };
</script>

<style scoped>
  .competition-detail {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  .competition-detail a {
    color: #1890ff;
    text-decoration: none;
  }

  .competition-detail a:hover {
    text-decoration: underline;
  }
</style>
