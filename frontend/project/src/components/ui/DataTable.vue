<script setup lang="ts">
defineProps<{
  columns: { key: string; label: string }[];
  data: any[];
  actions?: boolean;
}>();

defineEmits(['edit', 'delete', 'view']);
</script>

<template>
  <div class="overflow-x-auto">
    <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th
            v-for="column in columns"
            :key="column.key"
            class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
          >
            {{ column.label }}
          </th>
          <th v-if="actions" class="px-6 py-3 text-right">Actions</th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="(item, index) in data" :key="index">
          <td
            v-for="column in columns"
            :key="column.key"
            class="px-6 py-4 whitespace-nowrap text-sm text-gray-900"
          >
            {{ item[column.key] }}
          </td>
          <td v-if="actions" class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
            <button
              @click="$emit('view', item)"
              class="text-indigo-600 hover:text-indigo-900 mr-2"
            >
              View
            </button>
            <button
              @click="$emit('edit', item)"
              class="text-blue-600 hover:text-blue-900 mr-2"
            >
              Edit
            </button>
            <button
              @click="$emit('delete', item)"
              class="text-red-600 hover:text-red-900"
            >
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>