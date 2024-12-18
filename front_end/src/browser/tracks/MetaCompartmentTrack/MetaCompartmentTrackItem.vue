<template>
    <n-scrollbar v-if="true">
        <div ref="canvasContainer" class="basic-canvas" :style="props.style">
            <!-- <div ref="chartContainer" class="chart-container w-ful h-full"></div> -->
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
import { ref, onMounted, watch, computed, nextTick, onUnmounted } from 'vue';
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
    
    if (chart) {
        chart.dispose();
    }

    chart = echarts.init(canvasContainer.value);

    // 转换数据为百分比
    const processedData = data.map(item => {
        const total = item.A_samples + item.B_samples + item.NA_samples;
        return {
            start: item.start,
            A_percent: (item.A_samples / total * 100),
            B_percent: (item.B_samples / total * 100),
            NA_percent: (item.NA_samples / total * 100)
        };
    });

    const chartOption = {
        backgroundColor: "#fff",
        color: ["#fac858", "#5470c6", "grey"],
        tooltip: {
            trigger: 'axis',
            formatter: function(params) {
                return params[0].axisValue + '<br/>' +
                    params.map(param => 
                        param.seriesName + ': ' + param.value.toFixed(2) + '%'
                    ).join('<br/>');
            }
        },
        legend: {
            data: ['A_samples', 'B_samples', 'NA_samples']
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
            max: 100,
            axisLabel: {
                inside: true, // 将标签放在轴内部
                margin: 5,    // 标签与轴线之间的距离
                textStyle: {
                    color: '#666',
                    fontSize: 10
                },
                formatter: '{value}%'
            }
        },
        series: [
            {
                name: 'A_samples',
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: processedData.map(item => item.A_percent),
                symbol: 'none'  // 去掉线上的点
            },
            {
                name: 'B_samples',
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: processedData.map(item => item.B_percent),
                symbol: 'none'  // 去掉线上的点
            },
            {
                name: 'NA_samples',
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: processedData.map(item => item.NA_percent),
                symbol: 'none'  // 去掉线上的点
            }
        ],
        animation: false // 禁用动画

    };

    chart.setOption(chartOption);
}

onMounted(async () => {
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
                    A_samples: Number(arr[3]),
                    B_samples: Number(arr[4]),
                    NA_samples: Number(arr[5])
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

    watch([width, height], async ([newWidth, newHeight]) => {
        if (chart && newWidth > 0 && newHeight > 0) {
            await nextTick();
            chart.resize();
        }
    });
});

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