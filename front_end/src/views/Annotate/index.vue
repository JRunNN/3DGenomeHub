<template>
  <div>
    <n-card class="rounded-lg" style="margin-bottom: 16px">
      <ul>
        <li class="flex space-x-3 items-center mb-2">
          <!-- Icon -->
          <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"></path>
          </svg>
          <p class=" text-xl font-light text-gray-500"> Annotate user uploaded chromatin interaction files using
            multiple
            sources. </p>

        </li>
        <li class="flex space-x-3 items-center mb-2">
          <!-- Icon -->
          <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"></path>
          </svg>
          <p class="text-xl font-light text-gray-500">
            Provide interactive graphs and tables to display anotation results.
          </p>
        </li>
        <li class="flex space-x-3 items-center mb-2">
          <!-- Icon -->
          <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"></path>
          </svg>
          <p class="text-xl font-light text-gray-500">
            The results of the annotations can be shared through a link or are available for download.
          </p>
        </li>
        <li class="flex space-x-3 items-center mb-2">
          <!-- Icon -->
          <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"></path>
          </svg>
          <p class="text-xl font-light text-gray-500">
            Click to view existing sample dataset output or download sample dataset and upload it to our server.
          </p>
        </li>
      </ul>

    </n-card>
    <!-- <div class="flex flex-wrap pt-1 pb-4 border-t dark:border-gray-700">
      <div class="items-center hidden mt-3 mr-4 text-sm font-medium text-gray-900 md:flex dark:text-white">
        Input Type:
      </div>

      <div class="flex flex-wrap">
        <div class="flex items-center mt-3 mr-4">
          <input id="active" type="radio" value="" name="show-only"
            class="w-4 h-4 bg-gray-100 border-gray-300 text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
          <label for="active" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
            Chromatin Loops
          </label>
        </div>
        <div class="flex items-center mt-3 mr-4">
          <input id="pending" type="radio" value="" name="show-only"
            class="w-4 h-4 bg-gray-100 border-gray-300 text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
          <label for="pending" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
            Cis regulatory elements
          </label>
        </div>
        <div class="flex items-center mt-3 mr-4">
          <input id="inactive" type="radio" value="" name="show-only"
            class="w-4 h-4 bg-gray-100 border-gray-300 text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
          <label for="inactive" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
            Single nucleotide variations
          </label>
        </div>
      </div>
    </div> -->
    <router-view></router-view>

  </div>

  <!-- <n-modal v-model:show="showModal1" class="custom-card" preset="card" title="Screenshot of sample data output 1"
    size="huge" :bordered="false">
    <img class="mb-4 w-full lg:mb-0 rounded-lg" src="../../assets/sample_annotation_result_1.png" alt="feature image">
  </n-modal>
  <n-modal v-model:show="showModal2" class="custom-card" preset="card" title="Screenshot of sample data output 2"
    size="huge" :bordered="false">
    <img class="mb-4 w-full lg:mb-0 rounded-lg" src="../../assets/sample_annotation_result_2.png" alt="feature image">

  </n-modal> -->
</template>

<script setup lang="ts">
import { ref } from 'vue'

const showModal1 = ref(false)
const showModal2 = ref(false)

</script>

<style>
.redo-button {
  background-color: #4878D0;

}
</style>