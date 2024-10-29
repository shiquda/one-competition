<template>
  <!-- 表单信息和提交按钮 -->

  <form>
    <div class="form-container">
      <label for="title">竞赛名称</label>
      <div class="input-container">
        <span class="error" v-if="errors.title">{{ errors.title }}</span>
        <input type="text" id="title" v-model="title" @input="validateTitle" />
      </div>

      <label for="description">竞赛描述</label>
      <div class="input-container">
        <span class="error" v-if="errors.description">{{
          errors.description
        }}</span>
        <textarea
          id="description"
          v-model="description"
          @input="validateDescription"
        ></textarea>
      </div>

      <label for="url">竞赛官网</label>
      <div class="input-container">
        <span class="error" v-if="errors.url">{{ errors.url }}</span>
        <input type="text" id="url" v-model="url" @input="validateUrl" />
      </div>

      <label for="deadline">报名日期</label>
      <div class="date-container">
        <span>报名开始</span>
        <span class="error" v-if="errors.registerStart">{{
          errors.registerStart
        }}</span>
        <input
          type="date"
          id="register-start"
          v-model="registerStart"
          @input="validateRegisterStart"
        />

        <span>报名结束</span>
        <span class="error" v-if="errors.registerEnd">{{
          errors.registerEnd
        }}</span>
        <input
          type="date"
          id="register-end"
          v-model="registerEnd"
          @input="validateRegisterEnd"
        />
      </div>
      <label for="deadline">比赛日期</label>
      <div class="date-container">
        <span>比赛开始</span>
        <span class="error" v-if="errors.competitionStart">{{
          errors.competitionStart
        }}</span>
        <input
          type="date"
          id="competition-start"
          v-model="competitionStart"
          @input="validateCompetitionStart"
        />

        <span>比赛结束</span>
        <span class="error" v-if="errors.competitionEnd">{{
          errors.competitionEnd
        }}</span>
        <input
          type="date"
          id="competition-end"
          v-model="competitionEnd"
          @input="validateCompetitionEnd"
        />
      </div>
      <label for="other-info">其他备注</label>
      <textarea id="other-info" v-model="otherInfo"></textarea>
    </div>
    <button type="submit" @click.prevent="submitForm" :disabled="hasErrors">
      提交
    </button>
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
      errors.value.title = '请输入竞赛名称';
    } else {
      errors.value.title = '';
    }
  };

  const validateDescription = () => {
    if (!description.value) {
      errors.value.description = '请输入竞赛描述';
    } else {
      errors.value.description = '';
    }
  };

  const validateUrl = () => {
    if (url.value && !/^https?:\/\//.test(url.value)) {
      errors.value.url = '请输入正确的网址';
    } else {
      errors.value.url = '';
    }
  };

  const validateRegisterStart = () => {
    if (!registerStart.value) {
      errors.value.registerStart = '请选择报名开始日期';
    } else {
      errors.value.registerStart = '';
    }
  };

  const validateRegisterEnd = () => {
    if (!registerEnd.value) {
      errors.value.registerEnd = '请选择报名结束日期';
    } else {
      errors.value.registerEnd = '';
    }
  };

  const validateCompetitionStart = () => {
    if (!competitionStart.value) {
      errors.value.competitionStart = '请选择比赛开始日期';
    } else {
      errors.value.competitionStart = '';
    }
  };

  const validateCompetitionEnd = () => {
    if (!competitionEnd.value) {
      errors.value.competitionEnd = '请选择比赛结束日期';
    } else {
      errors.value.competitionEnd = '';
    }
  };

  const submitForm = () => {
    // 如果没有错误,则提交表单
    if (!hasErrors.value) {
      // TODO: 发送表单数据到服务器，并处理响应

      // 显示通知
      showNotification({
        message: '表单提交成功！3 秒后将自动刷新页面',
        type: 'success',
      });

      setTimeout(() => {
        window.location.reload();
      }, 3000);
    } else {
      // 显示通知
      showNotification({
        message: '表单有错误，请检查填写信息！',
        type: 'error',
      });
    }
  };
</script>

<style scoped>
  form {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f8f8f8;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }

  .form-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }

  .form-container > * {
    flex: 1 1 50%;
    box-sizing: border-box;
    padding-right: 20px;
    margin-bottom: 20px;
  }

  .date-container {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .date-container > span {
    margin-right: 20px;
  }

  .date-container > input {
    margin-right: 20px;
  }

  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: #333;
  }

  input[type='text'],
  textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
    color: #333;
  }

  textarea {
    height: 120px;
    resize: vertical;
  }

  button {
    display: block;
    width: 100%;
    max-width: 200px;
    margin: 20px auto 0;
    padding: 10px;
    border: none;
    border-radius: 5px;
    background-color: #1890ff;
    color: #fff;
    font-size: 18px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  button:hover {
    background-color: #40a9ff;
  }

  button[disabled] {
    background-color: #ccc;
    cursor: not-allowed;
  }

  .error {
    color: red;
    font-size: 12px;
    margin-top: 5px;
  }

  .input-container {
    position: relative;
  }

  .error {
    position: absolute;
    top: -20px;
    left: 0;
    color: red;
  }
</style>
