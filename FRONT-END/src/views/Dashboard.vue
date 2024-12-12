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
    <div class="bg-gray-100 min-h-screen py-8">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <!-- Header Section -->
        <div class="text-center mb-10">
          <h1 class="text-4xl font-extrabold text-gray-800">Dashboard Overview</h1>
          <p class="mt-2 text-lg text-gray-600">
           Summary of  companies' key statistics.
          </p>
        </div>

        <!-- Stats Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Companies Card -->
          <div class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow">
            <div class="p-6">
              <h2 class="text-sm font-medium text-gray-500 uppercase tracking-wide">
                Total Companies
              </h2>
              <p class="mt-4 text-4xl font-bold text-indigo-600">{{ stats.companies }}</p>
            </div>
          </div>

          <!-- Departments Card -->
          <div class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow">
            <div class="p-6">
              <h2 class="text-sm font-medium text-gray-500 uppercase tracking-wide">
                Total Departments
              </h2>
              <p class="mt-4 text-4xl font-bold text-green-600">{{ stats.departments }}</p>
            </div>
          </div>

          <!-- Employees Card -->
          <div class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow">
            <div class="p-6">
              <h2 class="text-sm font-medium text-gray-500 uppercase tracking-wide">
                Total Employees
              </h2>
              <p class="mt-4 text-4xl font-bold text-blue-600">{{ stats.employees }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </AppLayout>
</template>
