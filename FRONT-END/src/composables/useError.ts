import { ref } from 'vue';

export function useError() {
  const error = ref<string | null>(null);
  
  function setError(message: string) {
    error.value = message;
  }
  
  function clearError() {
    error.value = null;
  }
  
  return {
    error,
    setError,
    clearError
  };
}