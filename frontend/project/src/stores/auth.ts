import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { User } from '../types';
import { auth } from '../services/api';

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null);
  const token = ref<string | null>(null);

  async function login(username: string, password: string) {
    try {
      const response = await auth.login(username, password);
      token.value = response.data.token;
      user.value = response.data.user;
      return true;
    } catch (error) {
      console.error('Login failed:', error);
      return false;
    }
  }

  function logout() {
    user.value = null;
    token.value = null;
  }

  return {
    user,
    token,
    login,
    logout,
    isAuthenticated: () => !!token.value,
  };
});