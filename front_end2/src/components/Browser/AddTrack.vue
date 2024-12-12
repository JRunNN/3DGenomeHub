<template>
    <!-- <n-card round class="bg-white col-span-5 lg:col-span-4"> -->
    <!-- <template #header-extra> -->
    <!-- <div class="mb-6 flex flex-col items-center justify-between  space-y-3 md:flex-row md:space-y-0 md:space-x-4">
        <div class="w-full md:w-1/2">
            <form class="flex items-center">
                <label for="simple-search" class="sr-only">Search</label>
                <div class="relative w-full">
                    <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                        <svg aria-hidden="true" class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="currentColor"
                            viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                                clip-rule="evenodd" />
                        </svg>
                    </div>
                    <input type="text" id="simple-search"
                        class="block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                        placeholder="Search" required="">
                </div>
            </form>
        </div>
    </div> -->
    <!-- </template> -->
    <n-tabs type="line">

      <n-tab-pane name="hosted-tracks" tab="Hosted Tracks">
        <div class="gap-3">
        <n-data-table remote :bordered="false" :columns="columns" :loading="loadingRef" :data="dataRef"
            :pagination="paginationReactive" @update:page="handlePageChange" @update:sorter="handleSorterChange" />
        <div class="mb-4 flex items-center min-h-[28px]">
            <span class="text-sm font-medium text-gray-900 dark:text-white mr-3 flex-shrink-0">
                Showing {{ from }} to {{ to }}
                cell types of {{ itemCount }} in
                total.
            </span>
            <!-- <div class="flex items-center flex-wrap space-x-3"></div> -->
        </div>
    </div>
      </n-tab-pane>
      <!-- <n-tab-pane name="anno-track" tab="Annotation Tracks">
        Wonderwall
      </n-tab-pane> -->
    </n-tabs>



    <!-- <template #footer>
        <button type="button"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Default</button>
    </template> -->
    <!-- </n-card> -->
</template>

<script lang="ts" setup>
import { onMounted, ref, reactive, watch, computed, h, nextTick } from 'vue';
import { useRouter, useRoute } from 'vue-router'
import { NButton, NSpin } from 'naive-ui'
import axios from 'axios';
// import { type } from 'os';
import { v4 as uuid } from 'uuid'
import { useTrackStore } from '../../browser/store/TrackStore/TrackStore'
import { useSessionStore } from '../../browser/store/SessionStore/SessionStore'

const trackStore = useTrackStore();
const sessionStore = useSessionStore();

const diseaseStatus = ref([])
const bodySites = ref([])
const assays = ref([])
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

const props = defineProps({
    loadedTracks: {
        type: Array,
        required: true
    }
})

// const populateInitializedData = (data) => {
//     let output = []
//     const categories = ['diseaseStatus', 'bodySites', 'assays'];
//     categories.forEach(category => {
//         const counts = {};
//         data.forEach(product => {
//             const option = product[category];
//             if (category === 'assays') {
//                 // Handle 'assays' array separately
//                 option.forEach(assay => {
//                     if (!counts[assay]) {
//                         counts[assay] = 0;
//                     }
//                     counts[assay]++;
//                 });
//             } else {
//                 if (!counts[option]) {
//                     counts[option] = 0;
//                 }
//                 counts[option]++;
//             }
//         });

//         // Convert counts object to an array of arrays
//         const sortedCountsArray = Object.entries(counts).sort((a, b) => b[1] - a[1]);

//         output.push({
//             category: category,
//             options: sortedCountsArray
//         });
//     });
//     console.log(output)
//     return output;
// }




// const loadedData = ref([])

// column specification
const columns = [
    {
        title: 'Cell Id',
        key: 'cell_id'
    },
    {
        title: 'Disease',
        key: 'disease_status',
    },
    {
        title: 'BodySites',
        key: 'body_site',
    },
    {
        title: 'Assay',
        key: 'assay',
    },
    {
        title: 'Format',
        key: 'format'
    },
    {
        title: 'Factor',
        key: 'factor'
    },
    {
                    title: 'Action',
                    key: 'actions',
                    render: (row) => {
                        if (row.loadingStatus === 'loading') {
                            return h(NSpin)
                        }
                        return h(
                            NButton,
                            {
                size: 'small',
                onClick: () => {
                    if (row.loadingStatus !== 'loaded') {
                        addTrack(row)
                    }
                },
                disabled: row.loadingStatus === 'loaded'
            },
                            { default: () => row.loadingStatus === 'loaded' ? 'Loaded' : 'Add' }
                        )
                    }
                }
]

// navigate to individual cell type page
// const handleClick = (value) => {
//     // Your click handling logic goes here
//     console.log('SVG clicked!');
//     router.push({ path: '/celltype/' + value })
// }


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

const format = ref([])
const factor = ref([])

const CellTypeDataParams = computed(() => ({
    diseaseStatus: diseaseStatus.value,
    bodySites: bodySites.value,
    assays: assays.value,
    cellId: cellId.value,
    format: format.value,
    factor: factor.value,
    pagesize: pageSize.value,
    page: currentPage.value,
    includeInitialData: includeInitialData
}))
console.log(CellTypeDataParams)

const flattenObject = (ob)=> {
  const toReturn = {};
  
  for (const i in ob) {
    if (!ob.hasOwnProperty(i)) continue;
    
    if ((typeof ob[i]) === 'object' && ob[i] !== null) {
      const flatObject = flattenObject(ob[i]);
      for (const x in flatObject) {
        if (!flatObject.hasOwnProperty(x)) continue;
        
        toReturn[x] = flatObject[x];
      }
    } else {
      toReturn[i] = ob[i];
    }
  }
  return toReturn;
}


// function to retrieve data
const fnGetData = (params) => {
    axios.get(import.meta.env.VITE_BASE_URL + '/search/files', {
        responseType: 'json',
        params: params,
        paramsSerializer: {
            indexes: null
        }
    })
        .then(res => {
            console.log('data recevied')
            // console.log(res.data)
            loadingRef.value = false
            from.value = res.data.from
            to.value = res.data.to
            itemCount.value = res.data.itemCount
            paginationReactive.value.itemCount = res.data.itemCount
            paginationReactive.value.pageCount = Math.ceil(itemCount.value / pageSize.value)
            console.log(res.data)
            dataRef.value = res.data.data.map(flattenObject)
            if (includeInitialData) {
                initializedData.value = res.data.initial_data
                // console.log(initializedData.value)
                includeInitialData = false
            }

            dataRef.value.map((d)=> {
                console.log('loadedTracks', props.loadedTracks)
                console.log('d.id', d.id)
                d.loadingStatus = props.loadedTracks.includes(d.id) ? 'loaded' : 'unloaded'
            })
            console.log(dataRef.value)
            // itemCount.value = res.data.itemCount
            // // console.log(dataRef.data)
            // paginationReactive.pageCount = Math.ceil(itemCount.value / pagesize)
            // paginationReactive.itemCount = itemCount.value
            // loadingRef.value = false
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

const addTrack = (row) => {
    row.loadingStatus = 'loading';
    console.log(row)
    let file_url;
    let type;
    let display
    switch (row.format) {
        case 'bedpe':
        file_url = import.meta.env.VITE_FILE_SERVER_URL + '/3D_loops/' + row.data_id + '_WashU.bed.gz'
            type = 'CurvTrack'
            display = 'basicCurve'
            break;
        case 'hic':
        file_url = import.meta.env.VITE_FILE_SERVER_URL + '/3D_hic/' + row.data_id + '.' + 'hic'
            type = 'HicTrack'
            display = 'triangle'
            break;
        case 'bed':
            type = 'SclsTrack'
            break;
        case 'bigwig':
        file_url = import.meta.env.VITE_FILE_SERVER_URL + '/3D_bigwig/' + row.data_id + '.' + 'bigWig'
            type = 'LineGTrack'
            display = 'Coverage'
            break;
    }
    const label = row.cell_id + ' | ' + row.assay + ' | ' + display
    const name = row.cell_id + ' | ' + row.assay + ' | ' + display

      UploadJsonFile([{
        id: row.data_id + row.format + row.assay,
        name: name,
        label: label,
        type: type,
        url: file_url,
        style: display
    }])
    row.loadingStatus = 'loaded';
    console.log(row)



    // loadedData.value.push(row.id)
}

const UploadJsonFile = async (data) => {
    try {
        console.log(sessionStore.getSessionList)

        const promises = data.map(async (item, index) => {
            const trackComponentType = item.type;
            // item.uuid = uuid();

            // Make sure to uncomment these lines if necessary
            // await componentInstall(trackComponentType, fetchTrackComponent(item.type));
            // await componentInstall(`${trackComponentType}Config`, fetchConfigComponent(item.type));

            const newTrack = await createComponent(item.type);
            newTrack.key = String(item.id);
            newTrack.trackConfig.sessionId.push(sessionStore.getSessionList[0].key);
            newTrack.option.url = item.url;
            newTrack.option.style = item.style;
            newTrack.trackConfig.name = item.name;
            newTrack.trackConfig.label = item.label;
            // newTrack.trackConfig.order = index;

            sessionStore.getSessionList[0].trackIds.push(item.id);

            return trackStore.addTrackList(newTrack, false, true);
        });

        await Promise.all(promises);

    } catch (error) {
        console.error(error);
    }
};

const componentInstall = (key, component) => {
    if (!window.$vue.component(key)) {
        window.$vue.component(key, component)
    }
}

// const fetchTrackComponent = async (trackType) => {
//     const component = await import.meta.glob(`@/browser/tracks/${trackType}/${trackType}.vue`);
//     return component;
// };

// const fetchConfigComponent = async (trackType) => {
//     const component = await import.meta.glob(`@/browser/tracks/${trackType}/config.vue`);
//     return component;
// };
// import HeatmapGTrackConfig from '@/browser/tracks/LineGTrack/config.vue'

// import chartModule from '@/browser/tracks/LineGTrack/config.ts'
// console.log(new chartModule.default())
const modules = import.meta.glob('@/browser/tracks/*/config.ts', { eager: true })
const modulePaths = Object.keys(modules);
const createComponent = async (trackType) => {
    try {
        const modulePath = modulePaths.find(path => path.includes(`${trackType}`));
        const moduleImportFunction = await modules[modulePath];
        return new moduleImportFunction.default()
    } catch (error) {
        console.error(`Error while creating component of type ${trackType}: `, error);
        return null;
    }
}

onMounted(() => {
    watch(() => CellTypeDataParams, (newValue) => {
        // console.log(newValue.value)
        fnGetData(newValue.value)


    }, { immediate: true, deep: true })
})
</script>

<style scoped></style>