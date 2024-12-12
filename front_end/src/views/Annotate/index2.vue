<template>
    <div class="mx-auto max-w-8xl">
  
      <div class="flex grow">
        <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
          <CardActions :expand="expand" :isExpand="isExpand" :reload="reload" class="h-full" :segmented="{
            content: true,
            footer: true
          }">
            <template #header>
              <n-h3 align-text>Annotate</n-h3>
  
            </template>
            <template #default>
             
                <!-- <n-card title="歌曲" style="margin-bottom: 16px"> -->
    <n-tabs type="line" animated>
      <n-tab-pane name="Cis Regulatory elements" tab="Cis Regulatory elements">
        <div class="sm:col-span-2">
                  <!-- <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Description</label> -->
                  <textarea id="description" rows="8" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Write a product description here..."></textarea>
              </div>
      </n-tab-pane>
      <n-tab-pane name="Chromatin Loops" tab="Chromatin Loops">
        <div class="sm:col-span-2">
                  <!-- <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Description</label> -->
                  <textarea id="description" rows="8" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Write a product description here..."></textarea>
              </div>
      </n-tab-pane>
      <n-tab-pane name="SNPs" tab="SNPs">
        <div class="sm:col-span-2">
                  <!-- <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Description</label> -->
                  <textarea id="description" rows="8" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Write a product description here..."></textarea>
              </div>
      </n-tab-pane>
    </n-tabs>
  <!-- </n-card> -->
            </template>
            <template #header-extra>
            </template>
            <template #footer>
                <div class="flex items-center space-x-4">
                    <button  @click="showModal = true"  class="block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800" type="button">
        Advanced settings
    </button>
              <button type="button"class="text-red-600 inline-flex items-center hover:text-white border border-red-600 hover:bg-red-600 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:border-red-500 dark:text-red-500 dark:hover:text-white dark:hover:bg-red-600 dark:focus:ring-red-900">
                  Annotate
              </button>
              
          </div>
          <!-- Modal toggle -->
<!-- <div class="flex justify-center m-5">
    <button data-modal-target="defaultModal" data-modal-toggle="defaultModal" class="block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800" type="button">
        Toggle modal
    </button>
</div> -->



            </template>
          </CardActions>
        </CardWrapper>
      </div>

    </div>
    
    <!-- Main modal -->
<n-modal v-model:show="showModal">
    <!-- <form action="#" method="get" id="defaultModal" tabindex="-1" aria-hidden="true"
    class="fixed top-0 left-0 right-0 z-50  w-full p-4  overflow-y-auto md:inset-0 h-modal md:h-full"> -->
    <div class="relative w-full h-full max-w-md md:h-auto">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-800">
            <!-- Modal header -->
            <div class="flex items-start justify-between px-6 py-4 rounded-t">
                <h3 class="text-lg font-normal text-gray-500 dark:text-gray-400">
                    Filter by category
                </h3>
                <button type="button"
                    class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
                    data-modal-toggle="defaultModal">
                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                            clip-rule="evenodd"></path>
                    </svg>
                    <span class="sr-only">Close modal</span>
                </button>
            </div>
            <!-- Modal body -->
            <div class="grid grid-cols-2 gap-2 px-4 md:px-6 md:grid-cols-3">
                <div class="flex items-center">
                    <input id="apple" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="apple" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Apple (56)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="fitbit" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="fitbit" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Fitbit (56)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="dell" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="dell" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Dell (56)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="asus" type="checkbox" value="" checked
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="asus" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Asus (97)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="logitech" type="checkbox" value="" checked
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="logitech" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Logitech (97)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="msi" type="checkbox" value="" checked
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="msi" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        MSI (97)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="bosch" type="checkbox" value="" checked
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="bosch" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Bosch (176)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="sony" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="sony" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Sony (234)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="samsung" type="checkbox" value="" checked
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="samsung" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Samsung (76)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="canon" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="canon" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Canon (49)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="microsoft" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="microsoft"
                        class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Microsoft (45)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="razor" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="razor" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Razor (49)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="emetec" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="emetec" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Emetec (16)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="nvidia" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="nvidia" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Nvidia (45)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="hp" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="hp" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        HP (234)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="benq" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="benq" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        BenQ (45)
                    </label>
                </div>

                <div class="flex items-center">
                    <input id="rockstar" type="checkbox" value=""
                        class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />

                    <label for="rockstar" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Rockstar (49)
                    </label>
                </div>
            </div>
            <!-- Modal footer -->
            <div class="flex items-center p-6 space-x-4 rounded-b dark:border-gray-600">
                <button type="submit"
                    class="text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-700 dark:hover:bg-primary-800 dark:focus:ring-primary-800">
                    Apply
                </button>
                <button type="button"
                    class="py-2.5 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">
                    Reset
                </button>
            </div>
        </div>
    </div>
<!-- </form> -->
</n-modal>
  </template>
  <script setup lang="ts">
  import { ref, onMounted, h, watch, computed, reactive, nextTick } from 'vue'
  import type { DataTableColumns } from 'naive-ui'
  import axios from '@/plugins/axios';
  // import axios from 'axios'
  import { useRouter } from "vue-router";
  import { NCard, NDataTable, NButton } from "naive-ui";
  import { useLoadingBar } from 'naive-ui'
//   import SampleBarChart from './SampleBarChart.vue';
//   import SamplePcaChart from './SamplePcaChart.vue';
  
  import { useThemeStore } from "@/stores/theme"
  import AutocompleteDialogBiosample from '@/components/common/AutocompleteDialogBiosample.vue'
  
  import AutocompeleDialog from '@/components/common/AutocompleteDialog.vue'
  const SearchIcon = "ion:search-outline"
  
  const themeStore = useThemeStore()
  
  const style = computed<{ [key: string]: any }>(() => themeStore.style)
  
  const textSecondaryColor = computed<string>(() => style.value["--fg-secondary-color"])
  
  const router = useRouter()
  const healthStatus = ref([])
  const tissue = ref([])
  const data_type = ref([])
  const factor = ref([])
  
  const loadingRef = ref(true)
  const dataRef = ref(null)
  const TmpDataRef = ref(null)
  
  const currentPage = ref(1)
  const pageSize = ref(10)
  const initializedData = ref([])
  const itemCount = ref(0)
  const activatedButtons = ref([])

const showModal = ref(false)

 
  onMounted( () => {
  
});
  </script>
  <style scoped>
  .active {
    background-color: #e2e9ec;
    /* Green */
    color: white;
  }
  </style>