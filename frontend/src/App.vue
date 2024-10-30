<script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import Footer from '@/components/Footer.vue';
  import Header from '@/components/Header.vue';
  import NotificationContainer from '@/components/NotificationContainer.vue';

  const isTransitioning = ref(false);
  const router = useRouter();

  const handleBeforeLeave = () => {
    isTransitioning.value = true;
  };

  const handleLeave = () => {
    setTimeout(() => {
      isTransitioning.value = false;
    }, 20); // 延迟防止闪烁
  };

  const handleAfterEnter = () => {
    // 其他需要在新页面进入后执行的操作
  };

  onMounted(() => {
    router.afterEach(() => {
      if (isTransitioning.value) {
        router.go(0); // 重新加载当前页面
      }
    });
  });
</script>

<template>
  <div id="app" class="min-h-screen flex flex-col">
    <Header />

    <main class="flex-grow mt-16 overflow-y-auto">
      <transition
        name="fade"
        mode="out-in"
        @before-leave="handleBeforeLeave"
        @leave="handleLeave"
        @after-enter="handleAfterEnter"
      >
        <router-view v-if="!isTransitioning"></router-view>
      </transition>
    </main>

    <NotificationContainer />
    <Footer />
  </div>
</template>

<style>
  .fade-enter-active {
    transition: opacity 0.5s ease;
  }
  .fade-enter-from {
    opacity: 0;
  }
</style>
