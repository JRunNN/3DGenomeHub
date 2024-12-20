<template>
    <!-- <n-text>Sample {{ props.id }} has {{ totalStripeNo }} stripes</n-text> -->

    <div class="flex justify-between">
        <div class="mb-4 flex items-center min-h-[28px]">
            <span class="text-sm font-medium text-gray-900 dark:text-white mr-3 flex-shrink-0">
                Showing {{ offset + 1 }} to {{ itemCount < offset + 1 + pageSize ? itemCount:  offset + 1 + pageSize }}
                datasets of {{ itemCount }} in
                total.
            </span>
        </div>
        <div class="mb-4 flex items-center">

       
        </div>
    </div>
    <div class="gap-3">
        <n-data-table ref="table" v-if="dataRef" :bordered="false" :columns="columns"  :data="dataRef"
            :pagination="paginationReactive" />
    </div>
</template>
<script setup lang="ts">
import { ref, onMounted, reactive, h, watch, computed, defineAsyncComponent, nextTick } from 'vue'

import type { DataTableColumns } from 'naive-ui'
import axios from 'axios';
import { useRouter } from "vue-router";
import { NCard, NDataTable, NSpace, NRadioGroup, NRadioButton } from "naive-ui";
import { useLoadingBar } from 'naive-ui'
import { useThemeStore } from "@/stores/theme"

const router = useRouter()

const props = defineProps({
    downloadFiles: {
    type: Object,
    required: true
  }}
)

const themeStore = useThemeStore()

const style = computed<{ [key: string]: any }>(() => themeStore.style)


const loadingBar = useLoadingBar()
const loadingRef = ref(true)

const dataRef = ref(null)

const currentPage = ref(1)
const pageSize = ref(10)
const itemCount = ref(0)
const paginationReactive = reactive({
    page: 1,
    pageCount: 1,
    pageSize: 10,
    itemCount: itemCount.value,
    onChange: (page: number) => {
        paginationReactive.page = page
      },
    onUpdatePageSize: (pageSize: number) => {
        paginationReactive.pageSize = pageSize
        paginationReactive.page = 1
      }
})
const table=ref(null)

function hexToRGBA(hex, opacity) {
  let r = parseInt(hex.slice(1, 3), 16);
  let g = parseInt(hex.slice(3, 5), 16);
  let b = parseInt(hex.slice(5, 7), 16);
  return `rgba(${r}, ${g}, ${b}, ${opacity})`;
}

const createGeneLink = (geneString, row) => {
    if (geneString === 'NA') {
        return geneString;
    }
    const geneNames = geneString.split(',');
    const geneLinks = geneNames.map((genename) => (
        h('a', {
            key: genename,
            href: `javascript:void(0);`,
            onClick: () => { router.push(`/gene/${genename.trim()}`); },
            style: {
                color: 'blue',
                textDecoration: 'underline',
                cursor: 'pointer'
            },
            'data-tooltip': geneNames.join('  ,   ')
        }, genename)
    ));

    return geneLinks
};


const columns = [
  // {
  //   type: 'expand',
  //   expandable: (rowData) => true,
  //   renderExpand: (rowData) => {
  //     return 'sss'
  //   }
  // },
  {
    title: 'ID',
    key: 'id',
    width: 160
  },
  {
    title: 'Body Sites',
    key: 'tissue',
    width: 230,
    sortOrder: false,
    sorter: 'default',
    render(row) {
      // Define a mapping from tissue names to color codes
      const tissueColors = {
        'Adrenal gland': '#F6EC65',
        'Arthritis': '#E83F19',
        'Bladder': '#3C5EAA',
        'Blood': '#BD2321',
        'Bone': '#F2F2F3',
        'Brain': '#F6BBA7',
        'Breast': '#8B6679',
        'Bronchus': '#EE7E87',
        'Colon': '#F7C96B',
        'Embryo': '#99D6EF',
        'Eye': '#8D1C27',
        'Heart': '#EC6822',
        'Kidney': '#697F15',
        'Liver': '#8B5241',
        'Lung': '#F7D774',
        'Lymph': '#06763B',
        'Muscle tissue': '#F7BE92',
        'Nerve': '#F5E72E',
        'Ovary': '#B35CA0',
        'Pancreas': '#DFDE86',
        'Pharynx': '#FDE5C8',
        'Placenta': '#E83F29',
        'Prostate gland': '#ACC7E8',
        'Skin': '#854922',
        'Soft tissue': '#DBA883',
        'Spleen': '#781E4E',
        'Stomach': '#F5AF32',
        'Testis': '#788CA4',
        'Thymus': '#92C976',
        'Thyroid gland': '#F6B59C',
        'Uterus': '#EABDD7',
        'Vagina': '#DE4E96',
        'Vessel': '#4B83C4'
      };

      // Get the color for the current row's tissue
      const baseColor = tissueColors[row.tissue] || '#CCCCCC'; // Default to light grey if tissue is not listed
      const backgroundColor = hexToRGBA(baseColor, 0.2); // Set opacity to 20%

      // Return a div element with styled background color and text color
      return h('div', {
        style: {
          backgroundColor: backgroundColor,
          // color: baseColor,
          padding: '4px 8px',
          borderRadius: '4px',
          textAlign: 'center',
          width: '60%', // Adjust width as needed
        }
      }, row.tissue);
    }
  },
  {
    title: 'Health Status',
    key: 'health_status',
    width: 200,
    sortOrder: false,
    sorter: 'default',
  },
  {
    title: 'Biomaterial',
    key: 'biomaterial_type',
    // width: 120,
    sorter: 'default',
    sortOrder: false
  },
  {
    title: 'Assay',
    key: 'data_type',
    // width: 100,
    sortOrder: false,
    sorter: 'default',
    render(row) {
      const assayColor = {
        'ChIA-PET': '#6267FF',
        'HiChIP': '#FF61C9',
        'in-situ Hi-C': '#00B27B',
        'intact Hi-C': '#00B27B',
        // 'ATAC-seq': 'blue'
      };

      const color = assayColor[row.data_type] || 'grey';

      return h('div', {
        style: {
          backgroundColor: color,
          width: '10px',
          height: '10px',
          borderRadius: '50%',
          display: 'inline-block',
          marginLeft: '5px'
        }
      })

    }
  },
  {
    title: 'View',
    key: 'visualize',
    render: function (row) {
      return h('svg', {
        class: 'w-5 h-5 text-grey-500 hover:text-blue-500 cursor-pointer transition-colors duration-300',
        'aria-hidden': 'true',
        xmlns: 'http://www.w3.org/2000/svg',
        fill: 'none',
        viewBox: '0 0 18 18',
        onClick: (e) => { handleClick(row.id) }
      }, [
        h('path', {
          stroke: 'currentColor',
          'stroke-linecap': 'round',
          'stroke-linejoin': 'round',
          'stroke-width': '2',
          d: 'M15 11v4.833A1.166 1.166 0 0 1 13.833 17H2.167A1.167 1.167 0 0 1 1 15.833V4.167A1.166 1.166 0 0 1 2.167 3h4.618m4.447-2H17v5.768M9.111 8.889l7.778-7.778'
        })
      ]);
    }
  }
]

const assayColor = [
  {
    name: "Hi-C",
    color: '#00B27B'
  },
  {
    name: 'ChIA-PET',
    color: '#6267FF'
  },
  {
    name: 'HiChIP',
    color: '#FF61C9'
  }//,
  // {
  //   name: 'RNA-seq',
  //   color: '#FFB600'
  // },
  // {
  //   name: 'ChIP-seq',
  //   color: '#FF0156'
  // },
  // {
  //   name: 'ATAC-seq',
  //   color: 'blue'
  // }
]

const offset = computed(() => {
    return (currentPage.value - 1) * pageSize.value
})

onMounted(() => {

    // fnGetMenudata()
    watch(() => props.downloadFiles, (newValue) => {
        if(newValue && newValue.items) {
        console.log(newValue)
        itemCount.value = newValue.itemCount
        dataRef.value = newValue.items

        }
    }, { immediate: true, deep: true })


})
</script>
