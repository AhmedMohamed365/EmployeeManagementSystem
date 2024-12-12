import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import type { User, LoginCredentials, JWTTokens } from '@/types/auth.types';
import { AuthService } from '@/services/auth/auth.service';
import { TokenService } from '@/services/auth/token.service';

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null);
  const tokens = ref<JWTTokens | null>(TokenService.getTokens());
  const loading = ref(false);
  const error = ref<string | null>(null);

  const isAuthenticated = computed(() => !!tokens.value?.access);

  async function login(credentials: LoginCredentials) {
    try {
      loading.value = true;
      error.value = null;
      
      // Get JWT tokens
      const tokenResponse = await AuthService.login(credentials);
      tokens.value = tokenResponse;
      
      // Get user details
      const userResponse = await AuthService.getCurrentUser();
      user.value = userResponse;
      
      return true;
    } catch (err) {
      error.value = 'Invalid credentials';
      return false;
    } finally {
      loading.value = false;
    }
  }

  async function refreshToken() {
    try {
      if (tokens.value?.refresh) {
        const newTokens = await AuthService.refreshToken(tokens.value.refresh);
        tokens.value = newTokens;
        return true;
      }
      return false;
    } catch {
      logout();
      return false;
    }
  }

  function logout() {
    AuthService.logout();
    user.value = null;
    tokens.value = null;
    error.value = null;
  }

  return {
    user,
    tokens,
    loading,
    error,
    isAuthenticated,
    login,
    logout,
    refreshToken,
  };
});