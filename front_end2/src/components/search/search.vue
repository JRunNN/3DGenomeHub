<template>
  <n-card style="margin-bottom: 16px">
    <h1 class="mb-2 text-3xl font-bold tracking-tight text-gray-600"><a href="#">Search</a></h1>
    <p class="mb-5 text-xl font-light text-gray-500">Search for Cell Types, Genes, Chromation interactions and SNPs in the
      tables below. Or click one of the examples below. </p>
                <!-- <div class="mt-4">
            <n-data-table remote 
            ref="table"
            :bordered="false" 
            :columns="columns" 
            :loading="loadingRef" 
            :data="dataRef"
              :pagination="paginationReactive" 
              @update:page="handlePageChange" 
              @update:sorter="handleSorterChange"
               />
          </div>  -->
  </n-card>

  <n-card style="margin-bottom: 16px">
    <div class="flex flex-col ">
      <div class="w-full">
        <h1 class="mb-8 text-2xl font-bold tracking-tight text-gray-600"><a href="#">Filter using</a></h1>
      </div>
      <div class="mb-6 flex justify-start items-center">
        <div class="w-32  mr-6"><span class="text-gray-500">Cell Type:</span></div>
        <n-cascader ref="cascaderInstRef" multiple :cascade="false" v-model:value="selectedCellType"
          placeholder="Search cell types" :options="InitialData" check-strategy='child' :show-path="false"
          :filterable="true" @update:value="handleUpdateValue" />
      </div>

      <div class="flex justify-start items-start">
        <div class="w-32  mr-6 mt-4"><span class="text-gray-500 whitespace-nowrap">Genomic Regions:</span></div>
        <!-- <TrackList :session="session" :sessionId="session.key" :tracks="session.trackIds">
        </TrackList> -->
      </div>
      <div class="flex justify-end mt-8">

        <button type="button"
          class="w-24 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Search</button>
        <button type="button"
          class="w-24 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Reset</button>
      </div>
    </div>

  </n-card>
  <n-card style="margin-bottom: 14px">
    <h1 class="mb-2 text-2xl font-bold tracking-tight text-gray-600"><a href="#">Results</a></h1>

    <n-tabs default-value="loops" justify-content="space-evenly" type="line" tab-style="font-size: 16px;font-weight: bold"
      :bar-width="1000" @update:value="handleTabUpdateValue">
      <n-tab-pane name="loops" tab="CHROMATIN INTERACTIONS">
        <!-- Chromatin interactions -->
        <n-card :bordered="false">

          <div class="flex justify-between">
            <!-- top left section -->
            <div class="flex items-center	justify-start	">
              <!-- slot -->
              <form>
                <label class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
                  for="default-search">Search</label>
                <div class="relative">
                  <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                    <svg aria-hidden="true" class="w-4 h-4 text-gray-500 dark:text-gray-400" fill="none"
                      viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                      <path d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" stroke="currentColor" stroke-linecap="round"
                        stroke-linejoin="round" stroke-width="2" />
                    </svg>
                  </div>
                  <input id="default-search"
                    class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder="Search Mockups, Logos..." required type="search">
                  <button
                    class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                    type="submit">
                    Search
                  </button>
                </div>
              </form>
            </div>

            <!-- top right section -->
            <div class="flex justify-end flex-1 ">
              <!-- slot -->
              <n-dropdown :options="exportOptions" placement="bottom-start" size="medium" trigger="click"
                @select="handleExport">
                <n-button>Export</n-button>
              </n-dropdown>
            </div>

            <div class="mb-4 flex items-center min-h-[28px]">
              <span class="text-sm font-medium text-gray-900 dark:text-white mr-3 flex-shrink-0">
                Showing {{ from }} to {{ to }}
                cell types of {{ itemCount }} in
                total.
              </span>
              <!-- <div class="flex items-center flex-wrap space-x-3"></div> -->
            </div>
          </div>

          <!-- table body -->
          <n-data-table remote :bordered="false" :columns="columns" :loading="loadingRef" :data="dataRef"
            :pagination="paginationReactive"  />

        </n-card>
      </n-tab-pane>
      <n-tab-pane name="genes" tab="GENES">
        Genes
      </n-tab-pane>
      <n-tab-pane name="snps" tab="ENHANCERS">
        Enhancers
      </n-tab-pane>
      <n-tab-pane name="tf" tab="SNPS">
        SNPs
      </n-tab-pane>
    </n-tabs>
  </n-card>
</template>
<script lang="ts" setup>
import { onMounted, ref, reactive, watch, computed, nextTick, h } from 'vue';
import SearchList from './SearchList.vue'
import { useRouter, useRoute } from 'vue-router'
import ChromatinInteractionsFilter from "./ChromatinInteractionsFilter.vue";
import type { AutoCompleteInst } from 'naive-ui'
import type { CascaderOption } from 'naive-ui'
import axios from 'axios';
import { useLoadingBar } from 'naive-ui'
import TrackList from './TrackList.vue'

const router = useRouter()
const route = useRoute()
const value = ref(null)

const showModal = ref(false)
const loadingRef = ref(true)
const dataRef = ref([])
const itemCount = ref(0)

const paginationReactive = computed(() => ({
  page: currentPage.value,
  pageCount: Math.ceil(itemCount.value / pageSize.value),
  pageSize: pageSize.value,
  itemCount: itemCount.value
}))
const pageSize = ref(10)
const currentPage = ref(1)
const loadingBar = useLoadingBar()

const from = computed(() => (currentPage.value - 1) * pageSize.value + 1)
const to = computed(() => Math.min(currentPage.value * pageSize.value, itemCount.value))

const columns = [
  {
    title: 'chrom1',
    key: 'chrom1',
  },
  {
    title: 'start1',
    key: 'start1',
  },
  {
    title: 'end1',
    key: 'end1',
  },
  {
    title: 'chrom2',
    key: 'chrom2',
  },
  {
    title: 'start2',
    key: 'start2',
  },
  {
    title: 'end2',
    key: 'end2',
  },
  {
    title: 'Counts',
    key: 'counts',
  },
  {
    title: 'Anchor1',
    key: 'anchor1'
  },
  {
    title: 'Anchor2',
    key: 'anchor2'
  },
  {
    title: 'data_id',
    key: 'file_id'
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
        onClick: (e) => {handleClick(row.data_id) }
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
const numFilteredCellTypes = ref(2)
const filteredGenomicRegion = ref('chr1:10000-20000')
const filteredGene = ref('MALAT1')
const options = [
  {
    label: "Cell types",
    value: 'Cell types',
  },
  {
    label: "Genes",
    value: 'Genes',
  },
  {
    label: 'Genomic regions',
    value: 'Genomic regions'
  },
  {
    label: 'SNPs',
    value: 'SNPs'
  },
  {
    label: 'Transcription factor',
    value: 'song4'
  }
]

const handleClick = (value) => {
  // Your click handling logic goes here
  console.log('SVG clicked!');
  // router.push({ path: '/celltype/' + value.replace(/[\s,]+/g, "-") })
}
const handlePageChange = (page) => {
  if (!loadingRef.value) {
    currentPage.value = page
    loadingRef.value = true
  }
}

const handleSorterChange = (sorter) => {

}


const session = reactive({
  "key": "89a46bfa-5441-425a-aaca-e1ac115f2830",
  "trackIds": ["6b6f108c-f0d0-4231-8095-11fe65e931c5", "2530ad6a-2d57-471a-b5fe-79bb45a2577d", "c1692983-b75f-42ad-b375-5c1f3198ca06", "fed0a3d0-f017-40dc-bb24-edee970aabb2"],
  "sessionConfig": { "type": "TrackList", "maxTrackNum": 10 }
})

const handleTabUpdateValue = (value: string) => {
  router.push({
    name: 'Search',
    query: {
      type: value
    }
  })
}




const cascaderInstRef = ref(null)

const selectedCellType = ref(['A549', 'GM12878'])
const handleUpdateValue = (value: string, option: CascaderOption) => {
  console.log(value, option)
  // if (!tags.value.includes(value)) {
  //   tags.value.push(value)
  // }
}



const isOpen = ref(false)
const toggle = () => {
  isOpen.value = !isOpen.value
}

function mapDataToOptions(data) {
  const map = new Map();

  // Step 1: Create the nested Map structure
  for (const item of data) {
    const { body_site, cell_id, ...rest } = item;
    if (!map.has(body_site)) {
      map.set(body_site, new Map());
    }
    const bodySiteMap = map.get(body_site);
    if (!bodySiteMap.has(cell_id)) {
      bodySiteMap.set(cell_id, []);
    }
    bodySiteMap.get(cell_id).push(rest);
  }

  // Step 2: Transform into the desired output format
  const options = [];
  for (const [bodySiteValue, bodySiteMap] of map) {
    const bodySiteOption = {
      value: bodySiteValue,
      label: bodySiteValue,
      children: [],
    };
    for (const [cellIdValue, cellIdArray] of bodySiteMap) {
      const cellIdOption = {
        value: cellIdValue,
        label: cellIdValue
      };
      bodySiteOption.children.push(cellIdOption);
    }
    options.push(bodySiteOption);
  }

  return options;
}

let InitialData = ref([]);
// function to retrieve data
const fnGetData = () => {
  axios.get('http://47.107.91.5' + '/search/datalist', {
    responseType: 'json',
    params: { includeInitialData: true },
    paramsSerializer: {
      indexes: null
    }
  })
    .then(res => {
      console.log('data recevied')
      console.log(res.data)
      InitialData.value = mapDataToOptions(res.data.initial_data)
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


const CellTypeDataParams = computed(() => ({

  cellId: selectedCellType.value,
  pagesize: pageSize.value,
  page: currentPage.value

}))
// function to retrieve data
const fnGetChromatinLoops = (params) => {
  axios.get('http://47.107.91.5' + '/search/chromloops', {
    responseType: 'json',
    params: params,
    paramsSerializer: {
      indexes: null
    }
  })
    .then(res => {
      console.log('data recevied')
      console.log(res.data)
      loadingRef.value = false
      // from.value = res.data.from
      // to.value = res.data.to
      itemCount.value = res.data.count
      // paginationReactive.value.itemCount = res.data.itemCount
      // paginationReactive.value.pageCount = Math.ceil(itemCount.value / pageSize.value)

      dataRef.value = res.data.results
      // if (includeInitialData) {
      //   // initializedData.value = populateInitializedData(res.data.initial_data)
      //   // console.log(initializedData.value)
      //   includeInitialData = false
      // }
      // itemCount.value = res.data.itemCount
      // // console.log(dataRef.data)
      // paginationReactive.pageCount = Math.ceil(itemCount.value / pagesize)
      // paginationReactive.itemCount = itemCount.value
      // loadingRef.value = false
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
const handleExport = () => {

}

onMounted(() => {


  var element = document.querySelector('.n-tabs-bar');
  if (element) {
    element.style.height = '20px';
  }


  fnGetChromatinLoops(CellTypeDataParams.value)
  fnGetData()
  console.log(CellTypeDataParams.value)
  // watch(() => CellTypeDataParams, (newValue) => {
  //   console.log(newValue.value)
  //   loadingBar.start()
  //   fnGetChromatinLoops(newValue.value)
  // }, { immediate: true, deep: true })
})
</script>
<style scoped>
.n-tabs-wrapper {
  border-width: 2px;
}

.n-tabs-bar {
  height: 4px;
  background-color: blue;
}

.setting-item {
  display: flex;
  flex-direction: column;
  min-width: 110px;
  text-align: start;
  margin-bottom: 5px;
}

.setting-item .name {
  margin-top: 2px;
}

.config-item-box {
  position: relative;
  display: flex;
  margin: 10px 0;
}

.config-item-box .item-left {
  width: 60px;
  text-align: left;
  margin-top: 4px;
  margin-left: 10px;
  font-size: 14px;
}

.config-item-box .item-right {
  display: grid;
  grid-column-gap: 10px;
  width: calc(100% - 60px);
}
</style>