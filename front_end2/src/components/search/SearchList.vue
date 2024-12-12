<script lang="ts" setup>
// import SearchFilter from '@/components/search/SearchFilter.vue'
</script>
<template>
    <div class="flex justify-between gap-x-8">
        <div class="w-48">
            <SearchFilter />
        </div>
        <div class="grow">
            <DataTable />
        </div>
    </div>
</template>