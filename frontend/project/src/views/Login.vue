<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuth } from '../composables'; // Ensure this file exists and is functional

const email = ref('');
const password = ref('');
const errorMessage = ref('');
const router = useRouter();
const { login, loading } = useAuth();

async function handleLogin() {
  errorMessage.value = ''; // Reset the error message before login attempt
  
  if (!email.value || !password.value) {
    errorMessage.value = 'Email and password are required.';
    return;
  }

  try {
    const success = await login({
      email: email.value,
      password: password.value,
    });

    if (success) {
      router.push('/');
    } else {
      errorMessage.value = 'Invalid email or password.';
    }
  } catch (error) {
    errorMessage.value = 'An error occurred. Please try again later.';
    console.error('Login error:', error);
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Sign in to your account
        </h2>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="handleLogin">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="email" class="sr-only">Email</label>
            <input
              id="email"
              v-model="email"
              type="email"
              required
              aria-required="true"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Email address"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              v-model="password"
              type="password"
              required
              aria-required="true"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Password"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            :disabled="loading"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
          >
            <span v-if="loading">Signing in...</span>
            <span v-else>Sign in</span>
          </button>
        </div>
        
        <p v-if="errorMessage" class="text-red-500 text-center mt-4">
          {{ errorMessage }}
        </p>
      </form>
    </div>
  </div>
</template>
