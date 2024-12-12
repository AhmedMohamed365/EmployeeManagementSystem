<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { employees, departments } from '../../services/api';
import type { Employee, Department } from '../../types';
import AppLayout from '../../components/layout/AppLayout.vue';

const route = useRoute();
const router = useRouter();
const isEdit = route.name === 'EditEmployee';

const employee = ref<Partial<Employee>>({
  first_name: '',
  last_name: '',
  email: '',
  department: 0,
  position: '',
  hire_date: new Date().toISOString().split('T')[0],
});

const departmentList = ref<Department[]>([]);
const isLoading = ref(true);
const error = ref('');

onMounted(async () => {
  try {
    const [depsResponse, empResponse] = await Promise.all([
      departments.getAll(),
      isEdit ? employees.get(Number(route.params.id)) : Promise.resolve(null),
    ]);
    
    departmentList.value = depsResponse.data;
    
    if (isEdit && empResponse) {
      employee.value = empResponse.data;
    }
  } catch (err) {
    error.value = 'Failed to load data';
    console.error(err);
  } finally {
    isLoading.value = false;
  }
});

const handleSubmit = async () => {
  try {
    if (isEdit) {
      await employees.update(Number(route.params.id), employee.value);
    } else {
      await employees.create(employee.value);
    }
    router.push('/employees');
  } catch (err) {
    error.value = 'Failed to save employee';
    console.error(err);
  }
};
</script>

<template>
  <AppLayout>
    <div class="bg-white shadow sm:rounded-lg">
      <div class="px-4 py-5 sm:p-6">
        <h3 class="text-lg leading-6 font-medium text-gray-900">
          {{ isEdit ? 'Edit Employee' : 'Create Employee' }}
        </h3>
        <div v-if="isLoading" class="mt-4">Loading...</div>
        <form v-else @submit.prevent="handleSubmit" class="mt-5 space-y-4">
          <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div>
              <label for="first_name" class="block text-sm font-medium text-gray-700">First Name</label>
              <input
                type="text"
                id="first_name"
                v-model="employee.first_name"
                required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
            <div>
              <label for="last_name" class="block text-sm font-medium text-gray-700">Last Name</label>
              <input
                type="text"
                id="last_name"
                v-model="employee.last_name"
                required
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
          </div>
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
            <input
              type="email"
              id="email"
              v-model="employee.email"
              required
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            />
          </div>
          <div>
            <label for="department" class="block text-sm font-medium text-gray-700">Department</label>
            <select
              id="department"
              v-model="employee.department"
              required
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            >
              <option v-for="dept in departmentList" :key="dept.id" :value="dept.id">
                {{ dept.name }}
              </option>
            </select>
          </div>
          <div>
            <label for="position" class="block text-sm font-medium text-gray-700">Position</label>
            <input
              type="text"
              id="position"
              v-model="employee.position"
              required
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            />
          </div>
          <div>
            <label for="hire_date" class="block text-sm font-medium text-gray-700">Hire Date</label>
            <input
              type="date"
              id="hire_date"
              v-model="employee.hire_date"
              required
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            />
          </div>
          <div class="flex justify-end">
            <button
              type="submit"
              class="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
            >
              {{ isEdit ? 'Update' : 'Create' }}
            </button>
          </div>
          <p v-if="error" class="mt-2 text-sm text-red-600">{{ error }}</p>
        </form>
      </div>
    </div>
  </AppLayout>
</template>