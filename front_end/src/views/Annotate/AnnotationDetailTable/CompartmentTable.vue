<template>
    <div class="flex justify-between">
      <div class="mb-4 flex items-center min-h-[28px]">
        <span class="text-sm font-medium text-gray-900 dark:text-white mr-3">
          Showing {{ offset + 1 }} to {{ offset + pageSize }} cell types of {{ itemCount }} in total.
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
        :data="dataRef"
        :pagination="paginationReactive"
        @update:page="handlePageChange"
      />
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, computed, onMounted, watch, h } from 'vue'
  import { useRouter } from 'vue-router'
  import type { DataTableColumns } from 'naive-ui'
  
  // Router instance
  const router = useRouter()
  
  // Props
  const props = defineProps({
    id: {
      type: String,
      required: false
    },
    gene_id: {
      type: String,
      required: false
    }
  })
  
  // States
  const loadingRef = ref(false)
  const dataRef = ref([])
  const currentPage = ref(1)
  const pageSize = ref(10)
  const itemCount = ref(0)
  const typeValue = ref('')
  
  // Pagination
  const paginationReactive = computed(() => ({
    page: currentPage.value,
    pageCount: Math.ceil(itemCount.value / pageSize.value),
    pageSize: pageSize.value,
    itemCount: itemCount.value
  }))
  
  // Offset computation
  const offset = computed(() => {
    return (currentPage.value - 1) * pageSize.value
  })
  
  // Type filter
  const typeFilter = [
    { value: 'A', label: 'A compartment' },
    { value: 'B', label: 'B compartment' },
    { value: '', label: 'All' }
  ]
  
  // Columns definition
  const columns: DataTableColumns = [
    {
      title: 'Sample Id',
      key: 'sample_name',
      render: (row) =>
        h(
          'a',
          {
            href: 'javascript:void(0);',
            onClick: () => router.push(`/sample/${row.sample_name}`),
            style: { color: 'blue', textDecoration: 'underline', cursor: 'pointer' }
          },
          row.sample_name
        )
    },
    {
      title: 'Compartment',
      key: 'compartment',
      render: (row) => {
        const isPositive = row.value > 0
        const color = isPositive ? '#00B27B' : '#FF0156'
        const label = isPositive ? 'A' : 'B'
        return h(
          'div',
          {
            style: {
              backgroundColor: color,
              width: '20px',
              height: '20px',
              borderRadius: '50%',
              display: 'inline-block',
              textAlign: 'center',
              lineHeight: '20px',
              color: '#fff'
            }
          },
          label
        )
      }
    },
    {
      title: 'E1 Value',
      key: 'value'
    },
    {
      title: 'Action',
      key: 'action',
      render: (row) =>
        h(
          'n-button',
          {
            type: 'primary',
            size: 'small',
            onClick: () => handleActionClick(row)
          },
          'Click Me'
        )
    }
  ]
  
  // Methods
  const handlePageChange = (page: number) => {
    currentPage.value = page
    fetchData()
  }
  
  const handleActionClick = (row: any) => {
    console.log('Button clicked! Row data:', row)
    alert(`Action triggered for Sample: ${row.sample_name}`)
  }
  
  // Generate fake data
  const generateFakeData = (count: number) => {
    const fakeData = []
    for (let i = 0; i < count; i++) {
      fakeData.push({
        sample_name: `Sample_${i + 1}`,
        compartment: i % 2 === 0 ? 'A' : 'B',
        value: (Math.random() * 2 - 1).toFixed(2)
      })
    }
    return fakeData
  }
  
  // Fetch data
  const fetchData = () => {
    loadingRef.value = true
    setTimeout(() => {
      const fakeData = generateFakeData(50)
      dataRef.value = fakeData.slice(offset.value, offset.value + pageSize.value)
      itemCount.value = fakeData.length
      loadingRef.value = false
    }, 500)
  }
  
  // Watchers
  watch(() => typeValue.value, fetchData)
  
  // On mounted
  onMounted(fetchData)
  </script>