<template>
  <div class="admin-container max-w-screen-xl mx-auto p-6 space-y-8">
    <!-- Header -->
    <header class="text-center mb-6">
      <h1 class="text-3xl font-bold">审核管理</h1>
      <p class="text-lg text-gray-500">在此页面管理用户提交的审核请求</p>
    </header>

    <!-- 审核请求表格 -->
    <table class="min-w-full table-auto bg-gray-800 text-white rounded-lg shadow-md">
      <thead>
        <tr>
          <th class="py-3 px-4">ID</th>
          <th class="py-3 px-4">用户</th>
          <th class="py-3 px-4">提交内容</th>
          <th class="py-3 px-4">状态</th>
          <th class="py-3 px-4">操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(request, index) in requests" :key="request.id">
          <td class="py-3 px-4">{{ request.id }}</td>
          <td class="py-3 px-4">{{ request.user }}</td>
          <td class="py-3 px-4">{{ request.content }}</td>
          <td class="py-3 px-4">
            <span :class="{
              'bg-green-500': request.status === 'approved',
              'bg-red-500': request.status === 'rejected',
              'bg-yellow-500': request.status === 'pending'
            }" class="px-3 py-1 rounded text-white">
              {{ request.status }}
            </span>
          </td>
          <td class="py-3 px-4 space-x-2">
            <button @click="approveRequest(request.id)" class="bg-green-500 px-4 py-2 rounded text-white hover:bg-green-600" v-if="request.status === 'pending'">通过</button>
            <button @click="rejectRequest(request.id)" class="bg-red-500 px-4 py-2 rounded text-white hover:bg-red-600" v-if="request.status === 'pending'">拒绝</button>
            <button @click="editRequest(request)" class="bg-blue-500 px-4 py-2 rounded text-white hover:bg-blue-600">修改</button>
            <button @click="revokeRequest(request.id)" class="bg-gray-500 px-4 py-2 rounded text-white hover:bg-gray-600" v-if="request.status !== 'pending'">撤回</button>
            <button @click="viewDetails(request)" class="bg-yellow-500 px-4 py-2 rounded text-white hover:bg-yellow-600">详情</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- 模态框（修改表单） -->
    <div v-if="isEditModalVisible" class="fixed inset-0 flex justify-center items-center bg-black bg-opacity-50">
      <div class="bg-white p-6 rounded-lg w-1/2 max-h-80vh overflow-y-auto">
        <h2 class="text-2xl font-semibold mb-4">修改请求</h2>
        <div class="space-y-4">
          <div>
            <label class="font-bold">用户:</label>
            <input v-model="editableRequest.user" class="w-full p-2 border rounded" />
          </div>
          <div>
            <label class="font-bold">提交内容:</label>
            <textarea v-model="editableRequest.content" class="w-full p-2 border rounded"></textarea>
          </div>
          <div>
            <label class="font-bold">竞赛名称:</label>
            <input v-model="editableRequest.title" class="w-full p-2 border rounded" />
          </div>
          <div>
            <label class="font-bold">竞赛官网:</label>
            <input v-model="editableRequest.url" class="w-full p-2 border rounded" />
          </div>
          <div>
            <label class="font-bold">竞赛描述:</label>
            <textarea v-model="editableRequest.description" class="w-full p-2 border rounded"></textarea>
          </div>
        </div>
        <div class="mt-6 text-right">
          <button @click="saveEdit" class="bg-green-500 px-4 py-2 rounded text-white hover:bg-green-600">保存并通过</button>
          <button @click="closeEditModal" class="bg-gray-500 px-4 py-2 rounded text-white hover:bg-gray-600">取消</button>
        </div>
      </div>
    </div>

    <!-- 模态框（详情查看） -->
    <div v-if="isModalVisible" class="fixed inset-0 flex justify-center items-center bg-black bg-opacity-50">
      <div class="bg-white p-6 rounded-lg w-1/2 max-h-80vh overflow-y-auto">
        <h2 class="text-2xl font-semibold mb-4">请求详情</h2>
        <div class="space-y-4">
          <div><strong>ID:</strong> {{ selectedRequest.id }}</div>
          <div><strong>用户:</strong> {{ selectedRequest.user }}</div>
          <div><strong>提交内容:</strong> {{ selectedRequest.content }}</div>
          <div><strong>竞赛名称:</strong> {{ selectedRequest.title }}</div>
          <div><strong>竞赛官网:</strong> {{ selectedRequest.url }}</div>
          <div><strong>竞赛描述:</strong> {{ selectedRequest.description }}</div>
        </div>
        <div class="mt-6 text-right">
          <button @click="closeModal" class="bg-gray-500 px-4 py-2 rounded text-white hover:bg-gray-600">关闭</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      requests: [
        { id: 1, user: "张三", content: "提交了一个新功能请求", status: "pending", title: "AI挑战赛", url: "https://competition.ai", description: "一个关于AI的竞赛" },
        { id: 2, user: "李四", content: "提交了一个Bug报告", status: "pending", title: "编程挑战", url: "https://coding.com", description: "一场编程比赛" },
        // 其他请求...
      ],
      isModalVisible: false,
      isEditModalVisible: false,
      selectedRequest: {},
      editableRequest: {},
    };
  },
  methods: {
    approveRequest(id) {
      const request = this.requests.find(req => req.id === id);
      if (request) request.status = "approved";
    },
    rejectRequest(id) {
      const request = this.requests.find(req => req.id === id);
      if (request) request.status = "rejected";
    },
    editRequest(request) {
      this.editableRequest = { ...request };
      this.isEditModalVisible = true;
    },
    saveEdit() {
      const request = this.requests.find(req => req.id === this.editableRequest.id);
      Object.assign(request, this.editableRequest, { status: "approved" });
      this.isEditModalVisible = false;
    },
    revokeRequest(id) {
      const request = this.requests.find(req => req.id === id);
      if (request) request.status = "pending";
    },
    viewDetails(request) {
      this.selectedRequest = request;
      this.isModalVisible = true;
    },
    closeEditModal() {
      this.isEditModalVisible = false;
    },
    closeModal() {
      this.isModalVisible = false;
    },
  },
};
</script>