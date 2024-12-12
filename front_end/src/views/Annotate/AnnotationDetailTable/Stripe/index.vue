<template>
    <div class="mx-auto max-w-8xl">

  
      <div class="flex grow mt-6">
        <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
          <CardActions
            :expand="expand"
            :isExpand="isExpand"
            :reload="reload"
            class="h-full"
            title="Search the Stripe Atlas"
            :segmented="{ content: true, footer: true }"
          >
            <template #header>
              <n-h3 prefix="bar" align-text>Search the Stripe Atlas</n-h3>
            </template>
            <template #default>
              <!-- <SearchFilters
                :chipseq-value="chipseqValue"
                :chipseq-filter="chipseqFilter"
                :on-gene-submit="fetchGene"
                :on-biosample-submit="fetchBiosample"
                :on-reset="ResetTableData"
              /> -->
              <div class="gap-3">
                <n-data-table
                  remote
                  :bordered="false"
                  :columns="columns"
                  :loading="loadingRef"
                  :data="fakeData"
                  :pagination="paginationReactive"
                  @update:page="handlePageChange"
                  @update:sorter="handleSorterChange"
                />
              </div>
            </template>
          </CardActions>
        </CardWrapper>
      </div>
  
      <div class="flex grow mt-6">
        <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
          <CardActions
            :expand="expand"
            :isExpand="isExpand"
            :reload="reload"
            class="h-full"
            title="View Stripes in the Browser"
            :segmented="{ content: true, footer: true }"
          >
            <template #header>
              <n-h3 prefix="bar" align-text>View Stripes in the Browser</n-h3>
            </template>
            <template #default>
              <div>
                <span strong="false">{{ viewingStripes || 'No Stripes selected' }}</span>
                <component
                  :is="VueActiveBrowser"
                  v-if="VueActiveBrowser"
                  :key="vueActiveBrowserKey"
                  :id="id"
                  :assembly="asm"
                  :tracksInfo="tracksInfo"
                />
              </div>
            </template>
          </CardActions>
        </CardWrapper>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, computed, watch, defineAsyncComponent, nextTick } from "vue";
  import { useRouter } from "vue-router";
  import { useLoadingBar } from "naive-ui";
  import { NDataTable, NSpace, NRadioGroup, NRadioButton } from "naive-ui";
  import chromBands from "@/data/chromBands.json";
//   import SearchFilters from "@/components/SearchFilters.vue"; // Extracted filter component
  
  const router = useRouter();
  const loadingRef = ref(false);
  const viewingStripes = ref("");
  const VueActiveBrowser = ref(null);
  const vueActiveBrowserKey = ref(0);
  const chipseqValue = ref("h3k27ac");
  const fakeData = ref([
    {
      chrom1: "chr1",
      pos1: 100000,
      pos2: 200000,
      chrom2: "chr1",
      pos3: 300000,
      pos4: 400000,
      id: "GSM123456",
      pvalue: 0.01,
      gene_anno_1: "GeneA",
      gene_anno_2: "GeneB",
      chipseq_anno_1: "H3K27ac",
      chipseq_anno_2: "CTCF",
    },
    // Add more fake rows here
  ]);
  
  const stripeExamples = [
    { label: "MYC in Gastric cancer; GSM3333325", gene: "MYC", sample: "GSM3333325" },
    { label: "MYC in Breast cancer; GSM7900696", gene: "MYC", sample: "GSM7900696" },
    { label: "MYC in Bladder cancer; GSM4453814", gene: "MYC", sample: "GSM4453814" },
  ];
  
  const summaryList = [
    "We build a comprehensive Stripe Atlas consisting of 1,891,697 stripes from EXPRESSO Hi-C datasets.",
    "250,650 were further annotated by H3K27ac / H3K37me3 / CTCF ChIP-seq peaks.",
    "Click in Visualize column to access a dedicated genome browser view for each stripe.",
  ];
  
  const chipseqFilter = [
    { value: "h3k27ac", label: "H3K27ac" },
    { value: "h3k27me3", label: "H3K27me3" },
    { value: "ctcf", label: "CTCF" },
  ];
  
  const columns = [
    { title: "Chrom1", key: "chrom1" },
    { title: "Pos1", key: "pos1" },
    { title: "Pos2", key: "pos2" },
    { title: "Chrom2", key: "chrom2" },
    { title: "Pos3", key: "pos3" },
    { title: "Pos4", key: "pos4" },
    { title: "ID", key: "id" },
    { title: "P-value", key: "pvalue" },
    { title: "Gene Annotation 1", key: "gene_anno_1" },
    { title: "Gene Annotation 2", key: "gene_anno_2" },
    { title: "ChIP-seq Annotation 1", key: "chipseq_anno_1" },
    { title: "ChIP-seq Annotation 2", key: "chipseq_anno_2" },
  ];
  
  function SearchStripeExample(gene, sample) {
    console.log(`Searching for gene: ${gene}, sample: ${sample}`);
  }
  
  function ResetTableData() {
    viewingStripes.value = "";
    console.log("Table data reset.");
  }
  </script>
  
  <style scoped>
  .active {
    background-color: #e2e9ec;
    color: white;
  }
  </style>