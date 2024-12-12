<template>
  <n-card :bordered="true" >
    <!-- <div class="chart-item-container"> -->
      <n-skeleton text v-if="loading" :repeat="4" />
      <template v-else>
        <div ref="channelsChart" class="chart-item"> </div>
      </template>
  
    <!-- </div> -->
  </n-card>
  
</template>

<script lang="ts" setup>
import { defineComponent, nextTick, onBeforeUnmount, onMounted, ref } from 'vue'
import { dispose } from 'echarts'
import * as echarts from 'echarts'
import {NCard} from 'naive-ui'
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
        text: 'Data Types',
        left: 'center',
        top: '-5'
    },
    toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
    color: ['#4878D0', '#6C8EAD', '#9FBBD9', '#B3CDE3'], // Define the custom colors for the pie slices
    grid: {
      left: '-5%',
      right: '5%',
      top: '5%',
      bottom: '3%',
      containLabel: true,
    },
    tooltip: {
      trigger: 'axis',
    },
    series: [
      {
        name: '访问来源',
        type: 'pie',
        radius: ['30%', '60%'],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 10,
          borderColor: '#fff',
          borderWidth: 2,
        },
        emphasis: {
          label: {
            show: true,
            fontSize: '20',
            fontWeight: 'bold',
          },
        },
        labelLine: {
          show: true,
          length: 5,
          length2: 5,
          smooth: true,
        },
        data: [
          { value: 838, name: 'Hi-C' },
          { value: 152, name: 'HiChIP' },
          { value: 104, name: 'ChIA-PET'},
          // { value: 334, name: 'RNA-seq'},
          // { value: 344, name: 'ChIP-seq'},
          // { value: 274, name: 'ATAC-seq'}
        ],
      },
    ],
  }
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
    height: 180px;
  }


.cell-type-button {
  background-color: #4878D0;

}  
.cell-type-button:hover {
  background-color: #3561A7;
}
</style>
