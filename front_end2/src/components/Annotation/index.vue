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
          <p class=" text-xl font-light text-gray-500"> Annotate user uploaded chromatin interaction files using multiple
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

      <div class="mt-4">
        <div class="mr-6">
          <n-tooltip trigger="hover">
            <template #trigger>
              <button type="button"
                class="mr-2 text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                @click="$router.push({ name: 'AnnotationDetail', params: { taskId: 'b2295290-a6f1-43eb-a022-72a955a8955b' } })">
                View annotation output of sample 1
              </button>
            </template>
            # of chromatin loops: 500; takes ~ 1 min to complete annotation
          </n-tooltip>
          <n-tooltip trigger="hover">
            <template #trigger>
              <a href="/media/examples/ENCFF038FGR_sample100.bedpe">
              <svg class="inline w-[22px] h-[22px] text-gray-800 dark:text-white" aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                <path
                  d="M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z" />
                <path
                  d="M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z" />
              </svg>
            </a>
            </template>
            Download sample 1
          </n-tooltip>
        </div>
        <div class="mr-6">
          <n-tooltip trigger="hover">
            <template #trigger>
              <button type="button"
                class="mr-2 text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                @click="$router.push({ name: 'AnnotationDetail', params: { taskId: 'b2295290-a6f1-43eb-a022-72a955a8955b' } })">
                View annotation output of sample 2
              </button>
            </template>
            # of chromatin loops: 10000; takes ~ 80 seconds to complete annotation
          </n-tooltip>
          <n-tooltip trigger="hover">
            <template #trigger>
              <a href="/media/examples/ENCFF038FGR_sample10000.bedpe">

              <svg class="inline w-[22px] h-[22px] text-gray-800 dark:text-white" aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                <path
                  d="M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z" />
                <path
                  d="M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z" />
              </svg>
              </a>
            </template>
            Download sample 2
          </n-tooltip>
        </div>

      </div>
    </n-card>

    <router-view></router-view>

    <section class="bg-gray-50 dark:bg-gray-900">
        <div class="py-8 px-4 mx-auto max-w-screen-xl sm:py-16 lg:px-6">
            <div class="mx-auto max-w-screen-md text-center mb-8 lg:mb-16">
                <!-- <h2 class="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Secure platform,
                    secure data</h2> -->
                <p class="font-light text-gray-500 dark:text-gray-400 sm:text-xl">Example output screenshots.</p>
            </div>
            <div class="space-y-8 md:grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 md:gap-8 xl:gap-8 md:space-y-0">
                <div class="p-6 bg-white rounded shadow dark:bg-gray-800 relative" @click="showModal1 = true">
                  <img class="mb-4 w-full lg:mb-0 rounded-lg" src="../../assets/sample_annotation_result_1.png" alt="feature image">
                  <svg class="absolute inset-0  w-[45px] h-[45px] text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
    <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="m21 21-3.5-3.5M10 7v6m-3-3h6m4 0a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z"/>
  </svg>
                </div>
                <div class="p-6 bg-white rounded shadow dark:bg-gray-800 relative" @click="showModal2 = true">
                  <img class="mb-4 w-full lg:mb-0 rounded-lg" src="../../assets/sample_annotation_result_2.png" alt="feature image">
                  <svg class="absolute inset-0 w-[45px] h-[45px] text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
    <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="m21 21-3.5-3.5M10 7v6m-3-3h6m4 0a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z"/>
  </svg>
                </div>
            </div>
        </div>
    </section>
  </div>

  <n-modal
    v-model:show="showModal1"
    class="custom-card"
    preset="card"
    title="Screenshot of sample data output 1"
    size="huge"
    :bordered="false"
  >
  <img class="mb-4 w-full lg:mb-0 rounded-lg" src="../../assets/sample_annotation_result_1.png" alt="feature image">
  </n-modal>
  <n-modal
    v-model:show="showModal2"
    class="custom-card"
    preset="card"
    title="Screenshot of sample data output 2"
    size="huge"
    :bordered="false"
  >
  <img class="mb-4 w-full lg:mb-0 rounded-lg" src="../../assets/sample_annotation_result_2.png" alt="feature image">

  </n-modal>
</template>

<script setup lang="ts">
import {ref} from 'vue'
const showModal1 = ref(false)
const showModal2 = ref(false)

</script>

<style>
.redo-button {
  background-color: #4878D0;

}
</style>