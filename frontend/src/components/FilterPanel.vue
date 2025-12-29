<template>
  <div class="filter-panel">
    <div
      v-for="(field, key) in fields"
      :key="key"
      class="filter-field"
    >
      <label class="filter-label">
        {{ field.label }}
      </label>
      <input
        v-if="['string', 'number', 'date'].includes(field.type)"
        :type="field.type === 'string' ? 'text' : field.type"
        v-model="localFilters[key]"
        :placeholder="field.label"
      />

      <select
        v-else-if="field.type === 'classifier'"
        v-model="localFilters[key]"
      >
        <option
          v-for="opt in classifiers[field.classifier] || []"
          :key="opt.id"
          :value="opt.id"
        >
          {{ opt.name }}
        </option>
      </select>

      <select
        v-else-if="field.type === 'entity'"
        v-model="localFilters[key]"
      >
        <option
          v-for="opt in entities[field.entity] || []"
          :key="opt.id"
          :value="opt.id"
        >
          {{ opt.name || opt.number }}
        </option>
      </select>
    </div>

    <div class="filter-actions">
      <button @click="apply">Применить</button>
      <button @click="reset">Сбросить</button>
    </div>
  </div>
</template>

<script>
import api from '@/services/api'

export default {
  props: {
    fields: { type: Object, required: true },
  },

  data() {
    return {
      localFilters: {},
      classifiers: {},
      entities: {},
    }
  },

  async mounted() {
    for (const field of Object.values(this.fields)) {
      if (field.type === 'classifier') {
        this.classifiers[field.classifier] =
          (await api.get(`/classifiers/${field.classifier}`)).data
      }

      if (field.type === 'entity') {
        this.entities[field.entity] =
          (await api.get(`/${field.entity}`)).data
      }
    }
  },

  methods: {
    apply() {
      const cleaned = Object.fromEntries(
        Object.entries(this.localFilters)
          .filter(([_, v]) => v !== null && v !== '' && v !== undefined)
      )
      this.$emit('apply', cleaned)
    },

    reset() {
      this.localFilters = {}
      this.$emit('apply', {})
    },
  },
}
</script>

<style scoped>
.filter-panel {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}

.filter-field {
  min-width: 160px;
}

.filter-actions {
  display: flex;
  height: auto;
  align-items:end;
  /* gap: 8px; */
}

.filters {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}

.filter-field {
  display: flex;
  flex-direction: column;
  gap: 6px;
  min-width: 180px;
}

.filter-label {
  font-size: 13px;
  font-weight: 600;
  color: #334155;
}
</style>