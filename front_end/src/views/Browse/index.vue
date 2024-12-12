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
        <p class=" text-xl font-light text-gray-500"> Annotate user uploaded chromatin interaction files using
          multiple
          sources. </p>

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
          Provide interactive graphs and tables to display anotation results.
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
          The results of the annotations can be shared through a link or are available for download.
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
          Click to view existing sample dataset output or download sample dataset and upload it to our server.
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
        <div class="flex">
          <div class="flex flex-wrap pt-1 pb-4">
            <div class="items-center hidden mt-3 mr-4 text-sm font-medium text-gray-900 md:flex dark:text-white">
              Annotation Bin Size:
            </div>
            <div class="flex flex-wrap">
              <div class="flex items-center mt-3 mr-4">
                <input id="active" type="radio" value="" name="show-only"
                  class="w-4 h-4 bg-gray-100 border-gray-300 text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                <label for="active" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                  100bp
                </label>
              </div>
              <div class="flex items-center mt-3 mr-4">
                <input id="active" type="radio" value="" name="show-only"
                  class="w-4 h-4 bg-gray-100 border-gray-300 text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                <label for="active" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                  500bp
                </label>
              </div>
              <div class="flex items-center mt-3 mr-4">
                <input id="pending" type="radio" value="" name="show-only"
                  class="w-4 h-4 bg-gray-100 border-gray-300 text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                <label for="pending" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                  5000bp
                </label>
              </div>
              <div class="flex items-center mt-3 mr-4">
                <input id="inactive" type="radio" value="" name="show-only"
                  class="w-4 h-4 bg-gray-100 border-gray-300 text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                <label for="inactive" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                  10000bp
                </label>
              </div>
            </div>
          </div>
          <div class="inline" @click="showAddTrackModal = true">
            <n-button class="mr-4" strong secondary type="primary" size="large">Add Track</n-button>
          </div>
        </div>


      </template>
      <template #default>
        <ExpressoVue id="testID2" :assembly="asm" :tracksInfo="tracksInfo"></ExpressoVue>

        <ExpressoVue id="testID3" :assembly="asm_mouse" :tracksInfo="tracks_mouse"></ExpressoVue>
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

      </n-tab-pane>
    </n-tabs>
  </n-modal>
</template>
<script setup>
import { ref } from 'vue'
import ExpressoVue from "@/assets/js/dist/Expresso.es"
// import ExpressoVsue from "@/browser/elements/Expresso/ExpressoVue.vue"
import chromBands from '@/data/chromBands.json'

import AnnotationDetail from '@/views/Annotate/AnnotationDetailTable/index.vue'
import DownloadTable from './DownloadTable.vue'

const showAddTrackModal = ref(false)


let asm =
{
  label: 'hg38',
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
  },
  chromBands: chromBands

}


const tracksInfo = ref([
  {
    id: 'hg38-ucsc-gene-annotation-chromatin-interactions',
    name: 'UCSC Gene annotation',
    label: 'UCSC Gene annotation',
    type: 'GeneTrack',
    url: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/annotation/hg38/UCSC_gene_annotation_hg38.srt.reformat.txt.gz'
  },
  {
    id: 'meta domain',
    name: 'Meta domain insulation',
    label: 'Meta insulation score',
    type: 'MetaDomainTrack',
    url: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/3D_annotation/expresso_domain_boundary_stat_5k.bed.gz'
  },
  {
    id: 'meta compartment',
    name: 'Meta compartment type',
    label: 'Meta compartment type',
    type: 'MetaCompartmentTrack',
    url: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/3D_annotation/compartment_counts.bed.gz'
  },
  {
    id: 'meta loops',
    name: 'Meta loops type',
    label: 'Meta loops type',
    type: 'DotTrack',
    url: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/3D_annotation/merged_loops_with_counts.bed.gz'
  }

])

let asm_mouse = 
    {
      id: 'mm10_1',
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

const tracks_mouse = ref([
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

const downloadFiles_merged = ref({
  itemCount: 4,
  items: [
    {
      sample_name: 'Domain boundary Meta Track',
      info: 'Domain insulation score across 1000 Hi-C datasets',
      track_type: 'MetaDomainTrack',
      download_link: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/3D_annotation/expresso_domain_boundary_stat_5k.bed.gz'
    },
    {
      sample_name: 'Compartment Meta Track',
      info: 'Compartment proprotion across 1000 Hi-C datasets',
      track_type: 'MetaCompartmentTrack',
      download_link: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/3D_annotation/compartment_counts.bed.gz'
    },
    {
      sample_name: 'Chromatin Loop Meta Track',
      info: 'Ensembled chromatin loop across 1000 Hi-C datasets',
      track_type: 'DotTrack',
      download_link: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/3D_annotation/merged_loops_with_counts.bed.gz'
    }
  ]
}
)

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