<template>
  <div class="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow">
    <div class="mb-6 text-center">
      <h1 class="text-3xl font-bold">{{ competition.name }}</h1>
    </div>

    <div class="flex space-x-10 mb-6">
      <div class="flex-1">
        <span class="font-medium text-gray-700">类型：</span>
        <ul class="flex flex-wrap gap-2">
          <li
            v-for="type in competition.type"
            :key="type"
            class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm"
          >
            {{ type }}
          </li>
        </ul>
      </div>
      <div class="flex-1">
        <span class="font-medium text-gray-700">级别：</span>
        <ul class="flex flex-wrap gap-2">
          <li
            v-for="level in competition.level"
            :key="level"
            class="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm"
          >
            {{ level }}
          </li>
        </ul>
      </div>
    </div>

    <div class="mb-6">
      <h2 class="text-2xl font-semibold mb-2">简介</h2>
      <p class="text-gray-700">{{ competition.description }}</p>
    </div>

    <div class="mb-6">
      <h2 class="text-2xl font-semibold mb-2">时间节点</h2>
      <p>
        开始时间: <strong>{{ formatDate(competition.startTime) }}</strong>
      </p>
      <p>
        结束时间: <strong>{{ formatDate(competition.endTime) }}</strong>
      </p>
    </div>

    <div class="mb-6">
      <h2 class="text-2xl font-semibold mb-2">竞赛官网</h2>
      <a
        :href="competition.officialSiteUrl"
        target="_blank"
        class="text-blue-500 hover:underline"
      >
        {{ competition.officialSiteUrl }}
      </a>
    </div>

    <div>
      <h2 class="text-2xl font-semibold mb-2">其他信息</h2>
      <p class="text-gray-700">{{ competition.otherInfo }}</p>
    </div>
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
