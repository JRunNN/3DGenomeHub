<template>
    <div ref="canvasContainer" :style="props.style">
        <n-spin v-show="showSpin" class="absolute left-1/2 top-1/2"></n-spin>
        <n-alert title="" type="default" :bordered="true">
      {{ selectedInfo }}
    </n-alert>
    </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watch, computed } from 'vue';
import { useElementSize } from '@vueuse/core'
import { TabixIndexedFile } from '@gmod/tabix'
import { RemoteFile } from 'generic-filehandle'
import { useMessage } from 'naive-ui'

// define props
const props = defineProps({
    location: {
        type: Object,
        required: true
    },
    option: {
        type: Object,
        required: true
    },
    style: {
        type: Object,
        required: true
    }
})
const message = useMessage()

const canvasContainer = ref(null)
const canvasReady = ref(false)
const emit = defineEmits(['canvasReady'])
const showSpin = ref(false)

const selectedInfo = ref('')

const chrom = computed(
    () => props.location.chrom
)

const start = computed(
    () => props.location.start
)

const end = computed(
    () => props.location.end
)

const url = props.option.url
console.log(url)


const { width, height } = useElementSize(canvasContainer)


function processOffsetHook(plot, offset) {

    offset.top = 0;
    offset.bottom = 0;
    offset.left = 0;
    offset.right = 0;
}
const plot = ref(null)
const _drawPlot = (canvas, xvalues, steps, displayStyle = 'basicStyle') => {

    // console.log(canvas, xvalues, steps)
    // var opts = this.options;
    // if (!xvalues) xvalues = opts._xvalues;

    // canvas.css({
    //     height: (100),
    //     width: (1152)
    // });
    // console.log(canvas)

    // canvas.style.width = '100%'
    // canvas.style.height = '100%'
    console.log(option.value.style)
    var params = {
        // curvy: true,
        style: option.value.style,
        opacity: option.value.series[0].areaStyle.opacity || 0.05,
        series: {
            lines: {
                show: true
            },
            points: {
                show:true
            }
        },
        grid: {
            show: false,
            borderWidth: 1,
            borderColor: '#a0aec0',
            // "minBorderMargin" controls the default minimum margin around the border - it's used to make sure that points aren't accidentally clipped by the canvas edge so by default the value is computed from the point radius.
            minBorderMargin: 0,
            clickable: true,
            hoverable: false,
            mouseActiveRadius: 1000

        },
        xaxis: {
            show: false,
            ticks: 0,
            min: start.value,
            max: end.value
        },
        yaxis: {
            show: true,
            labelWidth: -5,
            reserveSpace: false,
            // font: 26,
            tickFormatter: function (val, axis) {
                if (val / 1000 != 0 && val % 1000 == 0) return (val / 1000) + "k";
                return val;
            }
        }//,
        // hooks: {
        //     processOffset: [processOffsetHook]
        // }
    };

    if (displayStyle == 'basicCurve') {
        params.basicCurve = true
    } else if (displayStyle == 'flatCurve') {
        params.flatCurve = true
    }

    // extend xaxis/yaxis
    // params.xaxis = $.extend(params.xaxis, _get(opts._options, 'xaxis'));
    // params.yaxis = $.extend(params.yaxis, _get(opts._options, 'yaxis'));

    // var yaxis_log = _get(_get(opts._options, 'yaxis', {}), 'log');
    // if (yaxis_log) {
    //     params.yaxis.tickFormatter = function (val) {
    //         if (val === 0) return 0;
    //         var neg = val < 0 ? -1 : 1;
    //         val = Math.round(Math.pow(yaxis_log, Math.abs(val)));
    //         if (Math.round(val) != val) val = val.toFixed(val < 10 ? 1 : 0);
    //         if (val / 1000 != 0 && val % 1000 == 0) return (val / 1000) + "k";
    //         return val * neg;
    //     };
    // }
    // console.log(start.value, end.value, xvalues)
    console.log('draw curv==============================')
    const plotObj = $.plot(canvas, xvalues, params);

    return plotObj
    // console.log(plotObj.width(), plotObj.height(), plotObj.offset(), plotObj.getPlotOffset())
}







const _makeInitialRequest = (canvasEle, xdata, width) => {
    var xvalues = [],
        l = start.value,
        r = end.value,
        w = width,

        step = Math.round((r - l) / w);
    // console.log(w)
    // var yaxis_log = _get(_get(opts._options, 'yaxis', {}), 'log'),
    //     show_outbound = _get(_get(opts._options, 'outbound', {}), 'show', false);
    let yaxis_log = false,
        show_outbound = false
    // console.log(xdata)
    // for (var k in xdata) {
    var values = []
    var data = xdata

    for (var i in data) {
        var d = data[i];
        if (d.chrom != d.chrom2) continue; // skip inter-chrom

        var m = (d.start + d.end) / 2,
            n = (d.start2 + d.end2) / 2;

        if (yaxis_log) {
            d.score = Math.log(d.score) / Math.log(yaxis_log);
        }

        // if show_outbound=false, only show those that strictly within the viewing range
        var modif = (Math.min(m, n) < l || Math.max(m, n) > r) ? -1 : 1;
        if (show_outbound) {
            values.push([Math.min(m, n), Math.max(m, n), d.score * modif]);
        } else {
            if (modif >= 0) values.push([Math.min(m, n), Math.max(m, n), d.score]);
        }
    }

    let fillColor = option.value.series[0].areaStyle.color || 'transparent',
        strokeColor = option.value.series[0].lineStyle.color || 'red'

    // switch (strokeColor.toLowerCase()) {
    //     case 'auto':
    //         strokeColor = fillColor; break;
    //     case 'off':
    //     case 'false':
    //         strokeColor = null; break;
    // }

    xvalues.push({
        color: fillColor,
        strokeColor: strokeColor,
        data: values.sort(function (p, q) { return q[2] - p[2]; })
    });
    // }


    // console.log(xvalues)
    canvasReady.value = false
    // loadingStart()
    plot.value = _drawPlot(canvasEle, xvalues, step, option.value.style);
    // loadingFinish()
    let previousPoint  = null
    // console.log(plot.value)
    $(canvasEle).bind("plotclick", function (event, pos, item) {
        console.log('item clicked')
 console.log(event, pos, item)
        if (item) {

                // var x = item.datapoint[0].toFixed(2),
                //     y = item.datapoint[1].toFixed(2);

                // showTooltip(item.pageX, item.pageY,
                //     "Dia=" + x + ", Quota=" + y);
                    selectedInfo.value = `${item.dataIndex}, ${item.series.label}` 

            }

    });

//     function showTooltip(x, y, contents) {
//     $("<div id='tooltip'>" + contents + "</div>").css({
//         position: "absolute",
//         display: "none",
//         top: y + 5,
//         left: x + 5,
//         border: "1px solid #fdd",
//         padding: "2px",
//         "background-color": "#fee",
//         opacity: 0.80
//     }).appendTo("body").fadeIn(200);
//     console.log('sssssssss')
// }
    canvasReady.value = true;

    // if (canvasContainer.value) {
    //     canvasContainer.value.addEventListener('resize', () => {
    //         plot.resize();
    //         plot.setupGrid();
    //         plot.draw();
    //     })
    // }
    // return plot.value

}


function _get(dict, key, altval) {
    return (dict == null) ? altval : (dict[key] == null ? altval : dict[key]);
}

// import the gene annotation file from the server
// const tracksStore = usetracksStore()

// const data = ref([]);
const filteredData = ref([]);
const cacheKey = ref('');
// const url = '/data/BASIC_HBAD5RP_FKDL190764711-1a.e500.clusters.cis.chiasig.txt';
const filename = url.substring(url.lastIndexOf('/') + 1);


const file = new TabixIndexedFile({
    filehandle: new RemoteFile(url),
    tbiFilehandle: new RemoteFile(url + '.tbi')
})

const option = computed(() => {
    return props.option
})


onMounted(() => {
    console.log('CurvTrack Mounted==========================')
    watch([() => option.value, () => chrom.value, () => start.value, () => end.value], async () => {
        showSpin.value = true
        console.log(chrom.value, start.value, end.value)
        let lines = []
        console.log(url)
        await file.getLines(chrom.value, start.value, end.value, function (line, fileOffset) {
            const splitData = line.split(/;/)
            const arr = splitData[0].split(/[\s,:-]+/)
            const anchor = splitData[1].split(/,/)
            const addedData = {
                chrom: arr[0],
                start: Number(arr[1]),
                end: Number(arr[2]),
                chrom2: arr[3],
                start2: Number(arr[4]),
                end2: Number(arr[5]),
                score: Number(arr[6]),
                anchor1: anchor[0],
                anchor2: anchor[1]
            }
            lines.push(addedData)

        })

        _makeInitialRequest(canvasContainer.value, lines, width.value)
        showSpin.value = false


    }, { immediate: true, deep: true });

    watch([() => width.value, () => props.style], () => {
        showSpin.value = true
        // console.log(eleWidth.value)
        // canvasContainer.value.style.width = eleWidth.value + 'px'

        // _makeInitialRequest(canvasContainer.value, filteredData.value)
        if (width.value > 0 && plot.value) {
            plot.value.resize();
            plot.value.setupGrid();
            plot.value.draw();
        }

        showSpin.value = false
    });


    // watch(() => props.attrValue.h.value, (newValue) => {
    //     showSpin.value = true
    //     canvasContainer.value.style.height = newValue + 'px'
    //     _makeInitialRequest(canvasContainer.value, filteredData.value)       
    //      showSpin.value = false;
    // }, { deep: true });

});


//     $('#track_0_content')
//         //     // .addClass("basic-content ui-dialog-content ui-widget-content")
//         .resizable({
//             handles: "s",
//             resize: function () {
//                 $(".basic-canvas").css({ height: $(this).height() });
//                 self._adjustTitle(0);
//                 self._resize();
//             },
//             start: self.disableSlide,
//             stop: function () { self.enableSlide(); $("#" + trackId + "_content").css({ width: '' }); }
//         })
// })

// const dataLoaded = computed(
//     () => props.dataLoaded)
</script>