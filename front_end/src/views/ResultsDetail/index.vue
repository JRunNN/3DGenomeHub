<template>
    <div class="page page-wrapped page-mobile-full flex flex-col page-without-footer border">
        <SegmentedPage @mounted="setCtx" hide-menu-btn enable-resize :use-main-scroll="true" :showDetailTable="false">
            <template #sidebar-header >
                <div class="compose-btn-wrap">
                    <n-button strong secondary type="primary" size="large">Annotation results</n-button>
                </div>
            </template>
            <template #sidebar-content >
                <n-menu class="folders-list" v-model:value="showApiDoc" :options="menuOptions" 
                :default-expanded-keys="defaultExpandedKeys"
                />
            </template>
            <template #main-toolbar>
                <span>Currently showing annotation results for region: {{ props.chrom }} : {{ props.start }} - {{ props.end }}</span>
            </template>
            <template #main-content v-show="showDetailTable">
                <component 
                :is="currentCardComponent"
                v-bind="getComponentProps(showApiDoc)"
                />
            </template>
        </SegmentedPage>
    </div>
</template>

<script setup lang="ts">
import { NButton, NMenu, type MenuOption } from "naive-ui"
import { ref, onMounted, defineAsyncComponent, computed, watch } from "vue"
import { useHideLayoutFooter } from "@/composables/useHideLayoutFooter"
import SegmentedPage, { type CtxSegmentedPage } from "@/components/common/SegmentedPage.vue"
import { NCard, NSpace, NCode, NTag } from "naive-ui"
import axios from 'axios' 

const props = withDefaults(
    defineProps<{
      chrom: string
      start: number
      end: number
    }>(),
    { 
        chrom: 'chr1',
        start: 100000,
        end: 10500000,
    }
)

const showApiDoc = ref('Overview')
const ctxPage = ref<CtxSegmentedPage | null>(null)
import APICodeExample from "./APICodeExample.vue";

const loadList = ref(false)

const showDetailTable =ref(false)

// Import individual components
const Overview = defineAsyncComponent(() => import('./Overview/index.vue'));
const Compartment = defineAsyncComponent(() => import('./Compartment/index.vue'));
const Domain = defineAsyncComponent(() => import('./Domain/index.vue'));
const Loop = defineAsyncComponent(() => import('./Loop/index.vue'));
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
  Domain: Domain,
  Loop: Loop,
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

// 定义接口类型
interface GenomicRegion {
  chrom: string;
  start: number;
  end: number;
}

interface QueryFilters {
  tissue?: string[];
  health_status?: string[];
  sample_id?: string[];
}

interface QueryParams {
  regions: GenomicRegion[];
  data_types: string[];
  filters?: QueryFilters;
  page?: number;
  page_size?: number;
}

// 定义响应数据类型
interface GenomicFeatureResponse {
  code: number;
  data: {
    compartments?: {
      total: number;
      page: number;
      page_size: number;
      total_pages: number;
      data: Array<{
        sample_id: string;
        tissue: string;
        health_status: string;
        E1score: number;
      }>;
    };
    domains?: {
      total: number;
      page: number;
      page_size: number;
      total_pages: number;
      data: Array<{
        sample_id: string;
        tissue: string;
        health_status: string;
        domain_type: string;
        score: number;
      }>;
    };
    loops?: {
      total: number;
      page: number;
      page_size: number;
      total_pages: number;
      data: Array<{
        sample_id: string;
        tissue: string;
        health_status: string;
        anchor1: GenomicRegion;
        anchor2: GenomicRegion;
        strength: number;
      }>;
    };
  };
}

// 创建axios实例
const api = axios.create({
  //TODO: baseURL: 'https://47.107.91.5:8080',
  baseURL: '/localhost:8000',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// 修改查询函数
const queryGenomicFeatures = async (params: QueryParams): Promise<GenomicFeatureResponse> => {
  try {
    // 构建查询参数
    const queryParams = new URLSearchParams({
      data_types: params.data_types.join(','),
      chrom: params.regions[0].chrom,
      start: params.regions[0].start.toString(),
      end: params.regions[0].end.toString(),
      page: (params.page || 1).toString(),
      page_size: (params.page_size || 10).toString()
    });

    // 如果有过滤条件，添加到查询参数中
    if (params.filters) {
      queryParams.append('filters', encodeURIComponent(JSON.stringify(params.filters)));
    }

    //TODO: index.vue是所有组件的父组件，在这里调用后端API获取数组并传入子组件
    //TODO: 调用后端API get_compartments获取compartment
    const response = await api.get<GenomicFeatureResponse>(
      `/genomic-features?${queryParams.toString()}`
    );
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.error('Query error:', error.response?.data || error.message);
      throw new Error(error.response?.data?.message || 'Failed to fetch genomic features');
    }
    throw error;
  }
};

// 使用示例
// 使用示例的修改
const fetchData = async () => {
  try {
    const response = await queryGenomicFeatures({
      regions: [{ chrom: "chr1", start: 1000, end: 2000 }],
      data_types: ["compartments", "domains", "loops"],
      filters: {
        tissue: ["liver"],
        health_status: ["healthy"],
        sample_id: ["GSM12344", "GSM32422"]
      },
      page: 1,
      page_size: 10
    });

    if (response.data.compartments) {
      console.log('Compartments data:', response.data.compartments);
    }
    
    if (response.data.domains) {
      console.log('Domains data:', response.data.domains);
    }
    
    if (response.data.loops) {
      console.log('Loops data:', response.data.loops);
    }

    return response;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

// TypeScript类型定义
interface GenomicRegion {
  chrom: string;
  start: number;
  end: number;
}

interface RegionSummary {
  location_type: 'gene_promoter' | 'intergenic' | 'gene_body';
  portions: {
    a_compartment: number;
    contact_domains: number;
    loops: number;
    enhancer: number;
  }
}

interface SummaryResponse {
  region: GenomicRegion;
  summary: RegionSummary;
}

// 使用示例
const testRequest = {
  regions: [
    { chrom: "chr1", start: 1000, end: 2000 },
    // { chrom: "chr2", start: 5000, end: 6000 }
  ]
};

// 修改区域摘要查询函数
const getRegionSummary = async (regions) => {
  try {
    // 构建查询参数
    const queryParams = new URLSearchParams({
      chrom: regions[0].chrom,
      start: regions[0].start.toString(),
      end: regions[0].end.toString()
    });

    const response = await axios.get(`/api/region-summary?${queryParams.toString()}`);
    // TODO: 调用后端API获取overview数据
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error('Failed to get region summary:', error);
    throw error;
  }
};



// 为不同的组件准备响应式数据
const overviewData = ref(null)
const compartmentData = ref(null)
const domainData = ref(null)
const loopData = ref(null)

// 添加一个方法来根据组件类型返回对应的props
const getComponentProps = (componentKey: string) => {
    switch(componentKey) {
        case 'Overview':
            return {
                // region: { chrom: props.chrom, start: props.start, end: props.end },
                data: overviewData.value
            }
        case 'Compartment':
            return {
                compartmentData: compartmentData.value,
                // filters: filters.value
            }
        case 'Domain':
            return {
                domainData: domainData.value,
                // tissueTypes: availableTissues.value
            }
        case 'Loop':
            return {
                loopData: loopData.value,
                // tissueTypes: availableTissues.value
            }
        // 其他组件的props...
        default:
            return {}
    }
}

// watch 部分的修改
watch(showApiDoc, async (newComponent) => {
  console.log(showApiDoc);
  try {
    if (newComponent === 'Overview') {
      overviewData.value = await getRegionSummary([{
        chrom: props.chrom,
        start: props.start,
        end: props.end
      }]);
    } else if (newComponent === 'Compartment') {
      const response = await queryGenomicFeatures({
        regions: [{
          chrom: props.chrom,
          start: props.start,
          end: props.end
        }],
        data_types: ['compartments'],
        page: 1,
        page_size: 10
      });
      compartmentData.value = response.data.compartments;
    } else if (newComponent === 'Domain') {
      const response = await queryGenomicFeatures({
        regions: [{
          chrom: props.chrom,
          start: props.start,
          end: props.end
        }],
        data_types: ['domains'],
        page: 1,
        page_size: 10
      });
      domainData.value = response.data.domains;
    } else if (newComponent === 'Loop') {
      const response = await queryGenomicFeatures({
        regions: [{
          chrom: props.chrom,
          start: props.start,
          end: props.end
        }],
        data_types: ['loops'],
        page: 1,
        page_size: 10
      });
      loopData.value = response.data.loops;
    }
    // 处理其他组件数据...
  } catch (error) {
    console.error('Error fetching data:', error);
    // 这里可以添加错误处理逻辑，比如显示错误提示
  }
}, { immediate: true });

onMounted(() => {
    // overviewData.value = getRegionSummary(testRequest.regions)
    // fetchData()
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
