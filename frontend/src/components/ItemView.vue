<template>
  <div class="entity-view">
    <div class="entity-fields">
      <div 
        v-for="(value, key) in displayFields" 
        :key="key" 
        class="entity-field"
      >
        <strong class="field-label">{{ formatKey(key) }}:</strong>
        <span class="field-value">{{ formatValue(value) }}</span>
      </div>
    </div>

    <div class="entity-actions">
      <button @click="$emit('edit', entity)" class="btn btn-edit">
        Edit
      </button>
      <button @click="$emit('delete', entity.id)" class="btn btn-delete">
        Delete
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    entity: { type: Object, required: true },
  },

  computed: {
    displayFields() {
      const { id, ...rest } = this.entity;
      return rest;
    },
  },

  methods: {
    formatKey(key) {
      return key
        .replace(/([A-Z])/g, ' $1')
        .replace(/^./, str => str.toUpperCase())
        .trim();
    },

    formatValue(value) {
      if (value === null || value === undefined) return '—';
      
      if (typeof value === 'boolean') {
        return value ? 'Да' : 'Нет';
      }

      if (typeof value === 'object') {
        // ✅ Правильный порядок приоритетов
        return value.name || 
               value.title || 
               value.code || 
               (value.id ? `#${value.id}` : '') ||
               this.formatDate(value);
      }

      return value;
    },

    formatDate(value) {
      const date = new Date(value);
      return !isNaN(date.getTime()) ? date.toLocaleString('ru-RU') : '';
    },
  },
};
</script>

<style scoped>
.entity-view {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 10px 0;
}

.entity-fields {
  margin-bottom: 20px;
}

.entity-field {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 12px 0;
  border-bottom: 1px solid #f0f0f0;
}

.entity-field:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.field-label {
  font-weight: 600;
  color: #333;
  min-width: 100px;
  flex-shrink: 0;
}

.field-value {
  color: #555;
  word-break: break-word;
  flex: 1;
  text-align: right;
}

.entity-actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 14px;
}

.btn-edit {
  background: #4f46e5;
  color: white;
}

.btn-edit:hover {
  background: #3730a3;
  transform: translateY(-1px);
}

.btn-delete {
  background: #ef4444;
  color: white;
}

.btn-delete:hover {
  background: #dc2626;
  transform: translateY(-1px);
}
</style>