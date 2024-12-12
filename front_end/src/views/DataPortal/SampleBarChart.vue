<template>
    <n-card :content-style="{ padding: '10px' }" :header-style="{ padding: '10px' }" :segmented="true">
        <!-- <template #header>
            <n-skeleton text style="width: 50%" v-if="loading" />
            <template v-else>
                <div class="text-sm">Cell Types</div>
                <n-h3 prefix="bar" align-text>Cell Types</n-h3>
                <n-statistic label="Cell Types">
                    138
                </n-statistic>
            </template>
        </template>
        <template #header-extra>
            <button type="button"
                class="cell-type-button text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm p-2.5 text-center inline-flex items-center me-2"
                @click="$router.push({ name: 'Datalist' })">
                <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M1 5h12m0 0L9 1m4 4L9 9" />
                </svg>
            </button>
        </template> -->
        <div class="chart-item-container">
            <n-space v-if="loading" vertical>
                <n-skeleton text width="30%" height="20px" :repeat="1" />
                <n-skeleton text width="60%" height="30px" :repeat="1" />
                <n-skeleton text width="100%" height="40px" :repeat="1" />
                <n-skeleton text width="30%" height="20px" :repeat="1" />
                <n-skeleton text width="60%" height="30px" :repeat="1" />
                <n-skeleton text width="100%" height="40px" :repeat="1" />
                <n-skeleton text width="30%" height="20px" :repeat="1" />
                <n-skeleton text width="60%" height="30px" :repeat="1" />
                <n-skeleton text width="100%" height="40px" :repeat="1" />
                <n-skeleton text width="30%" height="20px" :repeat="1" />
                <n-skeleton text width="60%" height="30px" :repeat="1" />
                <n-skeleton text width="100%" height="40px" :repeat="1" />
                <n-skeleton text width="30%" height="20px" :repeat="1" />
                <n-skeleton text width="60%" height="30px" :repeat="1" />
                <n-skeleton text width="100%" height="40px" :repeat="1" />
                <n-skeleton text width="30%" height="20px" :repeat="1" />
                <n-skeleton text width="60%" height="30px" :repeat="1" />
                <n-skeleton text width="100%" height="40px" :repeat="1" />
                <n-skeleton text width="30%" height="20px" :repeat="1" />
                <n-skeleton text width="60%" height="30px" :repeat="1" />

            </n-space>
            <template v-else>
                <div ref="channelsChart" class="chart-item"> </div>
            </template>

        </div>
    </n-card>
</template>
  
<script lang="ts" setup>
import { defineComponent, nextTick, onBeforeUnmount, onMounted, ref } from 'vue'
import { dispose } from 'echarts'
import * as echarts from 'echarts'
// import echarts from ''
function useEcharts(dom: HTMLElement, theme?: string) {
    let instance = echarts.getInstanceByDom(dom)
    if (!instance) {
        instance = echarts.init(dom, theme)
    }
    return instance
}

const loading = ref(true)
const channelsChart = ref<HTMLDivElement | null>(null)
const init = () => {
    const option = {
        title: {
            text: 'Bar Plot of sample sizes by tissue',
            subtext: 'Click the bar to filter the below summary table by individual body sites'
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
                    ['Adrenal gland', '#F6EC65', 4],
                    ['Arthritis', '#E83F19', 14],
                    ['Bladder', '#3C5EAA', 6],
                    ['Blood', '#BD2321', 218],
                    ['Bone', '#F2F2F3', 9],
                    ['Brain', '#F6BBA7', 185],
                    ['Breast', '#8B6679', 84],
                    ['Bronchus', '#EE7E87', 3],
                    ['Colon', '#F7C96B', 142],
                    ['Embryo', '#99D6EF', 6],
                    ['Eye', '#8D1C27', 50],
                    ['Heart', '#EC6822', 82],
                    ['Kidney', '#697F15', 13],
                    ['Liver', '#8B5241', 19],
                    ['Lung', '#F7D774', 58],
                    ['Lymph', '#06763B', 115],
                    ['Muscle tissue', '#F7BE92', 13],
                    ['Nerve', '#F5E72E', 2],
                    ['Ovary', '#B35CA0', 23],
                    ['Pancreas', '#DFDE86', 37],
                    ['Pharynx', '#FDE5C8', 1],
                    ['Placenta', '#E83F29', 2],
                    ['Prostate gland', '#ACC7E8', 2],
                    ['Skin', '#854922', 65],
                    ['Soft tissue', '#DBA883', 3],
                    ['Spleen', '#781E4E', 2],
                    ['Stomach', '#F5AF32', 6],
                    ['Testis', '#788CA4', 2],
                    ['Thymus', '#92C976', 12],
                    ['Thyroid gland', '#F6B59C', 2],
                    ['Uterus', '#EABDD7', 15],
                    ['Vagina', '#DE4E96', 3],
                    ['Vessel', '#4B83C4', 31]
                ]
            },
            {
                transform: {
                    type: 'sort',
                    config: { dimension: 'Number', order: 'desc' }
                }
            }
        ],
        xAxis: {
            type: 'category',
            axisLabel: { interval: 0, rotate: 45, fontSize: 20 },  // Rotate labels for better readability
            nameLocation: 'end',
            nameTextStyle: {
                fontSize: 20
            }
        },
        yAxis: {
            nameLocation: 'end',
            nameTextStyle: {
                fontSize: 25
            },
            axisLabel: {
                fontSize: 25
            }
        },
        series: {
            type: 'bar',
            encode: { x: 'Name', y: 'Number' },
            datasetIndex: 1,
            itemStyle: {
                color: function (params) {
                    // params.data refers to the data array for the specific item, e.g., ['Adrenal gland', '#F6EC65', 4]
                    return params.data[1]; // Index 1 is the 'Color' in the dimensions array
                }
            }
        },
        grid: {
            left: 50,
            top: 60,
            right: 10,
            bottom: 100
        }
    };
    setTimeout(() => {
        loading.value = false
        nextTick(() => {
            useEcharts(channelsChart.value as HTMLDivElement).setOption(option)
        })
    }, 100)
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
    height: 600px;
}


.cell-type-button {
    background-color: #4878D0;

}

.cell-type-button:hover {
    background-color: #3561A7;
}
</style>
  