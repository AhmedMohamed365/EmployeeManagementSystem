import { storeToRefs } from 'pinia';
import { useAuthStore } from '@/stores/auth.store';
import { useLoading } from './useLoading';
import { useError } from './useError';
import type { LoginCredentials } from '@/types/auth.types';

export function useAuth() {
  const store = useAuthStore();
  const { user, isAuthenticated } = storeToRefs(store);
  const { isLoading, startLoading, stopLoading } = useLoading();
  const { error, setError, clearError } = useError();

  async function login(credentials: LoginCredentials) {
    try {
      startLoading();
      clearError();
      return await store.login(credentials);
    } catch (err) {
      setError('Login failed. Please check your credentials.');
      return false;
    } finally {
      stopLoading();
    }
  }

  function logout() {
    store.logout();
  }

  return {
    user,
    isLoading,
    error,
    isAuthenticated,
    login,
    logout
  };
}