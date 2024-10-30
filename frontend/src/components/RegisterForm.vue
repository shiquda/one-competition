<template>
  <h1>注册</h1>
  <form>
    <label for="username">用户名</label>
    <input
      type="text"
      id="username"
      placeholder="请输入用户名"
      v-model="username"
    />

    <label for="email">邮箱</label>
    <span class="error">{{ emailError }}</span>
    <input
      type="email"
      id="email"
      placeholder="请输入邮箱"
      v-model="email"
      @input="validateEmail"
    />

    <label for="password">密码</label>
    <span class="error">{{ passwordError }}</span>
    <input
      type="password"
      id="password"
      placeholder="密码位数为8-32位，且包含大小写字母和数字"
      v-model="password"
      @input="validatePassword"
    />
    <!-- TODO: 邮箱验证 -->

    <button type="submit" @click.prevent="register">注册</button>
  </form>
</template>

<script setup>
  import { ref } from 'vue';

  const username = ref('');
  const email = ref('');
  const password = ref('');

  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  const passwordError = ref('');
  const emailError = ref('');

  const validatePassword = () => {
    if (!passwordRegex.test(password.value)) {
      passwordError.value = '密码位数为8-32位，且包含大小写字母和数字';
    } else {
      passwordError.value = ''; // 清空错误提示
    }
  };

  const validateEmail = () => {
    if (!emailRegex.test(email.value)) {
      emailError.value = '请输入正确的邮箱';
    } else {
      emailError.value = ''; // 清空错误提示
    }
  };

  const register = () => {
    validatePassword();
    validateEmail();
    if (passwordError.value || emailError.value) return;
    // TODO: 注册请求
    console.log(username.value, email.value, password.value);
  };
</script>

<style scoped>
  .error {
    color: #ff4d4f;
    font-size: 14px;
    margin-bottom: 12px;
    display: block;
  }

  input {
    width: 100%;
    max-width: 300px;
    margin-bottom: 16px;
    padding: 8px 12px;
    border: 1px solid #d9d9d9;
    border-radius: 4px;
    font-size: 14px;
    transition: all 0.3s;
    display: block;
    margin: 0 auto;
    margin-bottom: 12px;
    margin-top: 8px;
  }

  input:focus {
    border-color: #40a9ff;
    box-shadow: 0 0 0 2px rgba(24, 144, 255, 0.2);
    outline: none;
  }

  input:hover {
    border-color: #40a9ff;
  }

  button {
    margin-top: 12px;
    display: block;
    margin: 0 auto;
    padding: 8px 24px;
    width: 325px;
    border: none;
    border-radius: 4px;
    background-color: #40a9ff;
    color: #fff;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s;
    letter-spacing: 10px;
    text-align: center;
  }

  button:hover {
    background-color: #1890ff;
  }
</style>
