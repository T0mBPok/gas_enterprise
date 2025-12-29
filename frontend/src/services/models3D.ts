// src/api/models3d.ts
import api from '@/services/api'

export const Models3DApi = {
  getAll() {
    return api.get('/models/')
  },

  getById(id: number) {
    return api.get(`/models/${id}`)
  },

  generate(wellId: number, params: any) {
    return api.post(`/models/generate/${wellId}`, params)
  },

  view(modelId: number) {
    // важно: blob, т.к. FileResponse
    return api.get(`/models/view/${modelId}`, {
      responseType: 'blob',
    })
  },

  download(modelId: number) {
    return api.get(`/models/download/${modelId}`, {
      responseType: 'blob',
    })
  },

  delete(modelId: number) {
    return api.delete(`/models/${modelId}`)
  },
}