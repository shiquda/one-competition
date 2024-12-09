<template>
  <div class="admin-container max-w-screen-xl mx-auto p-6 space-y-8">
    <h1 class="text-2xl font-bold text-center">竞赛审核</h1>

    <!-- 审核请求表格 -->
    <div v-if="isLoading" class="text-center">
      <p>加载中...</p>
    </div>
    <div v-else>
      <table
        class="min-w-full table-auto bg-gray-800 text-white rounded-lg shadow-md"
      >
        <thead>
          <tr>
            <th class="py-3 px-4">ID</th>
            <th class="py-3 px-4">竞赛名称</th>
            <th class="py-3 px-4">状态</th>
            <th class="py-3 px-4">操作</th>
          </tr>
        </thead>
        <tbody>
          <template v-for="request in requests" :key="request.id">
            <tr>
              <td class="py-3 px-4">{{ request.id }}</td>
              <td class="py-3 px-4">{{ request.name }}</td>
              <td class="py-3 px-4">
                <span
                  :class="{
                    'bg-green-500': request.review_status === 'approved',
                    'bg-red-500': request.review_status === 'rejected',
                    'bg-yellow-500': request.review_status === 'pending',
                  }"
                  class="px-3 py-1 rounded text-white"
                >
                  {{ request.review_status }}
                </span>
              </td>
              <td class="py-3 px-4 space-x-2">
                <button
                  @click="approveRequest(request.id)"
                  class="bg-green-500 px-4 py-2 rounded text-white hover:bg-green-600"
                  v-if="request.review_status === 'pending'"
                >
                  通过
                </button>
                <button
                  @click="rejectRequest(request.id)"
                  class="bg-red-500 px-4 py-2 rounded text-white hover:bg-red-600"
                  v-if="request.review_status === 'pending'"
                >
                  拒绝
                </button>
                <button
                  @click="toggleExpand(request.id)"
                  class="bg-blue-500 px-4 py-2 rounded text-white hover:bg-blue-600"
                >
                  {{ isRowExpanded(request.id) ? '收起' : '展开' }}
                </button>
              </td>
            </tr>
            <tr v-if="isRowExpanded(request.id)" class="bg-gray-700">
              <td colspan="4" class="py-3 px-4">
                <CompetitionEditForm
                  :competition="request"
                  :onUpdate="handleUpdate"
                  :onCancel="() => toggleExpand(request.id)"
                />
              </td>
            </tr>
          </template>
        </tbody>
      </table>
    </div>

    <!-- 模态框省略 -->
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import api from '@/utils/api';
  import showNotification from '@/utils/showNotification';
  import { useAuthStore } from '@/store/authStore.js';
  import CompetitionEditForm from '@/components/CompetitionEditForm.vue';

  const requests = ref([]);
  const isLoading = ref(false);

  // 用于跟踪哪些行已展开
  const expandedRows = ref(new Set());

  // 获取审核请求
  const fetchRequests = async () => {
    isLoading.value = true;
    try {
      const response = await api.get('/admin/competitions/');
      requests.value = response.data;
    } catch (error) {
      console.error('获取审核请求失败:', error);
      showNotification({
        message: '获取审核请求失败，请稍后重试',
        type: 'error',
        duration: 3000,
      });
    } finally {
      isLoading.value = false;
    }
  };

  // 审批请求
  const approveRequest = async id => {
    try {
      await api.post(`/admin/competition/update/${id}/`, {
        review_status: 'approved',
      });
      showNotification({
        message: '请求已通过',
        type: 'success',
        duration: 2000,
      });
      fetchRequests();
    } catch (error) {
      console.error('批准请求失败:', error);
      showNotification({
        message: '批准请求失败，请稍后重试',
        type: 'error',
        duration: 3000,
      });
    }
  };

  // 拒绝请求
  const rejectRequest = async id => {
    try {
      await api.post(`/admin/audit-requests/${id}/reject/`);
      showNotification({
        message: '请求已拒绝',
        type: 'success',
        duration: 2000,
      });
      fetchRequests();
    } catch (error) {
      console.error('拒绝请求失败:', error);
      showNotification({
        message: '拒绝请求失败，请稍后重试',
        type: 'error',
        duration: 3000,
      });
    }
  };

  // 切换行的展开状态
  const toggleExpand = id => {
    if (expandedRows.value.has(id)) {
      expandedRows.value.delete(id);
    } else {
      expandedRows.value.add(id);
    }
  };

  // 判断行是否展开
  const isRowExpanded = id => {
    return expandedRows.value.has(id);
  };

  // 处理更新后的数据
  const handleUpdate = updatedCompetition => {
    const index = requests.value.findIndex(
      comp => comp.id === updatedCompetition.id
    );
    if (index !== -1) {
      requests.value[index] = updatedCompetition;
      showNotification({
        message: '竞赛信息已更新',
        type: 'success',
        duration: 3000,
      });
      toggleExpand(updatedCompetition.id);
    }
  };

  onMounted(() => {
    const authStore = useAuthStore();
    if (!authStore.isLoggedIn) {
      authStore.logout();
      return;
    }
    fetchRequests();
  });
</script>

<style scoped>
  /* 根据需要添加样式 */
</style>
