<template>
    <div class="page page-wrapped page-mobile-full flex flex-col page-without-footer">
        <SegmentedPage @mounted="setCtx" hide-menu-btn enable-resize :use-main-scroll="true">
            <template #sidebar-header>
                <div class="compose-btn-wrap">
                    <n-button strong secondary type="primary" size="large">Metadata and file Retrieval API</n-button>
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

const showApiDoc = ref('BaseUrl')
const ctxPage = ref<CtxSegmentedPage | null>(null)
import APICodeExample from "./APICodeExample.vue";

const loadList = ref(false)

// Import individual components
const BaseUrl = defineAsyncComponent(() => import('./BaseUrl.vue'));
const ExampleUsage = defineAsyncComponent(() => import('./ExampleUsage.vue'));
const SearchLibraryById = defineAsyncComponent(() => import('./SearchLibraryById.vue'));
const SearchLibrariesByAttr = defineAsyncComponent(() => import('./SearchLibrariesByAttr.vue'));
const SearchFilesById = defineAsyncComponent(() => import('./SearchFilesById.vue'));
const SearchGeneCompartment = defineAsyncComponent(() => import('./SearchGeneCompartment.vue'));
const DownloadFiles = defineAsyncComponent(() => import('./DownloadFiles.vue'));
const SearchCompartments = defineAsyncComponent(() => import('./SearchCompartments.vue'));
const SearchTADs = defineAsyncComponent(() => import('./SearchTADs.vue'));
const SearchStripes = defineAsyncComponent(() => import('./SearchStripes.vue'));
const SearchLoops = defineAsyncComponent(() => import('./SearchLoops.vue'));
const SearchBoundaryDomainGenes = defineAsyncComponent(() => import('./SearchBoundaryDomainGenes.vue'));
const SearchGeneStripes = defineAsyncComponent(() => import('./SearchGeneStripes.vue'));
const SearchGeneLoops = defineAsyncComponent(() => import('./SearchGeneLoops.vue'));

const apiLabels = [
    {
        title: 'Search sample using id'
    },
    {
        title: 'Search samples using attributes'
    },
    {
        title: 'Search files using id'
    },
    {
        title: 'Download files using id and file type'
    }
]


const menuOptions: MenuOption[] = [
    {
        label: 'Overview',
        key: 'Overview',
        children: [{
            label: 'Base URL',
            key: 'BaseUrl'
        }]
    },
    {
        label: 'Quick Start',
        key: 'QuickStart',
        children: [{
            label: 'Example Usage',
            key: 'ExampleUsage'
        }]
    },
    {
        label: 'Search Metadata',
        key: 'SearchMetadata',
        children: [
        {
            label: 'Search a sample using id',
            key: 'SearchLibraryById'
        },
        {
            label: 'Search a list of samples using attributes',
            key: 'SearchLibrariesByAttr'
        },
        {
            label: 'Search files associated with a sample',
            key: 'SearchFilesById'
        }
        ]
    },
    {
        label: 'Search 3D genomic data features',
        key: 'SearchFeatures',
        children: [
            {
                label: 'Search Compartments',
                key: 'SearchCompartments'
            },
            {
                label: 'Search Topologically Associated Domains',
                key: 'SearchTADs'
            },
            {
                label: 'Search Stripes',
                key: 'SearchStripes'
            },
            {
                label: 'Search chromatin loops',
                key: 'SearchLoops'
            },
        ]
    },
    {
        label: 'Search genes',
        key: 'SearchGenes',
        children: [
            {
                label: 'Search Genes compartment E1 scores',
                key: 'SearchGeneCompartment'
            },
            {
                label: 'Search Boundary and Domain genes',
                key: 'SearchBoundaryDomainGenes'
            },
            {
                label: 'Search genes with Stripes',
                key: 'SearchGeneStripes'
            },
            {
                label: 'Search genes with chromatin loops',
                key: 'SearchGeneLoops'
            },
        ]
    },
    {
        label: 'Download Files',
        key: 'DownloadFiles',
        children: [
        {
            label: 'Download files associated with a sample',
            key: 'DownloadFiles'
        }
        ]
    },

]
const defaultExpandedKeys = ref([
    'QuickStart', 'SearchMetadata', 'SearchFeatures', 'SearchGenes', 'DownloadFiles'
])

const componentMap = {
  BaseUrl: BaseUrl,
  ExampleUsage: ExampleUsage,
  SearchLibraryById: SearchLibraryById,
  SearchLibrariesByAttr: SearchLibrariesByAttr,
  SearchFilesById: SearchFilesById,
  SearchGeneCompartment: SearchGeneCompartment,
  DownloadFiles: DownloadFiles,
  SearchCompartments: SearchCompartments,
  SearchTADs: SearchTADs,
  SearchStripes: SearchStripes,
  SearchLoops: SearchLoops,
  SearchBoundaryDomainGenes: SearchBoundaryDomainGenes,
  SearchGeneStripes: SearchGeneStripes,
  SearchGeneLoops: SearchGeneLoops
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
