<template>
    <n-card>
        <div class="flex max-w-4xl">
            <select
                class="flex-shrink-0 z-10 inline-flex items-center py-2.5  text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-l-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600"
                id="search-type-select" aria-label="Search Type">
                <option value="celltype" selected>Cell types</option>
                <option value="gene">Genes</option>
                <option value="genomicregion">Genomic regions</option>
                <option value="snp">SNPs</option>
            </select>
            <div class="relative w-full">
                <input type="search" id="search-dropdown"
                    class="block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-r-lg border-l-gray-50 border-l-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-l-gray-700  dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-blue-500"
                    placeholder="Search Genes, Genomic regions, SNPs...Or click one of the examples below" required>
                <button type="submit"
                    class="absolute top-0 right-0 p-2.5 text-sm font-medium h-full text-white bg-blue-700 rounded-r-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 20 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                    </svg>
                    <span class="sr-only">Search</span>
                </button>
            </div>
        </div>
    </n-card>
    <n-card>
        <SearchList />
    </n-card>
</template>
<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import SearchList from './SearchList.vue'

const value = ref(null)
const options = [
    {
        label: "Cell types",
        value: 'Cell types',
    },
    {
        label: "Genes",
        value: 'Genes',
    },
    {
        label: 'Genomic regions',
        value: 'Genomic regions'
    },
    {
        label: 'SNPs',
        value: 'SNPs'
    },
    {
        label: 'Nowhere Man',
        value: 'song4'
    }
]
onMounted(() => {

})
</script>