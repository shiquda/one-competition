<!-- frontend/src/components/CompetitionViewSwitcher.vue -->
<template>
  <div class="flex justify-center mb-4">
    <button
      @click="setView('list')"
      :class="[
        'px-4 py-2 mr-2 rounded',
        currentView === 'list'
          ? 'bg-blue-500 text-white'
          : 'bg-gray-200 text-gray-700 hover:bg-gray-300',
      ]"
    >
      列表视图
    </button>
    <button
      @click="setView('calendar')"
      :class="[
        'px-4 py-2 rounded',
        currentView === 'calendar'
          ? 'bg-blue-500 text-white'
          : 'bg-gray-200 text-gray-700 hover:bg-gray-300',
      ]"
    >
      日历视图
    </button>
  </div>
</template>

<script setup>
  import { ref, watch } from 'vue';

  const emit = defineEmits(['viewChanged']);

  const props = defineProps({
    initialView: {
      type: String,
      default: 'list',
    },
  });

  const currentView = ref(props.initialView);

  const setView = view => {
    currentView.value = view;
  };

  // 监听 currentView 的变化并发出事件
  watch(currentView, newView => {
    emit('viewChanged', newView);
  });
</script>

<style scoped>
  /* 根据需要添加样式 */
</style>
