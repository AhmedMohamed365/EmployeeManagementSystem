<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { companies, departments, employees } from '../services/api';
import AppLayout from '../components/layout/AppLayout.vue';

const stats = ref({
  companies: 0,
  departments: 0,
  employees: 0,
});

onMounted(async () => {
  try {
    const [companiesData, departmentsData, employeesData] = await Promise.all([
      companies.getAll(),
      departments.getAll(),
      employees.getAll(),
    ]);

    stats.value = {
      companies: companiesData.data.length,
      departments: departmentsData.data.length,
      employees: employeesData.data.length,
    };
  } catch (error) {
    console.error('Error fetching dashboard data:', error);
  }
});
</script>

<template>
  <AppLayout>
    <div class="bg-white shadow rounded-lg">
      <div class="px-4 py-5 sm:p-6">
        <h3 class="text-lg leading-6 font-medium text-gray-900">Dashboard Overview</h3>
        <div class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-3">
          <div class="bg-gray-50 px-4 py-5 rounded-lg">
            <dt class="text-sm font-medium text-gray-500">Total Companies</dt>
            <dd class="mt-1 text-3xl font-semibold text-gray-900">{{ stats.companies }}</dd>
          </div>
          <div class="bg-gray-50 px-4 py-5 rounded-lg">
            <dt class="text-sm font-medium text-gray-500">Total Departments</dt>
            <dd class="mt-1 text-3xl font-semibold text-gray-900">{{ stats.departments }}</dd>
          </div>
          <div class="bg-gray-50 px-4 py-5 rounded-lg">
            <dt class="text-sm font-medium text-gray-500">Total Employees</dt>
            <dd class="mt-1 text-3xl font-semibold text-gray-900">{{ stats.employees }}</dd>
          </div>
        </div>
      </div>
    </div>
  </AppLayout>
</template>