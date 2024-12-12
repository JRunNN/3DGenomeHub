<template>
  <div class="mx-auto max-w-8xl">

		<div class="flex grow">
			<CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
				<CardActions :expand="expand" :isExpand="isExpand" :reload="reload" class="h-full"
					title="Search samples" :segmented="{
						content: true,
						footer: true
					}">
					<template #default>
						<ul>
							<li class="flex space-x-3 items-center mb-3">
								<!-- Icon -->
								<svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500"
									fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
									<path fill-rule="evenodd"
										d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
										clip-rule="evenodd"></path>
								</svg>
								<p class=" text-xl font-light text-gray-500"> Search samples by interactive plots, summary table, or search by gene names </p>

							</li>
							<li class="flex space-x-3 items-center mb-3">
								<!-- Icon -->
								<svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500"
									fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
									<path fill-rule="evenodd"
										d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
										clip-rule="evenodd"></path>
								</svg>
								<p class=" text-xl font-light text-gray-500"> Download compartments, contact domains, stripes, chromatin loops from Hi-C datasets.</p>

							</li>
							<li class="flex space-x-3 items-center">
								<!-- Icon -->
								<svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500"
									fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
									<path fill-rule="evenodd"
										d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
										clip-rule="evenodd"></path>
								</svg>
								<p class="text-xl font-light text-gray-500">
									Click
									<svg class="inline mb-1 w-4 h-4 text-grey-500 hover:text-blue-500 transition-colors duration-300"
										aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
										viewBox="0 0 18 18">
										<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
											stroke-width="2"
											d="M15 11v4.833A1.166 1.166 0 0 1 13.833 17H2.167A1.167 1.167 0 0 1 1 15.833V4.167A1.166 1.166 0 0 1 2.167 3h4.618m4.447-2H17v5.768M9.111 8.889l7.778-7.778" />
									</svg> in Visualize column to access a dedicated page for each cell type. Track view and
									tabular view of genome
									browser is provided.
								</p>
							</li>
						</ul>
					</template>
          <template #header-extra>
          </template>
				</CardActions>
			</CardWrapper>
		</div>

    <div class="flex grow mt-6 ">
      <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
        <CardActions :expand="expand" :isExpand="isExpand" :reload="reload" class="h-full" title="Filter by interactive charts"
          :segmented="{
            content: true,
            footer: true
          }">
          <template #header>
            <n-h3 prefix="bar" align-text>Filter by interactive plots</n-h3>

          </template>
          <template #header-extra>
          </template>
          <template #default>

            <n-tabs type="line" animated>
              <n-tab-pane name="bar" tab="Sample Bar Plot">
                <SampleBarChart></SampleBarChart>
              </n-tab-pane>
              <n-tab-pane name="pca" tab="Sample PCA Plot">
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
      <div>
        <n-card class="bg-white	 hidden lg:block col-span-1  rounded-lg border border-gray-200 p-2 flex-1 h-full">
          <div class="mb-5">
            <!-- <h5 class="text-lg font-medium ml-4 mb-4">Filter By Summary Table</h5> -->

            <n-h3 prefix="bar" align-text>Filter By Table</n-h3>

            <!-- <div class="relative flex-shrink-0 w-full mb-4 lg:mb-4 lg:mr-5 ">
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
              </div> -->
          </div>
          <hr class="bg-gray-200 dark:border-gray-700 mb-5">

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
                <n-scrollbar style="max-height: 200px" >
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

        </n-card>
      </div>


      <n-card round class="bg-white col-span-5 lg:col-span-4">
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
          <n-data-table remote :bordered="false" :columns="columns" :loading="loadingRef" :data="dataRef"
            :pagination="paginationReactive" @update:page="handlePageChange" @update:sorter="handleSorterChange"
             />
        </div>
      </n-card>

    </div>

    <div class="flex grow mt-6">
    <n-card>
        <template #header>
          <n-h3 prefix="bar" align-text>Filter By Genes</n-h3>
        </template>
        <template #header-extra>
          <AutocompeleDialog @submit-gene="handleGeneSearch"></AutocompeleDialog>
        </template>
      </n-card>
      </div>

  </div>
</template>
<script setup lang="ts">
import { ref, onMounted, h, watch, computed } from 'vue'
import type { DataTableColumns } from 'naive-ui'
import axios from '@/plugins/axios';
import { useRouter } from "vue-router";
import { NCard, NDataTable, NButton } from "naive-ui";
import { useLoadingBar } from 'naive-ui'
import SampleBarChart from './SampleBarChart.vue';
import SamplePcaChart from './SamplePcaChart.vue';

import { useThemeStore } from "@/stores/theme"

import AutocompeleDialog from '@/components/common/AutocompleteDialog.vue'

const themeStore = useThemeStore()

const style = computed<{ [key: string]: any }>(() => themeStore.style)

const textSecondaryColor = computed<string>(() => style.value["--fg-secondary-color"])

const router = useRouter()
const healthStatus = ref([])
const tissue = ref([])
const data_type = ref([])
const factor = ref([])

const loadingRef = ref(true)
const dataRef = ref([])

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
const id = ref()
const sortBy = ref(null)
const sortOrder = ref(null)

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





type RowData = {
  gsm_id: string
  health_status: string
  tissue: number
  data_type: string
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
const createColumns = (): DataTableColumns<RowData> => {
  return [
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
    },

    {
      title: 'Body Sites',
      key: 'tissue',
      sorter: true,
      sortOrder: sortBy.value === 'tissue' ? sortOrder.value : false,
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
      sorter: true,
      sortOrder: sortBy.value === 'health_status' ? sortOrder.value : false
    },
    {
      title: 'Biomaterial Type',
      key: 'biomaterial_type',
      sorter: true,
      sortOrder: false
    },
    {
      title: 'Data Type',
      key: 'data_type',
      sorter: true,
      sortOrder: sortBy.value === 'biomaterial_type' ? sortOrder.value : false,
      render(row) {
        const assayColor = {
          'ChIA-PET': '#6267FF',
          'HiChIP': '#FF61C9',
          'in-situ Hi-C': '#00B27B',
          'intact Hi-C': '#00B27B',
          'ATAC-seq': 'blue'
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
    // {
    //   title: 'Factor',
    //   key: 'factor'
    // },
    // promoterColumn,
    // transcriptColumn,
    // interactionColumn,
    {
      title: 'Visualize',
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
}

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
  },
  {
    name: 'RNA-seq',
    color: '#FFB600'
  },
  {
    name: 'ChIP-seq',
    color: '#FF0156'
  },
  {
    name: 'ATAC-seq',
    color: 'blue'
  }
]

const columns = ref(createColumns())

const updateColumns = () => {
      columns.value = createColumns();
};


// navigate to individual cell type page
const handleClick = (value) => {
  // Your click handling logic goes here
  router.push({ name: 'Sample', params: { id: value } })
}


const handleGeneSearch = (value) => {
  router.push({ path: `/gene/${value}` });
}

const handlePageChange = (page) => {
  if (!loadingRef.value) {
    currentPage.value = page
    loadingRef.value = true
    // fnGetData(currentPage)
  }
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
      // from.value = res.data.from
      // to.value = res.data.to
      itemCount.value = res.data.length
      paginationReactive.value.itemCount = res.data.length
      paginationReactive.value.pageCount = Math.ceil(itemCount.value / pageSize.value)

      // dataRef.value = res.data.data
      // if (includeInitialData) {
      initializedData.value = populateInitializedData(res.data)
      // includeInitialData = false
      // }
      console.log('initialized data',initializedData.value)
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

const CellTypeDataParams = computed(() => {
  const params = {
    health_status: healthStatus.value,
    tissue: tissue.value,
    data_type: data_type.value,
    id: id.value,
    limit: pageSize.value,
    offset: offset.value || 0,
    sort_by: sortBy.value,
    sort_order: sortOrder.value
  };

  // Format array values as comma-separated strings
  Object.keys(params).forEach(key => {
    if (Array.isArray(params[key])) {
      if (params[key].length > 0) {
        params[key] = params[key].join(',');
      } else {
        delete params[key]; // Remove empty arrays
      }
    } else if (!params[key]) {
      delete params[key]; // Remove parameters that are not provided or empty
    }
  });

  return params;
});

// function to retrieve data
const fnGetData = (params) => {
  axios.get('/samples', {
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
      // from.value = res.data.from
      // to.value = res.data.to
      itemCount.value = res.data.itemCount
      paginationReactive.value.itemCount = res.data.itemCount
      paginationReactive.value.pageCount = Math.ceil(itemCount.value / pageSize.value)
      // paginationReactive.value.currentPage = 1
      // sortBy.value = res.data.sort_by
      // sortOrder.value = res.data.sort_order === 'desc' ? 'descend' : 'ascend'
      // dataRef.value = res.data.items.forEach((d, index) => {
      //   d.key = index
      //   console.log(d)
      // })
      dataRef.value = res.data.items

      updateColumns()
      console.log(columns.value)
      console.log(dataRef.value)
      // if (includeInitialData) {
      //   initializedData.value = populateInitializedData(res.data.initial_data)
      //   includeInitialData = false
      // }
      loadingBar.finish()

    }).catch(function (error) {
      dataRef.value = []
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

// const columnBodySitesSortOrder = ref(false)
// const columnBiomaterialSortOrder = ref(false)
// const columnHealthStatusSortOrder = ref(false)
// const columnDataTypeSortOrder = ref(false)



const handleSorterChange = (sorter) => {
  console.log(sorter)
  console.log(columns.value)
      if (sorter.columnKey) {
        if(sortBy.value === sorter.columnKey) {
          sorter.order = sorter.order === 'descend' ? 'ascend': 'descend'
        } else {
          sortBy.value = sorter.columnKey
        }
        sortOrder.value = sorter.order === 'descend' ? 'desc' : ' asc'

      } else {
        sortBy.value = null
        sortOrder.value = null
      }
      //fetchData()
    
      console.log(sortOrder.value, sortBy.value)
}

// const handleSorterChange = (sorter) => {
//         if (!sorter || sorter.columnKey === 'health_status') {
//           if (!loadingRef.value) {
//             loadingRef.value = true
//             axios.get('http://47.107.91.5' + '/samples/', {
//     responseType: 'json',
//     params: params,
//     paramsSerializer: {
//       indexes: null
//     }
//   })
//               paginationReactive.page,
//               paginationReactive.pageSize,
//               !sorter ? false : sorter.order,
//               column2Reactive.filterOptionValues
//             ).then((data) => {
//               column1Reactive.sortOrder = !sorter ? false : sorter.order
//               dataRef.value = data.data
//               paginationReactive.pageCount = data.pageCount
//               paginationReactive.itemCount = data.total
//               loadingRef.value = false
//             })
//           }
//         }
//       },



onMounted(() => {
  fnGetMenudata()
  watch(() => CellTypeDataParams, (newValue) => {
    console.log(newValue.value)
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
}
</style>