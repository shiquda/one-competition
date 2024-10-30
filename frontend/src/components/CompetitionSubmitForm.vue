<template>
  <form class="max-w-4xl w-full mx-auto p-6 bg-gray-100 rounded-lg shadow">
    <div class="grid grid-cols-2 gap-6">
      <div>
        <label for="title" class="block text-sm font-medium text-gray-700"
          >竞赛名称</label
        >
        <div class="mt-1">
          <input
            type="text"
            id="title"
            v-model="title"
            @input="validateTitle"
            class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          />
          <span class="block text-red-500 text-xs mt-1" v-if="errors.title">{{
            errors.title
          }}</span>
        </div>
      </div>

      <div>
        <label for="url" class="block text-sm font-medium text-gray-700"
          >竞赛官网</label
        >
        <div class="mt-1">
          <input
            type="text"
            id="url"
            v-model="url"
            @input="validateUrl"
            class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          />
          <span class="block text-red-500 text-xs mt-1" v-if="errors.url">{{
            errors.url
          }}</span>
        </div>
      </div>

      <div class="col-span-2">
        <label for="description" class="block text-sm font-medium text-gray-700"
          >竞赛描述</label
        >
        <div class="mt-1">
          <textarea
            id="description"
            v-model="description"
            @input="validateDescription"
            class="block w-full px-3 py-2 h-32 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          ></textarea>
          <span
            class="block text-red-500 text-xs mt-1"
            v-if="errors.description"
            >{{ errors.description }}</span
          >
        </div>
      </div>

      <div class="col-span-2">
        <label class="block text-sm font-medium text-gray-700">报名日期</label>
        <div class="flex space-x-4 mt-2">
          <div class="relative">
            <span class="text-sm text-gray-600">开始</span>
            <input
              type="date"
              id="register-start"
              v-model="registerStart"
              @input="validateRegisterStart"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
            <span
              class="block text-red-500 text-xs mt-1"
              v-if="errors.registerStart"
            >
              {{ errors.registerStart }}
            </span>
          </div>

          <div class="relative">
            <span class="text-sm text-gray-600">结束</span>
            <input
              type="date"
              id="register-end"
              v-model="registerEnd"
              @input="validateRegisterEnd"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
            <span
              class="block text-red-500 text-xs mt-1"
              v-if="errors.registerEnd"
            >
              {{ errors.registerEnd }}
            </span>
          </div>
        </div>
      </div>

      <div class="col-span-2">
        <label class="block text-sm font-medium text-gray-700">比赛日期</label>
        <div class="flex space-x-4 mt-2">
          <div class="relative">
            <span class="text-sm text-gray-600">比赛开始</span>
            <input
              type="date"
              id="competition-start"
              v-model="competitionStart"
              @input="validateCompetitionStart"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
            <span
              class="block text-red-500 text-xs mt-1"
              v-if="errors.competitionStart"
            >
              {{ errors.competitionStart }}
            </span>
          </div>

          <div class="relative">
            <span class="text-sm text-gray-600">比赛结束</span>
            <input
              type="date"
              id="competition-end"
              v-model="competitionEnd"
              @input="validateCompetitionEnd"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
            <span
              class="block text-red-500 text-xs mt-1"
              v-if="errors.competitionEnd"
            >
              {{ errors.competitionEnd }}
            </span>
          </div>
        </div>
      </div>

      <div class="col-span-2">
        <label for="other-info" class="block text-sm font-medium text-gray-700"
          >其他信息</label
        >
        <div class="mt-1">
          <textarea
            id="other-info"
            v-model="otherInfo"
            class="block w-full px-3 py-2 h-32 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          ></textarea>
        </div>
      </div>

      <div class="col-span-2">
        <button
          type="button"
          @click="submitForm"
          :disabled="hasErrors"
          class="mt-6 w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          提交
        </button>
      </div>
    </div>
  </form>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue';
  import showNotification from '@/utils/showNotification';

  const title = ref('');
  const description = ref('');
  const url = ref('');
  const registerStart = ref('');
  const registerEnd = ref('');
  const competitionStart = ref('');
  const competitionEnd = ref('');
  const otherInfo = ref('');

  const errors = ref({
    title: '',
    description: '',
    url: '',
    registerStart: '',
    registerEnd: '',
    competitionStart: '',
    competitionEnd: '',
  });

  const hasErrors = computed(() => {
    return Object.values(errors.value).some(error => error);
  });

  onMounted(() => {
    validateTitle();
    validateDescription();
    validateUrl();
    validateRegisterStart();
    validateRegisterEnd();
    validateCompetitionStart();
    validateCompetitionEnd();
  });

  const validateTitle = () => {
    if (!title.value) {
      errors.value.title = '竞赛名称不能为空';
    } else {
      errors.value.title = '';
    }
  };

  const validateDescription = () => {
    if (!description.value) {
      errors.value.description = '竞赛描述不能为空';
    } else {
      errors.value.description = '';
    }
  };

  const validateUrl = () => {
    const urlPattern = /^(https?:\/\/)?([\w-]+\.)+[\w-]+(\/[\w-]*)*$/;
    if (!url.value) {
      errors.value.url = '竞赛官网不能为空';
    } else if (!urlPattern.test(url.value)) {
      errors.value.url = '请输入有效的URL';
    } else {
      errors.value.url = '';
    }
  };

  const validateRegisterStart = () => {
    if (!registerStart.value) {
      errors.value.registerStart = '报名开始日期不能为空';
    } else {
      errors.value.registerStart = '';
    }
  };

  const validateRegisterEnd = () => {
    if (!registerEnd.value) {
      errors.value.registerEnd = '报名结束日期不能为空';
    } else if (new Date(registerEnd.value) < new Date(registerStart.value)) {
      errors.value.registerEnd = '结束日期不能早于开始日期';
    } else {
      errors.value.registerEnd = '';
    }
  };

  const validateCompetitionStart = () => {
    if (!competitionStart.value) {
      errors.value.competitionStart = '比赛开始日期不能为空';
    } else if (new Date(competitionStart.value) < new Date(registerEnd.value)) {
      errors.value.competitionStart = '比赛开始日期不能早于报名结束日期';
    } else {
      errors.value.competitionStart = '';
    }
  };

  const validateCompetitionEnd = () => {
    if (!competitionEnd.value) {
      errors.value.competitionEnd = '比赛结束日期不能为空';
    } else if (
      new Date(competitionEnd.value) < new Date(competitionStart.value)
    ) {
      errors.value.competitionEnd = '比赛结束日期不能早于比赛开始日期';
    } else {
      errors.value.competitionEnd = '';
    }
  };

  const submitForm = () => {
    if (hasErrors.value) {
      showNotification({
        message: '请修正表单中的错误',
        type: 'error',
        duration: 3000,
      });
      return;
    }

    // 模拟表单提交
    console.log({
      title: title.value,
      description: description.value,
      url: url.value,
      registerStart: registerStart.value,
      registerEnd: registerEnd.value,
      competitionStart: competitionStart.value,
      competitionEnd: competitionEnd.value,
      otherInfo: otherInfo.value,
    });

    const success = true;

    if (success) {
      showNotification({
        message: '表单提交成功！',
        type: 'success',
        duration: 3000,
      });
    } else {
      showNotification({
        message: '表单提交失败！',
        type: 'error',
        duration: 3000,
      });
    }

    // 重置表单
    title.value = '';
    description.value = '';
    url.value = '';
    registerStart.value = '';
    registerEnd.value = '';
    competitionStart.value = '';
    competitionEnd.value = '';
    otherInfo.value = '';
  };
</script>

<style scoped>
  /* 样式通过 Tailwind CSS 完成，无需额外样式 */
</style>
