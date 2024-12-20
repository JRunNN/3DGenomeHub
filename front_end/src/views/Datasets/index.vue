<template>
  <div class="mx-auto max-w-8xl">
    <div class="flex grow">
      <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
        <CardActions :expand="expand" :isExpand="isExpand" :reload="reload" class="h-full" :segmented="{
          content: true,
          footer: true
        }">
          <template #header>
            <n-h3>Datasets used for annotation</n-h3>
          </template>
          <template #header-extra>
          </template>
          <template #default>
            <ul>
              <li class="flex space-x-3 items-center mb-2">
                <!-- Icon -->
                <svg
                  class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-50 hover:text-blue-500 transition-colors duration-300 cursor-pointer"
                  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                    clip-rule="evenodd"></path>
                </svg>
                <p class=" text-xl font-light text-gray-500"> This page documents the 3D genome datasets used for annotating genomic regions.
                </p>
              </li>
              <li class="flex space-x-3 items-center mb-2">
                <!-- Icon -->
                <svg
                  class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-50 hover:text-blue-500 transition-colors duration-300 cursor-pointer"
                  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                    clip-rule="evenodd"></path>
                </svg>
                <p class=" text-xl font-light text-gray-500"> Human 3D genome data is sourced from the EXPRESSO database.
                  <a href="https://expresso.sustech.edu.cn/home" target="_blank">

                  <svg @click="router.push({ name: 'dataportal' })"
                    class="inline mb-1 w-5 h-5 text-grey-500 hover:text-blue-500 transition-colors duration-300"
                    aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M15 11v4.833A1.166 1.166 0 0 1 13.833 17H2.167A1.167 1.167 0 0 1 1 15.833V4.167A1.166 1.166 0 0 1 2.167 3h4.618m4.447-2H17v5.768M9.111 8.889l7.778-7.778" />
                  </svg>
                 </a>
                </p>

              </li>
              <li class="flex space-x-3 items-center mb-2">
                <!-- Icon -->
                <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
                  viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                    clip-rule="evenodd"></path>
                </svg>
                <p class=" text-xl font-light text-gray-500"> We additionally collected and processed 400 mouse Hi-C datasets, with specific data IDs listed in the table below.
                </p>

              </li>
            </ul>
          </template>
        </CardActions>
      </CardWrapper>
    </div>

    <div class="flex grow mt-8">
      <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
        <CardActions :expand="expand" :isExpand="isExpand" :reload="reload" class="h-full" :segmented="{
          content: true,
          footer: true
        }">
          <template #header>
            <n-h3 prefix="bar" align-text>Mouse Hi-C datasets GSM IDs</n-h3>
          </template>
   <template #header-extra></template>
          <template #default>
    
            <div class="mt-6">
              <DownloadTable :downloadFiles="downloadFiles_single"></DownloadTable>
            </div>
          </template>
      
        </CardActions>
      </CardWrapper>
    </div>

    <div class="flex grow mt-8">
      <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
        <CardActions :expand="expand" :isExpand="isExpand" :reload="reload" class="h-full" :segmented="{
          content: true,
          footer: true
        }">
          <template #header>
            <n-h3 prefix="bar" align-text>Other 1D datasets</n-h3>
          </template>
          <template #default>
            <div >
              <DownloadTable :downloadFiles="downloadFiles_merged"></DownloadTable>
            </div>
          </template>
          <template #header-extra>
          </template>
        </CardActions>
      </CardWrapper>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted, reactive, h, watch, computed } from 'vue'
import type { DataTableColumns } from 'naive-ui'
import axios from '@/plugins/axios';
import { useRouter } from "vue-router";
import { NCard, NDataTable, NButton } from "naive-ui";
import { useLoadingBar } from 'naive-ui'
import DownloadTable from './DownloadTable.vue'
import { useThemeStore } from "@/stores/theme"

const themeStore = useThemeStore()

const style = computed<{ [key: string]: any }>(() => themeStore.style)

const textSecondaryColor = computed<string>(() => style.value["--fg-secondary-color"])

const router = useRouter()


const loadingBar = useLoadingBar()


const downloadFiles_merged = ref({
  itemCount: 4,
  items:[
  {
    sample_name: 'Gene expression',
    file_name: 'RNA-seq normalized count table',
    file_type: 'gzipped',
    file_size: '80M',
    download_link: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/rnaseq/gene_expression_long_format_converted.txt.gz'
  },
  {
    sample_name: 'Loop Anchor motif',
    file_name: 'Loop Anchor motif enrichment file',
    file_type: 'gzipped',
    file_size: '22.05M',
    download_link: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/download/loop_anchor_atac_motifs.zip'
  },
  {
    sample_name: 'Chromatin Loops',
    file_name: 'Loop anchor with annotation',
    file_type: 'gzipped ',
    file_size: '34.71M',
    download_link: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/download/merged_chromatin_loops.txt.zip'
  },
  {
    sample_name: 'Compartments',
    file_name: 'Merged compartment bed file',
    file_type: 'gzipped ',
    file_size: '207.12M',
    download_link: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/download/merged_sample_compartment.bed.gz'
  },
  {
    sample_name: 'Contact domains',
    file_name: 'Merged domain with gene file',
    file_type: 'gzipped ',
    file_size: '291.33M',
    download_link: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/download/merged_gene_domain_relations.txt.gz'
  }
  ]
}
)
const downloadFiles_single = ref([])

const fetchDownloadFiles = () => {
  axios.get('http://47.107.91.5:8888/api/genomehub/mousesamples', {
    responseType: 'json',

  })
    .then(res => {
      downloadFiles_single.value = res.data
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

// const downloadFiles_1d = ref([])

// const fetchDownload1DFiles = () => {
//   axios.get('/download1dfiles', {
//     responseType: 'json',

//   })
//     .then(res => {
//       downloadFiles_1d.value = res.data
//     }).catch(function (error) {
//       if (error.response) {
//         // The request was made and the server responded with a status code
//         // that falls out of the range of 2xx
//         console.log(error.response.data);
//         console.log(error.response.status);
//         console.log(error.response.headers);
//       } else if (error.request) {
//         // The request was made but no response was received
//         // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
//         // http.ClientRequest in node.js
//         console.log(error.request);
//       } else {
//         // Something happened in setting up the request that triggered an Error
//         console.log('Error', error.message);
//       }
//       console.log(error.config);
//     });
// }
onMounted(() => {
  fetchDownloadFiles()
  // fetchDownload1DFiles()
})
</script>
<style scoped>
.active {
  background-color: #e2e9ec;
  /* Green */
  color: white;
}
</style>