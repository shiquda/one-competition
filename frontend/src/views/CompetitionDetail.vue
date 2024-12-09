<template>
  <div class="relative">
    <!-- 蒙版 -->
    <div
      v-if="loading"
      class="absolute inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50 z-50"
    >
      <div class="text-white text-xl">正在加载中...</div>
    </div>

    <div class="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow">
      <div class="mb-6 text-center">
        <h1 class="text-3xl font-bold">{{ competition.name }}</h1>
      </div>

      <div class="flex space-x-10 mb-6">
        <div class="flex-1">
          <span class="font-medium text-gray-700">类型：</span>
          <ul class="flex flex-wrap gap-2">
            <li
              v-for="type in competition.types"
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
              v-for="level in competition.levels"
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
        <p class="text-gray-700 whitespace-pre-wrap">
          {{ competition.description }}
        </p>
      </div>

      <div class="mb-6">
        <h2 class="text-2xl font-semibold mb-2">时间节点</h2>
        <p>
          开始时间:
          <strong>{{
            formatDate(
              competition?.timeline?.find(
                node => node.node_name === 'start_time'
              )?.date
            )
          }}</strong>
        </p>
        <p>
          结束时间:
          <strong>{{
            formatDate(
              competition?.timeline?.find(node => node.node_name === 'end_time')
                ?.date
            )
          }}</strong>
        </p>
      </div>

      <div class="mb-6">
        <h2 class="text-2xl font-semibold mb-2">竞赛官网</h2>
        <a
          :href="competition.website"
          target="_blank"
          class="text-blue-500 hover:underline"
        >
          {{ competition.website }}
        </a>
      </div>

      <div>
        <h2 class="text-2xl font-semibold mb-2">其他信息</h2>
        <p class="text-gray-700 whitespace-pre-wrap">
          {{ competition.other_info }}
        </p>
      </div>
      <div class="mt-6">
        <hr class="border-t border-gray-300 my-6" />
        <h2 class="text-2xl font-semibold mb-2">评论区</h2>
        <div id="tcomment"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';

  const route = useRoute();
  const competition = ref({});
  const loading = ref(true);

  const loadScript = src => {
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = src;
      script.onload = () => resolve(script);
      script.onerror = () => reject(new Error(`加载脚本失败: ${src}`));
      document.head.appendChild(script);
    });
  };

  const fetchCompetitionDetail = async () => {
    const baseUrl = import.meta.env.VITE_API_BASE_URL;
    try {
      const response = await fetch(`${baseUrl}/competition/${route.params.id}`);
      const data = await response.json();
      competition.value = data;
    } catch (error) {
      console.error('获取竞赛详情失败:', error);
    }
  };

  const initializeTwikoo = async () => {
    try {
      await loadScript(
        'https://cdn.jsdelivr.net/npm/twikoo@1.6.40/dist/twikoo.all.min.js'
      );
      if (window.twikoo) {
        window.twikoo.init({
          envId: 'https://comment.shiquda.link',
          el: '#tcomment',
          lang: 'zh-CN',
        });
      } else {
        console.error('Twikoo 未加载');
      }
    } catch (error) {
      console.error(error);
    }
  };

  onMounted(async () => {
    await fetchCompetitionDetail();
    await initializeTwikoo();
    loading.value = false;
  });

  const formatDate = dateStr => {
    try {
      if (!dateStr) return 'N/A';
      const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
      return new Date(dateStr).toLocaleDateString('zh-CN', options);
    } catch (error) {
      console.error('日期格式化失败:', error);
      return 'N/A';
    }
  };
</script>

<style scoped>
  #tcomment {
    width: 60%;
    margin: 0 auto;
  }

  /* 蒙版样式 */
  .relative {
    position: relative;
  }

  .absolute {
    position: absolute;
  }

  .inset-0 {
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
  }

  .flex {
    display: flex;
  }

  .items-center {
    align-items: center;
  }

  .justify-center {
    justify-content: center;
  }

  .bg-gray-800 {
    background-color: rgba(31, 41, 55, 1); /* 根据需要调整颜色 */
  }

  .bg-opacity-50 {
    background-color: rgba(0, 0, 0, 0.5);
  }

  .z-50 {
    z-index: 50;
  }

  .text-white {
    color: white;
  }

  .text-xl {
    font-size: 1.25rem;
  }
</style>
