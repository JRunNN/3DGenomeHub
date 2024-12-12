<template>
    <div class="page page-wrapped page-mobile-full flex flex-col page-without-footer">
        <SegmentedPage @mounted="setCtx" hide-menu-btn enable-resize :use-main-scroll="true">
            <template #sidebar-header>
                <div class="compose-btn-wrap">
                    <n-button strong secondary type="primary" size="large">Annotation results</n-button>
                </div>
            </template>
            <template #sidebar-content>
                <n-menu class="folders-list" v-model:value="showApiDoc" :options="menuOptions" 
                :default-expanded-keys="defaultExpandedKeys"
                />


            </template>

            <template #main-toolbar>
                <span>Currently showing annotation results for region</span>

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
const Overview = defineAsyncComponent(() => import('./Overview/index.vue'));
const Compartment = defineAsyncComponent(() => import('./Compartment.vue'));
const ExampleUsage = defineAsyncComponent(() => import('./ExampleUsage.vue'));
const Stripe = defineAsyncComponent(() => import('./Stripe/index.vue'));
const Enhancer = defineAsyncComponent(() => import('./Enhancer/index.vue'));
const CancerCRE = defineAsyncComponent(() => import('./CancerCRE/index.vue'));
const GWASCatalog = defineAsyncComponent(() => import('./GWASCatalog/index.vue'));
const Eqtl = defineAsyncComponent(() => import('./Eqtl/index.vue'));


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
        key: 'Overview',
        // children: [{
        //     label: 'Base URL',
        //     key: 'Overview'
        // }]
    },
    // {
    //     label: 'Human 3D genome organization',
    //     key: 'QuickStart',
    //     children: [{
    //         label: 'Example Usage',
    //         key: 'ExampleUsage'
    //     }]
    // },
    {
        label: 'Human 3D genome organization',
        key: 'human3dgenome',
        children: [
        {
            label: 'Compartment',
            key: 'Compartment'
        },
        {
            label: 'Domain',
            key: 'Domain'
        },
        {
            label: 'Stripe',
            key: 'Stripe'
        },
        {
            label: 'Loop',
            key: 'Loop'
        }
        ]
    },
    {
        label: 'Cis regulatory landscape',
        key: 'cisregulatorylandscape',
        children: [
            {
                label: 'Enhancer',
                key: 'Enhancer'
            },
            {
                label: 'Cancer CRE',
                key: 'CancerCRE'
            },
            {
                label: 'GWAS Catalog',
                key: 'GWASCatalog'
            },
            {
                label: 'Eqtl',
                key: 'Eqtl'
            },
        ]
    },
    {
        label: 'Cross-species comparison',
        key: 'crossspecies',
        children: [
            {
                label: 'Sequence conservation',
                key: 'SearchGeneCompartment'
            },
            {
                label: 'Enhancer conservation',
                key: 'SearchBoundaryDomainGenes'
            },
            {
                label: 'TAD boundary conservation',
                key: 'SearchGeneStripes'
            }
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
    'QuickStart', 'human3dgenome', 'crossspecies', 'cisregulatorylandscape', 'DownloadFiles'
])

const componentMap = {
    Overview: Overview,
  Compartment: Compartment,
  ExampleUsage: ExampleUsage,
  Stripe: Stripe,
  Enhancer: Enhancer,
  CancerCRE: CancerCRE,
  GWASCatalog: GWASCatalog,
  Eqtl: Eqtl

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
