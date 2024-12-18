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
              placeholder="Search Gene symbol" required v-model="currentGene" @keyup.enter="handleGeneSearch">
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
  <!-- <div class="mt-6">
    <AnnotationDetail></AnnotationDetail>
  </div> -->

  <!-- <div>
    <div :class="['drawer', { open: isDrawerOpen }]">
      <div class="drawer-handle" @click="toggleDrawer">
        <template v-if="!isDrawerOpen">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                  <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 4H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-4m-8-2l8-8m0 0v5m0-5h-5"></path>
                </svg>
              </template>
              <template v-else>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                  <path fill="currentColor" d="M6.4 19L5 17.6l5.6-5.6L5 6.4L6.4 5l5.6 5.6L17.6 5L19 6.4L13.4 12l5.6 5.6l-1.4 1.4l-5.6-5.6z"></path>
                </svg>
              </template>
      </div>
      <div class="drawer-content">
        <AnnotationDetail />
      </div>
    </div>
  </div> -->
<!-- <div class="mt-6">
  <AnnotationDetail :modalData="modalStore.modalData"></AnnotationDetail>
</div> -->

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



  <!-- show loaded tracks -->
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
// import ExpressoVue from "@/assets/js/dist/Expresso.es"
import ExpressoVue from "@/browser/elements/Expresso/ExpressoVue.vue"
import chromBands from '@/data/chromBands.json'
import AutocompleteDialog from '@/components/common/AutocompleteDialog.vue'
import AnnotationDetail from '@/views/ResultsDetail/index.vue'
import DownloadTable from './DownloadTable.vue'
import ExpressoTable from './ExpressoTable.vue'
import { fetchGeneCoord } from './fetchGeneCoord.js'
import { useMessage } from 'naive-ui'
import { useModalStore } from '@/stores/modalStore'
const modalStore = useModalStore()

const showAddTrackModal = ref(false)
const showTracksInfoModal = ref(false)
const currentGene = ref('')
const value = ref(null)
const showDrawer = ref(true)
const isDrawerOpen = ref(false);
const openIcon = "majesticons:open"
// 切换抽屉状态
const toggleDrawer = () => {
  isDrawerOpen.value = !isDrawerOpen.value;
};

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
    start: 65370274,
    end: 65475274
  },
  chromBands: chromBands

}
// chr11:65,370,274-65,475,274

const tracksInfo = ref([
  {
    id: 'hg38-ucsc-gene-annotation-chromatin-interactions',
    name: 'Gene annotation',
    label: 'UCSC Gene annotation',
    type: 'GeneTrack',
    url: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/annotation/hg38/UCSC_gene_annotation_hg38.srt.reformat.txt.gz'
  },
  {
    id: 'meta domain',
    name: 'Meta domain insulation track',
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
  },
  {
    id: 'meta loops2',
    name: 'Meta loops type',
    label: 'Meta loops type',
    type: 'CurvTrack',
    url: 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/3D_annotation/merged_loops_with_counts.bed.gz'
  }
])

  // {
  //   id: 'GWAS Catalog',
  //   "name": "GWAS Catalog",
  //   "label": "GWAS Catalog",
  //   "type": "SnpTrack",
  //   "url": "https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/gwas/Finn_GWAS_srt.txt.gz",

  // },
  // {
  //   id: 'Adipose subcutaneous Eqtl',
  //   "name": "Adipose subcutaneous Eqtl",
  //   "label": "Adipose subcutaneous Eqtl",
  //   "type": "PclsTrack",
  //   "url": "https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/eqtl/Adipose_Subcutaneous.bed.gz",
  //   "style": 'block'
  // }

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
const message = useMessage()

const handleGeneSearch = async () => {
  console.log(currentGene.value)
  if (!currentGene.value) {
    message.warning('Please enter a gene symbol (e.g. NEAT1, GATA4)')
    return
  }

  const result = await fetchGeneCoord(currentGene.value)
  
  if (result.status === 'success') {
    message.success(result.message)
  } else {
    message.error(result.message)
  }
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

/* 抽屉样式 */
.drawer {
  z-index: 10000;
  position: fixed;
  bottom: 75px;
  left: 0;
  width: 100%;
  background-color: #ffffff;
  border-top: 2px solid #ddd;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
  transform: translateY(100%);
  transition: transform 0.3s ease;
}

.drawer.open {
  transform: translateY(0);
}

/* 抽屉内容区域 */
.drawer-content {
  // padding: 20px;
  height: 800px;
  overflow-y: auto;
}

/* 把手样式 */
.drawer-handle {
  position: absolute;
  top: -45px;
  right: -1%;
  transform: translateX(-50%);
  width: 50px;
  height: 80px;
  background-color: #007BFF;
  color: white;
  text-align: center;
  line-height: 30px;
  font-size: 14px;
  border-radius: 15px 15px 0 0;
  cursor: pointer;
  user-select: none;
}
</style>