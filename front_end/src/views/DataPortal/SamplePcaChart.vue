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
            <n-space  v-if="loading" vertical>
            <n-skeleton text width="30%"  height="20px" :repeat="1" />
            <n-skeleton text width="60%" height="30px" :repeat="1" /> 
            <n-skeleton text width="100%" height="40px"  :repeat="1" />
            <n-skeleton text width="30%"  height="20px" :repeat="1" />
            <n-skeleton text width="60%" height="30px" :repeat="1" /> 
            <n-skeleton text width="100%" height="40px"  :repeat="1" />
            <n-skeleton text width="30%"  height="20px" :repeat="1" />
            <n-skeleton text width="60%" height="30px" :repeat="1" /> 
            <n-skeleton text width="100%" height="40px"  :repeat="1" />
            <n-skeleton text width="30%"  height="20px" :repeat="1" />
            <n-skeleton text width="60%" height="30px" :repeat="1" /> 
            <n-skeleton text width="100%" height="40px"  :repeat="1" />
            <n-skeleton text width="30%"  height="20px" :repeat="1" />
            <n-skeleton text width="60%" height="30px" :repeat="1" /> 
            <n-skeleton text width="100%" height="40px"  :repeat="1" />
            <n-skeleton text width="30%"  height="20px" :repeat="1" />
            <n-skeleton text width="60%" height="30px" :repeat="1" />  
            <n-skeleton text width="100%" height="40px"  :repeat="1" />
            <n-skeleton text width="30%"  height="20px" :repeat="1" />
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
import { useRouter } from "vue-router";


const router = useRouter()
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

async function fetchData() {
      const response = await fetch('https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/others/pan3d_compartments_pca.txt');
      console.log(response)
      const text = await response.text();
      return text;
    }

// Function to parse the text data
function parseData(text) {
    const lines = text.split('\n').filter(line => line.trim() !== '');
    const headers = lines[0].split('\t');
    const data = lines.slice(1).map(line => {
    const values = line.split('\t');
    const obj = {};
    headers.forEach((header, index) => {
        obj[header] = values[index];
    });
    return obj;
    });
    return data;
}

    // Define your custom tissue-color mapping
    const tissueColors = {
      'Adrenal gland': '#F6EC65',
      'Arthritis': '#E83F19',
      'Bladder': '#3C5EAA',
      'Blood': '#BD2321',
      'Bone': '#F2F2F3',
      'Brain': '#F6BBA7',
      'Breast': '#8B6679',
      'Bronchus': '#EE7E87',
      'Colon': '#F7C96B',
      'Embryo': '#99D6EF',
      'Eye': '#8D1C27',
      'Heart': '#EC6822',
      'Kidney': '#697F15',
      'Liver': '#8B5241',
      'Lung': '#F7D774',
      'Lymph': '#06763B',
      'Muscle tissue': '#F7BE92',
      'Nerve': '#F5E72E',
      'Ovary': '#B35CA0',
      'Pancreas': '#DFDE86',
      'Pharynx': '#FDE5C8',
      'Placenta': '#E83F29',
      'Prostate gland': '#ACC7E8',
      'Skin': '#854922',
      'Soft tissue': '#DBA883',
      'Spleen': '#781E4E',
      'Stomach': '#F5AF32',
      'Testis': '#788CA4',
      'Thymus': '#92C976',
      'Thyroid gland': '#F6B59C',
      'Uterus': '#EABDD7',
      'Vagina': '#DE4E96',
      'Vessel': '#4B83C4'
    };

const init = (data) => {
    const option = {
  title: {
    text: 'PCA Plot based on whole genome compartmentation E1 value',
    subtext: 'Click the dots will navigate to individual sample page'
  },
  tooltip: {
    trigger: 'item',
    formatter: params => {
      return `ID: ${params.data.id}<br>PC1: ${params.data.value[0]}<br>PC2: ${params.data.value[1]}<br>Tissue: ${params.data.tissue}<br>Health Status: ${params.data.health_status}<br>Biomaterial: ${params.data.biomaterial_type}`;
    }
  },
  xAxis: {
    name: 'PC1',
    nameLocation: 'end',
            nameTextStyle: {
                fontSize: 16
            },
            axisLabel: {
                fontSize: 14
            }
  },
  yAxis: {
    name: 'PC2',
    nameLocation: 'end',
            nameTextStyle: {
                fontSize: 16
            },
            axisLabel: {
                fontSize: 14
            }
  },
  series: [{
    name: 'PCA',
    type: 'scatter',
    data: data.map(item => ({
      value: [item.PC1, item.PC2],
      id: item.id,
      tissue: item.tissue,
      health_status: item.health_status,
      biomaterial_type: item.biomaterial_type,
      itemStyle: {
        color: item.color
      }
    }))
  }]
};
    setTimeout(() => {
        loading.value = false
        nextTick(() => {
            const chartInstance = useEcharts(channelsChart.value as HTMLDivElement);
            chartInstance.setOption(option);
            chartInstance.on('click', params => {
                console.log(params)
                router.push({ name: 'Sample', params: { id: params.data.id } });
            });
        })
    }, 1000)
}
const updateChart = () => {
    useEcharts(channelsChart.value as HTMLDivElement).resize()
}
onMounted( async ()=>{

    const text = await fetchData();
    console.log(text)
    const data = parseData(text);
    data.forEach(item => {
  item.color = tissueColors[item.tissue] || '#000000'; // Default to black if tissue is NA
});
console.log(data)
    init(data)
})
onBeforeUnmount(() => {
    dispose(channelsChart.value as HTMLDivElement)
})

</script>
  
<style scoped>
.chart-item-container {
    width: 100%;


}

.chart-item {
    height:800px;
}


.cell-type-button {
    background-color: #4878D0;

}

.cell-type-button:hover {
    background-color: #3561A7;
}
</style>
  