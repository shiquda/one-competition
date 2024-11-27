<template>
  <div id="app" class="max-w-screen-lg mx-auto p-6 space-y-8">
    <!-- Header -->
    <header class="text-center">
      <h1 class="text-4xl font-bold">个人中心</h1>
    </header>

    <!-- 用户信息卡 -->
    <div class="card bg-gray-800 text-white rounded-lg p-6 shadow-md">
      <h2 class="text-2xl font-semibold mb-4">用户信息</h2>
      <p><strong>用户ID：</strong> {{ user.id }}</p>
      <p><strong>邮箱：</strong> {{ user.email }}</p>
    </div>

    <!-- 重置密码组件 -->
    <div class="card bg-gray-800 text-white rounded-lg p-6 shadow-md">
      <h2 class="text-2xl font-semibold mb-4">重置密码</h2>
      <form @submit.prevent="resetPassword" class="space-y-4">
        <div>
          <label for="current-password" class="block text-sm font-medium">当前密码：</label>
          <input
            type="password"
            id="current-password"
            v-model="passwords.current"
            class="w-full p-2 mt-1 border rounded-lg bg-gray-900 border-gray-600 focus:outline-none focus:ring focus:ring-blue-500"
            required
          />
        </div>

        <div>
          <label for="new-password" class="block text-sm font-medium">新密码：</label>
          <input
            type="password"
            id="new-password"
            v-model="passwords.new"
            class="w-full p-2 mt-1 border rounded-lg bg-gray-900 border-gray-600 focus:outline-none focus:ring focus:ring-blue-500"
            required
          />
        </div>

        <div>
          <label for="confirm-password" class="block text-sm font-medium">确认新密码：</label>
          <input
            type="password"
            id="confirm-password"
            v-model="passwords.confirm"
            class="w-full p-2 mt-1 border rounded-lg bg-gray-900 border-gray-600 focus:outline-none focus:ring focus:ring-blue-500"
            required
          />
        </div>

        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-500"
        >
          提交
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        id: "123456",
        email: "user@example.com",
      },
      passwords: {
        current: "",
        new: "",
        confirm: "",
      },
    };
  },
  methods: {
    resetPassword() {
      // 简单验证：新密码和确认密码是否一致
      if (this.passwords.new !== this.passwords.confirm) {
        alert("新密码与确认密码不一致！");
        return;
      }

      // 模拟提交逻辑
      alert(`密码重置成功！新密码：${this.passwords.new}`);
      // 清空输入框
      this.passwords.current = "";
      this.passwords.new = "";
      this.passwords.confirm = "";
    },
  },
};
</script>

<style scoped>
/* 仅保留样式隔离作用 */
</style>
