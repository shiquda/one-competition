<template>
  <!-- https://antoniandre.github.io/vue-cal/#api -->
  <div class="container mx-auto p-6 max-w-5xl">
    <vue-cal
      :events="events"
      @event-click="handleEventClick"
      :selected-date="selectedDate"
      :toolbar="true"
      :time="false"
      :locale="'zh-cn'"
      :disable-views="['day']"
      style="height: 500px"
      today-button
    />
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import VueCal from 'vue-cal';

  // 引入 vue-cal 的样式（已在 main.js 中引入，可选）
  import 'vue-cal/dist/vuecal.css';

  // 路由实例
  const router = useRouter();

  // 竞赛事件数据
  const events = ref([]);

  // 当前选中日期（可选）
  const selectedDate = ref(new Date());

  // 处理事件点击，跳转到竞赛详情页
  const handleEventClick = event => {
    const competitionId = event.id;
    router.push(`/competition/${competitionId}`);
  };

  // 获取竞赛数据并设置到日历事件中
  const fetchCompetitions = async () => {
    try {
      // 示例数据，包括一个硬编码的事件
      const data = [
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
          name: '2024期中考',
          startTime: '2024-11-19',
          endTime: '2024-11-22',
        },
        {
          id: 4,
          name: '2023半期考',
          startTime: '2023-11-19',
          endTime: '2023-11-22',
        },
        {
          id: 5,
          name: '马拉松',
          startTime: '2000-12-01',
          endTime: '2039-12-31',
        },
        {
          id: 100,
          name: '测试竞赛',
          startTime: '2024-11-19',
          endTime: '2024-11-22',
        },
      ];

      // 转换竞赛数据为 vue-cal 事件格式
      events.value = data.map(competition => ({
        id: competition.id,
        title: competition.name,
        start: competition.startTime,
        end: competition.endTime,
        class: getEventColorClass(competition),
        allDay: true,
      }));

      console.log('加载的日历事件:', events.value); // 调试日志
    } catch (error) {
      console.error('获取竞赛数据失败:', error);
    }
  };

  // 根据竞赛状态设置事件颜色
  const getEventColorClass = competition => {
    const now = new Date();
    const start = new Date(competition.startTime);
    const end = new Date(competition.endTime);
    if (start > now) {
      return 'bg-green-300'; // 即将开始 - 黄色
    } else if (end > now) {
      return 'bg-yellow-300'; // 正在进行 - 绿色
    } else {
      return 'bg-red-300'; // 已结束 - 红色
    }
  };

  // 在组件挂载时获取竞赛数据
  onMounted(() => {
    fetchCompetitions();
  });
</script>

<style scoped>
  /* 可根据需要添加自定义样式 */
</style>
