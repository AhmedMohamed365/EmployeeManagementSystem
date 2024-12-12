import axios from 'axios';
import type { User } from '../types';

// Define the API base URL
const API_URL = 'http://127.0.0.1:8000/api/auth';

// Interfaces for request/response data
export interface LoginCredentials {
  email: string;
  password: string;
}

export interface TokenResponse {
  access: string;
  refresh: string;
}

export interface RegisterData {
  email: string;
  username: string;
  password: string;
  re_password: string;
  role: 'admin' | 'manager' | 'employee';
}

// Axios instance for authentication-related requests
const authAxios = axios.create({
  baseURL: API_URL,
  timeout: 5000,
});

// Add a request interceptor for logging/debugging
authAxios.interceptors.request.use((config) => {
  console.log(`Request to ${config.url}:`, config);
  return config;
});

// Add a response interceptor for handling errors
authAxios.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

const authService = {
  async login(credentials: LoginCredentials): Promise<TokenResponse> {
    try {
      const response = await authAxios.post<TokenResponse>('/jwt/create/', credentials);
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Login failed');
    }
  },

  async register(data: RegisterData): Promise<User> {
    try {
      const response = await authAxios.post<User>('/users/', data);
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Registration failed');
    }
  },

  async refreshToken(refresh: string): Promise<TokenResponse> {
    try {
      const response = await authAxios.post<TokenResponse>('/jwt/refresh/', { refresh });
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Token refresh failed');
    }
  },

  async verifyToken(token: string): Promise<boolean> {
    try {
      await authAxios.post('/jwt/verify/', { token });
      return true;
    } catch (error) {
      console.error('Token verification failed:', error.response?.data || error.message);
      return false;
    }
  },

  async getCurrentUser(): Promise<User> {
    try {
      const token = localStorage.getItem('accessToken');
      if (!token) {
        throw new Error('No access token available');
      }

      const response = await authAxios.get<User>('/users/me/', {
        headers: { Authorization: `Bearer ${token}` },
      });
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch current user');
    }
  },

  async logout(): Promise<void> {
    try {
      const token = localStorage.getItem('accessToken');
      if (token) {
        await authAxios.post('/token/logout/', null, {
          headers: { Authorization: `Bearer ${token}` },
        });
      }
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
    } catch (error: any) {
      console.error('Logout failed:', error.response?.data || error.message);
    }
  },
};

export default authService;
