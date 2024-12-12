<template>
    <n-card round class="bg-white col-span-5 lg:col-span-4">
    <!-- <template #header-extra> -->

    <div class="mb-4 flex items-center min-h-[28px]">
        <span class="text-sm font-medium text-gray-900 dark:text-white mr-3 flex-shrink-0">
            You are downloading {{ scheduledFileNumber }} files. Up to 5 files can be downloaded simultaneously.
        </span>
        <!-- <div class="flex items-center flex-wrap space-x-3"></div> -->
    </div>
    <!-- </template> -->
    <n-tabs type="line">

        <n-tab-pane name="hosted-tracks" tab="Hosted Tracks">
            <div class="flex justify-between">
        <div class="mb-4 flex items-center min-h-[28px]">
          <span class="text-sm font-medium text-gray-900 dark:text-white mr-3 flex-shrink-0">
            Showing {{ from }} to {{ to }}
            cell types of {{ itemCount }} in
            total.
          </span>
          <!-- <div class="flex items-center flex-wrap space-x-3"></div> -->
        </div>

            <!-- search bar -->
    <form class="ml-8 mr-8 mb-4 flex w-18 items-center">
        <!-- <label for="simple-search" class="sr-only">Search</label> -->
        <input type="text" id="simple-search"
            class="relative m-0  block min-w-0 flex-auto  rounded-l border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-1.5 text-base font-normal text-neutral-700 outline-none transition duration-300 ease-in-out focus:border-primary focus:text-neutral-700 focus:shadow-te-primary focus:outline-none"
            placeholder="Search..." required v-model="currentLocString">
        <!-- <button
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
        </button> -->
    </form>
    </div>
            <div class="gap-3">
                <n-data-table remote :bordered="false" :columns="columns" :loading="loadingRef" :data="dataRef"
                    :pagination="paginationReactive" @update:page="handlePageChange" @update:sorter="handleSorterChange" />
            </div>
        </n-tab-pane>
        <!-- <n-tab-pane name="anno-track" tab="Annotation Tracks">
            Wonderwall
        </n-tab-pane> -->
    </n-tabs>


    <!-- Progress bar (only shown when a download is in progress) -->
    <!-- <div v-if="downloading" class="progress-container">
      <div class="progress-bar" :style="{ width: progress + '%' }"></div>
    </div>

    Optional: Display download progress as text
    <div v-if="downloading" class="progress-text">
      Downloading: {{ progress }}%
    </div> -->
    <!-- <template #footer>
        <button type="button"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Default</button>
    </template> -->
    </n-card>
</template>

<script lang="ts" setup>
import { onMounted, ref, reactive, watch, computed, h, nextTick } from 'vue';
import { useRouter, useRoute } from 'vue-router'
import { NButton, NProgress, NSpin } from 'naive-ui'
import axios from 'axios';
// import { type } from 'os';
import { v4 as uuid } from 'uuid'
import { useTrackStore } from '../../browser/store/TrackStore/TrackStore'
import { useSessionStore } from '../../browser/store/SessionStore/SessionStore'
import { useMessage } from 'naive-ui'

const message = useMessage()

const trackStore = useTrackStore();
const sessionStore = useSessionStore();

const diseaseStatus = ref([])
const bodySites = ref([])
const assays = ref([])
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

const currentLocString = ref('')
const handleLocationSearch = () => {
//   CellTypeDataParams.value = Object.assign(CellTypeDataParams.value, 
//   {
//     searchTerm: currentLocString.value
//   });

}
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
        title: 'Download',
        key: 'download',
        render: (row) => {

            if (row.loadingStatus === 'loading') {
                return h(NSpin)
            }
            return h(
                NButton,
                {
                    size: 'small',
                    onClick: () => {
                        
                        if (scheduledFileNumber.value < 5) {
                            row.schedule = true
                            scheduledFileNumber.value++
                            if (row.loadingStatus !== 'loaded') {
                                DownloadData(row)
                            }
                        } else {
                            message.warning('Up to 5 files can be downloaded simultaneously.')
                        }
                    },
                    disabled: row.loadingStatus === 'loaded'
                },
                [!row.schedule ?
                    h('svg', {
                        class: {
                            'w-4': true,
                            'h-4': true,
                            'text-gray-800': true,
                            'dark:text-white': true
                        },
                        'aria-hidden': 'true',
                        xmlns: 'http://www.w3.org/2000/svg',
                        fill: 'currentColor',
                        viewBox: '0 0 20 20'
                    }, [
                        h('path', {
                            d: 'M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'
                        }),
                        h('path', {
                            d: 'M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'
                        })
                    ]) :
                    h(NProgress, {
                        type: 'line',
                        percentage: row.progress
                    })
                ]
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
// const percentage = ref(0)

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
    searchTerm: currentLocString.value,
    includeInitialData: includeInitialData
}))
console.log(CellTypeDataParams)

const flattenObject = (ob) => {
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

            dataRef.value.map((d) => {
                console.log('loadedTracks', props.loadedTracks)
                console.log('d.id', d.id)
                d.loadingStatus = props.loadedTracks.includes(d.id) ? 'loaded' : 'unloaded'
                d.schedule = false
                d.progress = 0
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


const downloading = ref(false)
const scheduledFileNumber = ref(0)


const DownloadData = (row) => {
    let file_url
    let type
    let display
    let baseUrl
    let filename
    switch (row.format) {
        case 'bedpe':
            baseUrl = import.meta.env.VITE_FILE_SERVER_URL + '/3D_loops'
            filename = row.data_id + '_WashU.bed.gz'
            file_url = import.meta.env.VITE_FILE_SERVER_URL + '/3D_loops/' + row.data_id + '_WashU.bed.gz'
            type = 'CurvTrack'
            display = 'Loops'
            break;
        case 'hic':
            baseUrl = import.meta.env.VITE_FILE_SERVER_URL + '/3D_hic'
            filename = row.data_id + '.' + 'hic'
            file_url = import.meta.env.VITE_FILE_SERVER_URL + '/3D_hic/' + row.data_id + '.' + 'hic'
            type = 'HicTrack'
            display = 'Heatmap'
            break;
        case 'bed':
            type = 'SclsTrack'
            break;
        case 'bigwig':
            baseUrl = import.meta.env.VITE_FILE_SERVER_URL + '/3D_bigwig'
            filename = row.data_id + '.' + 'bigWig'
            file_url = import.meta.env.VITE_FILE_SERVER_URL + '/3D_bigwig/' + row.data_id + '.' + 'bigWig'
            type = 'LineGTrack'
            display = 'Coverage'
            break;
    }
    downloading.value = true;
    console.log(file_url)
    axios({
        method: 'get',
        url: `${baseUrl}/${filename}`,
        responseType: 'blob', // Important: indicates that we expect a binary file
        onDownloadProgress: (progressEvent) => {
            // console.log('进度事件1', progressEvent);

            // if (progressEvent.lengthComputable) {

            row.progress = Math.floor((progressEvent.loaded * 100) / progressEvent.total);
            console.log(row.progress)
            if (row.progress === 100) {
                row.schedule = false
                scheduledFileNumber.value--
            }
            // }
        }
    })
        .then(response => {
            // Create a URL for the file
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', filename); // Set the file name
            document.body.appendChild(link);
            link.click(); // Start the download
            link.parentNode.removeChild(link); // Clean up
            window.URL.revokeObjectURL(url);
        })
        .catch(error => {
            console.error('Download error:', error);
            alert('There was an error downloading the file.');
        })
        .finally(() => {
            downloading.value = false;
            progress.value = 0;
        });
}






onMounted(() => {
    watch(() => CellTypeDataParams, (newValue) => {
        // console.log(newValue.value)
        fnGetData(newValue.value)


    }, { immediate: true, deep: true })
})
</script>

<style scoped></style>