<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { companies } from '../../services/api';
import type { Company } from '../../types';
import AppLayout from '../../components/layout/AppLayout.vue';
import DataTable from '../../components/ui/DataTable.vue';

const router = useRouter();
const companyList = ref<Company[]>([]);

const columns = [
  { key: 'name', label: 'Company Name' },
  { key: 'description', label: 'Description' },
  { key: 'created_at', label: 'Created At' },
];

onMounted(async () => {
  try {
    const response = await companies.getAll();
    companyList.value = response.data;
  } catch (error) {
    console.error('Error fetching companies:', error);
  }
});

const handleView = (company: Company) => {
  router.push(`/companies/${company.id}`);
};

const handleEdit = (company: Company) => {
  router.push(`/companies/${company.id}/edit`);
};

const handleDelete = async (company: Company) => {
  if (confirm('Are you sure you want to delete this company?')) {
    try {
      await companies.delete(company.id);
      companyList.value = companyList.value.filter(c => c.id !== company.id);
    } catch (error) {
      console.error('Error deleting company:', error);
    }
  }
};
</script>

<template>
  <AppLayout>
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-xl font-semibold text-gray-900">Companies</h1>
      </div>
      <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
        <router-link
          to="/companies/new"
          class="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto"
        >
          Add Company
        </router-link>
      </div>
    </div>
    <div class="mt-8">
      <DataTable
        :columns="columns"
        :data="companyList"
        :actions="true"
        @view="handleView"
        @edit="handleEdit"
        @delete="handleDelete"
      />
    </div>
  </AppLayout>
</template>