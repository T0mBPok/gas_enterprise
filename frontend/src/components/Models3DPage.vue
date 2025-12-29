<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Models3DApi } from '../services/models3D'
import Model3DViewer from './model3DViewer.vue'
import Model3DCreate from './Model3DCreate.vue'

const models = ref([])
const selectedModel = ref(null)
const isCreating = ref(false)

const loadModels = async () => {
  const { data } = await Models3DApi.getAll()
  models.value = data
}

const selectModel = (model) => {
  selectedModel.value = model
  isCreating.value = false
}

const deleteModel = async (id: number) => {
  await Models3DApi.delete(id)
  await loadModels()
  selectedModel.value = null
}

const downloadModel = async () => {
  const res = await fetch(`/models/download/${selectedModel.value.id}`)

  const blob = await res.blob()
  const url = window.URL.createObjectURL(blob)

  const a = document.createElement('a')
  a.href = url
  a.download = `model_${selectedModel.value.id}.glb`
  document.body.appendChild(a)
  a.click()

  a.remove()
  window.URL.revokeObjectURL(url)
}

onMounted(loadModels)
</script>

<template>
  <div class="models3d-page">
    <!-- LEFT -->
    <aside class="sidebar">
      <button @click="isCreating = true">➕ Создать модель</button>

      <div
        v-for="m in models"
        :key="m.id"
        class="model-item"
        @click="selectModel(m)"
      >
        Модель #{{ m.id }} (скв. {{ m.well_id }})
        <button @click.stop="deleteModel(m.id)">🗑</button>
      </div>
    </aside>

    <!-- RIGHT -->
    <section class="content">
      <Model3DCreate
        v-if="isCreating"
        @created="loadModels"
      />

      <div v-else-if="selectedModel">
        <h3>Просмотр модели</h3>

        <Model3DViewer :modelId="selectedModel.id" />

        <button @click="downloadModel">
          Скачать
        </button>
      </div>

      <div v-else>
        Выбери модель или создай новую
      </div>
    </section>
  </div>
</template>

<style scoped>
.content {
  width: 100%;
}
.models3d-page {
  display: flex;
  height: 100%;
}
.sidebar {
  width: 260px;
  border-right: 1px solid #ddd;
  padding: 10px;
}
.model-item {
  cursor: pointer;
  padding: 6px;
}
.viewer {
  width: 100%;
  height: 500px;
  border: 1px solid #ccc;
}
</style>