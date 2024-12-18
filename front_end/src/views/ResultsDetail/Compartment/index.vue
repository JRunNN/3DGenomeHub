<template>
    <!-- <CompartmentChart></CompartmentChart> -->
    <!-- <CompartmentBrowser></CompartmentBrowser> -->
    <CompartmentTable :data="props.compartmentData" :loading="loading" :region="region" :page-size="10"
        @action="handleAction" />
</template>
<script setup lang="ts">
// import CompartmentChart from './CompartmentChart.vue';
// import CompartmentBrowser from './CompartmentBrowser.vue';
import CompartmentTable from './CompartmentTable.vue';
const props = defineProps([
    'compartmentData'
])

</script>
<style></style>