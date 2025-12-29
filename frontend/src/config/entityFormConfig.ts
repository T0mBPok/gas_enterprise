export const entityFormConfig = {
  classifiers: {
    fields: {
      code: { type: 'string', label: 'Код' },
      name: { type: 'string', label: 'Название' },
      description: { type: 'string', label: 'Описание', optional: true },
    },
  },

  customer: {
    fields: {
      name: { type: 'string', label: 'Имя' },
      phone_num: { type: 'string', label: 'Телефон' },
      contact_info: { type: 'string', label: 'Контакты', optional: true },
      country_id: { type: 'classifier', classifier: 'countries', label: 'Страна' },
      city_id: { type: 'classifier', classifier: 'cities', label: 'Город' },
      street_id: { type: 'classifier', classifier: 'streets', label: 'Улица' },
      house_id: { type: 'classifier', classifier: 'houses', label: 'Дом' },
    },
  },

  delivery: {
    fields: {
      delivery_date: { type: 'date', label: 'Дата доставки' },
      volume: { type: 'number', label: 'Объём', optional: true },
      enterprise_id: { type: 'entity', entity: 'enterprise', label: 'Предприятие' },
      order_id: { type: 'entity', entity: 'order', label: 'Заказ' },
      transport_id: { type: 'classifier', classifier: 'transports', label: 'Транспорт' },
      status_id: { type: 'classifier', classifier: 'delivery-statuses', label: 'Статус' },
    },
    export: true
  },

  deposit: {
    fields: {
      name: { type: 'string', label: 'Название' },
      region_id: { type: 'classifier', classifier: 'regions', label: 'Регион' },
      status_id: { type: 'classifier', classifier: 'deposit-statuses', label: 'Статус' },
    },
  },

  employee: {
    fields: {
      name: { type: 'string', label: 'Имя' },
      hire_date: { type: 'date', label: 'Дата найма', optional: true },
      position_id: { type: 'classifier', classifier: 'positions', label: 'Должность' },
      qualification_id: { type: 'classifier', classifier: 'qualifications', label: 'Квалификация' },
      enterprise_id: { type: 'entity', entity: 'enterprise', label: 'Предприятие' },
    },
  },

  enterprise: {
    fields: {
      name: { type: 'string', label: 'Название' },
      contacts: { type: 'string', label: 'Контакты', optional: true },
      status_id: { type: 'classifier', classifier: 'enterprise-statuses', label: 'Статус' },
      type_id: { type: 'classifier', classifier: 'enterprise-types', label: 'Тип' },
      deposit_id: { type: 'entity', entity: 'deposit', label: 'Месторождение' },
      country_id: { type: 'classifier', classifier: 'countries', label: 'Страна' },
      city_id: { type: 'classifier', classifier: 'cities', label: 'Город' },
      street_id: { type: 'classifier', classifier: 'streets', label: 'Улица' },
      house_id: { type: 'classifier', classifier: 'houses', label: 'Дом' },
    },
  },

  order: {
    fields: {
      gas_volume: { type: 'number', label: 'Объём газа' },
      cost: { type: 'number', label: 'Стоимость' },
      status_id: { type: 'classifier', classifier: 'order-statuses', label: 'Статус' },
      customer_id: { type: 'entity', entity: 'customer', label: 'Клиент' },
    },
    export: true
  },

  metrics: {
    fields: {
      gas_volume: { type: 'number', label: 'Объём газа' },
      pressure: { type: 'number', label: 'Давление' },
      temperature: { type: 'number', label: 'Температура' },
      well_id: { type: 'entity', entity: 'well', label: 'Скважина' },
    },
  },

  process: {
    fields: {
      name: { type: 'string', label: 'Название' },
      date_start: { type: 'date', label: 'Дата начала', optional: true },
      date_end: { type: 'date', label: 'Дата окончания', optional: true },
      notes: { type: 'string', label: 'Примечания', optional: true },
      enterprise_id: { type: 'entity', entity: 'enterprise', label: 'Предприятие' },
      well_id: { type: 'entity', entity: 'well', label: 'Скважина', optional: true },
      type_id: { type: 'classifier', classifier: 'process-types', label: 'Тип' },
      status_id: { type: 'classifier', classifier: 'process-statuses', label: 'Статус' },
    },
  },

  user: {
    fields: {
      email: { type: 'string', label: 'Email' },
      username: { type: 'string', label: 'Имя пользователя' },
      password: { type: 'password', label: 'Пароль' },
      role: { type: 'string', label: 'Права'}
    },
  },

  well: {
    fields: {
      number: { type: 'string', label: 'Номер' },
      depth: { type: 'number', label: 'Глубина' },
      enterprise_id: { type: 'entity', entity: 'enterprise', label: 'Предприятие' },
      status_id: { type: 'classifier', classifier: 'well-statuses', label: 'Статус' },
    },
  },
}