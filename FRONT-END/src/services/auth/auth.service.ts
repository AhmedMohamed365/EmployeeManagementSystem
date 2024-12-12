import axios from 'axios';
import { API_CONFIG } from '@/config/api';
import type { LoginCredentials, JWTTokens, User } from '@/types/auth.types';
import { TokenService } from './token.service';

// Create a dedicated axios instance for auth
const authAxios = axios.create({
  baseURL: API_CONFIG.AUTH_URL,
  timeout: API_CONFIG.TIMEOUT,
});

export const AuthService = {
  async login(credentials: LoginCredentials): Promise<JWTTokens> {
    const response = await authAxios.post('/jwt/create/', credentials);
    const tokens: JWTTokens = response.data;
    TokenService.saveTokens(tokens);
    return tokens;
  },

  async refreshToken(refresh: string): Promise<JWTTokens> {
    const response = await authAxios.post('/jwt/refresh/', { refresh });
    const tokens: JWTTokens = response.data;
    TokenService.saveTokens(tokens);
    return tokens;
  },

  async verifyToken(token: string): Promise<boolean> {
    try {
      await authAxios.post('/jwt/verify/', { token });
      return true;
    } catch {
      return false;
    }
  },

  async getCurrentUser(): Promise<User> {
    const token = TokenService.getAccessToken();
    console.log(token)
    const response = await authAxios.get('/users/me/', {
      headers: { Authorization: `Bearer ${token}` }
    });
    return response.data;
  },

  logout(): void {
    TokenService.removeTokens();
  }
};