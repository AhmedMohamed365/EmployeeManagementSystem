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
      const success = await store.login(credentials);
      if (!success) {
        setError('Invalid email or password.');
      }
      return success;
    } catch (err: any) {
      // If backend returns an error message, display it dynamically
      const errorMessage = err.response?.data?.detail || 'Login failed. Please try again.';
      setError(errorMessage);
      return false;
    } finally {
      stopLoading();
    }
  }

  function logout() {
    clearError(); // Clear error when logging out
    store.logout();
  }

  return {
    user,
    isLoading,
    error,
    isAuthenticated,
    login,
    logout,
  };
}
