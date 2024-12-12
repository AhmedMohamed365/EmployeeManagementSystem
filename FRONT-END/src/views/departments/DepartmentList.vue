<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { departments } from '../../services/api';
import type { Department } from '../../types';
import AppLayout from '../../components/layout/AppLayout.vue';
import DataTable from '../../components/ui/DataTable.vue';

const router = useRouter();
const departmentList = ref<Department[]>([]);

const columns = [
  { key: 'name', label: 'Department Name' },
  { key: 'description', label: 'Description' },
];

onMounted(async () => {
  try {
    const response = await departments.getAll();
    departmentList.value = response.data;
  } catch (error) {
    console.error('Error fetching departments:', error);
  }
});

const handleView = (department: Department) => {
  router.push(`/departments/${department.id}`);
};

const handleEdit = (department: Department) => {
  router.push(`/departments/${department.id}/edit`);
};

const handleDelete = async (department: Department) => {
  if (confirm('Are you sure you want to delete this department?')) {
    try {
      await departments.delete(department.id);
      departmentList.value = departmentList.value.filter(d => d.id !== department.id);
    } catch (error) {
      console.error('Error deleting department:', error);
    }
  }
};
</script>

<template>
  <AppLayout>
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-xl font-semibold text-gray-900">Departments</h1>
      </div>
      <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
        <router-link
          to="/departments/new"
          class="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto"
        >
          Add Department
        </router-link>
      </div>
    </div>
    <div class="mt-8">
      <DataTable
        :columns="columns"
        :data="departmentList"
        :actions="true"
        @view="handleView"
        @edit="handleEdit"
        @delete="handleDelete"
      />
    </div>
  </AppLayout>
</template>