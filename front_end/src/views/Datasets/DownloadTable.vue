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

const createColumns = (): DataTableColumns<RowData> => {
    return [

        // {
        //     title: 'Rank',
        //     key: 'Rank',
        //     width: 50
        // },
        {
            title: 'Sample Name',
            key: 'sample_name',
            width: 160
        },
        {
            title: 'Name',
            key: 'file_name',
            width: 400
        },
        {
            title: 'FIle Type',
            key: 'file_type',
            width: 200
        },
        {
            title: 'File Size',
            key: 'file_size',
            width: 200
        },
        {
            title: 'Download',
            key: 'download_link',
            width: 120,
            render(rowData) {
                let downloadUrl;
                if (rowData.download_link) {
                    downloadUrl = rowData.download_link
                } else {
                    const { sample_name, file_name } = rowData;
                    downloadUrl = `https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/hic/${sample_name}/${file_name}`;
                }
    
                return h(
                    'a',
                    {
                        href: downloadUrl,
                        target: '_blank',
                        download: true,
                        title: 'Download'
                    },
                    h(
                        'svg',
                        {
                            class: 'w-[26px] h-[26px] text-gray-800 dark:text-white',
                            'aria-hidden': 'true',
                            xmlns: 'http://www.w3.org/2000/svg',
                            width: '24',
                            height: '24',
                            fill: 'currentColor',
                            viewBox: '0 0 24 24'
                        },
                        [
                            h('path', {
                                'fill-rule': 'evenodd',
                                d: 'M13 11.15V4a1 1 0 1 0-2 0v7.15L8.78 8.374a1 1 0 1 0-1.56 1.25l4 5a1 1 0 0 0 1.56 0l4-5a1 1 0 1 0-1.56-1.25L13 11.15Z',
                                'clip-rule': 'evenodd'
                            }),
                            h('path', {
                                'fill-rule': 'evenodd',
                                d: 'M9.657 15.874 7.358 13H5a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2h-2.358l-2.3 2.874a3 3 0 0 1-4.685 0ZM17 16a1 1 0 1 0 0 2h.01a1 1 0 1 0 0-2H17Z',
                                'clip-rule': 'evenodd'
                            })
                        ]
                    )
                );
            }
        }
    ]
}
const columns = createColumns()


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
