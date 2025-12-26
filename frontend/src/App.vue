<template>
  <div id="app">
    <h1>SPA на Vue.js</h1>
    <ItemList />
  </div>
</template>

<script>
import ItemList from './components/ItemList.vue';

export default {
  components: { ItemList }
};
</script>