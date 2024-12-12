<template>
    <n-card :content-style="{ padding: '10px' }" :header-style="{ padding: '10px' }" :segmented="true">
      <template #header>
        <n-skeleton text style="width: 50%" v-if="loading" />
        <template v-else>
          <n-statistic label="Normal open chromatin regions">
            <!-- 299,740,245  -->
        </n-statistic>
        </template>
      </template>
      <!-- <template #header-extra>
        <button type="button" class="cell-type-button text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm p-2.5 text-center inline-flex items-center me-2"
        @click="$router.push({name: 'CellType', params: {id: 'GM12878'}})"
        >
  <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
  </svg>
  </button>
          </template>  -->
      <div class="chart-item-container">
        <n-skeleton text v-if="loading" :repeat="4" />
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
  // import echarts from '@/assets/echarts.min.js'
  function useEcharts(dom: HTMLElement, theme?: string) {
    let instance = echarts.getInstanceByDom(dom)
    if (!instance) {
      instance = echarts.init(dom, theme)
    }
    return instance
  }
  
  const props = defineProps({
  inputData: {
    type: Array,
    required: true
  }
})
  const loading = ref(true)
  const channelsChart = ref<HTMLDivElement | null>(null)
    const init = (inputData) => {
  // First, sort the inputData to find the top 5 values
  const sortedData = [...inputData].sort((a, b) => b.value - a.value);
  const topFiveValues = sortedData.slice(0, 5).map(item => item.name);
console.log(topFiveValues)

  // Define the option object with configurations for the polar histogram
  const option = {
    // Define colors for the bars
    color: ['#D65F5F', '#DF8A8A'],

    // Polar coordinate system
    polar: {},
    angleAxis: {
      show: true,
      type: 'category',
      data: inputData.map(item => item.name),
      // data: topFiveValues,
      interval: 10,
      boundaryGap: false, // Makes the bars stick to the edge
      splitLine: {
        show: true,
        lineStyle: {
          color: '#999',
          type: 'dashed',
        },
      },
      formatter: (value, index) => {
          // Check if the current value is in the top five
          if (topFiveValues.includes(inputData[index].name)) {
            return value;
          }
          return '';
        },
      axisLine: {
        show: false // Hide the axis line for a cleaner look
      },
    },
    radiusAxis: {
      splitLine: {
        lineStyle: {
          color: '#999',
          type: 'dashed',
        },
      },
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'cross' // Crosshair pointer for better accuracy
      }
    },
    series: [
      {
        type: 'bar',
        data: inputData.map(item => item.value),
        coordinateSystem: 'polar',
        name: 'Histogram',
        itemStyle: {
          // Optional: style for the bars
          emphasis: {
            shadowBlur: 10,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        },
      }
    ],
  };

  setTimeout(() => {
    loading.value = false; // Presumably this controls a loading indicator
    nextTick(() => {
      // Assuming useEcharts is a custom hook that initializes ECharts instance
      useEcharts(channelsChart.value as HTMLDivElement).setOption(option);
    });
  }, 1000); // Delay for visual effect, may not be needed in production
};
  const updateChart = () => {
    useEcharts(channelsChart.value as HTMLDivElement).resize()
  }
  onMounted(() => {
    console.log(props.inputData)
    init(props.inputData)
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
      height: 180px;
    }
  
    .cell-type-button {
    background-color: #D65F5F;
  
  }  
  .cell-type-button:hover {
    background-color: #B04646;
  }
  </style>
  