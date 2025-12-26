<template>
  <div>
    <button
      v-if="!isCreating && !editingWell"
      @click="startCreating"
    >
      Add well
    </button>

   <ItemForm
      v-if="isCreating"
      :editableWell="{}"
      @save="addWell"
      @cancel="cancelCreating"
    />

    <ItemForm
      v-if="editingWell"
      :editableWell="editingWell"
      @save="updateWell"
      @cancel="cancelEdit"
    />

    <div v-if="!isCreating && !editingWell">
      <ItemView
        v-for="well in wells"
        :key="well.id"
        :entity="well"
        @edit="startEdit"
        @delete="deleteWell"
      />
    </div>
  </div>
</template>

<script>
import ItemView from './ItemView.vue'
import ItemForm from './ItemForm.vue'
import {
  fetchWells,
  createWell,
  updateWell,
  deleteWell,
} from '../api.js'

export default {
  components: { ItemView, ItemForm },

  data() {
    return {
      wells: [],
      editingWell: null,
      isCreating: false,
    }
  },

  created() {
    fetchWells()
      .then(res => {
        this.wells = res.data
      })
      .catch(console.error)
  },

  methods: {
    startCreating() {
      this.isCreating = true
    },

    cancelCreating() {
      this.isCreating = false
    },

    addWell(payload) {
      createWell(payload)
        .then(res => {
          this.wells.push(res.data)
          this.isCreating = false
        })
        .catch(console.error)
    },

    updateWell(payload) {
      updateWell({ ...payload, id: this.editingWell.id })
        .then(res => {
          this.wells = this.wells.map(w =>
            w.id === this.editingWell.id ? res.data : w
          )
          this.editingWell = null
        })
        .catch(console.error)
    },

    deleteWell(id) {
      deleteWell(id)
        .then(() => {
          this.wells = this.wells.filter(w => w.id !== id)
        })
        .catch(console.error)
    },

    startEdit(well) {
      this.editingWell = well
    },

    cancelEdit() {
      this.editingWell = null
    },
  },
}
</script>