<template>
  <li>
    <RouterLink
      :to="to"
      class="menu-item"
      active-class="active"
    >
      {{ label }}
    </RouterLink>
  </li>
</template>

<script setup>
defineProps({
  to: { type: String, required: true },
  label: { type: String, required: true }
})
</script>

<style scoped>
.menu-item {
  display: block;
  padding: 10px 12px;
  color: #ddd;
  text-decoration: none;
  border-radius: 6px;
  transition: background 0.2s;
}

.menu-item:hover {
  background: #2a2a40;
}

.active {
  background: #3b82f6;
  color: #fff;
}
</style>