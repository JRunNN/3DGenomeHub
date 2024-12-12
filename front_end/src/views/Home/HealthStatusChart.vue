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
        text: 'Health status',
        left: 'center',
        top: '-5'
    },
    toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
    color: ['#074150', '#2B7186', '#4096B1', '#9CC6D4'] , // Define the custom colors for the pie slices
    grid: {
      left: '5%',
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
            fontSize: '16',
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
          { value: 443, name: 'Cancer' },
          { value: 107, name: 'Non-cancer' },
          { value: 51, name: 'Others' },
          { value: 493, name: 'Healthy' },
          // { value: 1594, name: '电话' },
          // { value: 1347, name: '地推' },
          // { value: 635, name: '直播' },
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
  background-color: #6E6E6E;

}  
.cell-type-button:hover {
  background-color: #565656;
}
</style>
