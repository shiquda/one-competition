<template>
  <!-- 表单信息和提交按钮 -->

  <form>
    <div class="form-container">
      <label for="title">竞赛名称</label>
      <input type="text" id="title" />
      <label for="description">竞赛描述</label>
      <textarea id="description"></textarea>
      <label for="url">竞赛官网</label>
      <input type="text" id="url" />
      <label for="deadline">报名日期</label>
      <div class="date-container">
        <span>报名开始</span>
        <input type="date" id="register-start" />
        <span>报名结束</span>
        <input type="date" id="register-end" />
      </div>
      <label for="deadline">比赛日期</label>
      <div class="date-container">
        <span>比赛开始</span>
        <input type="date" id="competition-start" />
        <span>比赛结束</span>
        <input type="date" id="competition-end" />
      </div>
      <label for="other-info">其他备注</label>
      <textarea id="other-info"></textarea>
    </div>
    <button type="submit">提交</button>
  </form>
</template>

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
</style>

<script>
  export default {
    name: 'CompetitionSubmitForm',
  };
</script>
