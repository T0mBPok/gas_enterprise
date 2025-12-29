<template>
  <div>
    <FilterPanel
      v-if="entityConfig && !isCreating && !editingItem"
      :fields="entityConfig.fields"
      @apply="applyFilters"
    />

    <button
      v-if="entityConfig && !isCreating && !editingItem"
      @click="startCreating"
    >
      Add {{ entity }}
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
    <div v-if="entityConfig?.export && entityConfig && !isCreating && !editingItem">
      <button @click="download('xlsx')">⬇ XLSX</button>
      <button @click="download('pdf')">⬇ PDF</button>
    </div>
  </div>
</template>

<script>
import { createEntityApi } from '@/services/api'
import ItemView from '../components/ItemView.vue'
import ItemForm from '../components/ItemForm.vue'
import FilterPanel from '@/components/FilterPanel.vue';
import { entityFormConfig } from '@/config/entityFormConfig';

export default {
  components: { ItemView, ItemForm, FilterPanel },

  data() {
    return {
      items: [],
      filters: {},
      editingItem: null,
      isCreating: false,
      api: null,
    }
  },

  computed: {
    entity() {
      return this.$route.params.entity
    },
    entityConfig() {
      return entityFormConfig[this.entity] || null
    },
  },

  watch: {
    entity: {
      immediate: true,
      handler(newEntity) {
        this.api = createEntityApi(newEntity)
        this.fetchItems()
      },
    },
  },

  methods: {
    applyFilters(filters) {
      this.filters = filters
      this.fetchItems()
    },

    fetchItems() {
      const params = Object.fromEntries(
        Object.entries(this.filters)
          .filter(([_, v]) => v !== null && v !== '' && v !== undefined)
      )

      this.api.fetchAll(params)
        .then(res => {
          this.items = res.data
        })
        .catch(console.error)
    },

    startCreating() {
      this.isCreating = true
    },

    cancelCreating() {
      this.isCreating = false
    },

    addItem(payload) {
      this.api.create(payload)
        .then(res => {
          this.items.push(res.data)
          this.isCreating = false
        })
        .catch(console.error)
    },

    updateItem(payload) {
      this.api.update({ ...payload, id: this.editingItem.id })
        .then(res => {
          this.items = this.items.map(i =>
            i.id === this.editingItem.id ? res.data : i
          )
          this.editingItem = null
        })
        .catch(console.error)
    },

    deleteItem(id) {
      this.api.delete(id)
        .then(() => {
          this.items = this.items.filter(i => i.id !== id)
        })
        .catch(console.error)
    },

    startEdit(item) {
      this.editingItem = item
    },

    cancelEdit() {
      this.editingItem = null
    },
    download(format) {
      // отфильтруем пустые фильтры
      const filtered = Object.fromEntries(
        Object.entries(this.filters)
          .filter(([_, v]) => v !== null && v !== '' && v !== undefined)
      )

      // добавим format
      const params = { ...filtered, format }

      this.api.export(params, format, { responseType: 'blob' })
        .then(res => {
          const blob = new Blob([res.data])
          const url = window.URL.createObjectURL(blob)

          const a = document.createElement('a')
          a.href = url
          a.download = `${this.entity}.${format}`
          a.click()

          URL.revokeObjectURL(url)
        })
        .catch(err => {
          console.error(err)
          alert('Ошибка экспорта')
        })
      }
  },
}
</script>