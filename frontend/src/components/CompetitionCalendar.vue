<template>
  <!-- https://antoniandre.github.io/vue-cal/#api -->
  <div class="container mx-auto p-6 max-w-5xl">
    <vue-cal
      :events="calendarEvents"
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
  import { ref, computed } from 'vue';
  import { useRouter } from 'vue-router';
  import VueCal from 'vue-cal';

  // 接收来自父组件的竞赛数据
  const props = defineProps({
    competitions: {
      type: Array,
      required: true,
    },
  });

  const router = useRouter();

  // 当前选中日期（可选）
  const selectedDate = ref(new Date());

  // 处理事件点击，跳转到竞赛详情页
  const handleEventClick = event => {
    const competitionId = event.id;
    router.push(`/competition/${competitionId}`);
  };

  // 转换竞赛数据为 vue-cal 事件格式
  const calendarEvents = computed(() => {
    return props.competitions.map(competition => ({
      id: competition.id,
      title: competition.name,
      start: competition.startTime,
      end: competition.endTime,
      class: getEventColorClass(competition),
      allDay: true,
    }));
  });

  // 根据竞赛状态设置事件颜色
  const getEventColorClass = competition => {
    const now = new Date();
    const start = new Date(competition.startTime);
    const end = new Date(competition.endTime);
    if (start > now) {
      return 'bg-green-300'; // 即将开始 - 绿色
    } else if (end > now) {
      return 'bg-yellow-300'; // 正在进行 - 黄色
    } else {
      return 'bg-red-300'; // 已结束 - 红色
    }
  };
</script>

<style scoped>
  /* 可以根据需要添加自定义样式 */
</style>
