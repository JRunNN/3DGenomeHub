<template>
  <div class="mx-auto max-w-8xl">

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
          <p class=" text-xl font-light text-gray-500"> This page contains transcription-associated chromatin interactions from 78 cancer and 60 non-cancer cell types. </p>

        </li>
        <li class="flex space-x-3 items-center mb-2">
          <!-- Icon -->
          <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"></path>
          </svg>
          <p class=" text-xl font-light text-gray-500"> Filter using Cell Types, Disease status, Body Sites or Assays</p>

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
            <svg class="inline mb-1 w-4 h-4 text-grey-500 hover:text-blue-500 transition-colors duration-300"
              aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 11v4.833A1.166 1.166 0 0 1 13.833 17H2.167A1.167 1.167 0 0 1 1 15.833V4.167A1.166 1.166 0 0 1 2.167 3h4.618m4.447-2H17v5.768M9.111 8.889l7.778-7.778" />
              </svg> in Action column to access a dedicated page for each cell type. Track view and tabular view of Active Browser is provided.
          </p>
        </li>
      </ul>

      <div class="mt-4">
        <button type="button"
          class="mr-4 text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          @click="$router.push({ name: 'CellType', params: { id: 'K562' } })">
          Try Example 1 (Cancer cell line K562)
        </button>

        <button type="button"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          @click="$router.push({ name: 'CellType', params: { id: 'GM12878' } })">
          Try Example 2 (Non-Cancer cell line GM12878)
        </button>
      </div>
    </n-card>

    <div class="grid grid-cols-5 gap-6 mt-4">
      <div>
        <aside class="bg-white	 hidden lg:block col-span-1  rounded-lg border border-gray-200  p-5 flex-1">
          <div class="mb-5">
            <h5 class="uppercase text-sm font-medium text-gray-500 dark:text-gray-400 mb-4">Filter By</h5>
            <div class="grid grid-cols-2 rounded-md shadow-sm w-full" role="group">
              <!-- <button type="button"
                class="inline-flex justify-center group items-center px-4 py-2 text-sm font-medium border border-gray-200 rounded-l-lg focus:z-10 focus:ring-2 dark:bg-gray-700 dark:border-gray-600 dark:text-gray-100 dark:hover:text-blue-600 hover:text-blue-700 focus:ring-blue-700 focus:text-blue-700 dark:focus:ring-blue-500 dark:focus:text-blue-600 dark:hover:bg-gray-900 text-blue-700 dark:text-blue-600 bg-gray-100 dark:bg-gray-900">
                   Table</button>
                   <button type="button"
                class="inline-flex justify-center group items-center px-4 py-2 text-sm font-medium border border-gray-200 rounded-r-lg focus:z-10 focus:ring-2 dark:bg-gray-700 dark:border-gray-600 dark:text-gray-100 dark:hover:text-blue-600 hover:text-blue-700 focus:ring-blue-700 focus:text-blue-700 dark:focus:ring-blue-500 dark:focus:text-blue-600 dark:hover:bg-gray-900 bg-white hover:bg-gray-100 text-gray-800">
                 Map</button> -->

            </div>
            <hr class="bg-gray-200 dark:border-gray-700 mb-5">

            <div class="relative flex-shrink-0 w-full mb-4 lg:mb-4 lg:mr-5 ">
              <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                  stroke="currentColor" aria-hidden="true" class="w-5 h-5 text-gray-500 dark:text-gray-400">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
              <label for="search" class="hidden">Search cell names</label>
              <input id="search" type="text"
                class="bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 py-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Search cell names" v-model="cellId">
            </div>
          </div>
          <hr class="bg-gray-200 dark:border-gray-700 mb-5">

          <div class="mb-5">
            <template v-for="(item, index) in initializedData" :key="index">
              <h5 class="uppercase text-sm font-medium text-gray-500 dark:text-gray-400 mb-4">{{
                splitCamelCase(item.category) }}</h5>
              <ul>
                <li v-for="(name, i) in item.options" class="mb-3" v-show="i < 5 || item.showAll" :key="i">
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
                <!-- Show toggle button if options exceed 5 -->
                <li v-if="item.options.length > 5" class="mb-2">
                  <button @click="item.showAll = !item.showAll" class="flex justify-center items-center w-full">
                    <svg :class="{ 'transform rotate-180': item.showAll }" xmlns="http://www.w3.org/2000/svg"
                      class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                    </svg>
                  </button>
                </li>
                <hr class="bg-gray-200 dark:border-gray-700 mb-5">
              </ul>
            </template>
          </div>

        </aside>
      </div>


      <n-card round class="bg-white col-span-5 lg:col-span-4">
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
            <div v-for="assay in assayColor">
              <div
                :style="{ backgroundColor: assay.color, width: '10px', height: '10px', borderRadius: '50%', display: 'inline-block', marginLeft: '16px', marginRight: '6px' }">
              </div>
              <span> {{ assay.name }} </span>
            </div>
          </div>
        </div>
        <div class="gap-3">
          <n-data-table remote :bordered="false" :columns="columns" :loading="loadingRef" :data="dataRef"
            :pagination="paginationReactive" @update:page="handlePageChange" @update:sorter="handleSorterChange" />
        </div>
      </n-card>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted, reactive, h, watch, computed } from 'vue'
import type { DataTableColumns } from 'naive-ui'
import axios from 'axios';
import { useRouter } from "vue-router";
import { NButton } from "naive-ui";
import { useLoadingBar } from 'naive-ui'

const router = useRouter()
const diseaseStatus = ref([])
const bodySites = ref([])
const assays = ref([])
const factor = ref([])
// const cellId = ref([])
const loadingRef = ref(true)
const dataRef = ref([])
const from = ref(0)
const to = ref(0)
const currentPage = ref(1)
const pageSize = ref(10)
const initializedData = ref([])
const itemCount = ref(0)
const paginationReactive = computed(() => ({
  page: currentPage.value,
  pageCount: 1,
  pageSize: pageSize.value,
  itemCount: itemCount.value
}))
let includeInitialData = true
const cellId = ref('')

const populateInitializedData = (data) => {
  let output = []
  const categories = ['disease_status', 'body_site', 'assays'];
  categories.forEach(category => {
    const counts = {};
    data.forEach(product => {
      const option = product[category];
      if (category === 'assays') {
        // Handle 'assays' array separately
        option.forEach(assay => {
          if (!counts[assay]) {
            counts[assay] = 0;
          }
          counts[assay]++;
        });
      } else {
        if (!counts[option]) {
          counts[option] = 0;
        }
        counts[option]++;
      }
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



// const promoterColumn = {
//   title: '# Promoters',
//   key: 'activePromoters',
//   sorter: true,
//   sortOrder: false,
//   render(row) {
//     return row.activePromoters.toLocaleString()
//   }
// }

// const transcriptColumn = {
//   title: '# Transcripts',
//   key: 'expressedTranscripts',
//   sorter: true,
//   sortOrder: false,
//   render(row) {
//     return row.expressedTranscripts.toLocaleString()
//   }
// }

// const interactionColumn = {
//   title: '# Interactions',
//   key: 'chromatinInteractions',
//   sorter: true,
//   sortOrder: false,
//   render(row) {
//     return row.chromatinInteractions.toLocaleString()
//   }
// }

// column specification
const columns = [
  {
    title: 'ID',
    key: 'cell_id',
  },
  {
    title: 'Disease',
    key: 'disease_status',
  },
  {
    title: 'Body Sites',
    key: 'body_site',
  },
  {
    title: 'Assays',
    key: 'assays',
    render(row) {
      return row.assays.map(assay => {
        let color;
        switch (assay) {
          case 'ChIA-PET': // ChIAPET
            color = 'red'; // Replace with desired color for 'ChIAPET/HiChIP'
            break;
          case 'HiChIP': // HiChIP
            color = 'blue'; // Replace with desired color for 'ChIAPET/HiChIP'
            break;
          case 'RNA-seq': // RNAseq
            color = 'green'; // Replace with desired color for 'RNA-seq'
            break;
          case 'ChIP-seq': // ChIPseq
            color = 'purple'; // Replace with desired color for 'ChIPseq'
            break;
          case 'ATAC-seq': // ATACseq
            color = '#000000'; // Replace with desired color for 'ChIPseq'
            break;
          default:
            color = 'orange'; // Default color if type is not recognized
        }

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
      })
    }
  },
  {
    title: 'Factor',
    key: 'factor'
  },
  // promoterColumn,
  // transcriptColumn,
  // interactionColumn,
  {
    title: 'Action',
    key: 'actions',
    render: function (row) {
      return h('svg', {
        class: 'w-4 h-4 text-grey-500 hover:text-blue-500 cursor-pointer transition-colors duration-300',
        'aria-hidden': 'true',
        xmlns: 'http://www.w3.org/2000/svg',
        fill: 'none',
        viewBox: '0 0 18 18',
        onClick: (e) => { handleClick(row.cell_id) }
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


// navigate to individual cell type page
const handleClick = (value) => {
  // Your click handling logic goes here
  router.push({ name: 'CellType', params: { id: value.replace(/[\s,]+/g, "-") } })
}


const handlePageChange = (page) => {
  if (!loadingRef.value) {
    currentPage.value = page
    loadingRef.value = true
    // fnGetData(currentPage)
  }
}

const handleSorterChange = (sorter) => {
  // if (!sorter || sorter.columnKey === 'column1') {
  //         if (!loadingRef.value) {
  //           loadingRef.value = true
  //           fnGetData()
  //         }
  // }
}

function splitCamelCase(string) {
  return string
    // insert a space before all caps
    .replace(/([a-z])([A-Z])/g, '$1 $2')
}

const activatedButtons = ref([])
const toggleButton = (buttonId, category) => {
  console.log('enter toggleButton')
  const index = activatedButtons.value.indexOf(buttonId);
console.log(category)
  if (index === -1) {
    console.log('not found')

    activatedButtons.value.push(buttonId);
    if (category == 'disease_status' && !diseaseStatus.value.includes(buttonId)) {
      diseaseStatus.value.push(buttonId);
    }
    if (category == 'body_site' && !bodySites.value.includes(buttonId)) {
      bodySites.value.push(buttonId);
    }
    if (category == 'assays' && !assays.value.includes(buttonId)) {
      assays.value.push(buttonId);
    }
    // if (!cellType.value === button) {
    //   cellType.value = button;
    // }
    // fnGetData(1)

  } else {
    console.log(' found')

    if (category == 'disease_status' && diseaseStatus.value.includes(buttonId)) {
      diseaseStatus.value = diseaseStatus.value.filter(item => item !== buttonId);
    }
    if (category == 'body_site' && bodySites.value.includes(buttonId)) {
      bodySites.value = bodySites.value.filter(item => item !== buttonId);
    }
    if (category == 'assays' && assays.value.includes(buttonId)) {
      assays.value = assays.value.filter(item => item !== buttonId);
    }
    activatedButtons.value.splice(index, 1);
    // fnGetData(1)

  }
}
const isActive = (buttonId) => {
  return activatedButtons.value.includes(buttonId);
}



const assayColor = [
  {
    name: 'ChIA-PET',
    color: 'red'
  },
  {
    name: 'HiChIP',
    color: 'blue'
  }
]

const CellTypeDataParams = computed(() => ({
  diseaseStatus: diseaseStatus.value,
  bodySites: bodySites.value,
  assays: assays.value,
  factor: factor.value,
  cellId: cellId.value,
  pagesize: pageSize.value,
  page: currentPage.value,
  // promoterSortOrder: promoterColumn.sortOrder,
  // transcriptSortOrder: transcriptColumn.sortOrder,
  // interactionSortOrder: interactionColumn.sortOrder,
  includeInitialData: includeInitialData
}))

// function to retrieve data
const fnGetData = (params) => {
  axios.get(import.meta.env.VITE_BASE_URL + '/search/datalist', {
    responseType: 'json',
    params: params,
    paramsSerializer: {
      indexes: null
    }
  })
    .then(res => {
      // console.log('data recevied')
      console.log(res.data)
      loadingRef.value = false
      from.value = res.data.from
      to.value = res.data.to
      itemCount.value = res.data.itemCount
      paginationReactive.value.itemCount = res.data.itemCount
      paginationReactive.value.pageCount = Math.ceil(itemCount.value / pageSize.value)

      dataRef.value = res.data.data
      if (includeInitialData) {
        initializedData.value = populateInitializedData(res.data.initial_data)
        includeInitialData = false
      }
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


const loadingBar = useLoadingBar()

onMounted(() => {
  watch(() => CellTypeDataParams, (newValue) => {
    // console.log(newValue.value)
    loadingBar.start()
    fnGetData(newValue.value)
  }, { immediate: true, deep: true })

})
</script>
<style scoped>
.active {
  background-color: #e2e9ec;
  /* Green */
  color: white;
}</style>