<template>
  <form @submit.prevent="submit">
    <div
      v-for="(field, key) in fields"
      :key="key"
      class="form-field"
    >
      <label>{{ field.label }}</label>

      <input
        v-if="field.type === 'string'"
        v-model="form[key]"
        type="text"
      />

      <input
        v-else-if="field.type === 'number'"
        v-model.number="form[key]"
        type="number"
      />

      <input
        v-else-if="field.type === 'date'"
        v-model="form[key]"
        type="date"
      />

      <input
        v-else-if="field.type === 'password'"
        v-model="form[key]"
        type="password"
      />

      <select
        v-else-if="field.type === 'classifier' || field.type === 'entity'"
        v-model="form[key]"
      >
        <option :value="null">—</option>
        <option
          v-for="opt in options[key]"
          :key="opt.id"
          :value="opt.id"
        >
          {{ opt.name || opt.number || opt.title  }}
        </option>
      </select>
    </div>

    <button type="submit">Сохранить</button>
    <button type="button" @click="$emit('cancel')">Отмена</button>
  </form>
</template>

<script>
import { entityFormConfig } from '@/config/entityFormConfig'
import { createEntityApi } from '@/services/api'

export default {
  props: {
    editableItem: { type: Object, required: true },
  },

  data() {
    return {
      form: {},
      fields: {},
      options: {},
    }
  },

  computed: {
    formKey() {
       if (this.$route.params.classifier) {
        return 'classifiers'
      }
      return this.$route.params.entity
    },
  },

  async created() {
    const config = entityFormConfig[this.formKey]
    this.fields = config.fields

    this.form = { ...this.editableItem }

    for (const [key, field] of Object.entries(this.fields)) {
      if (field.type === 'classifier') {
        const api = createEntityApi('classifiers', field.classifier)
        const res = await api.fetchAll()
        this.options[key] = res.data
      }

      if (field.type === 'entity') {
        const api = createEntityApi(field.entity)
        const res = await api.fetchAll()
        this.options[key] = res.data
      }
    }
  },

  methods: {
    submit() {
      console.log('Отправляемые данные:', this.form)
      this.$emit('save', this.form)
    },
  },
}
</script>


<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 24px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  max-width: 500px;
}

div {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

label {
  font-weight: 600;
  color: #1e293b;
  font-size: 14px;
}

input {
  padding: 12px 16px;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 15px;
  transition: all 0.2s ease;
}

input:focus {
  outline: none;
  border-color: #4f46e5;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

input:disabled {
  background: #f8fafc;
  color: #64748b;
  cursor: not-allowed;
  opacity: 0.7;
}

button {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 15px;
  cursor: pointer;
  transition: all 0.2s ease;
}

button[type="submit"] {
  background: linear-gradient(135deg, #4f46e5, #7c3aed);
  color: white;
}

button[type="submit"]:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4);
}

button[type="button"] {
  background: #f1f5f9;
  color: #475569;
}

button[type="button"]:hover {
  background: #e2e8f0;
}
</style>