<template>
    <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
        <CardActions class="h-full" :segmented="{
            content: true,
            footer: true
        }">
            <template #header>
                <n-h3>Multi-omics datasets from the same biosample</n-h3></template>
            <template #header-extra>
                <n-button type="primary" @click="handleClick">
                    <!-- <Icon class="mr-3" :name="CartIcon"></Icon> -->
                    Go To Data Portal
                </n-button>
            </template>
            <template #default>
                <div class="flex">
                    <div class="w-96 mr-12 flex flex-col items-center">
                        <p >Datasets by Body Map</p>
                        <div class="w-full h-full"><BodyMap></BodyMap></div>
                        
                    </div>
                    <div class="flex-auto ">
                        <div class="chart-item-container">
                            <n-skeleton text v-if="loading" :repeat="4" />
                            <template v-else>
                                <div ref="channelsChart" class="chart-item"> </div>
                            </template>
                        </div>
                    </div>
                    <div class="w-80">
                        <SampleStat></SampleStat>
                    </div>
                </div>
            </template>
        </CardActions>
    </CardWrapper>
</template>

<script lang="ts" setup>
import { defineComponent, nextTick, onBeforeUnmount, onMounted, ref } from 'vue'
import { dispose } from 'echarts'
import * as echarts from 'echarts'
import SampleStat from './SampleStat.vue'
import BodyMap from './BodyMap.vue'
import { useRouter } from "vue-router";

// import echarts from ''
function useEcharts(dom: HTMLElement, theme?: string) {
    let instance = echarts.getInstanceByDom(dom)
    if (!instance) {
        instance = echarts.init(dom, theme)
    }
    return instance
}
const router = useRouter()

const handleClick = ()=> {
    router.push({ name: 'dataportal' })
}

const loading = ref(true)
const channelsChart = ref<HTMLDivElement | null>(null)
const init = () => {
    const option = {
        title: {
            text: 'Datasets by Body Sites',
            left: 'center'
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        dataset: [
            {
                dimensions: ['Name', 'Color', 'Number'],
                source: [
                    ['Adrenal gland', '#F6EC65', 2],
                    ['Arthritis', '#E83F19', 5],
                    ['Bladder', '#3C5EAA', 6],
                    ['Blood', '#BD2321', 180],
                    ['Bone', '#F2F2F3', 6],
                    ['Brain', '#F6BBA7', 141],
                    ['Breast', '#8B6679', 56],
                    ['Bronchus', '#EE7E87', 4],
                    ['Colon', '#F7C96B', 93],
                    ['Embryo', '#99D6EF', 6],
                    ['Eye', '#8D1C27', 46],
                    ['Heart', '#EC6822', 34],
                    ['Kidney', '#697F15', 13],
                    ['Liver', '#8B5241', 6],
                    ['Lung', '#F7D774', 41],
                    ['Lymph', '#06763B', 1],
                    ['Muscle', '#F7BE92', 10],
                    ['Nerve', '#F5E72E', 1],
                    ['Ovary', '#B35CA0', 12],
                    ['Pancreas', '#DFDE86', 13],
                    ['Pharynx', '#FDE5C8', 1],
                    ['Placenta', '#E83F29', 2],
                    ['Prostate', '#ACC7E8', 13],
                    ['Skin', '#854922', 59],
                    ['Soft tissue', '#DBA883', 3],
                    ['Spleen', '#781E4E', 2],
                    ['Stomach', '#F5AF32', 2],
                    ['Testis', '#788CA4', 2],
                    ['Thymus', '#92C976', 9],
                    ['Thyroid gland', '#F6B59C', 1],
                    ['Uterus', '#EABDD7', 105],
                    ['Vagina', '#DE4E96', 3],
                    ['Vessel', '#4B83C4', 13]
                ]
            },
            {
                transform: {
                    type: 'sort',
                    config: { dimension: 'Number', order: 'asc' }
                }
            }
        ],
        yAxis: {
            type: 'category',
            axisLabel: { interval: 0, rotate: 0 }  // Rotate labels for better readability
        },
        xAxis: {},
        series: {
            type: 'bar',
            encode: { y: 'Name', x: 'Number' },
            datasetIndex: 1,
            itemStyle: {
                color: function (params) {
                    // params.data refers to the data array for the specific item, e.g., ['Adrenal gland', '#F6EC65', 4]
                    return params.data[1]; // Index 1 is the 'Color' in the dimensions array
                }
            }
        },
        grid: {
            left: 80,
            top: 30,
            right: 30,
            bottom: 20
        }
    };
    setTimeout(() => {
        loading.value = false
        nextTick(() => {
            useEcharts(channelsChart.value as HTMLDivElement).setOption(option)
        })
    }, 1000)
}
const updateChart = () => {
    useEcharts(channelsChart.value as HTMLDivElement).resize()
}
onMounted(init)
onBeforeUnmount(() => {
    dispose(channelsChart.value as HTMLDivElement)
})

</script>

<style scoped>
.chart-item-container {
    width: 100%;


}

.chart-item {
    height: 700px;
}


.cell-type-button {
    background-color: #4878D0;

}

.cell-type-button:hover {
    background-color: #3561A7;
}
</style>