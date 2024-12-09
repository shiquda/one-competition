<template>
  <div class="p-4 bg-gray-100 rounded-lg shadow-md">
    <form @submit.prevent="submitEdit">
      <div class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700"
            >竞赛名称</label
          >
          <input
            type="text"
            v-model="formData.name"
            @input="validateName"
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md text-black"
            required
          />
          <span class="block text-red-500 text-xs mt-1" v-if="errors.name">{{
            errors.name
          }}</span>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700"
            >竞赛类型</label
          >
          <input
            type="text"
            v-model="formData.types"
            @input="validateTypes"
            placeholder="使用逗号分隔，例如: 英语, 计算机"
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md text-black"
            required
          />
          <span class="block text-red-500 text-xs mt-1" v-if="errors.types">{{
            errors.types
          }}</span>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700"
            >竞赛级别</label
          >
          <input
            type="text"
            v-model="formData.levels"
            @input="validateLevels"
            placeholder="使用逗号分隔，例如: 国家级, 省级"
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md text-black"
            required
          />
          <span class="block text-red-500 text-xs mt-1" v-if="errors.levels">{{
            errors.levels
          }}</span>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">简介</label>
          <textarea
            v-model="formData.description"
            @input="validateDescription"
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md text-black"
            required
          ></textarea>
          <span
            class="block text-red-500 text-xs mt-1"
            v-if="errors.description"
            >{{ errors.description }}</span
          >
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700"
            >竞赛官网</label
          >
          <input
            type="url"
            v-model="formData.website"
            @input="validateWebsite"
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md text-black"
            required
          />
          <span class="block text-red-500 text-xs mt-1" v-if="errors.website">{{
            errors.website
          }}</span>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700"
            >其他信息</label
          >
          <textarea
            v-model="formData.other_info"
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md text-black"
          ></textarea>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700"
            >审核状态</label
          >
          <select
            v-model="formData.review_status"
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md text-black"
          >
            <option value="pending">待审核</option>
            <option value="approved">审核通过</option>
            <option value="rejected">审核拒绝</option>
          </select>
        </div>

        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700"
              >开始日期</label
            >
            <input
              type="date"
              v-model="formData.start_time"
              @input="validateCompetitionStart"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md text-black"
              required
            />
            <span
              class="block text-red-500 text-xs mt-1"
              v-if="errors.competition_start"
              >{{ errors.competition_start }}</span
            >
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700"
              >结束日期</label
            >
            <input
              type="date"
              v-model="formData.end_time"
              @input="validateCompetitionEnd"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md text-black"
              required
            />
            <span
              class="block text-red-500 text-xs mt-1"
              v-if="errors.competition_end"
              >{{ errors.competition_end }}</span
            >
          </div>
        </div>
      </div>

      <div class="mt-6 flex justify-end space-x-4">
        <button
          type="button"
          @click="cancelEdit"
          class="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600"
        >
          取消
        </button>
        <button
          type="submit"
          :disabled="hasErrors || isSubmitting"
          class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          {{ isSubmitting ? '保存中...' : '保存' }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
  import { ref, watch, computed } from 'vue';
  import showNotification from '@/utils/showNotification';
  import api from '@/utils/api';

  const props = defineProps({
    competition: {
      type: Object,
      required: true,
    },
    onUpdate: {
      type: Function,
      required: true,
    },
    onCancel: {
      type: Function,
      required: true,
    },
  });

  const isSubmitting = ref(false);

  console.log(props.competition.timeline);
  const formData = ref({
    id: props.competition.id || '',
    name: props.competition.name || '',
    types: props.competition.types ? props.competition.types.join(', ') : '',
    levels: props.competition.levels ? props.competition.levels.join(', ') : '',
    description: props.competition.description || '',
    website: props.competition.website || '',
    other_info: props.competition.other_info || '',
    review_status: props.competition.review_status || 'pending',
    start_time:
      props.competition.timeline?.find(t => t.node_name === 'start_time')
        ?.date || '',
    end_time:
      props.competition.timeline?.find(t => t.node_name === 'end_time')?.date ||
      '',
  });

  const errors = ref({
    name: '',
    types: '',
    levels: '',
    description: '',
    website: '',
    start_time: '',
    end_time: '',
  });

  const hasErrors = computed(() => {
    return Object.values(errors.value).some(error => error);
  });

  const resetErrors = () => {
    errors.value = {
      name: '',
      types: '',
      levels: '',
      description: '',
      website: '',
      start_time: '',
      end_time: '',
    };
  };

  watch(
    () => props.competition,
    newVal => {
      formData.value = {
        id: newVal.id || '',
        name: newVal.name || '',
        types: newVal.types ? newVal.types.join(', ') : '',
        levels: newVal.levels ? newVal.levels.join(', ') : '',
        description: newVal.description || '',
        website: newVal.website || '',
        other_info: newVal.other_info || '',
        review_status: newVal.review_status || 'pending',
        start_time:
          newVal.timeline?.find(t => t.node_name === 'start_time')?.date || '',
        end_time:
          newVal.timeline?.find(t => t.node_name === 'end_time')?.date || '',
      };
      console.log(formData);
      resetErrors();
    },
    { immediate: true }
  );

  const validateName = () => {
    if (!formData.value.name) {
      errors.value.name = '竞赛名称不能为空';
    } else {
      errors.value.name = '';
    }
  };

  const validateTypes = () => {
    if (!formData.value.types) {
      errors.value.types = '竞赛类型不能为空';
    } else {
      errors.value.types = '';
    }
  };

  const validateLevels = () => {
    if (!formData.value.levels) {
      errors.value.levels = '竞赛级别不能为空';
    } else {
      errors.value.levels = '';
    }
  };

  const validateDescription = () => {
    if (!formData.value.description) {
      errors.value.description = '简介不能为空';
    } else {
      errors.value.description = '';
    }
  };

  const validateWebsite = () => {
    const urlPattern = /^(https?:\/\/)?([\w-]+\.)+[\w-]+(\/[\w-]*)*$/;
    if (!formData.value.website) {
      errors.value.website = '竞赛官网不能为空';
    } else if (!urlPattern.test(formData.value.website)) {
      errors.value.website = '请输入有效的URL';
    } else {
      errors.value.website = '';
    }
  };

  const validateRegisterStart = () => {
    if (!formData.value.register_start) {
      errors.value.register_start = '报名开始日期不能为空';
    } else {
      errors.value.register_start = '';
      if (
        formData.value.register_end &&
        new Date(formData.value.register_start) >
          new Date(formData.value.register_end)
      ) {
        errors.value.register_start = '报名开始日期不能晚于报名结束日期';
      }
    }
  };

  const validateRegisterEnd = () => {
    if (!formData.value.register_end) {
      errors.value.register_end = '报名结束日期不能为空';
    } else {
      errors.value.register_end = '';
      if (
        formData.value.register_start &&
        new Date(formData.value.register_end) <
          new Date(formData.value.register_start)
      ) {
        errors.value.register_end = '报名结束日期不能早于报名开始日期';
      }
    }
  };

  const validateCompetitionStart = () => {
    if (!formData.value.start_time) {
      errors.value.start_time = '比赛开始日期不能为空';
    } else {
      errors.value.start_time = '';
      if (
        formData.value.register_end &&
        new Date(formData.value.start_time) <
          new Date(formData.value.register_end)
      ) {
        errors.value.start_time = '比赛开始日期不能早于报名结束日期';
      }
    }
  };

  const validateCompetitionEnd = () => {
    if (!formData.value.end_time) {
      errors.value.end_time = '比赛结束日期不能为空';
    } else {
      errors.value.end_time = '';
      if (
        formData.value.start_time &&
        new Date(formData.value.end_time) < new Date(formData.value.start_time)
      ) {
        errors.value.end_time = '比赛结束日期不能早于比赛开始日期';
      }
    }
  };

  const submitEdit = async () => {
    // 触发所有验证
    validateName();
    validateTypes();
    validateLevels();
    validateDescription();
    validateWebsite();

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
      const response = await api.put(
        `/competition/update/${formData.value.id}/`,
        {
          name: formData.value.name,
          types: formData.value.types.split(',').map(t => t.trim()),
          levels: formData.value.levels.split(',').map(l => l.trim()),
          description: formData.value.description,
          website: formData.value.website,
          other_info: formData.value.other_info,
          review_status: formData.value.review_status,
          timeline: [
            {
              node_name: 'start_time',
              date: formData.value.start_time,
            },
            {
              node_name: 'end_time',
              date: formData.value.end_time,
            },
          ],
        }
      );

      if (response.status !== 200) {
        throw new Error('更新失败');
      }

      const updatedData = response.data;
      showNotification({
        message: '竞赛信息已更新',
        type: 'success',
        duration: 3000,
      });
      props.onUpdate(updatedData.data);
    } catch (error) {
      console.error('更新失败:', error);
      showNotification({
        message: `更新失败: ${error.message}`,
        type: 'error',
        duration: 3000,
      });
    } finally {
      isSubmitting.value = false;
    }
  };

  const cancelEdit = () => {
    props.onCancel();
  };
</script>

<style scoped>
  /* 根据需要添加样式 */
</style>
