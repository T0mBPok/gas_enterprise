<template>
  <div class="layout">
    <Sidebar />

    <main class="content">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import Sidebar from '../components/Sidebar.vue'
</script>

<style scoped>
.layout {
  display: flex;
  min-height: 100vh;
}

.content {
  flex: 1;
  padding: 24px;
  overflow-y: auto;
  background: #f5f6fa;
}
</style>