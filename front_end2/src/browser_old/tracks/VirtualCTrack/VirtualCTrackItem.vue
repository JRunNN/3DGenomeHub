<template>
    <n-scrollbar v-if="isVisible && isActive">
        <div ref="canvasContainer" class="basic-canvas" :style="props.style">
            <!-- <canvas ref="canvas"></canvas> -->
            <n-spin v-show="showSpin" class="absolute left-1/2 top-1/2"></n-spin>
        </div>
    </n-scrollbar>
    <div v-else>
        <div ref="canvasContainer" class="basic-canvas" :style="props.style">
            <n-alert title="" type="warning">
                {{ message }}
            </n-alert>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watch, computed } from 'vue';
import HicStraw from 'hic-straw/dist/hic-straw.min.js'
import { useMouseInElement } from '@vueuse/core'
import { useElementSize } from '@vueuse/core'
import * as d3 from 'd3'

const props = defineProps({
    location: {
        type: Object,
        required: true
    },
    option: {
        type: Object,
        required: true
    },
    // attr: {
    //     type: Object,
    //     required: true
    // },
    dataLoaded: {
        type: Boolean,
        required: false
    },
    controllerConfig: {
        type: Object,
        required: true
    },
    style: {
        type: Object,
        required: true
    }
})

// const emit = defineEm its(['updateIsSelective'])

const isActive = computed(
    () => props.controllerConfig.isActive
)


// const isSelective = ref(props.controllerConfig.isSelective)

const chrom = computed(
    () => props.location.chrom
)

const start = computed(
    () => props.location.start
)

const end = computed(
    () => props.location.end
)

const message = ref('Zoom in to see features')
const visibilityWidth = 1000000
const isVisible = ref(false)
const showSpin = ref(false)
const canvasContainer = ref(null)
const canvas = ref(null)
// const corenavStore = usecorenavStore()
// const { chrom, min, max, start, end, isLoaded, chromSizes, chromBands } = storeToRefs(corenavStore)
let plot = ref(null)
const canvasReady = ref(false)
const minBin = ref(0)
const maxBin = ref(0)
const { width, height } = useElementSize(canvasContainer)

const _drawPlot = (canvas, xvalues) => {
    // var opts = this.options;
    // if (!xvalues) {
    //     xvalues = opts._xvalues;
    // }

    // opts._canvas.css({
    //     height: opts._canvas.height(),
    //     width: opts._canvas.width()
    // });
    // canvas.value.style.width = '100%'
    // canvas.value.style.height = '100%'

    var params = {
        grid: { borderWidth: 1, reserveSpace: false, clickable: true, hoverable: true, minBorderMargin: 0 },
        series: {
            lines: { fill: false, lineWidth: 1 }
            // bars: { show: true, lineWidth: 1, barWidth: 1 }
        },
        xaxis: { ticks: 0 },
        yaxis: {
            show: true,
            autoscale: 'loose',
            labelWidth: -5,
            labelHeight: 5,
            autoScaleMargin: null,
            growOnly: false,
            reserveSpace: false,
            tickFormatter: function (val, axis) {
                if (val / 1000 != 0 && val % 1000 == 0) return (val / 1000) + "k";
                return Math.round(val);
            }
        },
        fill: true
    };

    // if (xvalues.length == 1) {
    //     params.series.lines.fill = 1;
    //     params.series.lines.lineWidth = 1;
    // }

    // var opacity = _get(opts._options, "opacity", params.series.lines.fill);
    // params.series.lines.fill = opacity;

    // if (opacity != null && opacity != 1) {
    //     params.series.lines.lineWidth = 1; // we need clear outline
    // }

    // // extend xaxis/yaxis
    // params.xaxis = $.extend(params.xaxis, _get(opts._options, "xaxis"));
    // params.yaxis = $.extend(params.yaxis, _get(opts._options, "yaxis"));

    // if (params.yaxis.log) {
    //     params.yaxis.tickFormatter = function(val) {
    //         if (val < 0) {
    //             val = Math.round(Math.pow(params.yaxis.log, -val)); 
    //             if (Math.round(val) != val) val = val.toFixed(val < 10 ? 1 : 0);
    //             if (val/1000!=0 && val%1000==0) return (-val/1000) + "k"; else return -val;
    //         } else {
    //             val = Math.round(Math.pow(params.yaxis.log, val)); 
    //             if (Math.round(val) != val) val = val.toFixed(val < 10 ? 1 : 0);
    //             if (val/1000!=0 && val%1000==0) return (val/1000) + "k"; else return val;
    //         }
    //     };
    // }

    let plot = $.plot(canvas, xvalues, params);
    // HACK: make the font smaller for a quick'n'dirty fix to problem with text overflow
    // $(opts._canvas).find('.tickLabel'); //.css({'font-size': '80%'});
    plot.draw()
    $(canvasContainer.value).bind('plotclick', function (event, pos, item) {
        // if (item) {
        //     var x = item.datapoint[0].toFixed(2),
        //         y = item.datapoint[1].toFixed(2);
        //     $(canvasContainer.value + ' .hover').html(item.series.label + " of " + x + " = " + y)
        //         .css({top: item.pageY+5, left: item.pageX+5})
        //         .fadeIn(200);
        // } else {
        //     $(canvasContainer.value + ' .hover').hide();
        // }
        console.log(pos.x.toFixed(2), pos.y.toFixed(2))
        if (item) {
            console.log(item.datapoint[0].toFixed(2), item.datapoint[1].toFixed(2))
        }

    })

    return plot
}


// const _makeInitialRequest = (canvasEle, xdata) => {

//     var xvalues = [],
//         l = start.value,
//         r = end.value,
//         w =  canvasEle.getBoundingClientRect().width,
//         step = (r - l) / w;

//     // var ylog = _get(_get(opts._options, "yaxis", {}), "log");
//     // const ylog = false
//     // for (var k in xdata) {
//     //     var values = [],
//     //         data = xdata[k];

//     //     // modifier
//     //     // var negate = _get(opts._sries, k, {}).negate;
//     //     const negate = false

//     //     for (var i = 0; i < w; i++) {
//     //         var v = data[i];
//     //         if (ylog && v > 0) v = Math.log(v) / Math.log(ylog);
//     //         if (negate) v = -v;
//     //         values.push([i * step + l, v]);
//     //     }

//     //     xvalues.push($.extend(_get(opts._series, k, {}), { data: values }));
//     // }
//     const xvalues2 = xdata.map(obj => {
//         const average = (obj.start + obj.end) / 2;
//         const score = obj.score;
//         return [average, score];
//     });

//     const xvalues3 = [{
//         color: 'red',
//         data: xvalues2
//     }]
//     console.log(xvalues3)
//     _drawPlot(canvasEle, xvalues3);

// }

// function _get(dict, key, altval) {
//     return (dict == null) ? altval : (dict[key] == null ? altval : dict[key]);
// }

// import the gene annotation file from the server
// const tracksStore = usetracksStore()

// // const data = ref([]);
// const filteredData = ref([]);
// const cacheKey = ref('');
// // const url = '/data/BASIC_HBAD5RP_FKDL190764711-1a.e500.clusters.cis.chiasig.txt';
// const url = '/data/IBRD9_BRD9_rep1.RPKM.bigwig'
// const filename = url.substring(url.lastIndexOf('/') + 1);

// const file = new BigWig({
//     filehandle: new RemoteFile(url)
// }
// )
const straw = new HicStraw({
    url: "http://localhost:5173/data/ENCFF379AWZ.hic"
})

function getBinData(binNumber, data, downSampleSize = 1000) {


    let result = [];

    data.forEach((d) => {
        if (d.bin1 === binNumber) {
            result.push([d.bin2, d.counts]);
        } else if (d.bin2 === binNumber) {
            result.push([d.bin1, d.counts]);
        }
    });

    // If the result array length is greater than the specified downSampleSize,
    // then downsample by selecting a random subset of size downSampleSize
    if (result.length > downSampleSize) {
        result = result
            .sort(() => 0.5 - Math.random()) // shuffle the result array
            .slice(0, downSampleSize); // select first downSampleSize elements
    }

    return result;
}

const toggleBtn = ref(null)
// const toggleBtn = document.getElementById("toggleLine");

// const numBins = 10; // number of equally-sized bins
// const binWidth = canvas.value.width / numBins;
let mouseX = 0; // current x position of mouse relative to canvas

let ctx = ref(null)
let prevMouseX = null;


const drawLine = () => {
    console.log(drawLine, mouseX)
    ctx.value.beginPath();
    ctx.value.moveTo(mouseX, 0);
    ctx.value.lineTo(mouseX, canvasContainer.value.height);
    // ctx.fillStyle = 'red'
    ctx.value.stroke();
}

const clearCanvas = () => {

    // console.log(ctx)
    // const imageData = ctx.value.getImageData(0, 0, canvas.value.width, canvas.value.height);
    ctx.value.clearRect(0, 0, canvasContainer.value.width, canvasContainer.value.height);
    // ctx.value.putImageData(imageData, 0, 0);
}

const handleMouseMove = (event) => {
    // mouseX = event.clientX - rect.left;
    clearCanvas();
    // ctx.value.clearRect(0, 0, canvas.value.width, canvas.value.height);
    const rect = plot.value.getCanvas().getBoundingClientRect();
    // drawLine();
    mouseX = event.clientX - rect.left;

    // prevMouseX = mouseX;
    // if (prevMouseX !== null) {
    //     console.log(prevMouseX, mouseX)
    //     ctx.value.beginPath();
    //     ctx.value.strokeStyle = 'white';
    //     ctx.linwWidth = 2
    //     ctx.value.moveTo(prevMouseX, 0);
    //     ctx.value.lineTo(prevMouseX, canvas.value.height);
    //     ctx.value.stroke();
    // }
    ctx.value.beginPath();
    ctx.value.strokeStyle = 'red';
    ctx.value.moveTo(mouseX, 0);
    ctx.value.lineTo(mouseX, canvasContainer.value.height);
    ctx.value.stroke();
    console.log('mousemove', mouseX)
}


const data = ref([])

const handleMouseDown = (event) => {
    // const rect = plot.value.getCanvas().getBoundingClientRect();
    // mouseX = event.clientX - rect.left;
    console.log('mousedown', mouseX)
    // clearCanvas();
    // while(canvas.value.firstChild) {
    //     canvas.value.removeChild(canvas.value.firstChild);
    // }
    // _drawPlot(canvas.value, data.value);
    console.log(elementWidth.value, maxBin.value, minBin.value, elementX.value)
    const binNumber = Math.floor((maxBin.value - minBin.value) * (elementX.value / elementWidth.value) + minBin.value);
    console.log(binNumber)
    const xvalues = getBinData(binNumber, data.value);
    const xvalues3 = [{
        color: 'red',
        data: xvalues
    }]
    console.log(data.value)
    console.log(xvalues)
    plot.value.setData(xvalues3);
    plot.value.draw();
}
// const canvasLine = ref(null)
// const toggleLine = () => {
//     // console.log(ctx.value)
//     clearCanvas();
//     if (isSelective.value) {
//         // toggleBtn.value.innerText = "Hide Line";
//         canvasContainer.value.addEventListener("mousemove", handleMouseMove);
//         canvasContainer.value.addEventListener("mousedown", handleMouseDown);
//         drawLine();
//     } else {
//         // toggleBtn.value.innerText = "Toggle Line";
//         canvasContainer.value.removeEventListener("mousemove", handleMouseMove);
//         canvasContainer.value.removeEventListener("mousedown", handleMouseDown);
//     }
//     // console.log('toggle')
// }



const findMatchingZoomIndex = (targetResolution, resolutionArray) => {
    // const isObject = resolutionArray.length > 0 && resolutionArray[0].index !== undefined
    const isObject = false
    for (let z = resolutionArray.length - 1; z > 0; z--) {
        const binSize = isObject ? resolutionArray[z].binSize : resolutionArray[z]
        const index = isObject ? resolutionArray[z].index : z
        if (binSize >= targetResolution) {
            return index
        }
    }
    return 0
};



const plotVirtual4C = (straw, chrom, start, end, canvasEle, resolution) => {
    const newChrom = chrom.replace(/chr/g, '')
    console.log(newChrom, start, end, resolution)
    straw.getContactRecords(
        "NONE",
        { chr: newChrom, start: start, end: end },
        { chr: newChrom, start: start, end: end },
        "BP",
        5000
    )
        .then(function (d) {
            const maxBin1 = d3.max(d, function (d) { return d.bin1; })
            const minBin1 = d3.min(d, function (d) { return d.bin1; })
            const maxBin2 = d3.max(d, function (d) { return d.bin2; })
            const minBin2 = d3.min(d, function (d) { return d.bin2; })
            minBin.value = Math.min(minBin1, minBin2);
            maxBin.value = Math.max(maxBin1, maxBin2)
            const middleBin = Math.floor((minBin.value + maxBin.value) / 2)
            console.log(maxBin.value)

            const xvalues = getBinData(middleBin, d);
            data.value = d
            const xvalues3 = [{
                color: 'red',
                data: xvalues
            }]
            
            // console.log(xvalues3)
            plot.value = _drawPlot(canvasEle, xvalues3);
            //     console.log(canvas.value)
            //     canvas.value.addEventListener('plothover', function (event, pos, item) {
            //         if (item) {
            //             alert("You clicked point " + item.dataIndex + " in " + item.series.label + ".");
            //             console.log("You clicked at " + pos.x + ", " + pos.y);
            //             // axis coordinates for other axes, if present, are in pos.x2, pos.x3, ...
            //             // if you need global screen coordinates, they are pos.pageX, pos.pageY

            //             // highlight(item.series, item.datapoint);
            //             console.log("You clicked a point!");
            //         }
            //     })
            ctx.value = canvasEle.getElementsByTagName("canvas")[1].getContext("2d")

        });
}
// import { useMiddlePanelWidth } from '../../hooks/useLayout'
// import { FileSearchOutlined } from '@ant-design/icons-vue';

// const { eleWidth } = useMiddlePanelWidth()
// const { elementX, elementY, elementWidth } = useMouseInElement(canvasContainer.value)

onMounted(async () => {
    const metaData = await straw.getMetaData()
    const bpResolutions = metaData['resolutions']


    //     watch(, (newValue) => {
    //     console.log(isSelective.value)
    //     // clearCanvas();
    //     // if (newValue) {
    //     //     // toggleBtn.value.innerText = "Hide Line";
    //     //     canvasContainer.value.addEventListener("mousemove", handleMouseMove);
    //     //     canvasContainer.value.addEventListener("mousedown", handleMouseDown);
    //     //     drawLine();
    //     // } else {
    //     //     // toggleBtn.value.innerText = "Toggle Line";
    //     //     canvasContainer.value.removeEventListener("mousemove", handleMouseMove);
    //     //     canvasContainer.value.removeEventListener("mousedown", handleMouseDown);
    //     // }

    // })

    watch([() => isActive.value, () => chrom.value, () => start.value, () => end.value], () => {

        if (end.value - start.value < visibilityWidth) {

            if (!isActive.value) {
                message.value = 'Please turn on the plot first'
                return
            }
            console.log('end.value - start.value < visibilityWidth')
            isVisible.value = true


            showSpin.value = true
            console.log(canvasContainer.value.style.width)

            let targetResolution = Math.max((end.value - start.value) / width.value, (end.value - start.value) / width.value)
            let zoomIndex = findMatchingZoomIndex(targetResolution, bpResolutions)
            plotVirtual4C(straw, chrom.value, start.value, end.value, canvasContainer.value, bpResolutions[zoomIndex])
            showSpin.value = false;
        } else {
            console.log('not visible')
            isVisible.value = false

        }
    }, { immediate: true })


    // watch(, () => {
    //     if (!isActive.value) {
    //         message.value = 'Please turn on the plot first'
    //     }
    // })

    watch(() => width.value, () => {
        showSpin.value = true
        if (width.value > 0) {
            let targetResolution = Math.max((end.value - start.value) / width.value, (end.value - start.value) / width.value)
            let zoomIndex = findMatchingZoomIndex(targetResolution, bpResolutions)
            plotVirtual4C(straw, chrom.value, start.value, end.value, canvasContainer.value, bpResolutions[zoomIndex])
        }
        showSpin.value = false;
    })


});




</script>