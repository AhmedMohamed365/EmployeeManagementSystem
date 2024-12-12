import { TokenService } from '@/services/auth/token.service.ts'; // Adjust the path based on your folder structure

import axios from 'axios';
import type { User } from '../types';

const API_URL = 'http://127.0.0.1:8000/auth';

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

const authService = {
  async login(credentials: LoginCredentials): Promise<TokenResponse> {
    const response = await axios.post(`${API_URL}/jwt/create/`, credentials);
    TokenService.saveTokens(response.data)
    return response.data;
  },

  async register(data: RegisterData): Promise<User> {
    const response = await axios.post(`${API_URL}/users/`, data);
    return response.data;
  },

  async refreshToken(refresh: string): Promise<TokenResponse> {
    const response = await axios.post(`${API_URL}/jwt/refresh/`, { refresh });
    return response.data;
  },

  async verifyToken(token: string): Promise<void> {
    

    await axios.post(`${API_URL}/jwt/verify/`, { token });
  },

  async getCurrentUser(): Promise<User> {
    const token = TokenService.getAccessToken()
    console.log("THIS is access token ! " + token);
    const response = await axios.get(`${API_URL}/users/me/`,{
      headers: {
        Authorization: `Bearer ${token}`,
      },
  });
    return response.data;
  },

  async logout(): Promise<void> {
    await axios.post(`${API_URL}/token/logout/`);
  }
};

export default authService;