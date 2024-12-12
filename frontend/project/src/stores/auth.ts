import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { User, TokenPair } from '../types';
import authService, { type LoginCredentials } from '../services/auth';

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null);
  const tokens = ref<TokenPair | null>(null);

  async function login(credentials: LoginCredentials) {
    try {
      const tokenResponse = await authService.login(credentials);
      tokens.value = tokenResponse;
      
      // Get user details after successful login
      const userResponse = await authService.getCurrentUser();
      user.value = userResponse;
      
      return true;
    } catch (error) {
      console.error('Login failed:', error);
      return false;
    }
  }

  async function refreshToken() {
    try {
      if (tokens.value?.refresh) {
        const newTokens = await authService.refreshToken(tokens.value.refresh);
        tokens.value = newTokens;
        return true;
      }
      return false;
    } catch (error) {
      console.error('Token refresh failed:', error);
      return false;
    }
  }

  function logout() {
    user.value = null;
    tokens.value = null;
  }

  return {
    user,
    tokens,
    login,
    logout,
    refreshToken,
    isAuthenticated: () => !!tokens.value?.access,
  };
});