<template>
  <h1>登录</h1>
  <form>
    <label for="username">用户名/邮箱</label>
    <input
      type="text"
      id="username"
      placeholder="请输入用户名或邮箱"
      v-model="username"
    />

    <label for="password">密码</label>
    <input
      type="password"
      id="password"
      placeholder="请输入密码"
      v-model="password"
    />

    <span class="error" v-if="passwordError">{{ passwordError }}</span>
    <button type="submit" @click="login" @click.prevent="login">登录</button>
    <p>还没有账号？<router-link to="/register">注册</router-link></p>
  </form>
</template>

<script setup>
  import { ref } from 'vue';
  import showNotification from '@/utils/showNotification';
  import { useRouter } from 'vue-router';

  const router = useRouter();

  const username = ref('');
  const password = ref('');

  const login = () => {
    console.log(username.value, password.value);

    // test
    const success = true;
    if (success) {
      showNotification({
        message: '登录成功！将自动跳转至首页',
        type: 'success',
        duration: 2000,
      });
      setTimeout(() => {
        router.push('/'); // 使用 router 实例进行路由跳转
      }, 2500);
    } else {
      showNotification({
        message: '登录失败！请稍后再试',
        type: 'error',
        duration: 3000,
      });
    }
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

  a {
    color: #40a9ff;
    text-decoration: none;
    font-weight: bold;
  }
</style>
