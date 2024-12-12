<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { companies } from '../../services/api';
import type { Company } from '../../types';
import AppLayout from '../../components/layout/AppLayout.vue';

const route = useRoute();
const router = useRouter();
const company = ref<Company | null>(null);
const isLoading = ref(true);
const error = ref('');

onMounted(async () => {
  try {
    const id = Number(route.params.id);
    const response = await companies.get(id);
    company.value = response.data;
  } catch (err) {
    error.value = 'Failed to load company details';
    console.error(err);
  } finally {
    isLoading.value = false;
  }
});
</script>

<template>
  <AppLayout>
    <div class="bg-white shadow overflow-hidden sm:rounded-lg">
      <div v-if="isLoading" class="p-4 text-center">Loading...</div>
      <div v-else-if="error" class="p-4 text-red-500 text-center">{{ error }}</div>
      <template v-else-if="company">
        <div class="px-4 py-5 sm:px-6">
          <h3 class="text-lg leading-6 font-medium text-gray-900">Company Details</h3>
        </div>
        <div class="border-t border-gray-200">
          <dl>
            <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">Company Name</dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{ company.name }}</dd>
            </div>
            <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">Description</dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{ company.description }}</dd>
            </div>
            <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">Created At</dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{ company.created_at }}</dd>
            </div>
          </dl>
        </div>
      </template>
    </div>
  </AppLayout>
</template>