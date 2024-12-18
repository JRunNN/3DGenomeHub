<template>
    <meta-compartment-track-item
    :location="props.location"
    :option="props.config.option"
    >
    </meta-compartment-track-item> 
  </template>
  
<script setup lang="ts">
import { defineProps } from 'vue'
import MetaCompartmentTrackItem from './MetaCompartmentTrackItem.vue'

const props = defineProps({
    config: {
        type: Object,
        required: true
    },
    location: {
        type: Object,
        required: true
    }
})
</script>
