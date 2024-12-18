<template>
    <meta-domain-track-item
    :location="props.location"
    :option="props.config.option"
    >
    </meta-domain-track-item> 
  </template>
  
<script setup lang="ts">
import { defineProps } from 'vue'
import MetaDomainTrackItem from './MetaDomainTrackItem.vue'

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
