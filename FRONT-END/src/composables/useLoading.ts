import { ref } from 'vue';

export function useLoading(initialState = false) {
  const isLoading = ref(initialState);
  
  function startLoading() {
    isLoading.value = true;
  }
  
  function stopLoading() {
    isLoading.value = false;
  }
  
  return {
    isLoading,
    startLoading,
    stopLoading
  };
}