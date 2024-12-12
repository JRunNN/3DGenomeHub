<script setup lang="ts">
import NavBar from '@/layout/NavBar.vue'
import MainView from '@/layout/MainView.vue'
import BottomPanel from '@/layout/BottomPanel.vue'
</script>

<template>
  <div class="min-w-[800px] bg-brand-lighter-gray">
  <NavBar />
  <div class="h-16	 w-full"></div>
   <div class="flex items-center justify-center">
  <MainView />
   </div>
  <!-- <BottomPanel /> -->
  </div>
</template>
