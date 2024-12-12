<template>
    <div class="page page-wrapped page-mobile-full flex flex-col page-without-footer">
        <SegmentedPage @mounted="setCtx" hide-menu-btn enable-resize :use-main-scroll="true">
            <template #sidebar-header>
                <div class="compose-btn-wrap">
                    <n-button strong secondary type="primary" size="large">Documentation</n-button>
                </div>
            </template>
            <template #sidebar-content>
                <n-menu class="folders-list" v-model:value="showApiDoc" :options="menuOptions" 
                :default-expanded-keys="defaultExpandedKeys"
                />


            </template>

            <template #main-toolbar>
            </template>
            <template #main-content>
                <component :is="currentCardComponent" />
            </template>
        </SegmentedPage>
    </div>
</template>

<script setup lang="ts">
import { NButton, NMenu, type MenuOption } from "naive-ui"
import { ref, onMounted, defineAsyncComponent, computed } from "vue"
import { useHideLayoutFooter } from "@/composables/useHideLayoutFooter"
import SegmentedPage, { type CtxSegmentedPage } from "@/components/common/SegmentedPage.vue"

import { NCard, NSpace, NCode, NTag } from "naive-ui"

const showApiDoc = ref('Overview')
const ctxPage = ref<CtxSegmentedPage | null>(null)
import APICodeExample from "./APICodeExample.vue";

const loadList = ref(false)

// Import individual components
const Overview = defineAsyncComponent(() => import('./Overview.vue'));
const DataPipeline = defineAsyncComponent(() => import('./DataPipeline.vue'));
const Usage = defineAsyncComponent(() => import('./Usage.vue'));
// const apiLabels = [
//     {
//         title: 'Search sample using id'
//     },
//     {
//         title: 'Search samples using attributes'
//     },
//     {
//         title: 'Search files using id'
//     },
//     {
//         title: 'Download files using id and file type'
//     }
// ]


const menuOptions: MenuOption[] = [
    {
        label: 'Overview',
        key: 'Overview'
    },
    {
        label: 'Data processing pipeline',
        key: 'DataPipeline'
    },
    {
        label: 'Usage',
        key: 'Usage'
    }
    // {
    //     label: 'Search Metadata',
    //     key: 'SearchMetadata',
    //     children: [
    //     {
    //         label: 'Search a sample using id',
    //         key: 'SearchLibraryById'
    //     },
        // {
        //     label: 'Search a list of samples using attributes',
        //     key: 'SearchLibrariesByAttr'
        // },
        // {
        //     label: 'Search files associated with a sample',
        //     key: 'SearchFilesById'
        // }
        // ]
    // },
    // {
    //     label: 'Search 3D genomic data features',
    //     key: 'SearchFeatures',
    //     children: [
    //         {
    //             label: 'Search Compartments',
    //             key: 'SearchCompartments'
    //         },
    //         {
    //             label: 'Search Topologically Associated Domains',
    //             key: 'SearchTADs'
    //         },
    //         {
    //             label: 'Search Stripes',
    //             key: 'SearchStripes'
    //         },
    //         {
    //             label: 'Search chromatin loops',
    //             key: 'SearchLoops'
    //         },
    //     ]
    // },
    // {
    //     label: 'Search genes',
    //     key: 'SearchGenes',
    //     children: [
    //         {
    //             label: 'Search Genes compartment E1 scores',
    //             key: 'SearchGeneCompartment'
    //         },
    //         {
    //             label: 'Search Boundary and Domain genes',
    //             key: 'SearchBoundaryDomainGenes'
    //         },
    //         {
    //             label: 'Search genes with Stripes',
    //             key: 'SearchGeneStripes'
    //         },
    //         {
    //             label: 'Search genes with chromatin loops',
    //             key: 'SearchGeneLoops'
    //         },
    //     ]
    // },
    // {
    //     label: 'Download Files',
    //     key: 'DownloadFiles',
    //     children: [
    //     {
    //         label: 'Download files associated with a sample',
    //         key: 'DownloadFiles'
    //     }
    //     ]
    // },

]
const defaultExpandedKeys = ref([
    'DataPipeline',
])

const componentMap = {
    Overview: Overview,
  DataPipeline: DataPipeline,
  Usage: Usage
};

const currentCardComponent = computed(() => componentMap[showApiDoc.value]);

function setCtx(ctx: CtxSegmentedPage) {
    ctxPage.value = ctx
}

onMounted(() => {
    setTimeout(() => {
        loadList.value = true
    }, 100)
})

// :has() CSS relational pseudo-class not yet supported by Firefox
// (https://caniuse.com/css-has)
// at the moment this worker around permit to hide Layout Footer
useHideLayoutFooter()
</script>

<style lang="scss" scoped>
.page {
    .compose-btn-wrap {
        width: 100%;

        :deep() {
            .n-button {
                width: 100%;
            }
        }
    }

    .folders-list {
        margin-bottom: 20px;

        :deep() {
            .n-menu-item-content::before {
                left: 0;
                right: 0;
            }
        }
    }

    .sidebar-toggler,
    .new-btn {
        display: none;
    }

    @media (max-width: 700px) {

        .sidebar-toggler,
        .new-btn {
            display: flex;
        }
    }
}
</style>
