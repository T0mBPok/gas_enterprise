import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '../views/LoginView.vue'
import Dashboard from '@/views/Dashboard.vue'
import EntityPage from '@/views/EntityPage.vue'
import ClassifierPage from '@/views/ClassifierPage.vue'
import api from '../services/api'
import Models3DPage from '@/components/Models3DPage.vue'
import FilesPage from '@/components/FilesPage.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', name: 'Login', component: LoginView },
    { path: '/dashboard', name: 'Dashboard', component: Dashboard, 
      children: [
        { path: 'entity/:entity', name: 'Entity', component: EntityPage},
        { path: 'classifiers/:classifier', component: ClassifierPage },
        { path: 'models', name: 'Models3d', component: Models3DPage },
        { path: 'files', name: 'Files', component: FilesPage }
      ]
    },
  ]
})

router.beforeEach(async (to, from, next) => {
  if (to.name !== 'Login') {
    try{
      const response = await api.get('/user/check/')
      if (!response.data.ok) return next('/login')
    } catch (error) {
      return next('/login')
    }
  }
  next()
})

export default router