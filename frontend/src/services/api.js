import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:9000",
  withCredentials: true,
});

export const createEntityApi = (entity, classifier = null) => {
  const url = classifier ? `/classifiers/${classifier}` : `/${entity}`;

  return {
    fetchAll: (params = {}) => api.get(url, { params }),
    create: (data) => api.post(url, data),
    update: (data) => api.put(`${url}/${data.id}`, data),
    delete: (id) => api.delete(`${url}/${id}`),
    export: (params = {}, format, config = {}) => 
      api.get(`${url}/export`, { params: { ...params, format }, ...config })
  };
};

export default api;