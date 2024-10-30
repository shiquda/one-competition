<template>
  <div class="container mx-auto p-6">
    <div class="flex flex-col lg:flex-row lg:space-x-6 space-y-6 lg:space-y-0">
      <!-- 即将到来的比赛 -->
      <div class="flex-1 bg-white rounded-lg shadow p-4">
        <h2 class="text-2xl font-semibold mb-4 flex items-center">
          ✨即将到来的比赛
          <span class="ml-2 text-sm text-gray-500"
            >({{ sortedUpComingCompetitions.length }})</span
          >
        </h2>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-yellow-500 text-white">
              <tr>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  竞赛名称
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  开始时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  结束时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  距离开始
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr
                v-for="competition in sortedUpComingCompetitions"
                :key="competition.id"
                class="hover:bg-yellow-50 transition-colors"
              >
                <td class="py-4 px-4">
                  <router-link
                    :to="`/competition/${competition.id}`"
                    class="text-yellow-700 hover:underline font-medium"
                  >
                    {{ competition.name }}
                  </router-link>
                </td>
                <td class="py-4 px-4">
                  {{ formatDate(competition.startTime) }}
                </td>
                <td class="py-4 px-4">{{ formatDate(competition.endTime) }}</td>
                <td class="py-4 px-4">
                  {{ formatDistanceToNow(competition.startTime) }}
                </td>
              </tr>
              <tr v-if="sortedUpComingCompetitions.length === 0">
                <td colspan="4" class="py-4 px-4 text-center text-gray-500">
                  暂无即将到来的比赛
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- 正在进行的比赛 -->
      <div class="flex-1 bg-white rounded-lg shadow p-4">
        <h2 class="text-2xl font-semibold mb-4 flex items-center">
          🔥正在进行的比赛
          <span class="ml-2 text-sm text-gray-500"
            >({{ sortedActivateCompetitions.length }})</span
          >
        </h2>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-blue-600 text-white">
              <tr>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  竞赛名称
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  开始时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  结束时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  距离结束
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr
                v-for="competition in sortedActivateCompetitions"
                :key="competition.id"
                class="hover:bg-blue-50 transition-colors"
              >
                <td class="py-4 px-4">
                  <router-link
                    :to="`/competition/${competition.id}`"
                    class="text-blue-500 hover:underline font-medium"
                  >
                    {{ competition.name }}
                  </router-link>
                </td>
                <td class="py-4 px-4">
                  {{ formatDate(competition.startTime) }}
                </td>
                <td class="py-4 px-4">{{ formatDate(competition.endTime) }}</td>
                <td class="py-4 px-4">
                  {{ formatDistanceToNow(competition.endTime) }}
                </td>
              </tr>
              <tr v-if="sortedActivateCompetitions.length === 0">
                <td colspan="4" class="py-4 px-4 text-center text-gray-500">
                  暂无正在进行的比赛
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- 已结束的比赛 -->
      <div class="flex-1 bg-white rounded-lg shadow p-4">
        <h2 class="text-2xl font-semibold mb-4 flex items-center">
          💀已结束的比赛
          <span class="ml-2 text-sm text-gray-500"
            >({{ sortedEndedCompetitions.length }})</span
          >
        </h2>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-600 text-white">
              <tr>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  竞赛名称
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  开始时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  结束时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium">
                  距离结束
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr
                v-for="competition in sortedEndedCompetitions"
                :key="competition.id"
                class="hover:bg-gray-50 transition-colors"
              >
                <td class="py-4 px-4">
                  <router-link
                    :to="`/competition/${competition.id}`"
                    class="text-gray-700 hover:underline font-medium"
                  >
                    {{ competition.name }}
                  </router-link>
                </td>
                <td class="py-4 px-4">
                  {{ formatDate(competition.startTime) }}
                </td>
                <td class="py-4 px-4">{{ formatDate(competition.endTime) }}</td>
                <td class="py-4 px-4">
                  {{ formatDistanceToNow(competition.startTime) }}
                </td>
              </tr>
              <tr v-if="sortedEndedCompetitions.length === 0">
                <td colspan="4" class="py-4 px-4 text-center text-gray-500">
                  暂无已结束的比赛
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, computed } from 'vue';

  const competitions = ref([]);

  const fetchCompetitions = async () => {
    try {
      // const response = await fetch('http://127.0.0.1:8000/competitions');
      // const data = await response.json();

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

  const sortedUpComingCompetitions = computed(() => {
    const now = new Date();
    return competitions.value
      .filter(competition => new Date(competition.startTime) > now)
      .sort((a, b) => new Date(a.startTime) - new Date(b.startTime));
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
    if (diffDays > 0) {
      return `${diffDays}天`;
    } else if (diffDays === 0) {
      return '今天';
    } else {
      return `${Math.abs(diffDays)}天前`;
    }
  };
</script>

<style scoped>
  /* 样式通过 Tailwind CSS 完成，无需额外样式 */
</style>
