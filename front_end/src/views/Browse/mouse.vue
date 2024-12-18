<template>
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
          <p class=" text-xl font-light text-gray-500"> This is the Browser selection page for human. </p>
  
        </li>
        <li class="flex space-x-3 items-center mb-2">
          <!-- Icon -->
          <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"></path>
          </svg>
          <p class="text-xl font-light text-gray-500">
            Provides track types integrated from 1036 human Hi-C datasets: MetaCompartment, MetaDomain, and MetaLoop
            tracks.
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
          <p class="text-xl font-light text-gray-500">
            Additionally, you can load 5000 Hi-C data tracks from EXPRESSO.
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
          <p class="text-xl font-light text-gray-500">
            After navigating to the region of interest, click and select Annotate genomic region to perform the
            annotation.
          </p>
        </li>
      </ul>
    </n-card>
    <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full  w-full">
      <CardActions :expand="expand" :isExpand="isExpand" :reload="reload" class="h-full" title="Genome Browser"
        :segmented="{
          content: true
        }">
        <template #header>
          <n-h3 prefix="bar" align-text>Browse genomic regions</n-h3>
  
          <!-- <div class="compose-btn-wrap ">
            <n-button strong secondary type="primary" size="large">Browse genomic regions</n-button>
          </div> -->
        </template>
        <template #header-extra>
          <!-- <n-button strong secondary type="primary" size="large">Add EXPRESSO Track</n-button>
          <n-button strong secondary type="primary" size="large">Add Custome Track</n-button> -->
          <!-- <div class="inline mr-6">
              <n-switch v-model:value="showTrackLabel" size="medium" class="  mr-3"/>
              <span v-if="showTrackLabel">Exploration mode</span>
              <span v-else>Selection mode</span>
          </div> -->
          <!-- <AutocompleteDialog @submit-gene="fetchGene" ></AutocompleteDialog> -->
           <div class="flex">
            <form class="flex flex-grow items-center" @submit.prevent="handleGeneSearch">
              <!-- <label for="simple-search" class="sr-only">Search</label> -->
              <input type="text"
                  class="relative m-0  block min-w-0 flex-auto  rounded-l border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-1.5 text-base font-normal text-neutral-700 outline-none transition duration-300 ease-in-out focus:border-primary focus:text-neutral-700 focus:shadow-te-primary focus:outline-none"
                  placeholder="Search" required 
                  v-model="currentGene"
                  @keyup.enter="handleGeneSearch"
                  >
              <button
                  class="relative flex items-center mr-3 px-4 py-2.5
                              text-white
                              rounded-r 
                              bg-indigo-500	 transition duration-150 ease-in-out hover:bg-primary-700 hover:shadow-lg focus:bg-primary-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-primary-800 active:shadow-lg"
                  type="button" id="location-search" data-te-ripple-init data-te-ripple-color="light"
                  @click="handleGeneSearch">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-5 w-5">
                      <path fill-rule="evenodd"
                          d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z"
                          clip-rule="evenodd" />
                  </svg>
              </button>
          </form>
          <div class="inline mr-4" @click="showAddTrackModal = true">
            <n-button class="mr-4" strong secondary type="primary" size="large">Add Track</n-button>
  
          </div>
          <div class="inline" @click="showTracksInfoModal = true">
            <n-button strong secondary type="info" size="large">Show loaded Tracks</n-button>
          </div>
  
           </div>
               </template>
        <template #default>
          <ExpressoVue id="testID2" :assembly="asm" :tracksInfo="tracksInfo"></ExpressoVue>
        </template>
      </CardActions>
    </CardWrapper>
    <div class="mt-6">
      <AnnotationDetail></AnnotationDetail>
    </div>
  
    <n-modal v-model:show="showAddTrackModal" preset="card" size="huge" header-class="bg-white" content-class="bg-white">
      <n-tabs type="line" animated>
        <n-tab-pane name="Add Meta Track" tab="Add Meta Track" display-directive="if">
          <DownloadTable :downloadFiles="downloadFiles_merged" @addTrack="addTrack"></DownloadTable>
  
        </n-tab-pane>
        <n-tab-pane name="Add EXPRESSO track" tab="Add EXPRESSO track" display-directive="show">
          <ExpressoTable @add-track="addTrack"></ExpressoTable>
        </n-tab-pane>
      </n-tabs>
    </n-modal>
  
    <n-modal v-model:show="showTracksInfoModal" preset="card" style="max-width: 900px" title="Current Tracks Information"
      :bordered="false" size="huge">
      <n-table :bordered="false" :single-line="false">
        <thead>
          <tr>
            <th>Track Id</th>
            <th>Track label</th>
            <th>Track Type</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="track in tracksInfo" :key="track.id">
            <td>{{ track.id }}</td>
            <td>{{ track.name }}</td>
            <td>{{ track.type }}</td>
          </tr>
        </tbody>
      </n-table>
    </n-modal>
  </template>
  <script setup>
  import { ref } from 'vue'
  import ExpressoVue from "@/assets/js/dist/Expresso.es"
  // import ExpressoVsue from "@/browser/elements/Expresso/ExpressoVue.vue"
  import chromBands from '@/data/chromBands.json'
  import AutocompleteDialog from '@/components/common/AutocompleteDialog.vue'
  import AnnotationDetail from '@/views/ResultsDetail/index.vue'
  import DownloadTable from './DownloadTable.vue'
  import ExpressoTable from './ExpressoTable.vue'
  import {fetchGeneCoord} from './fetchGeneCoord.js'
  
  const showAddTrackModal = ref(false)
  const showTracksInfoModal = ref(false)
  const currentGene = ref('')
  const value = ref(null)

  let asm = 
    {
      id: 'mm10',
      chromSizes: {
        "chr1": 195471971,
        "chr2": 182113224,
        "chrX": 171031299,
        "chr3": 160039680,
        "chr4": 156508116,
        "chr5": 151834684,
        "chr6": 149736546,
        "chr7": 145441459,
        "chr10": 130694993,
        "chr8": 129401213,
        "chr14": 124902244,
        "chr9": 124595110,
        "chr11": 122082543,
        "chr13": 120421639,
        "chr12": 120129022,
        "chr15": 104043685,
        "chr16": 98207768,
        "chr17": 94987271,
        "chrY": 91744698,
        "chr18": 90702639,
        "chr19": 61431566,
        "chrM": 16299
      },
      initPos:
      {
        chrom: 'chr1',
        start: 22790000,
        end: 26290000
      }
    }

const tracksInfo = ref([
{
    id: 'meta domain mouse',
    name: 'Meta domain insulation',
    label: 'Meta insulation score',
    type: 'MetaDomainTrack',
    url: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/3D_annotation/mm10/mouse_domain_meta_track.srt.bed.gz'
  },
  {
    id: 'meta compartment mouse',
    name: 'Meta compartment type',
    label: 'Meta compartment type',
    type: 'MetaCompartmentTrack',
    url: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/3D_annotation/mm10/mouse_compartment_meta_track.txt.gz'
  },
  {
    id: 'meta loops2',
    name: 'Meta loops type',
    label: 'Meta loops type',
    type: 'DotTrack',
    url: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/3D_annotation/mm10/mouse_merged_loop_track_srt.bed.gz'
  }
  ])

  
  // Add method to add new track
  const addTrack = (trackData) => {
    tracksInfo.value.push({
      id: trackData.sample_name.toLowerCase().replace(/\s+/g, '-'),
      name: trackData.sample_name,
      label: trackData.sample_name,
      type: trackData.track_type,
      url: trackData.download_link
    })
  }
  
  const handleGeneSearch = () => {
    console.log(currentGene.value)
    fetchGeneCoord(currentGene.value)
  
  }
   
  </script>
  <style lang="scss" scoped>
  .compose-btn-wrap {
    width: 20%;
  
    :deep() {
      .n-button {
        width: 100%;
      }
    }
  }
  </style>