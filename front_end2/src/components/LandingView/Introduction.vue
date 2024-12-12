<template>
  <n-card class="w-full  relative">
    <div class="w-full px-4 md:px-4 xl:px-4 py-4 lg:py-4 max-w-[1440px] mx-auto">
      <div class="flex justify-center items-center mb-6">
        <img alt="Expresso Logo" class="h-24 mx-auto" src="../../assets/logo_banner.svg">
      </div>
      <p class="mb-3 text-lg text-gray-500 dark:text-gray-400 leading-8">
        <span class="font-semibold text-gray-900 dark:text-white">EXPRESSO (EXPloration of
          Regulatory Epigenome with Spatial and Sequence Observations)</span> is a platform to visualize and explore the
        non-coding mutations contributing to deregulation of cis-regulatory elements. Noncoding regulatory sequences,
        particularly enhancers and promoters, are key determinants of tissue-specific gene
        expression. Multiple mutation types have been reported to disrupt enhancers and promoters and expression of their
        target genes, including single-nucleotide variants (SNVs), small insertion and deletions (indels), and large
        structural variants (SVs). <span class="font-semibold text-gray-900 dark:text-white">EXPRESSO</span> has the
        following features:
      </p>

      <ul class="space-y-2 text-left text-gray-500 dark:text-gray-400 text-lg">
        <li class="flex items-center space-x-3 rtl:space-x-reverse">
          <svg class="flex-shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400" aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 12">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M1 5.917 5.724 10.5 15 1.5" />
          </svg>
          <span>Provided <span
              class="text-lg font-bold bg-gradient-to-r from-pink-500 to-violet-500 bg-clip-text text-transparent">Active
              Browser</span>, a <span
              class="text-lg font-bold bg-gradient-to-r from-pink-500 to-violet-500 bg-clip-text text-transparent">WebGL</span>
            powered genome browser to explore and visualize multi-omics datasets, hosted ~ <span
              class="text-blue-600">700</span> processed files on the cloud.</span>
        </li>
        <li class="flex items-center space-x-3 rtl:space-x-reverse">
          <svg class="flex-shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400" aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 12">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M1 5.917 5.724 10.5 15 1.5" />
          </svg>
          <span>Intergrated <span class="text-blue-600">299,740,245</span> transcription-associated chromatin interactions
            from <span class="text-blue-600">78</span> cancer and <span class="text-blue-600">60</span>
            non-cancer cell types. Each cell line contains individual web page of Active Browser track view and tabular view.
          </span>
        </li>

        <li class="flex items-center space-x-3 rtl:space-x-reverse">
          <svg class="flex-shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400" aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 12">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M1 5.917 5.724 10.5 15 1.5" />
          </svg>
          <span>Annotated <span class="text-blue-600">1,886,345</span> cancer-associated anchor promoter and enhancers
            using ATAC-seq datasets from TCGA, as well as <span class="text-blue-600">1,543,335</span> noncoding somatic
            SNVs and <span class="text-blue-600">37,374</span> SVs
            from from PCWAG whole genome sequencing datasets, to visualize and explore the non-coding mutations contributing to deregulation of cis-regulatory elements.
          </span>
        </li>

        <li class="flex items-center space-x-3 rtl:space-x-reverse">
          <svg class="flex-shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400" aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 12">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M1 5.917 5.724 10.5 15 1.5" />
          </svg>
          <span>Conduct cloud-based annotation of user-uploaded chromatin loops using public chromatin interactions and open chromatin regions.
          </span>
        </li>
      </ul>
    </div>
  </n-card>

  <section class="bg-white dark:bg-gray-900 mt-6">
    <div
      class="items-center py-]\
      px-6 mx-auto max-w-screen-xl lg:grid xl:grid-cols-3 lg:gap-8 xl:gap-24 sm:py-6 lg:px-6">
      <div class="mb-8 lg:mb-0">
        <h2 class="mb-4 text-3xl tracking-tight font-extrabold text-gray-900 dark:text-white">A database and api service for transcription associated chromatin interactions</h2>
        <p class="mb-4 text-gray-500 sm:text-xl dark:text-gray-400">Host ~664 3D genomic datasets of various data types.</p>
        <!-- <a href="#"
          class="inline-flex items-center text-lg font-medium text-primary-600 hover:text-primary-800 dark:text-primary-500 dark:hover:text-primary-700">
          Learn more
          <svg class="ml-1 w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
              clip-rule="evenodd"></path>
          </svg>
        </a> -->
      </div>
      <div class="col-span-2 space-y-8 md:grid md:grid-cols-2 md:gap-12 md:space-y-0">
        <CellTypeSummaryChart />
        <ChromatinInteractionSummaryChart />
        <NoncodingMutationChart />
        <CloudDatasetChart />
      </div>
    </div>
  </section>

  <section class="bg-white dark:bg-gray-900 mt-6">
    <div
      class="items-center py-4 px-4 mx-auto max-w-screen-xl lg:grid xl:grid-cols-2 lg:gap-4 xl:gap-12 sm:py-8 lg:px-3">
      <div class="col-span-1 md:grid-cols-1 md:gap-0 md:space-y-0">
        <CancerBodyMap />
      </div>
      <div class="mb-8 lg:mb-0">
        <h2 class="mb-4 text-3xl tracking-tight font-extrabold text-gray-900 dark:text-white">Noncoding somatic mutatoins
          disrupting chromatin interactions</h2>
        <p class="mb-4 text-gray-500 sm:text-xl dark:text-gray-400">Diverse noncoding mutations contribute to deregulation
          of cis-regulatory elements in 9 cancer types.</p>
          <ul role="list" class="pt-8 my-7 space-y-5 border-t border-gray-200 dark:border-gray-700">
          <li class="flex space-x-3">
            <!-- Icon -->
            <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clip-rule="evenodd"></path>
            </svg>
            <span class="text-base font-medium leading-tight text-gray-900 dark:text-white">Identify cancer-associated chromatin interactions in nine cancer types</span>
          </li>
          <li class="flex space-x-3">
            <!-- Icon -->
            <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clip-rule="evenodd"></path>
            </svg>
            <span class="text-base font-medium leading-tight text-gray-900 dark:text-white">Identify chromatin interactions disrupted by somatic SNVs and SVs</span>
          </li>
          <!-- <li class="flex space-x-3">
            <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clip-rule="evenodd"></path>
            </svg>
            <span class="text-base font-medium leading-tight text-gray-900 dark:text-white">Knowledge
              management</span>
          </li> -->
        </ul>
        <!-- <a href="#"
          class="inline-flex items-center text-lg font-medium text-primary-600 hover:text-primary-800 dark:text-primary-500 dark:hover:text-primary-700">
          Learn more
          <svg class="ml-1 w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
              clip-rule="evenodd"></path>
          </svg>
        </a> -->
      </div>

    </div>
  </section>

  <section class="bg-white dark:bg-gray-900 mt-6 p-6">
    <div class="gap-8 items-center lg:grid lg:grid-cols-2 xl:gap-16">
      <FrontPageCarousel />
      <div class="text-gray-500 sm:text-lg dark:text-gray-400">
        <h2 class="mb-4 text-3xl tracking-tight font-extrabold text-gray-900 dark:text-white">Visulize multi-omics data
          using Active Browser</h2>
        <p class="mb-8 font-light lg:text-xl">Advanced Computational Tool for Interactive Visualization and Exploration
        </p>
        <!-- List -->
        <ul role="list" class="pt-8 my-7 space-y-5 border-t border-gray-200 dark:border-gray-700">
          <li class="flex space-x-3">
            <!-- Icon -->
            <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clip-rule="evenodd"></path>
            </svg>
            <span class="text-base font-medium leading-tight text-gray-900 dark:text-white">Supports both 1D and 3D
              genomic data formats</span>
          </li>
          <li class="flex space-x-3">
            <!-- Icon -->
            <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clip-rule="evenodd"></path>
            </svg>
            <span class="text-base font-medium leading-tight text-gray-900 dark:text-white">Provides synchronized track
              and tabular view</span>
          </li>
          <li class="flex space-x-3">
            <!-- Icon -->
            <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clip-rule="evenodd"></path>
            </svg>
            <span class="text-base font-medium leading-tight text-gray-900 dark:text-white">Optimizes structural
              variation visualization</span>
          </li>
          <li class="flex space-x-3">
            <!-- Icon -->
            <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clip-rule="evenodd"></path>
            </svg>
            <span class="text-base font-medium leading-tight text-gray-900 dark:text-white">Hosts ~ 700 multi-omics
              datasets in the cloud</span>
          </li>
        </ul>
        <p class="font-light lg:text-xl">Fast and interactive exploration of multi-omics datasets, powered by WebGL</p>
      </div>
    </div>
  </section>

  <section class="bg-white dark:bg-gray-900 mt-6 p-10 bordered">
    <div class="gap-8 items-center lg:grid lg:grid-cols-2 xl:gap-16">
      <div class="text-gray-500 sm:text-lg dark:text-gray-400">
        <h2 class="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Annotate user uploaded
          chromatin loops on the cloud</h2>
        <p class="mb-8 font-light lg:text-xl">Annotate chromatin loops using multiple data sources</p>
        <!-- List -->
        <ul role="list" class="pt-8 my-7 space-y-5 border-t border-gray-200 dark:border-gray-700">
          <li class="flex space-x-3">
            <!-- Icon -->
            <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clip-rule="evenodd"></path>
            </svg>
            <span class="text-base font-medium leading-tight text-gray-900 dark:text-white">Annotate chromatin interactions using multi-omics dataset</span>
          </li>
          <li class="flex space-x-3">
            <!-- Icon -->
            <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clip-rule="evenodd"></path>
            </svg>
            <span class="text-base font-medium leading-tight text-gray-900 dark:text-white">Output file ready for visualization or direct download</span>
          </li>
          <li class="flex space-x-3">
            <svg class="flex-shrink-0 w-5 h-5 text-primary-600 dark:text-primary-500" fill="currentColor"
              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clip-rule="evenodd"></path>
            </svg>
            <span class="text-base font-medium leading-tight text-gray-900 dark:text-white"> Shareable link for annotation results</span>
          </li>
        </ul>
        <!-- <p class="mb-8 font-light lg:text-xl">Deliver great service experiences fast - without the
          complexity of traditional ITSM solutions.</p>  -->
      </div>
      <img class="hidden mb-4 w-full lg:mb-0 lg:flex rounded-lg"
        src="../../assets/annotation_banner.png"
        alt="office feature image">
    </div>
  </section>
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import CellTypeSummaryChart from './CellTypeSummaryChart.vue'
import ChromatinInteractionSummaryChart from './ChromatinInteractionSummaryChart.vue'
import FrontPageCarousel from './FrontPageCarousel.vue'
import  CancerBodyMap from '../CancerCRE/CancerBodyMap.vue'
const loading = ref(true);

onMounted(() => {
  loading.value = false
})
</script>