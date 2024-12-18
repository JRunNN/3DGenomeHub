<template>
    <n-scrollbar v-if="isVisible">
        <div ref="canvasContainer" class="basic-canvas" :style="props.style">
            <!-- <div ref="chartContainer" class="chart-container"></div> -->
            <n-spin v-show="showSpin" class="absolute left-1/2 top-1/2"></n-spin>
        </div>
    </n-scrollbar>
    <div v-else>
        <div ref="canvasContainer" class="basic-canvas">
            <n-alert title="" type="warning">
                Too many items. Zoom in to see features
            </n-alert>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watch, computed, nextTick ,onUnmounted} from 'vue';
import { useElementSize } from '@vueuse/core'
import { TabixIndexedFile } from '@gmod/tabix'
import { RemoteFile } from 'generic-filehandle'
import * as echarts from 'echarts';

const props = defineProps({
    location: {
        type: Object,
        required: true
    },
    option: {
        type: Object,
        required: true
    },
    dataLoaded: {
        type: Boolean,
        required: false
    },
    style: {
        type: Object,
        required: true
    },
})

const canvasContainer = ref(null)
const chartContainer = ref(null)
const showSpin = ref(false)
const isVisible = ref(false)
let visibilityWidth = 50000000
let chart = null

const chrom = computed(() => props.location.chrom)
const start = computed(() => props.location.start)
const end = computed(() => props.location.end)
const option = computed(() => props.option)

const url = props.option.url

const file = new TabixIndexedFile({
    filehandle: new RemoteFile(url),
    tbiFilehandle: new RemoteFile(url + '.tbi')
})
const { width, height } = useElementSize(canvasContainer)

const initChart = (data) => {
    if (!canvasContainer.value) return;
    
    // If chart exists, dispose it first
    if (chart) {
        chart.dispose();
    }

    // Initialize new chart
    chart = echarts.init(canvasContainer.value);
    
    const minValue = data.reduce((min, val) => Math.min(min, val.quan25), Infinity);
    const base = -minValue;

    const chartOption = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross',
                animation: false,
                label: {
                    backgroundColor: '#ccc',
                    borderColor: '#aaa',
                    borderWidth: 1,
                    shadowBlur: 0,
                    color: '#222'
                }
            }
        },
        grid: {
            top: '0',
            left: '0',
            right: '0',
            bottom: '0',
            containLabel: false // 设置为 false 确保图表扩展到边缘
        },
        xAxis: {
            type: 'category',
            data: data.map(item => item.start),
            boundaryGap: false,
            axisLine: {
                show: false // 隐藏 x 轴线
            },
            axisTick: {
                show: false // 隐藏刻度线
            },
            axisLabel: {
                show: false // 隐藏刻度标签
            },
            position: 'top' // 将 x 轴放置在图表内部顶部
        },
        yAxis: {
            type: 'value',
            position: 'left',
            offset: 0,
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                inside: true, // 将标签放在轴内部
                margin: 5,    // 标签与轴线之间的距离
                textStyle: {
                    color: '#666',
                    fontSize: 10
                },
                formatter: function(value) {
                    return value.toFixed(1); // 格式化数字显示
                }
            },
            splitLine: {
                show: false  // 隐藏网格线
            }
        },
        series: [
            {
                name: 'Lower Band',
                type: 'line',
                data: data.map(item => item.quan25 + base),
                lineStyle: {
                    opacity: 0
                },
                stack: 'confidence-band',
                symbol: 'none'
            },
            {
                name: 'Upper Band',
                type: 'line',
                data: data.map(item => item.quan75 - item.quan25),
                lineStyle: {
                    opacity: 0
                },
                areaStyle: {
                    color: '#ccc'
                },
                stack: 'confidence-band',
                symbol: 'none'
            },
            {
                name: 'Average',
                type: 'line',
                data: data.map(item => item.ave + base),
                itemStyle: {
                    color: '#333'
                },
                showSymbol: false
            }
        ],
        animation: false // 禁用动画
    };

    chart.setOption(chartOption);
}

onMounted(async () => {
    // Wait for DOM to be updated
    await nextTick();
    
    watch([() => option.value.series, () => chrom.value, () => start.value, () => end.value], 
    async (newValue) => {
        showSpin.value = true;
        if (end.value - start.value < visibilityWidth) {
            isVisible.value = true;
            let lines = [];
            
            await file.getLines(chrom.value, start.value, end.value, function(line) {
                const arr = line.split(/[\s]+/);
                const addedData = {
                    chrom: arr[0],
                    start: Number(arr[1]),
                    end: Number(arr[2]),
                    ave: Number(arr[3]),
                    quan25: Number(arr[4]),
                    quan75: Number(arr[5])
                };
                lines.push(addedData);
            });

            await nextTick();
            initChart(lines);
            showSpin.value = false;
        } else {
            isVisible.value = false;
        }
    }, { immediate: true, deep: true });

    // Handle resize
    // Watch for size changes (both width and height)
    watch([width, height], async ([newWidth, newHeight]) => {
        if (chart && newWidth > 0 && newHeight > 0) {
            await nextTick();
            chart.resize();
        }
    });
});

// Clean up chart instance when component is unmounted
onUnmounted(() => {
    if (chart) {
        chart.dispose();
        chart = null;
    }
});
</script>

<style scoped>
.basic-canvas {
    width: 100%;
    height: 100%;
    position: relative;
}

.chart-container {
    width: 100%;
    height: 100%;
    min-height: 200px;
}
</style>