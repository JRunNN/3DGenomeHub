<template>
    <div :class="{ 'bg-gray-300 bg-opacity-50': show }" aria-hidden="true"
        class="fixed inset-0 z-50 flex items-center justify-center h-screen" tabindex="-1">
        <div class="relative w-full max-w-6xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow">
                <!-- Modal header -->
                <div class="flex items-start justify-between p-4 border-b rounded-t ">
                    <div v-if="step === 1">
                        <h3 class="text-xl font-semibold text-gray-900">
                            Choose a method to create a session
                        </h3>

                    </div>
                    <div v-else-if="step === 2 && uploadType === 'uploadFile'">
                        <h3 class="text-xl font-semibold text-gray-900">Tracks to be uploaded:</h3>
                    </div>
                    <div v-else-if="step === 2 && uploadType === 'emptyBrowser'">
                        <h3 class="text-xl font-semibold text-gray-900">Please choose an assembly</h3>
                    </div>
                    <button
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center"
                        data-modal-hide="staticModal" type="button" @click="toggleSessionInitModal">
                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path clip-rule="evenodd"
                                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                                fill-rule="evenodd"></path>
                        </svg>
                    </button>
                </div>

                <!-- Modal body -->
                <div class="p-6 h-[26rem]">
                    <!-- <div v-for="index in tabs.length" :key="index"> -->
                    <div v-if="step === 1" class="flex">
                        <!-- <slot name="modalContent"> -->
                        <!-- <button @click="ChooseJsonFile" data-modal-hide="staticModal" type="button"
            class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10">JSON
            file</button> -->
                        <div class="flex items-center justify-center w-full">
                            <label
                                class="flex flex-col items-center justify-center w-full h-96 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100 hover:border-blue-400"
                                for="dropzone-file">
                                <div class="flex flex-col items-center justify-center pt-5 pb-6">
                                    <svg class="w-10 h-10 mb-3 text-gray-400" fill="none" stroke="currentColor"
                                        stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                        <path
                                            d="M12 16.5V9.75m0 0l3 3m-3-3l-3 3M6.75 19.5a4.5 4.5 0 01-1.41-8.775 5.25 5.25 0 0110.233-2.33 3 3 0 013.758 3.848A3.752 3.752 0 0118 19.5H6.75z"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                    <p class="mb-2 text-lg	 text-gray-500"><span class="font-semibold">Click
                                            to upload</span> or drag and drop</p>
                                    <p class="text-base	 text-gray-500">JSON, CSV, TSV or EXCEL
                                    </p>
                                </div>
                                <input id="dropzone-file" ref="fileInput" class="hidden" type="file"
                                    @change="ChooseJsonFile" />
                            </label>
                        </div>
                        <div class="mx-4 w-px  bg-gray-300"></div>
                        <div class="flex items-center justify-center w-full" @click="handleEmptySession">
                            <div
                                class="empty-browser flex flex-col items-center justify-center w-full h-96 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100 hover:border-blue-400">
                                <div class="flex flex-col items-center justify-center p-6">
                                    <svg class="w-10 h-10 mb-3 text-gray-400" fill="none" stroke="currentColor"
                                        stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                        <path
                                            d="M6 20.25h12m-7.5-3v3m3-3v3m-10.125-3h17.25c.621 0 1.125-.504 1.125-1.125V4.875c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125z"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                    <p class="mb-2 text-lg	 text-gray-500"><span class="font-semibold">Start with an
                                            empty
                                            session</span></p>
                                    <p class="text-base	 text-gray-500"> and upload tracks later
                                    </p>
                                </div>
                                <!-- <input id="dropzone-file" type="file" class="hidden" /> -->
                            </div>
                        </div>
                        <!-- </slot> -->
                    </div>
                    <div v-else-if="step === 2 && uploadType === 'uploadFile'">
                        <!-- <div id="json-modal" :style="{ display: modalDisplay }"> -->
                        <div class="modal-content">
                            <n-data-table v-if="showTable" :columns="columns" :data="jsonData.tracks" :pagination="paginationRef"></n-data-table>
                            <div v-if="showError" class="error">{{ errorMessage }}</div>
                        </div>
                        <!-- </div> -->
                    </div>
                    <div v-else-if="step === 2 && uploadType === 'emptyBrowser'" class="flex">
                        <div class="flex items-center pl-4 border border-gray-200 rounded dark:border-gray-700">
                            <input id="bordered-radio-1"
                                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                                name="bordered-radio" type="radio" value="">
                            <label class="w-full py-4 ml-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                                for="bordered-radio-1">hg38</label>
                        </div>
                        <div class="flex items-center pl-4 border border-gray-200 rounded dark:border-gray-700">
                            <input id="bordered-radio-2" checked
                                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                                name="bordered-radio" type="radio" value="">
                            <label class="w-full py-4 ml-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                                for="bordered-radio-2">hg19</label>
                        </div>
                    </div>
                    <!-- </div> -->
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-6 space-x-2 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <!-- <div v-if="step === 1">
              <button @click="UploadJsonFile(jsonData)" type="button"
                  class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                  Next</button>
                  </div> -->
                    <div v-if="step === 2">
                        <button
                            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                            type="button" @click="step--">
                            Back
                        </button>
                        <button
                            class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600"
                            type="button" @click="UploadJsonFile(jsonData)">
                            Done
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { reactive, ref, watch, computed } from 'vue'
import { NDataTable } from 'naive-ui'
import { useSessionStore } from '../../browser/store/SessionStore/SessionStore'
import type { CreateSessionType } from  '../../browser/store/SessionStore/SessionStore'
// import CurvTrack from './tracks/index.vue'
import { useLayoutStore } from '../../browser/store/LayoutStore/LayoutStore'
// import { useTabsStore } from '../../store/tabs';
import { v4 as uuid } from 'uuid'
import type { CreateTrackType } from '../../browser/elements';
import { useTrackStore } from '../../browser/store/TrackStore/TrackStore'

const paginationRef = computed(() => ({
      pageSize: 6
    }))

// const props = defineProps({
//     show: Boolean,
// })
const emit = defineEmits(['close'])
const show = ref(false)

// const emit = defineEmits(['close'])
// const props = defineProps({
//     show: Boolean
// })
const LayoutStore = useLayoutStore()

const toggleSessionInitModal = () => {
    showTable.value = false
    LayoutStore.toggleSessionInitModal()
    step.value = 1
}

const step = ref(1)
const uploadType = ref('uploadFile')

const tabs = reactive([
    {
        step: 1,
        slotModalHeader: 'Choose a method to initialize your session'
    },
    {
        step: 2,
        uploadType: 'uploadFile',
        slotModalHeader: 'Validate your data'
    },
    {
        step: 2,
        uploadType: 'emptyBrowser',
        slotModalHeader: 'Choose your genome assembly'
    }
])

watch(props, newValue => {
    show.value = newValue.show
    console.log(show.value)
})

// 关闭对话框
const closeHandle = () => {
    emit('close', false)
}

// 处理按钮点击
const btnHandle = (key: string) => {
    closeHandle()
}

const fileInput = ref(null)
const ChooseJsonFile = (event) => {
    // const input = document.createElement("input");
    // input.type = "file";
    // input.accept = ".json";
    // input.addEventListener("change", (event) => {
    const file = event.target.files[0];
    validateJsonFile(file);
    // });
    fileInput.value.click();
}

const jsonData = ref(null)
const showError = ref(false)
const errorMessage = ref('')
const showTable = ref(false)
const modalDisplay = ref('')

const validateJsonFile = (file) => {
    const reader = new FileReader();
    reader.onload = (event) => {
        try {
            const data = JSON.parse(event.target.result);
            // perform validations on jsonData
            // if (validateUrls(data.tracks) && validateFields(data.tracks)) {
                if(validateFields(data.tracks)){
                jsonData.value = data
                console.log('validated: ', jsonData.value)

                // showJsonTable(jsonData);
                showTable.value = true
                modalDisplay.value = "block"
            } else {
                showError.value = true
                errorMessage.value = 'Invalid JSON file'
            }
        } catch (error) {
            // report error message and stop validation
            showError.value = true
            errorMessage.value = "Invalid JSON syntax: " + error.message
            // console.error("Invalid JSON syntax:", error.message);
        }
    };
    reader.readAsText(file);
    step.value = 2
    uploadType.value = 'uploadFile'
}

// const validateUrls = (jsonData) => {
//     for (const file of jsonData) {
//         if (!file.url) {
//             console.error("URL is a required field:", file);
//             return false;
//         } else {
//             fetch(file.url)
//                 .then((response) => {
//                     if (!response.ok) {
//                         console.error("Invalid URL:", file.url);
//                         return false;
//                     }
//                 })
//                 .catch((error) => {
//                     console.error("Error fetching URL:", error);
//                     return false;
//                 });
//         }
//     }
//     return true;
// }

const validateFields = (jsonData) => {
    console.log('jsonData', jsonData)
    const nameMap = new Map();
    for (let i = 0; i < jsonData.length; i++) {
        const file = jsonData[i];
        if (!file.type) {
            console.error("Type is a required field:", file);
            return false;
        } else if (![ "CurvTrack",  'SclsTrack', "VirtualCTrack","CovTrack", "PclsTrack", "InterChromCurvTrack", "GeneTrack", 'HicTrack', 'LineGTrack', 'HeatmapGTrack'].includes(file.type)) {
            console.error("Invalid type:", file.type);
            return false;
        }
        if (!file.label) {
            file.label = file.name || "";
        }
        if (!file.name) {
            const fileName = file.url.split("/").pop();
            file.name = fileName.substring(0, Math.min(fileName.length, 30));
        }
        if (nameMap.has(file.name)) {
            let suffix = 2;
            while (nameMap.has(file.name + "_" + suffix)) {
                suffix++;
            }
            file.name = file.name + "_" + suffix;
        }
        nameMap.set(file.name, i);
    }
    return true;
}

const showJsonTable = (jsonData) => {
    const table = document.createElement("table");
    const headerRow = document.createElement("tr");
    const headers = ["Name", "Type", "Label", "URL"];
    for (const header of headers) {
        const th = document.createElement("th");
        th.innerText = header;
        headerRow.appendChild(th);
    }
    table.appendChild(headerRow);
    for (const file of jsonData) {
        const row = document.createElement("tr");
        const data = [file.name, file.type, file.label, file.url];
        for (const datum of data) {
            const td = document.createElement("td");
            td.innerText = datum;
            row.appendChild(td);
        }
        table.appendChild(row);
    }
    // display table in modal
}

const hideModal = () => {
    modalDisplay.value = "none"
    jsonData.value = null
    showTable.value = false
    showError.value = false
    errorMessage.value = ''
}

const createColumns = () => {
    return [
        {
            title: "Name",
            key: "name"
        },
        {
            title: "Title",
            key: "title"
        },
        {
            title: "Type",
            key: "type"
        },
        {
            title: "URL",
            key: "url"
        }
    ];
};

const columns = createColumns();
// const data = reactive({
//     id: 'testID',
//     tracks: [
//         {
//             "name": "pair_ends_clusters",
//             "type": "PclsTrack",
//             "label": "pair_ends_clusters",
//             "url": "/data/BASIC_HBAD5RP_FKDL190764711-1a.e500.clusters.cis.chiasig.sample.txt"
//         },
//         {
//             "name": "testCurvData",
//             "type": "CurvTrack",
//             "label": "testCurvData",
//             "url": "/data/BASIC_HBAD5RP_FKDL190764711-1a.e500.clusters.cis.chiasig.sample.txt"
//         }
//     ]
// })

// const camelToKebab = (str) => {
//     return str.replace(/([a-z0-9])([A-Z])/g, '$1-$2').toLowerCase();
// }
// const tabsViewStore = useTabsStore();
const trackStore = useTrackStore();
const sessionStore = useSessionStore();


const UploadJsonFile = async (data) => {
  try {
    const sessionUuid = uuid();
    const newSession = {
      key: sessionUuid,
      trackIds: [],
      sessionConfig: {
        type: 'TrackList',
        maxTrackNum: 10,
      },
    };

    await Promise.all(
      data.tracks.map(async (item, index) => {
        const trackComponentType = item.type;
        item.uuid = uuid();
        // item.order = index
        await Promise.all([
          componentInstall(trackComponentType,  fetchTrackComponent(item.type)),
          componentInstall(`${trackComponentType}Config`,  fetchConfigComponent(item.type)),
        ]);

        const newTrack = await createComponent(item.type);
        newTrack.key = item.uuid;
        newTrack.trackConfig.sessionId.push(sessionUuid);
        newTrack.option.url = item.url;
        newTrack.trackConfig.name = item.name;
        newTrack.trackConfig.label = item.label;
        // newTrack.trackConfig.order = index

        trackStore.addTrackList(newTrack, false, true);
        newSession.trackIds.push(item.uuid);
      })
    );

    sessionStore.addSession(newSession);
    sessionStore.targetedSession.push(sessionUuid);
    toggleSessionInitModal();
  } catch (error) {
    console.log(error);
  }
};

const componentInstall = (key, component) => {
    if (!window.$vue.component(key)) {
        window.$vue.component(key, component)
    }
}

const fetchTrackComponent = async (trackType) => {
    const component = await import(`../tracks/${trackType}/${trackType}.vue`);
    return component;
};

const fetchConfigComponent = async (trackType) => {
    const component = await  import(`../tracks/${trackType}/config.vue`);
    return component;
};

const createComponent = async (trackType) => {
    // const { key } = targetData
    // console.log(key)
   // console.log(trackType)
    const chart =  await import(`../tracks/${trackType}/config.ts`)
   // console.log(chart)
    return new chart.default()
}


const handleEmptySession = () => {
    step.value = 2
    uploadType.value = 'emptyBrowser'
}
</script>
<style></style>