<template>
  <form @submit.prevent="submitForm">
    <div v-for="field in visibleFields" :key="field.key" class="field-wrapper">
      <label>{{ field.label }}:</label>
      
      <input
        v-if="field.type === 'lookup'"
        type="number"
        v-model.number="editableFields[field.key].id"
      />
      
      <input
        v-else-if="field.type === 'number'"
        type="number"
        v-model.number="editableFields[field.key]"
      />
      
      <input
        v-else
        type="text"
        v-model="editableFields[field.key]"
      />
    </div>

    <button type="submit">{{ hasId ? 'Save' : 'Add' }}</button>
    <button type="button" @click="$emit('cancel')">Cancel</button>
  </form>
</template>

<script>
export default {
  props: {
    editableWell: { type: Object, default: () => ({}) },
  },

  data() {
    const base = {
      number: '',
      depth: 0,
      enterprise: { id: null },
      status: { id: null },
    };

    return {
      editableFields: {
        ...base,
        ...JSON.parse(JSON.stringify(this.editableWell)),
      },
    };
  },

  computed: {
    hasId() {
      return !!this.editableFields.id;
    },

    visibleFields() {
      const fields = [];

      const defaultFields = this.editableWell.id ? this.editableFields : {
        number: '',
        depth: 0,
        enterprise: { id: null },
        status: { id: null }
      };
      
      Object.entries(defaultFields).forEach(([key, value]) => {
        if (key === 'id') {
          return;
        }

        let type = 'string';
        let displayValue = value;

        if (value && typeof value === 'object' && 'id' in value) {
          type = 'lookup';
          displayValue = value.id;
        } else if (typeof value === 'number') {
          type = 'number';
        }

        fields.push({
          key,
          label: this.formatKey(key),
          value: displayValue,
          type
        });
      });

      return fields;
    }
  },

  watch: {
    editableWell(newVal) {
      const base = {
        number: '',
        depth: 0,
        enterprise: { id: null },
        status: { id: null },
      };

      this.editableFields = {
        ...base,
        ...JSON.parse(JSON.stringify(newVal)),
      };
    },
  },

  methods: {
    formatKey(key) {
      if (!key) return '';
      return key
        .replace(/([A-Z])/g, ' $1')
        .replace(/^./, str => str.toUpperCase())
        .replace(/_/g, ' ')
        .trim();
    },

    submitForm() {
      const payload = {};
      
      Object.entries(this.editableFields).forEach(([key, value]) => {
        if (key === 'id' || key === 'created_at' || key === 'updated_at') {
          return;
        }

        if (value && typeof value === 'object' && 'id' in value) {
          payload[`${key}_id`] = value.id;
        } else {
          payload[key] = value;
        }
      });

      this.$emit('save', payload);
    },
  },
};
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