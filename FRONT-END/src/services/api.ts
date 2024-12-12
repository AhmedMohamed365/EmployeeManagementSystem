import axios from 'axios';
import { useAuthStore } from '../stores/auth';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
});

// Request interceptor for API calls
api.interceptors.request.use(
  (config) => {
    const authStore = useAuthStore();
    if (authStore.tokens?.access) {
      config.headers.Authorization = `Bearer ${authStore.tokens.access}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for API calls
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    const authStore = useAuthStore();

    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      
      const refreshed = await authStore.refreshToken();
      if (refreshed && authStore.tokens?.access) {
        originalRequest.headers.Authorization = `Bearer ${authStore.tokens.access}`;
        return api(originalRequest);
      }
    }
    return Promise.reject(error);
  }
);

export const companies = {
  getAll: () => api.get('/companies/'),
  get: (id: number) => api.get(`/companies/${id}/`),
  create: (data: Partial<Company>) => api.post('/companies/', data),
  update: (id: number, data: Partial<Company>) => api.put(`/companies/${id}/`, data),
  delete: (id: number) => api.delete(`/companies/${id}/`),
  getStats: (id: number) => api.get(`/companies/${id}/stats/`),
};

export const departments = {
  getAll: () => api.get('/departments/'),
  get: (id: number) => api.get(`/departments/${id}/`),
  create: (data: Partial<Department>) => api.post('/departments/', data),
  update: (id: number, data: Partial<Department>) => api.put(`/departments/${id}/`, data),
  delete: (id: number) => api.delete(`/departments/${id}/`),
  getStats: (id: number) => api.get(`/departments/${id}/stats/`),
};

export const employees = {
  getAll: () => api.get('/employees/'),
  get: (id: number) => api.get(`/employees/${id}/`),
  create: (data: Partial<Employee>) => api.post('/employees/', data),
  update: (id: number, data: Partial<Employee>) => api.put(`/employees/${id}/`, data),
  delete: (id: number) => api.delete(`/employees/${id}/`),
};

export default api;