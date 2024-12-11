import axios from 'axios';
import { useAuthStore } from '../stores/auth';

const api = axios.create({
  baseURL: 'http://your-django-api-url/api',
});

api.interceptors.request.use((config) => {
  const authStore = useAuthStore();
  if (authStore.token) {
    config.headers.Authorization = `Bearer ${authStore.token}`;
  }
  return config;
});

export const auth = {
  login: (username: string, password: string) => 
    api.post('/auth/login/', { username, password }),
};

export const companies = {
  getAll: () => api.get('/companies/'),
  get: (id: number) => api.get(`/companies/${id}/`),
  create: (data: Partial<Company>) => api.post('/companies/', data),
  update: (id: number, data: Partial<Company>) => api.put(`/companies/${id}/`, data),
  delete: (id: number) => api.delete(`/companies/${id}/`),
};

export const departments = {
  getAll: () => api.get('/departments/'),
  get: (id: number) => api.get(`/departments/${id}/`),
  create: (data: Partial<Department>) => api.post('/departments/', data),
  update: (id: number, data: Partial<Department>) => api.put(`/departments/${id}/`, data),
  delete: (id: number) => api.delete(`/departments/${id}/`),
};

export const employees = {
  getAll: () => api.get('/employees/'),
  get: (id: number) => api.get(`/employees/${id}/`),
  create: (data: Partial<Employee>) => api.post('/employees/', data),
  update: (id: number, data: Partial<Employee>) => api.put(`/employees/${id}/`, data),
  delete: (id: number) => api.delete(`/employees/${id}/`),
};

export default api;