<template>
  <div class="competition-lists">
    <h2>🔥正在进行的比赛</h2>
    <table class="competition-list">
      <thead>
        <tr>
          <th>竞赛名称</th>
          <th>开始时间</th>
          <th>结束时间</th>
          <th>距离结束</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="competition in sortedActivateCompetitions"
          :key="competition.id"
        >
          <td>
            <router-link :to="`/competition/${competition.id}`">
              {{ competition.name }}
            </router-link>
          </td>
          <td>{{ formatDate(competition.startTime) }}</td>
          <td>{{ formatDate(competition.endTime) }}</td>
          <td>
            {{ formatDistanceToNow(competition.endTime) }}
          </td>
        </tr>
      </tbody>
    </table>

    <h2>✨即将到来的比赛</h2>
    <table class="competition-list">
      <thead>
        <tr>
          <th>竞赛名称</th>
          <th>开始时间</th>
          <th>结束时间</th>
          <th>距离现在</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="competition in sortedUpComingCompetitions"
          :key="competition.id"
        >
          <td>
            <router-link :to="`/competition/${competition.id}`">
              {{ competition.name }}
            </router-link>
          </td>
          <td>{{ formatDate(competition.startTime) }}</td>
          <td>{{ formatDate(competition.endTime) }}</td>
          <td>
            {{ formatDistanceToNow(competition.startTime) }}
          </td>
        </tr>
      </tbody>
    </table>

    <h2>💀已结束的比赛</h2>
    <table class="competition-list">
      <thead>
        <tr>
          <th>竞赛名称</th>
          <th>开始时间</th>
          <th>结束时间</th>
          <th>距离现在</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="competition in sortedEndedCompetitions"
          :key="competition.id"
        >
          <td>
            <router-link :to="`/competition/${competition.id}`">
              {{ competition.name }}
            </router-link>
          </td>
          <td>{{ formatDate(competition.startTime) }}</td>
          <td>{{ formatDate(competition.endTime) }}</td>
          <td>
            {{ formatDistanceToNow(competition.startTime) }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
  import { ref, onMounted, computed } from 'vue';

  const competitions = ref([]);

  const fetchCompetitions = async () => {
    try {
      //   const response = await fetch('http://127.0.0.1:8000/competitions');
      //   const data = await response.json();

      // TODO: 对接后端

      // 测试数据
      competitions.value = [
        {
          id: 1,
          name: '竞赛1',
          startTime: '2024-12-01',
          endTime: '2024-12-02',
        },
        {
          id: 2,
          name: '竞赛2',
          startTime: '2025-01-05',
          endTime: '2025-01-08',
        },
        {
          id: 3,
          name: '竞赛3',
          startTime: '2024-11-06',
          endTime: '2024-11-06',
        },
        {
          id: 4,
          name: '竞赛4',
          startTime: '2023-11-06',
          endTime: '2023-11-06',
        },
        {
          id: 5,
          name: '竞赛5',
          startTime: '2000-12-01',
          endTime: '2039-12-31',
        },
      ];
    } catch (error) {
      console.error('获取竞赛数据失败:', error);
    }
  };

  onMounted(() => {
    fetchCompetitions();
  });

  const sortedActivateCompetitions = computed(() => {
    const now = new Date();
    return competitions.value
      .filter(
        competition =>
          new Date(competition.startTime) < now &&
          new Date(competition.endTime) > now
      )
      .sort((a, b) => new Date(a.startTime) - new Date(b.startTime));
  });

  const sortedUpComingCompetitions = computed(() => {
    const now = new Date();
    return competitions.value
      .filter(competition => new Date(competition.startTime) > now)
      .sort((a, b) => new Date(a.startTime) - new Date(b.startTime));
  });

  const sortedEndedCompetitions = computed(() => {
    const now = new Date();
    return competitions.value
      .filter(competition => new Date(competition.endTime) < now)
      .sort((a, b) => new Date(a.startTime) - new Date(b.startTime));
  });

  const formatDate = dateStr => {
    const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
    return new Date(dateStr).toLocaleDateString('zh-CN', options);
  };

  const formatDistanceToNow = dateStr => {
    const now = new Date();
    const targetDate = new Date(dateStr);
    const diffTime = targetDate - now;
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    return `${diffDays}天`;
  };
</script>

<style scoped>
  .competition-list {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  table {
    width: 100%;
  }

  th,
  td {
    padding: 10px;
    text-align: left;
  }

  tr:nth-child(even) {
    background-color: #f2f2f2;
  }

  tr:hover {
    background-color: #ddd;
  }

  th {
    background-color: #0396ff;
    color: white;
  }

  a {
    color: #0396ff;
    text-decoration: none;
  }
</style>
