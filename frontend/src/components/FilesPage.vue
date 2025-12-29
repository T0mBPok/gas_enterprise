<template>
  <div class="files-page">
    <h2>Файлы</h2>

    <!-- Upload -->
    <div class="upload-box">
      <input
        type="file"
        multiple
        @change="onFileChange"
        accept=".csv,.xlsx,.png,.jpg,.jpeg,.pdf"
      />
      <button @click="upload" :disabled="!selectedFiles.length">
        Загрузить
      </button>
    </div>

    <!-- Files list -->
    <div v-if="files.length" class="files-list">
      <div
        v-for="file in files"
        :key="file.id"
        class="file-row"
      >
        <span class="file-name">{{ file.original_name }}</span>

        <div class="actions">
          <button @click="download(file.id)">Скачать</button>
          <button class="danger" @click="remove(file.id)">Удалить</button>
        </div>
      </div>
    </div>

    <div v-else class="empty">
      Файлов пока нет
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'

const files = ref([])
const selectedFiles = ref([])

const loadFiles = async () => {
  const { data } = await api.get('/files')
  files.value = data
}

onMounted(loadFiles)

const onFileChange = (e) => {
  selectedFiles.value = Array.from(e.target.files)
}

const upload = async () => {
  const formData = new FormData()

  selectedFiles.value.forEach(file => {
    formData.append('file', file)
  })

  await api.post('/files/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })

  selectedFiles.value = []
  await loadFiles()
}

const download = (id) => {
  window.open(`http://localhost:9000/files/download/${id}`, '_blank')
}

const remove = async (id) => {
  if (!confirm('Удалить файл?')) return
  await api.delete(`/files/${id}`)
  await loadFiles()
}
</script>

<style scoped>
.files-page {
  padding: 24px;
  background: #f8fafc;
  height: 100%;
}

h2 {
  margin-bottom: 16px;
}

.upload-box {
  display: flex;
  gap: 12px;
  margin-bottom: 24px;
}

.files-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.file-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fff;
  padding: 12px 16px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,.05);
}

.file-name {
  font-weight: 500;
}

.actions {
  display: flex;
  gap: 8px;
}

button {
  padding: 6px 12px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  background: #4f46e5;
  color: #fff;
}

button:hover {
  opacity: .9;
}

button.danger {
  background: #ef4444;
}

.empty {
  opacity: .6;
}
</style>