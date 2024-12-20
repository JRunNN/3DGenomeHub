<template>
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-1 gap-4">
        <GenomeCard
          v-for="item in currentPageItems"
          :key="`${item.chrom}-${item.start}`"
          :data="item"
        />
      </div>
  
      <!-- Pagination -->
      <div v-if="totalPages > 1" class="mt-4 flex justify-center space-x-2">
        <button 
          @click="currentPage--" 
          :disabled="currentPage === 1"
          class="px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-300"
        >
          Previous
        </button>
        <span class="px-4 py-2">{{ currentPage }} / {{ totalPages }}</span>
        <button 
          @click="currentPage++" 
          :disabled="currentPage === totalPages"
          class="px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-300"
        >
          Next
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import GenomeCard from './GenomeCard.vue';
  
  const props = defineProps({
    data: {
      type: Array,
      required: true,
      validator: (array) => {
        return array.every(item => 
          ['chrom', 'start', 'end', 
           'A_compartment', 'B_compartment', 'NA_compartment',
           'IS_lower_bound', 'IS_average', 'IS_higher_bound'
          ].every(key => key in item)
        );
      }
    }
  });
  
  const itemsPerPage = 10;
  const currentPage = ref(1);
  
  const totalPages = computed(() => Math.ceil(props.data.length / itemsPerPage));
  const currentPageItems = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage;
    return props.data.slice(start, start + itemsPerPage);
  });
  </script>