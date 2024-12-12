import axios from 'axios';
import type { AxiosInstance } from 'axios';
import { API_BASE_URL } from '@/config/constants';
import { TokenService } from '@/services/auth/token.service';

export function createAxiosInstance(baseURL: string = API_BASE_URL): AxiosInstance {
  const instance = axios.create({
    baseURL,
    timeout: 10000,
    headers: {
      'Content-Type': 'application/json'
    }
  });

  // Request interceptor
  instance.interceptors.request.use(
    (config) => {
      const token = TokenService.getAccessToken();
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    },
    (error) => Promise.reject(error)
  );

  return instance;
}

export const http = createAxiosInstance();