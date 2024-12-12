<template>
  <div class="mx-auto max-w-8xl">

    <div class="flex grow">
      <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
        <CardActions :expand="expand" :isExpand="isExpand" :reload="reload" class="h-full" :segmented="{
          content: true,
          footer: true
        }">
          <template #header>
            <n-h3 align-text>Search samples</n-h3>

          </template>
          <template #default>
            <ul>
              <li class="flex space-x-3 items-center mb-3">
                <!-- Icon -->
                <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
                  viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                    clip-rule="evenodd"></path>
                </svg>
                <p class=" text-xl font-light text-gray-500"> Search samples by summary table</p>

              </li>
              <li class="flex space-x-3 items-center">
                <!-- Icon -->
                <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
                  viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                    clip-rule="evenodd"></path>
                </svg>
                <p class="text-xl font-light text-gray-500">
                  Click
                  <svg class="inline mr-2 mb-1 w-4 h-4 text-grey-500 hover:text-blue-500 transition-colors duration-300"
                    aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M15 11v4.833A1.166 1.166 0 0 1 13.833 17H2.167A1.167 1.167 0 0 1 1 15.833V4.167A1.166 1.166 0 0 1 2.167 3h4.618m4.447-2H17v5.768M9.111 8.889l7.778-7.778" />
                  </svg>button in <n-tag class="mr-2">View </n-tag>column to access a dedicated page of a specific
                  dataset.
                </p>
              </li>
            </ul>
            <div class="mt-6 ml-6 ">
              <n-space align="center">
                <n-tag type="info">Hi-C examples :</n-tag>

                <!-- <button type="button"
                class="mr-4 text-white bg-blue-600 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                @click="$router.push({ name: 'Sample', params: { id: 'GSM3564252' } })">
                Normal prostate cells; GSM356425
              </button>
              <button type="button"
                class="text-white bg-blue-600 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                @click="$router.push({ name: 'Sample', params: { id: 'GSM4908718' } })">
                Prostate cancer cells; GSM4908718
              </button>
              <button type="button"
                class="mr-4 text-white bg-blue-600 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                @click="$router.push({ name: 'Sample', params: { id: 'GSM2692023' } })">
                Non-failing heart; GSM2692023
              </button>

              <button type="button"
                class="text-white bg-blue-600 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                @click="$router.push({ name: 'Sample', params: { id: 'GSM5029740' } })">
                Dilated Cardiomyopathy heart; GSM5029740
              </button> -->


                <button type="button"
                  class="text-white bg-blue-600 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                  @click="$router.push({ name: 'Sample', params: { id: 'GSM7900696' } })">
                  Breast cancer cells; GSM7900696
                </button>

                <button type="button"
                  class="text-white bg-blue-600 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                  @click="$router.push({ name: 'Sample', params: { id: 'GSM4453814' } })">
                  Bladder cancer cells; GSM4453814
                </button>

                <button type="button"
                  class="text-white bg-blue-600 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                  @click="$router.push({ name: 'Sample', params: { id: 'GSM3333325' } })">
                  Gastric cancer cells; GSM3333325
                </button>
              </n-space>
            </div>
            <div class="mt-6 ml-6">
              <n-space align="center">
                <n-tag type="info">HiChIP / ChIA-PET examples :</n-tag>

                <button type="button"
                  class="mr-4 text-white bg-blue-600 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                  @click="$router.push({ name: 'Sample', params: { id: 'GSM5379365' } })">
                  Liver cancer cells; GSM5379365
                </button>
              </n-space>
            </div>
          </template>
          <template #header-extra>
          </template>
        </CardActions>
      </CardWrapper>
    </div>

    <div class="flex grow mt-6 ">
      <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
        <CardActions :expand="expand" :isExpand="isExpand" :reload="reload" class="h-full"
          title="Filter by interactive charts" :segmented="{
            content: true,
            footer: true
          }">
          <template #header>
            <n-h3 prefix="bar" align-text>Sample statistics</n-h3>

          </template>
          <template #header-extra>
          </template>
          <template #default>

            <n-tabs type="line" animated>
              <n-tab-pane name="bar" tab="Sample Bar Plot" display-directive="show">
                <SampleBarChart></SampleBarChart>
              </n-tab-pane>
              <n-tab-pane name="pca" tab="Sample PCA Plot" display-directive="show:lazy">
                <SamplePcaChart></SamplePcaChart>
              </n-tab-pane>
              <!-- <n-tab-pane name="bodymap" tab="Body Map">
                七里香
              </n-tab-pane> -->
            </n-tabs>


          </template>
        </CardActions>
      </CardWrapper>
    </div>

    <div class="grid grid-cols-5 gap-6 mt-6">
      <!-- <div> -->
      <n-card class="bg-white	 hidden lg:block col-span-1  rounded-lg border border-gray-200 p-2 flex-1 h-full">
        <div class="mb-5">
          <!-- <h5 class="text-lg font-medium ml-4 mb-4">Filter By Summary Table</h5> -->

          <n-h3 prefix="bar" align-text>Summary Table</n-h3>

          <div class="relative flex-shrink-0 w-full mb-4 lg:mb-4 lg:mr-5 ">
                <!-- <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                    stroke="currentColor" aria-hidden="true" class="w-5 h-5 text-gray-500 dark:text-gray-400">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                  </svg>
                </div>
                <label for="search" class="hidden">Search cell names</label>
                <input id="search" type="text"
                  class="bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 py-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Search cell names" v-model="cellId">-->
                <AutocompleteDialogBiosample @submit-gene="fetchBiosample"></AutocompleteDialogBiosample>

              </div> 
              
        </div>
                <!-- <div class="search-box border border-gray-200 ">
                  <div class="search-input flex items-center">
                    <Icon :name="SearchIcon" :size="24"></Icon>
                    <input placeholder="NEAT1" v-model="search" class="grow bg-white" @input="fetchData" />
                    <n-text code>ESC</n-text> 
                    <div v-show="showSearchBox">
                      <Icon :name="CloseIcon" :size="20" @click="closeBox()" class="cursor-pointer"></Icon>
                    </div>

                  </div>
                </div> -->
               <hr class="bg-gray-200 dark:border-gray-700 mt-5 mb-5">
        <div class="mb-5">
          <template v-for="(item, index) in initializedData" :key="index">
            <h5 class="uppercase text-sm font-medium text-gray-500 dark:text-gray-400 mb-4">{{
              splitCamelCase(item.category) }}</h5>
            <ul class="list-none pl-0">
              <!-- <li v-for="(name, i) in item.options" class="mb-3" v-show="i < 5 || item.showAll" :key="i">
                  <button type="button" class="flex items-center justify-between group w-full"
                    :class="{ active: isActive(name[0]) }" @click="toggleButton(name[0], item.category)">
                    <span class="flex items-center">
                      <span
                        class="text-gray-900 dark:text-white text-base font-medium group-hover:text-blue-700 dark:group-hover:text-blue-600">
                        {{ name[0] }}
                      </span>
                    </span>
                    <span
                      class="text-base font-medium text-gray-500 dark:text-gray-400 group-hover:text-blue-700 dark:group-hover:text-blue-600">
                      {{ name[1] }}
                    </span>
                  </button>
                </li>
                <li v-if="item.options.length > 5" class="mb-2">
                  <button @click="item.showAll = !item.showAll" class="flex justify-center items-center w-full">
                    <svg :class="{ 'transform rotate-180': item.showAll }" xmlns="http://www.w3.org/2000/svg"
                      class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                    </svg>
                  </button>
                </li> -->

              <n-scrollbar style="min-height: 100px; max-height: 290px">
                <li v-for="(name, i) in item.options" class="mb-3" :key="i">
                  <button type="button" class="flex items-center justify-between group w-full"
                    :class="{ active: isActive(name[0]) }" @click="toggleButton(name[0], item.category)">
                    <span class="flex items-center">
                      <span
                        class="text-gray-900 dark:text-white text-base font-medium group-hover:text-blue-700 dark:group-hover:text-blue-600">
                        {{ name[0] }}
                      </span>
                    </span>
                    <span
                      class="text-base font-medium text-gray-500 dark:text-gray-400 group-hover:text-blue-700 dark:group-hover:text-blue-600">
                      {{ name[1] }}
                    </span>
                  </button>
                </li>
              </n-scrollbar>
              <hr class="bg-gray-200 dark:border-gray-700 mb-5">

            </ul>

          </template>
        </div>
        <div class="mb-5 flex justify-center	">
          <n-button secondary size="large" @click="reloadAnchorMotifTable">
            Reset
          </n-button>
        </div>
      </n-card>
      <!-- </div> -->


      <n-card round class="bg-white col-span-5 lg:col-span-4">
        <div>
          <div class="flex justify-between">
            <div class="mb-4 flex items-center min-h-[28px]">
              <span class="text-sm font-medium text-gray-900 dark:text-white mr-3 flex-shrink-0">
                Showing {{ offset + 1 }} to {{ offset + 1 + pageSize }}
                cell types of {{ itemCount }} in
                total.
              </span>
              <!-- <div class="flex items-center flex-wrap space-x-3"></div> -->
            </div>
            <div class="mb-4 flex items-center">
              <div v-for="assay in assayColor">
                <div
                  :style="{ backgroundColor: assay.color, width: '10px', height: '10px', borderRadius: '50%', display: 'inline-block', marginLeft: '16px', marginRight: '6px' }">
                </div>
                <span> {{ assay.name }} </span>
              </div>
            </div>
          </div>
          <div class="gap-3">
            <n-data-table ref="table" v-if="dataRef" :bordered="false" :columns="columnsRef" :loading="loadingRef"
              :data="TmpDataRef" :pagination="paginationReactive" @update:sorter="handleSorterChange" />
          </div>
        </div>
      </n-card>

    </div>

    <!-- <div class="flex grow mt-6">
    <n-card>
        <template #header>
          <n-h3 prefix="bar" align-text>Filter By Genes</n-h3>
        </template>
        <template #header-extra>
          <AutocompeleDialog @submit-gene="handleGeneSearch"></AutocompeleDialog>
        </template>
      </n-card>
      </div> -->

  </div>
</template>
<script setup lang="ts">
import { ref, onMounted, h, watch, computed, reactive } from 'vue'
import type { DataTableColumns } from 'naive-ui'
import axios from '@/plugins/axios';
// import axios from 'axios'
import { useRouter } from "vue-router";
import { NCard, NDataTable, NButton } from "naive-ui";
import { useLoadingBar } from 'naive-ui'
import SampleBarChart from './SampleBarChart.vue';
import SamplePcaChart from './SamplePcaChart.vue';

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

const paginationReactive = reactive({
  page: 1,
  pageCount: 1,
  pageSize: 15,
  showSizePicker: true,
  pageSizes: [10, 15, 20],
  itemCount: itemCount.value,
  onChange: (page: number) => {
    paginationReactive.page = page
  },
  onUpdatePageSize: (pageSize: number) => {
    paginationReactive.pageSize = pageSize
    paginationReactive.page = 1
  }
})

const populateInitializedData = (data) => {
  let output = []
  const categories = ['health_status', 'tissue', 'data_type'];
  categories.forEach(category => {
    const counts = {};
    console.log(data)
    data.forEach(product => {
      const option = product[category];
      // if (category === 'assays') {
      //   // Handle 'assays' array separately
      //   option.forEach(assay => {
      //     if (!counts[assay]) {
      //       counts[assay] = 0;
      //     }
      //     counts[assay]++;
      //   });
      // } else {
      if (!counts[option]) {
        counts[option] = 0;
      }
      counts[option]++;
      // }
    });

    // Convert counts object to an array of arrays
    const sortedCountsArray = Object.entries(counts).sort((a, b) => b[1] - a[1]);

    output.push({
      category: category,
      options: sortedCountsArray
    });
  });
  return output;
}

// type RowData = {
//   gsm_id: string
//   health_status: string
//   tissue: number
//   data_type: string
// }


const reloadAnchorMotifTable = () => {
  TmpDataRef.value = dataRef.value
  activatedButtons.value = []
  itemCount.value = dataRef.value.length
  paginationReactive.page = 1
  paginationReactive.pageSize = 15

}

function lightenColor(color, percent) {
  const num = parseInt(color.slice(1), 16);
  const amt = Math.round(2.55 * percent);
  const R = (num >> 16) + amt;
  const G = (num >> 8 & 0x00FF) + amt;
  const B = (num & 0x0000FF) + amt;

  return '#' + (0x1000000 + (R < 255 ? R : 255) * 0x10000 + (G < 255 ? G : 255) * 0x100 + (B < 255 ? B : 255)).toString(16).slice(1);
}

function hexToRGBA(hex, opacity) {
  let r = parseInt(hex.slice(1, 3), 16);
  let g = parseInt(hex.slice(3, 5), 16);
  let b = parseInt(hex.slice(5, 7), 16);
  return `rgba(${r}, ${g}, ${b}, ${opacity})`;
}


// column specification
const columns = [
  // {
  //   type: 'expand',
  //   expandable: (rowData) => true,
  //   renderExpand: (rowData) => {
  //     return 'sss'
  //   }
  // },
  {
    title: 'ID',
    key: 'id',
    width: 160
  },
  {
    title: 'Body Sites',
    key: 'tissue',
    width: 230,
    sortOrder: false,
    sorter: 'default',
    render(row) {
      // Define a mapping from tissue names to color codes
      const tissueColors = {
        'Adrenal gland': '#F6EC65',
        'Arthritis': '#E83F19',
        'Bladder': '#3C5EAA',
        'Blood': '#BD2321',
        'Bone': '#F2F2F3',
        'Brain': '#F6BBA7',
        'Breast': '#8B6679',
        'Bronchus': '#EE7E87',
        'Colon': '#F7C96B',
        'Embryo': '#99D6EF',
        'Eye': '#8D1C27',
        'Heart': '#EC6822',
        'Kidney': '#697F15',
        'Liver': '#8B5241',
        'Lung': '#F7D774',
        'Lymph': '#06763B',
        'Muscle tissue': '#F7BE92',
        'Nerve': '#F5E72E',
        'Ovary': '#B35CA0',
        'Pancreas': '#DFDE86',
        'Pharynx': '#FDE5C8',
        'Placenta': '#E83F29',
        'Prostate gland': '#ACC7E8',
        'Skin': '#854922',
        'Soft tissue': '#DBA883',
        'Spleen': '#781E4E',
        'Stomach': '#F5AF32',
        'Testis': '#788CA4',
        'Thymus': '#92C976',
        'Thyroid gland': '#F6B59C',
        'Uterus': '#EABDD7',
        'Vagina': '#DE4E96',
        'Vessel': '#4B83C4'
      };

      // Get the color for the current row's tissue
      const baseColor = tissueColors[row.tissue] || '#CCCCCC'; // Default to light grey if tissue is not listed
      const backgroundColor = hexToRGBA(baseColor, 0.2); // Set opacity to 20%

      // Return a div element with styled background color and text color
      return h('div', {
        style: {
          backgroundColor: backgroundColor,
          // color: baseColor,
          padding: '4px 8px',
          borderRadius: '4px',
          textAlign: 'center',
          width: '60%', // Adjust width as needed
        }
      }, row.tissue);
    }
  },
  {
    title: 'Health Status',
    key: 'health_status',
    width: 200,
    sortOrder: false,
    sorter: 'default',
  },
  {
    title: 'Biomaterial',
    key: 'biomaterial_type',
    // width: 120,
    sorter: 'default',
    sortOrder: false
  },
  {
    title: 'Assay',
    key: 'data_type',
    // width: 100,
    sortOrder: false,
    sorter: 'default',
    render(row) {
      const assayColor = {
        'ChIA-PET': '#6267FF',
        'HiChIP': '#FF61C9',
        'in-situ Hi-C': '#00B27B',
        'intact Hi-C': '#00B27B',
        // 'ATAC-seq': 'blue'
      };

      const color = assayColor[row.data_type] || 'grey';

      return h('div', {
        style: {
          backgroundColor: color,
          width: '10px',
          height: '10px',
          borderRadius: '50%',
          display: 'inline-block',
          marginLeft: '5px'
        }
      })

    }
  },
  {
    title: 'View',
    key: 'visualize',
    render: function (row) {
      return h('svg', {
        class: 'w-5 h-5 text-grey-500 hover:text-blue-500 cursor-pointer transition-colors duration-300',
        'aria-hidden': 'true',
        xmlns: 'http://www.w3.org/2000/svg',
        fill: 'none',
        viewBox: '0 0 18 18',
        onClick: (e) => { handleClick(row.id) }
      }, [
        h('path', {
          stroke: 'currentColor',
          'stroke-linecap': 'round',
          'stroke-linejoin': 'round',
          'stroke-width': '2',
          d: 'M15 11v4.833A1.166 1.166 0 0 1 13.833 17H2.167A1.167 1.167 0 0 1 1 15.833V4.167A1.166 1.166 0 0 1 2.167 3h4.618m4.447-2H17v5.768M9.111 8.889l7.778-7.778'
        })
      ]);
    }
  }
]



const assayColor = [
  {
    name: "Hi-C",
    color: '#00B27B'
  },
  {
    name: 'ChIA-PET',
    color: '#6267FF'
  },
  {
    name: 'HiChIP',
    color: '#FF61C9'
  }//,
  // {
  //   name: 'RNA-seq',
  //   color: '#FFB600'
  // },
  // {
  //   name: 'ChIP-seq',
  //   color: '#FF0156'
  // },
  // {
  //   name: 'ATAC-seq',
  //   color: 'blue'
  // }
]

// const columns = createColumns()


const table = ref(null)
const columnsRef = ref(columns)

const handleSorterChange = (sorter) => {
  columnsRef.value.forEach((column) => {
    /** column.sortOrder !== undefined means it is uncontrolled */
    if (column.sortOrder === undefined)
      return
    if (!sorter) {
      column.sortOrder = false
      return
    }
    if (column.key === sorter.columnKey)
      column.sortOrder = sorter.order
    else column.sortOrder = false
  })
}

// navigate to individual cell type page
const handleClick = (value) => {
  const cleanedValue = value.replace(/^[^a-zA-Z0-9]+/, '');
  router.push({ name: 'Sample', params: { id: cleanedValue } })
}


const handleGeneSearch = (value) => {
  router.push({ path: `/gene/${value}` });
}

function splitCamelCase(string) {
  return string
    // insert a space before all caps
    .replace(/([a-z])([A-Z])/g, '$1 $2')
}

const toggleButton = (buttonId, category) => {
  console.log('enter toggleButton')
  const index = activatedButtons.value.indexOf(buttonId);
  console.log(category)
  if (index === -1) {
    console.log('not found')

    activatedButtons.value.push(buttonId);
    if (category == 'health_status' && !healthStatus.value.includes(buttonId)) {
      healthStatus.value.push(buttonId);
    }
    if (category == 'tissue' && !tissue.value.includes(buttonId)) {
      tissue.value.push(buttonId);
    }
    if (category == 'data_type' && !data_type.value.includes(buttonId)) {
      data_type.value.push(buttonId);
    }
    // if (!cellType.value === button) {
    //   cellType.value = button;
    // }
    // fnGetData(1)

  } else {
    console.log('not found')

    if (category == 'health_status' && healthStatus.value.includes(buttonId)) {
      healthStatus.value = healthStatus.value.filter(item => item !== buttonId);
    }
    if (category == 'tissue' && tissue.value.includes(buttonId)) {
      tissue.value = tissue.value.filter(item => item !== buttonId);
    }
    if (category == 'data_type' && data_type.value.includes(buttonId)) {
      data_type.value = data_type.value.filter(item => item !== buttonId);
    }
    activatedButtons.value.splice(index, 1);
    // fnGetData(1)

  }
  currentPage.value = 1


}

const isActive = (buttonId) => {
  return activatedButtons.value.includes(buttonId);
}
const fnGetMenudata = () => {
  axios.get('/samples', {
    responseType: 'json',
  })
    .then(res => {
      // console.log('data recevied')
      console.log(res.data)
      loadingRef.value = false
      dataRef.value = res.data
      // from.value = res.data.from
      // to.value = res.data.to
      itemCount.value = res.data.length
      TmpDataRef.value = res.data
      // paginationReactive.value.itemCount = res.data.length
      // paginationReactive.value.pageCount = Math.ceil(itemCount.value / pageSize.value)

      // dataRef.value = res.data.data
      // if (includeInitialData) {
      initializedData.value = populateInitializedData(res.data)
      // includeInitialData = false
      // }
      // console.log('initialized data',initializedData.value)
      loadingBar.finish()

    }).catch(function (error) {
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        console.log(error.response.data);
        console.log(error.response.status);
        console.log(error.response.headers);
      } else if (error.request) {
        // The request was made but no response was received
        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
        // http.ClientRequest in node.js
        console.log(error.request);
      } else {
        // Something happened in setting up the request that triggered an Error
        console.log('Error', error.message);
      }
      console.log(error.config);
    });

}

const offset = computed(() => {
  return (currentPage.value - 1) * pageSize.value
})

const loadingBar = useLoadingBar()

const id = ref('')
const fetchBiosample = (biosample) => {
  id.value = biosample
  console.log('id:', biosample);
}

onMounted(() => {
  fnGetMenudata()
  // activatedButtons.value = ['in-situ Hi-C', 'Blood']
  watch([() => healthStatus.value, () => tissue.value, () => data_type.value, () => id.value], (newValues) => {
    const [newHealthStatus, newTissue, newDataType, newId] = newValues;

    // Debugging output
    console.log('HealthStatus:', newHealthStatus);
    console.log('Tissue:', newTissue);
    console.log('DataType:', newDataType);
    console.log('id:', newId);

    if (!newHealthStatus.length && !newTissue.length && !newDataType.length && !newId.length) {
      TmpDataRef.value = dataRef.value;
    } else {
      TmpDataRef.value = dataRef.value.filter((item: any) => {
        const healthStatusMatch = !newHealthStatus.length || newHealthStatus.includes(item.health_status);
        const tissueMatch = !newTissue.length || newTissue.includes(item.tissue);
        const dataTypeMatch = !newDataType.length || newDataType.includes(item.data_type);
        const idMatch = !newId.length || newId.includes(item.id);
        return healthStatusMatch && tissueMatch && dataTypeMatch && idMatch;
      });
    }

    paginationReactive.page = 1
    paginationReactive.pageSize = 15
    itemCount.value = TmpDataRef.value.length;
  }, { deep: true });

  // watch(() => tissue.value, (newValue) => {
  //     console.log(newValue);
  //     if (newValue.length == 0) {
  //       TmpDataRef.value= dataRef.value
  //     }
  //     TmpDataRef.value = TmpDataRef.value.filter((item: any) => newValue.includes(item.tissue));
  //      itemCount.value = TmpDataRef.value.length

  // }, { deep: true });

  // watch(() => data_type.value, (newValue, oldValue) => {
  //     console.log(newValue);
  //     if (newValue.length == 0) {
  //       TmpDataRef.value= dataRef.value
  //     }
  //     TmpDataRef.value = TmpDataRef.value.filter((item: any) => newValue.includes(item.data_type));
  //     itemCount.value = TmpDataRef.value.length

  // }, { deep: true });
})
</script>
<style scoped>
.active {
  background-color: #e2e9ec;
  /* Green */
  color: white;
}
</style>