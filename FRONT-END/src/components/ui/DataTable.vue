<script setup lang="ts">
defineProps<{
  columns: { key: string; label: string }[];
  data: any[];
  actions?: boolean;
}>();

defineEmits(['edit', 'delete', 'view']);
</script>

<template>
  <div class="overflow-x-auto shadow-md rounded-lg">
    <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50 sticky top-0 z-10">
        <tr>
          <th
            v-for="column in columns"
            :key="column.key"
            class="px-6 py-3 text-left text-sm font-semibold text-gray-700 uppercase tracking-wider"
          >
            {{ column.label }}
          </th>
          <th v-if="actions" class="px-6 py-3 text-right text-sm font-semibold text-gray-700 uppercase">
            Actions
          </th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr 
          v-for="(item, index) in data" 
          :key="index"
          class="hover:bg-gray-100 transition-colors duration-200"
        >
          <td
            v-for="column in columns"
            :key="column.key"
            class="px-6 py-4 whitespace-nowrap text-sm text-gray-900"
          >
            {{ item[column.key] }}
          </td>
          <td v-if="actions" class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
            <div class="flex justify-end space-x-3">
              <button
                @click="$emit('view', item)"
                class="text-indigo-600 hover:text-indigo-900 hover:bg-indigo-50 px-3 py-2 rounded-lg transition-all"
              >
                View
              </button>
              <button
                @click="$emit('edit', item)"
                class="text-green-600 hover:text-green-900 hover:bg-green-50 px-3 py-2 rounded-lg transition-all"
              >
                Edit
              </button>
              <button
                @click="$emit('delete', item)"
                class="text-red-600 hover:text-red-900 hover:bg-red-50 px-3 py-2 rounded-lg transition-all"
              >
                Delete
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

