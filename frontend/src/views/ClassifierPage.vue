<template>
  <div>
    <h2>{{ classifier }}</h2>

    <button v-if="!editing" @click="startCreate">Добавить</button>

    <div v-if="editing" class="modal">
        <div class="modal-content">
            <ItemForm
            :editableItem="current"
            @save="save"
            @cancel="cancel"
            />
        </div>
    </div>

    <ItemView
      v-for="item in items"
      :key="item.id"
      :entity="item"
      @edit="edit"
      @delete="remove"
    />
  </div>
</template>

<script>
import ItemForm from '@/components/ItemForm.vue'
import ItemView from '@/components/ItemView.vue'
import { createEntityApi } from '@/services/api'

export default {
  components: { ItemForm, ItemView },

  data() {
    return {
      items: [],
      editing: false,
      current: {},
      api: null,
    }
  },

  computed: {
    classifier() {
      return this.$route.params.classifier
    },
  },

  watch: {
    classifier: {
      immediate: true,
      handler(val) {
        // создаём API объект для конкретного классификатора
        this.api = createEntityApi('classifiers', val)
        this.load()
      },
    },
  },

  methods: {
    load() {
      this.api.fetchAll().then(r => this.items = r.data).catch(console.error)
    },

    startCreate() {
      this.current = {}
      this.editing = true
    },

    edit(item) {
      this.current = item
      this.editing = true
    },

    cancel() {
      this.editing = false
    },

    save(payload) {
      const req = payload.id
        ? this.api.update(payload)
        : this.api.create(payload)

      req.then(() => {
        this.editing = false
        this.load()
      }).catch(console.error)
    },

    remove(id) {
      this.api.delete(id).then(this.load).catch(console.error)
    },
  },
}
</script>