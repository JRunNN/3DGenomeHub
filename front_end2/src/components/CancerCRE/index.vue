<template>
  <div class="px-4 mx-auto max-w-8xl">
        <div class="rounded-lg flex flex-wrap bg-white border-slate-400	p-8" style="margin-bottom: 16px">
            <div class="w-1/2">
      <h1 class="mb-4 text-3xl font-bold tracking-tight text-gray-600"><a href="#">Non-coding mutations in cis-regulatory elements of various cancers</a></h1>
       <p class="mb-2 text-xl font-light text-gray-500"> </p>
    
       <ul class="mb-6">
        <li class="flex space-x-3 items-center mb-2">
          <!-- Icon -->
          <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"></path>
          </svg>
          <p class=" text-xl font-light text-gray-500"> Annotation of <span class="text-blue-600">1,886,345</span> cancer-associated loop anchors supported by open chromatin regions from the corresponding cancer types in TCGA, as well as <span class="text-blue-600">1,543,335</span> somatic noncoding SNVs and <span class="text-blue-600">37,374</span> SVs from PCWAG whole genome sequencing datasets</p>

        </li>
        <!-- <li class="flex space-x-3 items-center mb-2">
          <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"></path>
          </svg>
          <p class=" text-xl font-light text-gray-500"> Filter using Cell Types, Disease status, Body Sites or Assays</p>

        </li> -->
        <li class="flex space-x-3 items-center">
          <!-- Icon -->
          <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"></path>
          </svg>
          <p class="text-xl font-light text-gray-500">
            Click on the <span class="text-blue-600">right body map</span> to access a dedicated page for each cancer type.
          </p>
        </li>
      </ul>
      <div class="mt-4">
        <button type="button"
          class="mr-4 mb-4 text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          @click="$router.push({ name: 'CancerCREDetail',params: {id: 'Lung'}})">
          Try Example 1 (Lung cancer)
        </button>

        <!-- <button type="button"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          @click="$router.push({ name: 'CancerCREDetail',params: {id: 'Colon'}})">
          Try Example 2 (Colon cancer)
        </button> -->
      </div>
    </div>
        <div class="w-1/2">
            <CancerBodyMap />
        </div>
    </div>

    </div>
  </template>
  
  <script lang="ts" setup>
  import CancerBodyMap from './CancerBodyMap.vue';
  
  </script>