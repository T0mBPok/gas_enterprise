<template>
  <div>
    <button
      v-if="!isCreating && !editingItem"
      @click="startCreating"
    >
      Add item
    </button>

    <ItemForm
      v-if="isCreating"
      :editableItem="{}"
      @save="addItem"
      @cancel="cancelCreating"
    />

    <ItemForm
      v-if="editingItem"
      :editableItem="editingItem"
      @save="updateItem"
      @cancel="cancelEdit"
    />

    <div v-if="!isCreating && !editingItem">
      <ItemView
        v-for="item in items"
        :key="item.id"
        :entity="item"
        @edit="startEdit"
        @delete="deleteItem"
      />
    </div>
  </div>
</template>

<script>
import ItemView from './ItemView.vue'
import ItemForm from './ItemForm.vue'
import { createEntityApi } from "../services/api.js";

// создаем API объект для Items
const entity = computed(() => route.params.entity)
const itemsApi = createEntityApi(entity);

export default {
  components: { ItemView, ItemForm },

  data() {
    return {
      items: [],
      editingItem: null,
      isCreating: false,
    }
  },

  created() {
    this.fetchItems();
  },

  methods: {
    fetchItems() {
      itemsApi.fetchAll()
        .then(res => {
          this.items = res.data;
        })
        .catch(console.error);
    },

    startCreating() {
      this.isCreating = true;
    },

    cancelCreating() {
      this.isCreating = false;
    },

    addItem(payload) {
      itemsApi.create(payload)
        .then(res => {
          this.items.push(res.data);
          this.isCreating = false;
        })
        .catch(console.error);
    },

    updateItem(payload) {
      itemsApi.update({ ...payload, id: this.editingItem.id })
        .then(res => {
          this.items = this.items.map(w =>
            w.id === this.editingItem.id ? res.data : w
          );
          this.editingItem = null;
        })
        .catch(console.error);
    },

    deleteItem(id) {
      itemsApi.delete(id)
        .then(() => {
          this.items = this.items.filter(w => w.id !== id);
        })
        .catch(console.error);
    },

    startEdit(item) {
      this.editingItem = item;
    },

    cancelEdit() {
      this.editingItem = null;
    },
  },
}
</script>