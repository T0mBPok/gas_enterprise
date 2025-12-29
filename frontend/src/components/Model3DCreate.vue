<script setup lang="ts">
import { ref } from 'vue'
import { Models3DApi } from '../services/models3D'

const emit = defineEmits(['created'])

const wellId = ref<number | null>(null)

const params = ref({
  domain: {
    x_min: 0,
    x_max: 1000,
    y_min: 0,
    y_max: 1000,
    nx: 200,
    ny: 200,
  },
  layers: [
    {
      top_depth: -50,
      thickness: 30,
      amplitude: 10,
      frequency_x: 150,
      frequency_y: 200,
      layer_type: 'gas',
      color: 'orange',
      opacity: 0.7,
    },
  ],
})

const addLayer = () => {
  params.value.layers.push({
    top_depth: 0,
    thickness: 10,
    amplitude: 5,
    frequency_x: 100,
    frequency_y: 100,
    layer_type: 'gas',
    color: 'gray',
    opacity: 0.5,
  })
}

const submit = async () => {
  if (!wellId.value) return
  await Models3DApi.generate(wellId.value, params.value)
  emit('created')
}
</script>

<template>
  <div>
    <h3>Генерация 3D модели</h3>

    <label>Скважина ID</label>
    <input type="number" v-model.number="wellId" />

    <h4>Слои</h4>
    <div v-for="(l, i) in params.layers" :key="i">
      <input v-model.number="l.top_depth" placeholder="top_depth" />
      <input v-model.number="l.thickness" placeholder="thickness" />
      <input v-model="l.layer_type" placeholder="type" />
    </div>

    <button @click="addLayer">➕ слой</button>
    <button @click="submit">Сгенерировать</button>
  </div>
</template>