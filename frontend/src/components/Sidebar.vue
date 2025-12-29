<template>
  <aside class="sidebar">
    <div class="top">
      <button class="logout" @click="logout">
        Выйти
      </button>
    </div>
    <nav>
      <ul class="menu">
        <li class="menu-section">Основные</li>

        <SidebarItem to="/dashboard/entity/deposit" label="Месторождения" />
        <SidebarItem to="/dashboard/entity/enterprise" label="Предприятия" />
        <SidebarItem to="/dashboard/entity/well" label="Скважины" />

        <li class="menu-section">Производство</li>

        <SidebarItem to="/dashboard/entity/process" label="Производственные процессы" />
        <SidebarItem to="/dashboard/entity/metrics" label="Показатели скважины" />

        <li class="menu-section">Логистика и клиенты</li>

        <SidebarItem to="/dashboard/entity/customer" label="Клиенты" />
        <SidebarItem to="/dashboard/entity/delivery" label="Поставки" />
        <SidebarItem to="/dashboard/entity/order" label="Заказы" />

        <li class="menu-section">Персонал</li>

        <SidebarItem to="/dashboard/entity/employee" label="Сотрудники" />

        <li class="menu-section">Визуализация</li>

        <SidebarItem to="/dashboard/models" label="3D модели" />

        <li
          v-if="isAdmin"
          class="menu-section"
        >
          Администрирование
        </li>

        <SidebarItem
          v-if="isAdmin"
          to="/dashboard/files"
          label="Файлы"
        />

        <li
          v-if="isAdmin"
          class="dropdown"
        >
          <div class="dropdown-title" @click="toggle">
            Классификаторы
          </div>

          <ul v-if="opened" class="submenu">
            <li
              v-for="c in classifiers"
              :key="c.title"
              @click="go(c.title)"
            >
              {{ c.title }}
            </li>
          </ul>
        </li>

        <SidebarItem
          v-if="isAdmin"
          to="/dashboard/entity/user"
          label="Пользователи"
        />
      </ul>
    </nav>
  </aside>
</template>

<script setup>
import SidebarItem from './SidebarItem.vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { ref, onMounted } from 'vue'

const opened = ref(false)
const classifiers = ref([])
const router = useRouter()

const isAdmin = ref(false)

onMounted(async () => {
  const { data } = await api.get('/user/check/')
  isAdmin.value = data.user.role
})

const toggle = async () => {
  opened.value = !opened.value

  if (opened.value && classifiers.value.length === 0) {
    const res = await api.get('/classifiers')
    classifiers.value = res.data
  }
}

const go = (classifier) => {
  router.push(`/dashboard/classifiers/${classifier}`)
  opened.value = false
}

const logout = async () => {
  await api.post('/user/logout/')
  router.push('/login')
}
</script>

<style scoped>
  .dropdown-title {
  cursor: pointer;
  font-weight: 500;
  padding: 6px 0;
}

.submenu {
  padding-left: 12px;
  font-size: 14px;
}

.submenu li {
  cursor: pointer;
  opacity: 0.85;
  padding: 4px 0;
}
.submenu li:hover {
  opacity: 1;
}
.sidebar {
  width: 260px;
  background: #1e1e2f;
  color: #fff;
  padding: 16px;
}

.menu {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu-section {
  margin: 16px 0 8px;
  font-size: 12px;
  text-transform: uppercase;
  opacity: 0.6;
}

.top {
  margin-bottom: 16px;
}

.logout {
  width: 100%;
  padding: 8px;
  background: transparent;
  border: 1px solid #444;
  color: #fff;
  cursor: pointer;
  border-radius: 4px;
}

.logout:hover {
  background: #ff4d4f;
  border-color: #ff4d4f;
}
</style>