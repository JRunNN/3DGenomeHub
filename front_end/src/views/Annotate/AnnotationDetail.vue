<template>
  <div class="p-4">
    <div v-if="state === 'processing'" class="space-y-4">
      <!-- Processing Header -->
      <div class="progress-header bg-white p-4 rounded-lg shadow">
        <h2 class="text-xl font-bold">Processing Status</h2>
        <div class="text-sm text-gray-500">Started: {{ startTime }}</div>
        <div class="text-sm text-gray-500">Elapsed Time: {{ elapsedTime }}</div>
      </div>

      <!-- Progress Bar -->
      <div class="progress-bar-container bg-white p-4 rounded-lg shadow">
        <n-progress type="line" :percentage="progressBarContent.percent" processing :height="40" :border-radius="8" />
        <div class="mt-2 text-center font-medium">
          {{ progressBarContent.notation }}
        </div>
        <div class="mt-1 text-sm text-gray-500 text-center">
          Current Step: {{ progressBarContent.current_step }}
        </div>
      </div>

      <!-- Processing Steps -->
      <div class="steps-container bg-white p-4 rounded-lg shadow">
        <h3 class="text-lg font-semibold mb-4">Processing Steps</h3>
        <div class="space-y-2">
          <div v-for="(step, index) in processingSteps" :key="index" class="step-item flex items-center p-2 rounded"
            :class="{
              'bg-green-50': step.completed,
              'bg-blue-50': step.current,
              'bg-gray-50': !step.completed && !step.current
            }">
            <!-- Step Icon -->
            <!-- <div class="step-icon mr-3">
              <n-icon v-if="step.completed" class="text-green-500">
                <CheckCircleOutlined />
              </n-icon>
              <n-icon v-else-if="step.current" class="text-blue-500">
                <LoadingOutlined />
              </n-icon>
              <n-icon v-else class="text-gray-400">
                <ClockCircleOutlined />
              </n-icon>
            </div> -->
            <!-- Step Content -->
            <div class="step-content flex-1">
              <div class="font-medium" :class="{
                'text-green-700': step.completed,
                'text-blue-700': step.current,
                'text-gray-500': !step.completed && !step.current
              }">
                {{ step.name }}
              </div>
              <div class="text-sm text-gray-500" v-if="step.detail">
                {{ step.detail }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Success State -->
    <div v-else-if="state === 'success'" class="space-y-4">
      <div class="success-header bg-white p-4 rounded-lg shadow">
        <div class="flex items-center">
          <!-- <n-icon class="text-green-500 text-2xl mr-2">
            <CheckCircleOutlined />
          </n-icon> -->
          <h2 class="text-xl font-bold text-green-700">Processing Completed</h2>
        </div>
        <div class="text-sm text-gray-500 mt-2 leading-normal">
          Task ID: {{ route.params.taskId }} <br>
          Started: {{ startTime }}<br>
          Completed: {{ endTime }}<br>
          Total Time: {{ processingTime }}
        </div>
      </div>

      <!-- Results Section -->
      <div class="result-content bg-white p-4 rounded-lg shadow">
        <h3 class="text-lg font-semibold mb-4">Processing Results</h3>
        <div class="space-y-4">
          <!-- Summary Stats -->
          <!-- <div class="summary-stats grid grid-cols-2 gap-4">
            <div v-for="(stat, key) in resultSummary" 
                 :key="key" 
                 class="stat-item p-3 bg-gray-50 rounded">
              <div class="text-sm text-gray-500">{{ key }}</div>
              <div class="font-medium">{{ stat }}</div>
            </div>
          </div> -->

          <!-- Detailed Results -->
          <!-- <div class="detailed-results">
            <n-collapse>
              <n-collapse-item title="Raw Results" name="raw">
                <pre class="bg-gray-50 p-4 rounded overflow-auto">{{ JSON.stringify(result, null, 2) }}</pre>
              </n-collapse-item>
            </n-collapse>
          </div> -->
          <div class="box-bottom">
            <div class="flex flex-col gap-5">
              <!-- <CardCombo5 v-if="isSwitchChartHorizontal" size="large" /> -->
              <!-- <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full w-full">
						<CardExtra6
							class="h-full"
							:expand="expand"
							:is-expand="isExpand"
							:reload="reload"
							show-actions
							show-date
							:min-width="760"
              :processed-data="result.processed_data" 

						/>
					</CardWrapper> -->
            </div>
          </div>
          <!-- <n-data-table
      :columns="columns"
      :data="processedData"
      :pagination="pagination"
      :scroll-x="2000"
      :single-line="false"

      class="custom-table"
    /> -->
          <TableBase :bordered="false" :show-actions="false" :data="testSummaryData" v-model="showSummaryTable" />
        </div>
      </div>
    </div>

    <!-- Error State -->
    <div v-else-if="state === 'error'" class="error-container bg-white p-4 rounded-lg shadow">
      <div class="flex items-center">
        <n-icon class="text-red-500 text-2xl mr-2">
          <CloseCircleOutlined />
        </n-icon>
        <h2 class="text-xl font-bold text-red-700">Processing Error</h2>
      </div>
      <div class="mt-4 p-4 bg-red-50 rounded">
        <div class="text-red-700">{{ error }}</div>
        <div class="mt-2 text-sm text-red-500">
          Time of error: {{ errorTime }}
        </div>
      </div>
      <div class="mt-4">
        <n-button @click="retryProcessing" type="primary">
          Retry Processing
        </n-button>
      </div>
    </div>
  </div>

  <n-modal v-model:show="showDetailTable" preset="card" size="huge">
    <AnnotationDetail></AnnotationDetail>

  </n-modal>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { NButton, NIcon, NProgress, NCollapse, NCollapseItem, useMessage } from 'naive-ui'
// import { CheckCircleOutlined, LoadingOutlined, ClockCircleOutlined, CloseCircleOutlined } from '@vicons/antd'
import axios from 'axios'
// import CardWrapper from '../ResultsSummary/CardWrapper.vue'
// import CardExtra6 from "../ResultsSummary/CardExtra6.vue"

import TableBase from "../ResultsSummary/index.vue"
import AnnotationDetail from '../ResultsDetail/index.vue'
const route = useRoute()
const router = useRouter()
const message = useMessage()

// State management
const state = ref('processing')
const error = ref(null)
const result = ref(null)
const startTime = ref(new Date().toLocaleString())
const endTime = ref(null)
const errorTime = ref(null)

const datatmp = ref(createData())
//const columns =  ref(createCols())
const pagination = ref({
  pageSize: 10
})
const showSummaryTable = ref(true)
//       function createCols() {
//   return [
//     {
//       title: 'Human 3D genome organization',
//       key: '3d_genome',
//       children: [
//         {
//           title: 'Compartment',
//           key: 'compartment'
//         },
//         {
//           title: 'Domain',
//           key: 'domain'
//         },
//         {
//           title: 'Stripe',
//           key: 'stripe'
//         },
//         {
//           title: 'Loop',
//           key: 'loop'
//         }
//       ]
//     },
//     {
//       title: 'Cross-species comparative 3D genome',
//       key: 'comparative_3d',
//       children: [
//         {
//           title: 'Sequence',
//           key: 'sequence'
//         },
//         {
//           title: 'Enhancer',
//           key: 'enhancer_comp'
//         },
//         {
//           title: 'Domain',
//           key: 'domain_comp'
//         },
//         {
//           title: 'Loop',
//           key: 'loop_comp'
//         }
//       ]
//     },
//     {
//       title: 'Cis regulatory landscape',
//       key: 'cis_regulatory',
//       children: [
//         {
//           title: 'Enhancer',
//           key: 'enhancer_cis'
//         },
//         {
//           title: 'Cancer CRE',
//           key: 'cancer_cre'
//         },
//         {
//           title: 'GWAS',
//           key: 'gwas'
//         },
//         {
//           title: 'Eqtl',
//           key: 'eqtl'
//         }
//       ]
//     },
//     {
//       title: 'Cell specific epigenome',
//       key: 'cell_specific',
//       children: [
//         {
//           title: 'scATAC-seq',
//           key: 'scatac_seq'
//         }
//       ]
//     },
//     {
//       title: 'Actions',
//       key: 'actions',
//       width: 100,
//       fixed: 'right'
//     }
//   ]
// }
const showDetailTable = ref(false)


const renderStackedBar = (row) => {
  return h('div', {
    style: {
      width: '100%',
      height: '20px',
      display: 'flex',
      borderRadius: '4px',
      overflow: 'hidden'
    }
  }, [
    // 正值部分（例如：A compartment）
    h('div', {
      style: {
        width: `${row.summary.portions.a_compartment * 100}%`,
        backgroundColor: '#4CAF50',
        transition: 'width 0.3s'
      }
    }),
    // 负值部分（例如：B compartment）
    h('div', {
      style: {
        width: `${(1 - row.summary.portions.a_compartment) * 100}%`,
        backgroundColor: '#F44336',
        transition: 'width 0.3s'
      }
    })
  ])
}

const renderDonut = (row, key) => {
  const value = row.summary.portions[key]
  const size = 24
  const strokeWidth = 4
  const radius = (size - strokeWidth) / 2
  const circumference = 2 * Math.PI * radius
  const dashArray = circumference
  const dashOffset = circumference * (1 - value)

  return h('div', {
    style: {
      width: `${size}px`,
      height: `${size}px`,
      position: 'relative',
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center'
    }
  }, [
    h('svg', {
      width: size,
      height: size,
      viewBox: `0 0 ${size} ${size}`,
      style: {
        transform: 'rotate(-90deg)'
      }
    }, [
      // Background circle
      h('circle', {
        cx: size / 2,
        cy: size / 2,
        r: radius,
        fill: 'none',
        stroke: '#eee',
        'stroke-width': strokeWidth
      }),
      // Progress circle
      h('circle', {
        cx: size / 2,
        cy: size / 2,
        r: radius,
        fill: 'none',
        stroke: '#1890ff',
        'stroke-width': strokeWidth,
        'stroke-dasharray': dashArray,
        'stroke-dashoffset': dashOffset,
        style: {
          transition: 'stroke-dashoffset 0.3s ease'
        }
      })
    ]),
    // Percentage text
    h('span', {
      style: {
        position: 'absolute',
        fontSize: '8px',
        color: '#666'
      }
    }, `${(value * 100).toFixed(0)}%`)
  ])
}


const getRegionSummary =  () => {
  const chromosomes = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6'];
  const data = [];
  
  for (let i = 0; i < 20; i++) {
    const start = Math.floor(Math.random() * 1000000);
    data.push({
      chrom: chromosomes[Math.floor(Math.random() * chromosomes.length)],
      start: start,
      end: start + 10000,
      A_compartment: Math.floor(Math.random() * 100),
      B_compartment: Math.floor(Math.random() * 100),
      NA_compartment: Math.floor(Math.random() * 50),
      IS_lower_bound: Math.random() * 2,
      IS_average: Math.random() * 2 + 2,
      IS_higher_bound: Math.random() * 2 + 4
    });
  }
  return data;
};

const testSummaryData = getRegionSummary()

const createCols = function () {
  const summaryData = ref(null)

  return ([
    {
      title: 'Location',
      key: 'location',
      children: [
        {
          title: 'Chrom',
          key: 'bed_region.chrom',
          minWidth: 10,
          maxWidth: 20,
          width: 60
        },
        {
          title: 'Start',
          key: 'bed_region.start',
          // width: 15
          width: 120
        },
        {
          title: 'End',
          key: 'bed_region.end',
          width: 120
        }
      ]
    },
    // {
    // title: 'Genomic context',
    // key: 'context',
    // children: [
    //   {
    //     title: 'Nearest gene',
    //     key: 'nearest_gene',
    //     minWidth: 10,
    //     maxWidth: 20,
    //     width: 60
    //   },
    //   {
    //     title: 'Nearest gene',
    //     key: 'nearest_gene',
    //     minWidth: 10,
    //     maxWidth: 20,
    //     width: 60
    //   }
    // ]
    // },
    {
      title: 'Human 3D genome organization',
      key: '3d_genome',
      children: [
        {
          title: 'Compartment',
          key: 'compartment',
          width: 120,
          render: (row) => renderStackedBar(row)
        },
        {
          title: 'Domain',
          key: 'domain',
          width: 80,
          render: (row) => renderStackedBar(row)
        },
        {
          title: 'Stripe',
          key: 'stripe',
          width: 60,
          render: (row) => renderDonut(row, 'stripes')
        },
        {
          title: 'Loop',
          key: 'loops',
          width: 60,
          render: (row) => renderDonut(row, 'loops')
        }
      ]
    },
    {
      title: 'Cross-species comparative 3D genome',
      key: 'comparative_3d',
      children: [
        {
          title: 'Sequence',
          key: 'sequence',
          width: 120,
          // render: (row) => renderStackedBar(row)
        },
        {
          title: 'Enhancer',
          key: 'enhancer_comp',
          width: 120,
          // render: (row) => renderStackedBar(row)
        },
        {
          title: 'Domain',
          key: 'domain_comp',
          width: 70,
          render: (row) => renderDonut(row, 'domain_comp')
        },
        {
          title: 'Loop',
          key: 'loop_comp',
          width: 60,
          render: (row) => renderDonut(row, 'loop_comp')
        }
      ]
    },
    {
      title: 'Cis regulatory landscape',
      key: 'cis_regulatory',
      children: [
        {
          title: 'Enhancer',
          key: 'enhancer_cis',
          width: 120,
          // render: (row) => renderStackedBar(row)
        },
      ]
    },
    {
      title: 'Actions',
      key: 'actions',
      fixed: 'right',
      // width: 100,
      // render: () => h('div', { class: 'actions flex items-center justify-end gap-2' }, [
      //   h(NButton, { secondary: true }, {
      //     icon: () => h(Icon, { name: DeleteIcon })
      //   }),
      //   h(NButton, { secondary: true }, {
      //     icon: () => h(Icon, { name: DownloadIcon })
      //   }),
      //   h(NPopselect, {
      //     options: [
      //       { label: 'Share', value: 'Share' },
      //       { label: 'View', value: 'View' }
      //     ]
      //   }, {
      //     default: () => h(NButton, { secondary: true }, {
      //       icon: () => h(Icon, { name: MenuIcon })
      //     })
      //   })
      // ])
    },
  ]
  )
}

const columns = ref(createCols())

function createData() {
  return Array.from({ length: 50 }).map((_, i) => {
    return {
      key: i,
      compartment: `compartment_${i}`,
      domain: `domain_${i}`,
      stripe: `stripe_${i}`,
      loop: `loop_${i}`,
      sequence: `sequence_${i}`,
      enhancer_comp: `enhancer_comp_${i}`,
      domain_comp: `domain_comp_${i}`,
      loop_comp: `loop_comp_${i}`,
      enhancer_cis: `enhancer_cis_${i}`,
      cancer_cre: `cancer_cre_${i}`,
      gwas: `gwas_${i}`,
      eqtl: `eqtl_${i}`,
      scatac_seq: `scatac_seq_${i}`
    }
  })
}

// Progress tracking
const statusCheckInterval = ref(null)
const progressBarContent = ref({
  percent: 0,
  notation: 'Initializing...',
  current_step: 'loading'
})

// Processing steps definition
const processingSteps = ref([
  { name: 'Loading Input Dataset', step_key: 'loading', completed: false, current: true },
  { name: 'Initial Annotation', step_key: 'initial_annotation', completed: false, current: false },
  { name: 'Compartment Profile Analysis', step_key: 'compartment_profile', completed: false, current: false },
  { name: 'Contact Domain Analysis', step_key: 'contact_domain', completed: false, current: false },
  { name: 'Stripe Profile Analysis', step_key: 'stripe_profile', completed: false, current: false },
  { name: 'Chromatin Loop Analysis', step_key: 'chromatin_loop', completed: false, current: false }
])

// Computed properties
const elapsedTime = computed(() => {
  if (!startTime.value) return '0:00'
  const elapsed = new Date() - new Date(startTime.value)
  const minutes = Math.floor(elapsed / 60000)
  const seconds = Math.floor((elapsed % 60000) / 1000)
  return `${minutes}:${seconds.toString().padStart(2, '0')}`
})

const processingTime = computed(() => {
  if (!startTime.value || !endTime.value) return ''
  const elapsed = new Date(endTime.value) - new Date(startTime.value)
  const minutes = Math.floor(elapsed / 60000)
  const seconds = Math.floor((elapsed % 60000) / 1000)
  return `${minutes} minutes ${seconds} seconds`
})

const resultSummary = computed(() => {
  if (!result.value) return {}
  return {
    'Input Type': result.value?.input_type || 'Unknown',
    'Elements Processed': result.value?.element_count || 0,
    'Success Rate': '100%',
    'Processing Time': processingTime.value
  }
})

// Methods
const updateProcessingStep = (currentStep) => {
  if (!currentStep) return;

  console.log('Current step:', currentStep);  // 调试输出

  const stepIndex = processingSteps.value.findIndex(step =>
    step.step_key === currentStep
  )

  console.log('Found step index:', stepIndex);  // 调试输出

  if (stepIndex > -1) {
    processingSteps.value.forEach((step, index) => {
      step.completed = index < stepIndex
      step.current = index === stepIndex
    })
  }
}

const checkTaskStatus = async () => {
  try {
    const response = await axios.get(`http://47.107.91.5:8888/api/annotations/task-info/${route.params.taskId}/`)
    const data = response.data

    console.log('Response data:', data);  // 调试输出

    progressBarContent.value.percent = data.percent || 0
    progressBarContent.value.notation = data.notation || 'Processing...'

    // 更新current_step
    if (data.current_step) {
      progressBarContent.value.current_step = data.current_step
      updateProcessingStep(data.current_step)
    }

    if (data.task_status === 'SUCCESS') {
      state.value = 'success'
      endTime.value = new Date().toLocaleString()
      result.value = data.results
      // 确保最后一个步骤显示为完成
      processingSteps.value.forEach(step => {
        step.completed = true
        step.current = false
      })
      clearInterval(statusCheckInterval.value)
      message.success('Processing completed successfully!')
    } else if (data.task_status === 'FAILURE') {
      state.value = 'error'
      errorTime.value = new Date().toLocaleString()
      error.value = data.error || 'An unknown error occurred'
      clearInterval(statusCheckInterval.value)
      message.error(data.error || 'Processing failed')
    }
  } catch (err) {
    console.error('Error checking task status:', err)
    state.value = 'error'
    errorTime.value = new Date().toLocaleString()
    error.value = err.message
    clearInterval(statusCheckInterval.value)
    message.error('Error checking task status')
  }
}

const retryProcessing = () => {
  state.value = 'processing'
  startTime.value = new Date().toLocaleString()
  error.value = null
  progressBarContent.value = {
    percent: 0,
    notation: 'Initializing...',
    current_step: 'loading'
  }
  processingSteps.value.forEach(step => {
    step.completed = false
    step.current = false
  })
  processingSteps.value[0].current = true
  startStatusCheck()
}

const startStatusCheck = () => {
  checkTaskStatus()
  statusCheckInterval.value = setInterval(checkTaskStatus, 1000)
}

const fetchRegionSummary = async () => {
  try {
    const response = await axios.get('/api/region-summary', {
      params: {
        chrom: route.params.chrom,
        start: route.params.start,
        end: route.params.end
      }
    });

    if (response.data.code === 200) {
      summaryData.value = response.data.data;
    }
  } catch (error) {
    console.error('Error fetching region summary:', error);
    message.error('Failed to fetch region summary data');
  }
};

// Lifecycle hooks
onMounted(() => {
  startTime.value = new Date().toLocaleString()
  startStatusCheck()
  fetchRegionSummary();
})

onUnmounted(() => {
  if (statusCheckInterval.value) {
    clearInterval(statusCheckInterval.value)
  }
})
</script>

<style scoped>
/* .step-item {
  transition: all 0.3s ease;
}

.step-icon {
  transition: all 0.3s ease;
}

.detailed-results pre {
  max-height: 500px;
} */

/* 移除表格单元格的竖直边框 */
.custom-table :deep(.n-data-table-td) {
  border-right: none;
}

/* 修改表头竖直分割线样式 */
.custom-table :deep(.n-data-table-th) {
  /* position: relative; */
  padding: 18px 18px;
  /* background-color: #f5f7fa; */
  border-right: none;
  /* border-bottom: 1px solid #ebeef5; */
}

/* 使用伪元素创建居中的竖直分割线 */
.custom-table :deep(.n-data-table-th::after) {
  content: '';
  position: absolute;
  right: 0;
  /* 计算中间50%的位置 */
  top: 25%;
  height: 50%;
  /* 高度减半 */
  width: 2px;
  background-color: #ebeef5;
}

/* 去掉最后一列表头的分割线 */
.custom-table :deep(.n-data-table-th:last-child::after) {
  /* display: none; */
}

.custom-table :deep(.n-data-table-th[rowspan="2"]:last-child::after) {
  display: none;
}


/* 可选：为不同层级的表头设置不同样式 */
/* .custom-table :deep(.n-data-table-th[rowspan="2"]) {
  font-weight: bold;
  background-color: #f0f2f5;
} */

.custom-table :deep(.n-data-table-th[rowspan="1"][colspan="4"]) {
  /* background-color: #f5f7fa; */
  font-weight: bold;
}

/* 表头文字样式 */
/* .custom-table :deep(.n-data-table-th .n-data-table-th__title) {
  font-size: 14px;
  color: #606266;
} */
</style>