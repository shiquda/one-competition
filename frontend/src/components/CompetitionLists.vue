<template>
  <div class="container mx-auto p-6">
    <div
      class="flex flex-col lg:flex-row lg:space-x-6 space-y-6 lg:space-y-0 justify-center"
    >
      <!-- 即将到来的比赛 -->
      <div class="bg-white rounded-lg shadow p-4">
        <h2 class="text-2xl font-semibold mb-4 flex items-center">
          ✨即将到来的比赛
          <span class="ml-2 text-sm text-gray-500"
            >({{ sortedUpComingCompetitions.length }})</span
          >
        </h2>
        <div class="overflow-x-auto">
          <table class="min-w-[500px] table-auto divide-y divide-gray-200">
            <thead class="bg-yellow-500 text-white">
              <tr>
                <th class="py-3 px-4 text-left text-sm font-medium w-2/5">
                  竞赛名称
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium w-1/5">
                  开始时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium w-1/5">
                  结束时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium w-1/5">
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
                    :title="competition.name"
                  >
                    {{ competition.name }}
                  </router-link>
                </td>
                <td class="py-4 px-4">
                  {{ formatDate(competition.startTime) }}
                </td>
                <td class="py-4 px-4">
                  {{ formatDate(competition.endTime) }}
                </td>
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
      <div class="bg-white rounded-lg shadow p-4">
        <h2 class="text-2xl font-semibold mb-4 flex items-center">
          🔥正在进行的比赛
          <span class="ml-2 text-sm text-gray-500"
            >({{ sortedActivateCompetitions.length }})</span
          >
        </h2>
        <div class="overflow-x-auto">
          <table class="min-w-[500px] table-auto divide-y divide-gray-200">
            <thead class="bg-blue-600 text-white">
              <tr>
                <th class="py-3 px-4 text-left text-sm font-medium w-2/5">
                  竞赛名称
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium w-1/5">
                  开始时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium w-1/5">
                  结束时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium w-1/5">
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
                    :title="competition.name"
                  >
                    {{ competition.name }}
                  </router-link>
                </td>
                <td class="py-4 px-4">
                  {{ formatDate(competition.startTime) }}
                </td>
                <td class="py-4 px-4">
                  {{ formatDate(competition.endTime) }}
                </td>
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
      <div class="bg-white rounded-lg shadow p-4">
        <h2 class="text-2xl font-semibold mb-4 flex items-center">
          💀已结束的比赛
          <span class="ml-2 text-sm text-gray-500"
            >({{ sortedEndedCompetitions.length }})</span
          >
        </h2>
        <div class="overflow-x-auto">
          <table class="min-w-[500px] table-auto divide-y divide-gray-200">
            <thead class="bg-gray-600 text-white">
              <tr>
                <th class="py-3 px-4 text-left text-sm font-medium w-2/5">
                  竞赛名称
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium w-1/5">
                  开始时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium w-1/5">
                  结束时间
                </th>
                <th class="py-3 px-4 text-left text-sm font-medium w-1/5">
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
                    :title="competition.name"
                  >
                    {{ competition.name }}
                  </router-link>
                </td>
                <td class="py-4 px-4">
                  {{ formatDate(competition.startTime) }}
                </td>
                <td class="py-4 px-4">
                  {{ formatDate(competition.endTime) }}
                </td>
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
  import { computed } from 'vue';
  import { useRoute } from 'vue-router';

  // 接收来自父组件的竞赛数据
  const props = defineProps({
    competitions: {
      type: Array,
      required: true,
    },
  });

  // 计算即将到来的比赛
  const sortedUpComingCompetitions = computed(() => {
    const now = new Date();
    return props.competitions
      .filter(competition => new Date(competition.startTime) > now)
      .sort((a, b) => new Date(a.startTime) - new Date(b.startTime));
  });

  // 计算正在进行的比赛
  const sortedActivateCompetitions = computed(() => {
    const now = new Date();
    return props.competitions
      .filter(
        competition =>
          new Date(competition.startTime) < now &&
          new Date(competition.endTime) > now
      )
      .sort((a, b) => new Date(a.startTime) - new Date(b.startTime));
  });

  // 计算已结束的比赛
  const sortedEndedCompetitions = computed(() => {
    const now = new Date();
    return props.competitions
      .filter(competition => new Date(competition.endTime) < now)
      .sort((a, b) => new Date(a.startTime) - new Date(b.startTime));
  });

  // 日期格式化函数
  const formatDate = dateStr => {
    const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
    return new Date(dateStr).toLocaleDateString('zh-CN', options);
  };

  // 计算距离现在的天数
  const formatDistanceToNow = dateStr => {
    const now = new Date();
    const targetDate = new Date(dateStr);
    const diffTime = targetDate - now;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
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
  /* 增加表格整体宽度 */
  .container {
    max-width: 9000px;
  }

  /* 限制表格单元格的宽度并允许换行 */
  th,
  td {
    max-width: 300px;
    word-wrap: break-word;
  }

  /* 允许竞赛名称换行 */
  td:nth-child(1) {
    white-space: normal;
    overflow: visible;
  }

  /* 设置表格最小宽度 */
  table {
    min-width: 500px;
  }

  /* 调整表格容器的对齐方式 */
  .flex {
    display: flex;
    justify-content: center;
  }

  /* 保留悬浮显示完整名称 */
  router-link {
    display: block;
  }
</style>
