<template>
  <div class="competition-detail-header">
    <h1>{{ competition.name }}</h1>
  </div>

  <div class="competition-detail-tag-item">
    类型：
    <ul class="tag-list">
      <li v-for="type in competition.type">{{ type }}</li>
    </ul>
    级别：
    <ul class="tag-list">
      <li v-for="level in competition.level">{{ level }}</li>
    </ul>
  </div>

  <div class="competition-detail-content">
    <h2>简介</h2>

    <p>{{ competition.description }}</p>
    <h2>时间节点</h2>
    <p>
      开始时间: <strong>{{ formatDate(competition.startTime) }}</strong>
    </p>
    <p>
      结束时间: <strong>{{ formatDate(competition.endTime) }}</strong>
    </p>
    <h2>竞赛官网</h2>
    <a :href="competition.officialSiteUrl" target="_blank">{{
      competition.officialSiteUrl
    }}</a>
    <h2>其他信息</h2>
    <p>{{ competition.otherInfo }}</p>
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
        description: '竞赛1是1个竞赛',
        officialSiteUrl: 'https://example.com',
        type: ['计算机', '数学'],
        level: ['国家级', '省级'],
        otherInfo: '备考可以参考B站的一些网课',
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
  .competition-detail-header {
    margin: 0 auto;
    padding: 10px;
  }

  .competition-detail-content {
    margin-left: 20%;
    text-align: left;
  }

  .competition-detail-content a {
    color: #1890ff;
    text-decoration: none;
  }

  .competition-detail-content a:hover {
    text-decoration: underline;
  }

  .competition-detail-tag-item {
    display: inline-block;
    margin-right: 40px;
  }

  .competition-detail-tag-item ul {
    display: inline-block;
    margin: 0;
    padding: 0;
  }

  .competition-detail-tag-item li {
    display: inline-block;
    margin-right: 10px;
  }

  .tag-list {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  .tag-list li {
    list-style: none;
    padding: 5px 10px;
    border: 1px solid #1890ff;
    border-radius: 5px;
  }
</style>
