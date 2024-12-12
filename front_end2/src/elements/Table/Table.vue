<template>
      <n-card :bordered="true" :segmented="{ content: true }" class="mb-6"
        header-style="font-size: 20px;background-color: #D8D8D8;color: #09253D;padding-top: 4px;padding-bottom: 4px;"
        size="small" title="Cancer associated somatic SNV">
        <div class="flex justify-between">
          <div class="mb-4 flex items-center min-h-[28px]">
            <span class="text-sm font-medium text-gray-900 dark:text-white mr-3 flex-shrink-0">
              Showing {{ from }} to {{ to }}
              cell types of {{ itemCount }} in
              total.
            </span>
            <!-- <div class="flex items-center flex-wrap space-x-3"></div> -->
          </div>
          <div class="mb-4 flex items-center">
            <!-- <div v-for="assay in assayColor">
                <div
                  :style="{ backgroundColor: assay.color, width: '10px', height: '10px', borderRadius: '50%', display: 'inline-block', marginLeft: '16px', marginRight: '6px' }">
                </div>
                <span> {{ assay.name }} </span>
              </div> -->
          </div>
              <!-- search bar -->
      <form class="ml-8 mr-8 mb-4 flex w-18 items-center">
          <!-- <label for="simple-search" class="sr-only">Search</label> -->
          <input type="text" id="simple-search"
              class="relative m-0  block min-w-0 flex-auto  rounded-l border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-1.5 text-base font-normal text-neutral-700 outline-none transition duration-300 ease-in-out focus:border-primary focus:text-neutral-700 focus:shadow-te-primary focus:outline-none"
              placeholder="Search gene names ..." required v-model="currentLocString">
          <button
              class="relative flex items-center mr-3 px-4 py-2.5
                              text-white
                              rounded-r bg-blue-700 transition duration-150 ease-in-out hover:bg-primary-700 hover:shadow-lg focus:bg-primary-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-primary-800 active:shadow-lg"
              type="button" id="location-search" data-te-ripple-init data-te-ripple-color="light"
              @click="handleLocationSearch">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-5 w-5">
                  <path fill-rule="evenodd"
                      d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z"
                      clip-rule="evenodd" />
              </svg>
          </button>
      </form>
          <div class="mb-4 flex items-center" role="group">
            <button type="button"
              class="text-blue-700 border border-blue-700 hover:bg-blue-700 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-l text-sm text-center inline-flex items-center p-2 h-10"
              @click="syncWithBrowser">
              Sync
            </button>
            <button type="button"
              class="text-blue-700 border-t border-b border-r border-blue-700 hover:bg-blue-700 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-r text-sm text-center inline-flex items-center p-2 h-10"
              @click="reloadFullData">
              Reload
            </button>
          </div>
          <div class="ml-10 mb-4 flex items-center" role="group">
            <button type="button"
              class="text-blue-700 border border-blue-700 hover:bg-blue-700 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded text-sm text-center inline-flex items-center p-2 h-10"
              @click="exportFullData">
              Export
            </button>
          </div>
        </div>
        <div class="gap-3">
          <n-data-table remote :bordered="false" :columns="columns" :loading="loadingRef" :data="dataRef"
            :pagination="paginationReactive" @update:page="handlePageChange" @update:sorter="handleSorterChange" />
        </div>
      </n-card>
</template>

<script lang="ts" setup>

</script>

<style scoped>

</style>