<script setup lang="ts">
import { onMounted, h, ref, reactive } from 'vue'
import axios from 'axios';
import type {DataTableColumns} from 'naive-ui'
import {NButton, NTag, useMessage} from "naive-ui";
import {useRouter} from "vue-router";

const pagesize = 10
const type = 'chromatin-interactions'
const loadingRef = ref(true)
const dataRef = ref([])
const itemCount = ref(0)
const paginationReactive = reactive({
      page: 2,
      pageCount: 1,
      pageSize: 10,
      itemCount: 0
    })

const fnGetData = (num) => {
    axios.get('http://127.0.0.1:8000' + '/search', {
        responseType: 'json',
        params: {
            type: type,
            gene: 'Transcript_68963',
            pagesize: pagesize,
            page: num,
        }
    })
        .then(res => {
          console.log('data recevied')
          dataRef.value = res.data.data
          itemCount.value = res.data.itemCount
          // console.log(dataRef.data)
          paginationReactive.pageCount = Math.ceil(itemCount.value / pagesize)
          paginationReactive.itemCount = itemCount.value
          loadingRef.value = false

        }).catch(err => {
          console.log('error happened')
            console.log(err);
        })
}

const router = useRouter()

const exportOptions = [
  {
    type: 'menu',
    label: 'tsv',
    key: 'tsv',
  },
  {
    type: 'menu',
    label: 'csv',
    key: 'csv',
  }
];

const handleExport = () => {
  console.log('export')
}

type RowData = {
  id: number;
  chrom1: string;
  start1: number;
  end1: number;
  chrom2: string;
  start2: number;
  end2: number;
  anchor1: string;
  anchor2: string;
  cellType: string;
}

const createColumns = ({
                         sendMail
                       }: {
  sendMail: (rowData: RowData) => void
}): DataTableColumns<RowData> => {
  return [
    {
      title: 'Id',
      key: 'id',
      defaultSortOrder: 'ascend',
      sorter: 'default'
    },
    {
      title: 'chrom1',
      key: 'chrom1',
      sorter: 'default'
    },
    {
      title: 'start1',
      key: 'start1',
      sorter: 'default'
    },
    {
      title: 'end1',
      key: 'end1',
      sorter: 'default'
    },
    {
      title: 'chrom2',
      key: 'chrom2',
      sorter: 'default'
    },
    {
      title: 'start2',
      key: 'start2',
      sorter: 'default'
    },
    {
      title: 'end2',
      key: 'end2',
      sorter: 'default'
    },
    {
      title: 'anchor1',
      key: 'anchor1',
      sorter: 'default'
    },
    {
      title: 'anchor2',
      key: 'anchor2',
      sorter: 'default'
    },
    {
      title: 'Action',
      key: 'actions',
      render(row) {
        return h(
            NButton,
            {
              size: 'small',
              onClick: () => sendMail(row)
            },
            {default: () => 'Send Email'}
        )
      }
    }
  ]
}

const message = useMessage()
// const data = dataRef()
const columns = createColumns({
  sendMail(rowData) {
    message.info('open page ' + rowData.id)
    router.push({path: '/celltype/' + rowData.id})
  }
})

// const pagination = {
//   pageSize: 10
// }

onMounted(() => {
    fnGetData(1)
})
</script>
<template>
     <n-card :bordered="false">

    <div class="flex justify-between">
      <!-- top left section -->
      <div class="flex items-center	justify-start	">
        <!-- slot -->
        <form>
          <label class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
                 for="default-search">Search</label>
          <div class="relative">
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg aria-hidden="true" class="w-4 h-4 text-gray-500 dark:text-gray-400"
                   fill="none" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" stroke="currentColor" stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"/>
              </svg>
            </div>
            <input id="default-search"
                   class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                   placeholder="Search Mockups, Logos..."
                   required type="search">
            <button
                class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                type="submit">
              Search
            </button>
          </div>
        </form>
      </div>

      <!-- top right section -->
      <div class="flex justify-end flex-1 ">
        <!-- slot -->
        <n-dropdown
            :options="exportOptions"
            placement="bottom-start"
            size="medium"
            trigger="click"
            @select="handleExport"
        >
          <n-button>Export</n-button>
        </n-dropdown>
      </div>
    </div>

    <!-- table body -->
    <div class="mt-4">
      <n-data-table
          remote
          :bordered="false"
          :columns="columns"
          :loading="loadingRef"
          :data="dataRef"
          :pagination="paginationReactive"
          :single-line="false"
      />
    </div>
  </n-card>
</template>
<style></style>