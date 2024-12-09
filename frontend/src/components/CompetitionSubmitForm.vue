<template>
  <form class="max-w-4xl w-full mx-auto p-6 bg-gray-100 rounded-lg shadow">
    <div class="grid grid-cols-2 gap-6">
      <div>
        <label for="name" class="block text-sm font-medium text-gray-700"
          >竞赛名称</label
        >
        <div class="mt-1">
          <input
            type="text"
            id="name"
            v-model="formData.name"
            @input="validateName"
            class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            required
          />
          <span class="block text-red-500 text-xs mt-1" v-if="errors.name">{{
            errors.name
          }}</span>
        </div>
      </div>

      <div>
        <label for="website" class="block text-sm font-medium text-gray-700"
          >竞赛官网</label
        >
        <div class="mt-1">
          <input
            type="url"
            id="website"
            v-model="formData.website"
            @input="validateWebsite"
            class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            required
          />
          <span class="block text-red-500 text-xs mt-1" v-if="errors.website">{{
            errors.website
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
            v-model="formData.description"
            @input="validateDescription"
            class="block w-full px-3 py-2 h-32 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            required
          ></textarea>
          <span
            class="block text-red-500 text-xs mt-1"
            v-if="errors.description"
            >{{ errors.description }}</span
          >
        </div>
      </div>

      <div class="col-span-2">
        <label class="block text-sm font-medium text-gray-700">竞赛类型</label>
        <div class="mt-1">
          <div class="flex flex-wrap gap-2">
            <span
              v-for="(type, index) in formData.types"
              :key="index"
              class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm"
            >
              {{ type }}
              <button
                type="button"
                @click="removeType(index)"
                class="ml-1 text-red-500"
              >
                &times;
              </button>
            </span>
          </div>
          <input
            type="text"
            v-model="newType"
            @keyup.enter="addType"
            placeholder="输入竞赛类型并按回车添加，例如，计算机、数学"
            class="mt-2 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          />
          <span class="block text-red-500 text-xs mt-1" v-if="errors.types">{{
            errors.types
          }}</span>
        </div>
      </div>

      <div class="col-span-2">
        <label class="block text-sm font-medium text-gray-700">竞赛级别</label>
        <div class="mt-1">
          <div class="flex flex-wrap gap-2">
            <span
              v-for="(level, index) in formData.levels"
              :key="index"
              class="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm"
            >
              {{ level }}
              <button
                type="button"
                @click="removeLevel(index)"
                class="ml-1 text-red-500"
              >
                &times;
              </button>
            </span>
          </div>
          <input
            type="text"
            v-model="newLevel"
            @keyup.enter="addLevel"
            placeholder="输入竞赛级别并按回车添加，例如，国家级、省级"
            class="mt-2 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          />
          <span class="block text-red-500 text-xs mt-1" v-if="errors.levels">{{
            errors.levels
          }}</span>
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
              v-model="formData.start_time"
              @input="validateCompetitionStart"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              required
            />
            <span
              class="block text-red-500 text-xs mt-1"
              v-if="errors.competitionStart"
              >{{ errors.competitionStart }}</span
            >
          </div>

          <div class="relative">
            <span class="text-sm text-gray-600">比赛结束</span>
            <input
              type="date"
              id="competition-end"
              v-model="formData.end_time"
              @input="validateCompetitionEnd"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              required
            />
            <span
              class="block text-red-500 text-xs mt-1"
              v-if="errors.competitionEnd"
              >{{ errors.competitionEnd }}</span
            >
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
            v-model="formData.other_info"
            class="block w-full px-3 py-2 h-32 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          ></textarea>
        </div>
      </div>

      <div class="col-span-2">
        <button
          type="button"
          @click="submitForm"
          :disabled="hasErrors || isSubmitting"
          class="mt-6 w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          {{ isSubmitting ? '提交中...' : '提交' }}
        </button>
      </div>
    </div>
  </form>
</template>

<script setup>
  import { ref, computed } from 'vue';
  import showNotification from '@/utils/showNotification';
  import api from '@/utils/api';
  import { useRouter } from 'vue-router';

  const router = useRouter();

  const formData = ref({
    name: '',
    website: '',
    description: '',
    types: [],
    levels: [],
    start_time: '',
    end_time: '',
    other_info: '',
  });

  const newType = ref('');
  const newLevel = ref('');

  const errors = ref({
    name: '',
    website: '',
    description: '',
    types: '',
    levels: '',
    competitionStart: '',
    competitionEnd: '',
  });

  const hasErrors = computed(() => {
    return Object.values(errors.value).some(error => error);
  });

  const isSubmitting = ref(false);

  const validateName = () => {
    if (!formData.value.name.trim()) {
      errors.value.name = '竞赛名称不能为空';
    } else {
      errors.value.name = '';
    }
  };

  const validateWebsite = () => {
    const urlPattern = /^(https?:\/\/)?([\w-]+\.)+[\w-]+(\/[\w-]*)*$/;
    if (!formData.value.website.trim()) {
      errors.value.website = '竞赛官网不能为空';
    } else if (!urlPattern.test(formData.value.website.trim())) {
      errors.value.website = '请输入有效的URL';
    } else {
      errors.value.website = '';
    }
  };

  const validateDescription = () => {
    if (!formData.value.description.trim()) {
      errors.value.description = '竞赛描述不能为空';
    } else {
      errors.value.description = '';
    }
  };

  const validateTypes = () => {
    if (formData.value.types.length === 0) {
      errors.value.types = '至少添加一个竞赛类型';
    } else {
      errors.value.types = '';
    }
  };

  const validateLevels = () => {
    if (formData.value.levels.length === 0) {
      errors.value.levels = '至少添加一个竞赛级别';
    } else {
      errors.value.levels = '';
    }
  };

  const validateCompetitionStart = () => {
    if (!formData.value.start_time) {
      errors.value.competitionStart = '比赛开始日期不能为空';
    } else if (
      formData.value.end_time &&
      new Date(formData.value.start_time) > new Date(formData.value.end_time)
    ) {
      errors.value.competitionStart = '比赛开始日期不能晚于比赛结束日期';
    } else {
      errors.value.competitionStart = '';
    }
  };

  const validateCompetitionEnd = () => {
    if (!formData.value.end_time) {
      errors.value.competitionEnd = '比赛结束日期不能为空';
    } else if (
      formData.value.start_time &&
      new Date(formData.value.end_time) < new Date(formData.value.start_time)
    ) {
      errors.value.competitionEnd = '比赛结束日期不能早于比赛开始日期';
    } else {
      errors.value.competitionEnd = '';
    }
  };

  const addType = () => {
    const type = newType.value.trim();
    if (type && !formData.value.types.includes(type)) {
      formData.value.types.push(type);
      newType.value = '';
      validateTypes();
    }
  };

  const removeType = index => {
    formData.value.types.splice(index, 1);
    validateTypes();
  };

  const addLevel = () => {
    const level = newLevel.value.trim();
    if (level && !formData.value.levels.includes(level)) {
      formData.value.levels.push(level);
      newLevel.value = '';
      validateLevels();
    }
  };

  const removeLevel = index => {
    formData.value.levels.splice(index, 1);
    validateLevels();
  };

  const resetForm = () => {
    formData.value = {
      name: '',
      website: '',
      description: '',
      types: [],
      levels: [],
      start_time: '',
      end_time: '',
      other_info: '',
    };
    newType.value = '';
    newLevel.value = '';
    errors.value = {
      name: '',
      website: '',
      description: '',
      types: '',
      levels: '',
      competitionStart: '',
      competitionEnd: '',
    };
  };

  const submitForm = async () => {
    // 触发所有验证
    validateName();
    validateWebsite();
    validateDescription();
    validateTypes();
    validateLevels();
    validateCompetitionStart();
    validateCompetitionEnd();

    if (hasErrors.value) {
      showNotification({
        message: '请修正表单中的错误',
        type: 'error',
        duration: 3000,
      });
      return;
    }

    isSubmitting.value = true;

    try {
      const response = await api.post('/competition/submit/', {
        name: formData.value.name.trim(),
        website: formData.value.website.trim(),
        description: formData.value.description.trim(),
        types: formData.value.types,
        levels: formData.value.levels,
        timeline: {
          start_time: formData.value.start_time,
          end_time: formData.value.end_time,
        },
        other_info: formData.value.other_info.trim(),
      });

      if (response.status === 201) {
        showNotification({
          message: '竞赛投稿成功，等待审核',
          type: 'success',
          duration: 3000,
        });
        resetForm();
        router.push('/'); // 投稿成功后跳转到首页或其他页面
      } else {
        showNotification({
          message: '竞赛投稿失败，请稍后重试',
          type: 'error',
          duration: 3000,
        });
      }
    } catch (error) {
      console.error('竞赛投稿失败:', error);
      const errorMessage =
        error.response?.data?.error || '竞赛投稿失败，请稍后重试';
      showNotification({
        message: `竞赛投稿失败: ${errorMessage}`,
        type: 'error',
        duration: 3000,
      });
    } finally {
      isSubmitting.value = false;
    }
  };
</script>

<style scoped>
  /* 根据需要添加样式 */
  button {
    background: none;
    border: none;
    cursor: pointer;
  }
</style>
