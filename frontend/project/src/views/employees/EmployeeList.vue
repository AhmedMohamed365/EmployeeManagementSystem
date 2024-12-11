<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { employees } from '../../services/api';
import type { Employee } from '../../types';
import AppLayout from '../../components/layout/AppLayout.vue';
import DataTable from '../../components/ui/DataTable.vue';

const router = useRouter();
const employeeList = ref<Employee[]>([]);

const columns = [
  { key: 'first_name', label: 'First Name' },
  { key: 'last_name', label: 'Last Name' },
  { key: 'email', label: 'Email' },
  { key: 'position', label: 'Position' },
];

onMounted(async () => {
  try {
    const response = await employees.getAll();
    employeeList.value = response.data;
  } catch (error) {
    console.error('Error fetching employees:', error);
  }
});

const handleView = (employee: Employee) => {
  router.push(`/employees/${employee.id}`);
};

const handleEdit = (employee: Employee) => {
  router.push(`/employees/${employee.id}/edit`);
};

const handleDelete = async (employee: Employee) => {
  if (confirm('Are you sure you want to delete this employee?')) {
    try {
      await employees.delete(employee.id);
      employeeList.value = employeeList.value.filter(e => e.id !== employee.id);
    } catch (error) {
      console.error('Error deleting employee:', error);
    }
  }
};
</script>

<template>
  <AppLayout>
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-xl font-semibold text-gray-900">Employees</h1>
      </div>
      <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
        <router-link
          to="/employees/new"
          class="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto"
        >
          Add Employee
        </router-link>
      </div>
    </div>
    <div class="mt-8">
      <DataTable
        :columns="columns"
        :data="employeeList"
        :actions="true"
        @view="handleView"
        @edit="handleEdit"
        @delete="handleDelete"
      />
    </div>
  </AppLayout>
</template>