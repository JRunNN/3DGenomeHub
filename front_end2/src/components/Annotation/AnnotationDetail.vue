<template>
  <div v-if="overallProgress != 'COMPLETE'" class="flex items-center justify-center w-full">
    <div
      class="bg-white flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">

      <div class="flex flex-col w-3/5">
        <n-progress class="w-16" type="line" indicator-placement="inside" :percentage="progressBarContent.percent"
          processing :height="40" :border-radius="8" :fill-border-radius="0" />
      </div>
      <div>
        {{ progressBarContent.notation }}
      </div>

    </div>
  </div>

  <div v-else>
    <div class="col-span-2 space-y-8 md:grid md:grid-cols-2 md:gap-12 md:space-y-0">
      <anchor-stat :inputData="AnchorStatInput"></anchor-stat>
      <interaction-stat :inputData="InteractionStatInput"></interaction-stat>
      <normal-atac-stat :inputData="NormalAtacStatInput"></normal-atac-stat>
      <cancer-atac-stat :inputData="CancerAtacStatInput"></cancer-atac-stat>

    </div>
    <!-- <n-data-table remote :columns="columns" :data="data" :pagination="pagination" :bordered="false" /> -->

    <n-card :bordered="true" :segmented="{ content: true }" class="mb-6 mt-6"
      header-style="font-size: 20px;background-color: #D8D8D8;color: #09253D;padding-top: 4px;padding-bottom: 4px;"
      size="small" title="Chromatin interactions">
      <div class="flex justify-between">

        <!-- search bar -->
        <div class="mb-4 w-20 mr-3 text-l rounded-l" style="height: 40px">
          <n-select size="large" v-model:value="chrom" :options="chromValues" :consistent-menu-width="false" />

        </div>
        <!-- <form class="ml-8 mr-8 mb-4 flex w-18 items-center">
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
    </form> -->
        <div class="mb-4 flex items-center" role="group">
          <button
            class="relative flex items-center mr-3 px-4 py-2.5
                            text-white
                            rounded-r bg-blue-700 transition duration-150 ease-in-out hover:bg-primary-700 hover:shadow-lg focus:bg-primary-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-primary-800 active:shadow-lg"
            type="button" id="location-search" data-te-ripple-init data-te-ripple-color="light" @click="downloadData">
            Download annotated dataset
          </button>
        </div>
      </div>
      <div class="mt-2">
        <n-data-table :columns="columns" :data="data" :pagination="pagination" :bordered="false" />
      </div>
    </n-card>

  </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { h, ref, onMounted } from 'vue'
import { useRouter, useRoute } from "vue-router";
import { NButton, useMessage } from 'naive-ui'
import type { DataTableColumns } from 'naive-ui'
import AnchorStat from './AnchorStat.vue'
import InteractionStat from './InteractionStat.vue'
import NormalAtacStat from './NormalAtacStat.vue'
import CancerAtacStat from './CancerAtacStat.vue'
import { TabixIndexedFile } from '@gmod/tabix'
import { RemoteFile } from 'generic-filehandle'
const message = useMessage()
// const router = useRouter()

const props = defineProps({
  taskId: {
    type: String,
    required: true
  }
})

const chrom = ref('chr1')

let chromSizes = {
  "chrY": 59373566,
  "chrX": 155270560,
  "chr13": 115169878,
  "chr12": 133851895,
  "chr11": 135006516,
  "chr10": 135534747,
  "chr17": 81195210,
  "chr16": 90354753,
  "chr15": 102531392,
  "chr14": 107349540,
  "chr19": 59128983,
  "chr18": 78077248,
  "chrM": 16571,
  "chr22": 51304566,
  "chr20": 63025520,
  "chr21": 48129895,
  "chr7": 159138663,
  "chr6": 171115067,
  "chr5": 180915260,
  "chr4": 191154276,
  "chr3": 198022430,
  "chr2": 243199373,
  "chr1": 249250621,
  "chr9": 141213431,
  "chr8": 146364022
}

const chromValues = Object.keys(chromSizes).map(chr => ({ value: chr, label: chr }))
// console.log(chromValues)
type Song = {
  chrom1: string
  start1: number
  end1: number
  chrom2: string
  start2: number
  end2: number
  petCounts: number
  GenomicAnno1: string
  GenomicAnno2: string
  ENCODE_ATAC1: string
  ENCODE_ATAC2: string
  TCGA_ATAC1: string
  TCGA_ATAC2: string
}

const createColumns = ({
  play
}: {
  play: (row: Song) => void
}): DataTableColumns<Song> => {
  return [
    {
      title: 'chrom1',
      key: 'chrom1'
    },
    {
      title: 'start1',
      key: 'start1'
    },
    {
      title: 'end1',
      key: 'end1'
    },
    {
      title: 'chrom2',
      key: 'chrom2'
    },
    {
      title: 'start2',
      key: 'start2'
    },
    {
      title: 'end2',
      key: 'end2'
    },
    {
      title: 'petCounts',
      key: 'petCounts'
    },
    {
      title: 'GenomicAnno1',
      key: 'GenomicAnno1',
      ellipsis: {
        tooltip: true
      }
    },
    {
      title: 'GenomicAnno2',
      key: 'GenomicAnno2',
      ellipsis: {
        tooltip: true
      }
    },
    {
      title: 'ENCODE_ATAC1',
      key: 'ENCODE_ATAC1',
      ellipsis: {
        tooltip: true
      }
    },
    {
      title: 'ENCODE_ATAC2',
      key: 'ENCODE_ATAC2',
      ellipsis: {
        tooltip: true
      }
    },
    {
      title: 'TCGA_ATAC1',
      key: 'TCGA_ATAC1',
      ellipsis: {
        tooltip: true
      }
    },
    {
      title: 'TCGA_ATAC2',
      key: 'TCGA_ATAC2',
      ellipsis: {
        tooltip: true
      }
    }
  ]
}


const data = ref([])

const columns = createColumns({
  play(row: Song) {
    message.info(`Play ${row.chrom1}`)
  }
})

const overallProgress = ref('annotation')
const pagination = ref(true)

const progressBarContent = ref({
  percent: 0,
  notation: 'Start Annotation'

})
const result = ref(null)


const parseTSV = (data, headers) => {
  // Split data into lines
  const lines = data.trim().split(/\r?\n/);

  // Map the rows to objects with provided headers
  const result = lines.map(line => {
    const fields = line.split('\t');
    const entry = headers.reduce((object, header, index) => {
      object[header] = fields[index];
      return object;
    }, {});
    return entry;
  });
  // const result = lines.map(line => line.split('\t'));

  return result;
}

// Define the headers as they are not present in the file
const headers = [
  'chrom1', 'start1', 'end1',
  'chrom2', 'start2', 'end2',
  'petCounts', 'GenomicAnno1', 'GenomicAnno2',
  'ENCODE_ATAC1', 'ENCODE_ATAC2', 'TCGA_ATAC1', 'TCGA_ATAC2'
]

function convertStringToArray(str) {
  // Split the string into lines
  const lines = str.trim().split('\n');
  // console.log(lines)
  // Map each line to an object
  const result = lines.map(line => {
    // Extract the parts of the line before and after the colon
    const [name, value] = line.split(':');

    // Return a new object with the name and value
    return {
      value: value.trim() === "0" ? value.trim() : parseInt(value.trim(), 10), // Parse the value as an integer
      name: name.trim() // Trim the name to remove any excess white space
    };
  });

  return result;
}

// console.log(resultArray);
const AnchorStatInput = ref([])
const InteractionStatInput = ref([])
const NormalAtacStatInput = ref([])
const CancerAtacStatInput = ref([])




const initPoll = (taskId) => {
  axios.get(import.meta.env.VITE_BASE_URL + `/annotations/task-info/${taskId}`)
    .then((response) => {
      // console.log(import.meta.env.VITE_BASE_URL + `/annotations/task-info/${taskId}`)
      // console.log('response.data', response.data)
      // result.value = response.data.task_result;
      const processUnderCondition = async () => {

        if (await response.data.task_status === 'SUCCESS') {
          // console.log('11111', response.data)

          progressBarContent.value.percent = 95
          progressBarContent.value.notation = 'Generating summary tables!'
          // clearInterval(poll);
          result.value = response.data.task_result.notation;

          // promoter enhancer statistics
          const P_E_stat = result.value.split('=====')[0]
          if(P_E_stat) {
            AnchorStatInput.value = convertStringToArray(P_E_stat)

          }

          // interaction type statistics
          const Interaction_stat = result.value.split('=====')[1]
          if(Interaction_stat) {
          InteractionStatInput.value = convertStringToArray(Interaction_stat)
          }

          // Normal tissue statistics
          const Normal_stat = result.value.split('=====')[2]
          if(Normal_stat) {
          NormalAtacStatInput.value = convertStringToArray(Normal_stat)
          }

          // Cancer tissue statistics
          const Cancer_stat = result.value.split('=====')[3]
          if(Cancer_stat) {
          CancerAtacStatInput.value = convertStringToArray(Cancer_stat)
          }

          const fileUrl = '/media' + result.value.split('=====')[4].split(' ')[1];
          // console.log(fileUrl)

          const file = new TabixIndexedFile({
            filehandle: new RemoteFile(fileUrl),
            tbiFilehandle: new RemoteFile(`${fileUrl}.tbi`)
          });
          // console.log(file)
          let lines = []

          await file.getLines(chrom.value, 0, undefined, function (line, fileOffset) {
            // console.log(line)
            const splitData = line.split(/;;/)
            const arr = splitData[0].split(/[\s,:-]+/)
            const anchor = splitData[1].split(/;/)
            const addedData = {
              chrom1: arr[0],
              start1: Number(arr[1]),
              end1: Number(arr[2]),
              chrom2: arr[3],
              start2: Number(arr[4]),
              end2: Number(arr[5]),
              petCounts: Number(arr[6]),
              GenomicAnno1: anchor[0],
              GenomicAnno2: anchor[1],
              ENCODE_ATAC1: anchor[2],
              ENCODE_ATAC2: anchor[3],
              TCGA_ATAC1: anchor[4],
              TCGA_ATAC2: anchor[5]
            }
            lines.push(addedData)
          })
          // console.log(lines)
          data.value = lines
          overallProgress.value = 'COMPLETE'
        } else if (await response.data.task_status === 'FAILURE') {
          // clearInterval(poll);
          console.error('Task failed');
        } else if (await response.data.task_status === 'PROGRESS') {
          // console.log(overallProgress.value)
          // console.log(response.data.task_result)
          progressBarContent.value.percent = response.data.task_result.percent
          progressBarContent.value.notation = response.data.task_result.notation
        }
      }
      processUnderCondition()
      // For other statuses like 'PENDING' or 'PROGRESS', keep polling
    })
    .catch(error => {
      // clearInterval(poll);
      console.error('Error while polling for result:', error);
    });
}

const bedpeUrl = ref('')
const browserUrl = ref('')
const pollForResult = (taskId) => {
  // Poll for the result of the background job
  const poll = setInterval(() => {
    // console.log(taskId)
    axios.get(import.meta.env.VITE_BASE_URL + `/annotations/task-info/${taskId}`)
      .then((response) => {
        // console.log(import.meta.env.VITE_BASE_URL + `/annotations/task-info/${taskId}`)
        // console.log('response.data', response.data)
        // result.value = response.data.task_result;
        const processUnderCondition = async () => {

          if (await response.data.task_status === 'SUCCESS') {
            // console.log('22222', response.data)

            progressBarContent.value.percent = 95
            progressBarContent.value.notation = 'Generating summary tables!'
            // clearInterval(poll);
            result.value = response.data.task_result.notation;
          // promoter enhancer statistics
          const P_E_stat = result.value.split('=====')[0]
          if(P_E_stat) {
            AnchorStatInput.value = convertStringToArray(P_E_stat)

          }

          // interaction type statistics
          const Interaction_stat = result.value.split('=====')[1]
          if(Interaction_stat) {
          InteractionStatInput.value = convertStringToArray(Interaction_stat)
          }

          // Normal tissue statistics
          const Normal_stat = result.value.split('=====')[2]
          if(Normal_stat) {
          NormalAtacStatInput.value = convertStringToArray(Normal_stat)
          }

          // Cancer tissue statistics
          const Cancer_stat = result.value.split('=====')[3]
          if(Cancer_stat) {
          CancerAtacStatInput.value = convertStringToArray(Cancer_stat)
          }

            // axios.get("http://47.107.91.5/media" + result.value.split('=====')[4].split(' ')[1])
            //   .then(res => {
            //     data.value = parseTSV(res.data, headers);
            //     progressBarContent.value.percent = 100
            //     progressBarContent.value.notation = 'Full annotation table generated!'
            //     overallProgress.value = 'output'
            //     console.log(data.value);
            //   })
            //   .catch(err => {
            //     console.error('Error while downloading file:', err);
            //   })

            const fileUrl = '/media' + result.value.split('=====')[4].split(' ')[1];
            // console.log(fileUrl)
            browserUrl.value = '/media' + result.value.split('=====')[4].split(' ')[0];
            bedpeUrl.value = '/media' + result.value.split('=====')[4].split(' ')[2];
            const file = new TabixIndexedFile({
              filehandle: new RemoteFile(fileUrl),
              tbiFilehandle: new RemoteFile(`${fileUrl}.tbi`)
            });
            // console.log(file)
            let lines = []

            await file.getLines(chrom.value, 0, undefined, function (line, fileOffset) {
              // console.log(line)
              const splitData = line.split(/;;/)
              const arr = splitData[0].split(/[\s,:-]+/)
              const anchor = splitData[1].split(/;/)
              const addedData = {
                chrom1: arr[0],
                start1: Number(arr[1]),
                end1: Number(arr[2]),
                chrom2: arr[3],
                start2: Number(arr[4]),
                end2: Number(arr[5]),
                petCounts: Number(arr[6]),
                GenomicAnno1: anchor[0],
                GenomicAnno2: anchor[1],
                ENCODE_ATAC1: anchor[2],
                ENCODE_ATAC2: anchor[3],
                TCGA_ATAC1: anchor[4],
                TCGA_ATAC2: anchor[5]
              }
              lines.push(addedData)
            })
            // console.log(lines)
            data.value = lines
            overallProgress.value = 'COMPLETE'

          } else if (response.data.task_status === 'FAILURE') {
            // clearInterval(poll);
            console.error('Task failed');
          } else if (response.data.task_status === 'PROGRESS') {
            progressBarContent.value.percent = response.data.task_result.percent
            progressBarContent.value.notation = response.data.task_result.notation
          }
        }
        processUnderCondition()

      })
      .catch(error => {
        clearInterval(poll);
        console.error('Error while polling for result:', error);
      });
  }, 1000); // Poll every 2 seconds
}
const route = useRoute()

const downloadProgress = ref(0)
const downloadData = () => {
  axios({
    method: 'get',
    url: bedpeUrl.value,
    responseType: 'blob', // Important: indicates that we expect a binary file
    onDownloadProgress: (progressEvent) => {
      // console.log('进度事件1', progressEvent);

      // if (progressEvent.lengthComputable) {

      downloadProgress.value = Math.floor((progressEvent.loaded * 100) / progressEvent.total);

    }
  })
    .then(response => {
      // Create a URL for the file
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      // link.setAttribute('download', filename); // Set the file name
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
      // downloading.value = false;
      downloadProgress.value = 0;
    });
}


onMounted(() => {
  initPoll(route.params.taskId)

  if (overallProgress.value != 'COMPLETE') {
    pollForResult(route.params.taskId)
  }
  // console.log(route.params.taskId)
})
</script>


<style>
.redo-button {
  background-color: #4878D0;

}
</style>