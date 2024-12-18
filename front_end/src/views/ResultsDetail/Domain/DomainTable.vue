<!-- DomainTable.vue -->
<template>
  <div class="domain-table">
    <div class="flex justify-between">
      <div class="mb-4 flex items-center min-h-[28px]">
        <span class="text-sm font-medium text-gray-900 dark:text-white mr-3">
          Showing {{ offset + 1 }} to {{ offset + pageSize }} domains of {{ itemCount }} in total.
        </span>
      </div>
      <div class="mb-4 flex items-center">
        <n-radio-group v-model:value="typeValue" name="radiobuttongroup">
          <n-radio-button
            v-for="type in typeFilter"
            :key="type.value"
            :value="type.value"
            :label="type.label"
          />
        </n-radio-group>
      </div>
    </div>
    <div>
      <n-data-table
        remote
        :bordered="false"
        :columns="columns"
        :loading="loadingRef"
        :data="displayData"
        :pagination="paginationReactive"
        @update:page="handlePageChange"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch, h } from 'vue'
import { useRouter } from 'vue-router'
import { NRadioGroup, NRadioButton, NButton, NDataTable } from 'naive-ui'
import type { DataTableColumns } from 'naive-ui'

// 定义类型
interface DomainData {
  sample_id: string
  tissue: string
  health_status: string
  chrom: string
  start: number
  end: number
  domain_type: 'TAD' | 'LAD' | 'CTCF'
  score: number
}

interface Props {
  data?: DomainData[]
  loading?: boolean
  pageSize?: number
  onAction?: (row: DomainData) => void
  region?: {
    chrom: string
    start: number
    end: number
  }
}

// Props定义
const props = withDefaults(defineProps<Props>(), {
  data: () => [],
  loading: false,
  pageSize: 10,
  onAction: undefined,
  region: undefined
})

// 状态管理
const router = useRouter()
const loadingRef = ref(props.loading)
const currentPage = ref(1)
const pageSize = ref(props.pageSize)
const typeValue = ref('')

// 计算属性
const displayData = computed(() => {
  let filteredData = props.data
  if (typeValue.value) {
    filteredData = props.data.filter(item => item.domain_type === typeValue.value)
  }
  return filteredData.data.slice(offset.value, offset.value + pageSize.value)
})

const itemCount = computed(() => {
  if (typeValue.value) {
    return props.data.filter(item => item.domain_type === typeValue.value).length
  }
  return props.data.length
})

const offset = computed(() => {
  return (currentPage.value - 1) * pageSize.value
})

const paginationReactive = computed(() => ({
  page: currentPage.value,
  pageCount: Math.ceil(itemCount.value / pageSize.value),
  pageSize: pageSize.value,
  itemCount: itemCount.value
}))

// 常量定义
const typeFilter = [
  { value: 'TAD', label: 'TAD' },
  { value: 'LAD', label: 'LAD' },
  { value: 'CTCF', label: 'CTCF' },
  { value: '', label: 'All' }
]

// 列定义
const columns: DataTableColumns = [
  {
    title: 'Sample Id',
    key: 'sample_id',
    render: (row) => h(
      'a',
      {
        href: 'javascript:void(0);',
        onClick: () => router.push(`/sample/${row.sample_id}`),
        style: { color: 'blue', textDecoration: 'underline', cursor: 'pointer' }
      },
      row.sample_id
    )
  },
  {
    title: 'Tissue',
    key: 'tissue'
  },
  {
    title: 'Health Status',
    key: 'health_status'
  },
  {
    title: 'Location',
    key: 'location',
    render: (row) => `${row.chrom}:${row.start}-${row.end}`
  },
  {
    title: 'Domain Type',
    key: 'domain_type',
    render: (row) => {
      const colorMap = {
        'TAD': '#00B27B',
        'LAD': '#FF0156',
        'CTCF': '#FFA500'
      }
      return h(
        'div',
        {
          style: {
            backgroundColor: colorMap[row.domain_type],
            padding: '2px 8px',
            borderRadius: '12px',
            display: 'inline-block',
            color: '#fff'
          }
        },
        row.domain_type
      )
    }
  },
  {
    title: 'Score',
    key: 'score',
    render: (row) => row.score.toFixed(2)
  },
  {
    title: 'Action',
    key: 'action',
    render: (row) => h(
      NButton,
      {
        type: 'primary',
        size: 'small',
        onClick: () => handleActionClick(row)
      },
      { default: () => 'View Details' }
    )
  }
]

// 方法定义
const handlePageChange = (page: number) => {
  currentPage.value = page
}

const handleActionClick = (row: DomainData) => {
  if (props.onAction) {
    props.onAction(row)
  }
}

// 监听器
watch(() => props.loading, (newVal) => {
  loadingRef.value = newVal
})

// 生命周期
onMounted(() => {
  console.log(props.data)
  if (props.region) {
    console.log(`Showing domain data for region: ${props.region.chrom}:${props.region.start}-${props.region.end}`)
  }
})
</script>

<style scoped>
.domain-table {
  width: 100%;
}
</style>