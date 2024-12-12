<template>
    <div :id="`${props.trackId}` + '-canvascontainer'" ref="canvasContainer" :style="props.style">
        <n-spin v-show="showSpin" class="absolute left-1/2 top-1/2"></n-spin>
        <canvas ref="canvasRef" style="width:100%;height:100%;"></canvas>
    </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watch, computed, defineEmits, defineProps } from 'vue';
import { BigWig }  from '@gmod/bbi'
import { RemoteFile } from 'generic-filehandle'
import { useElementSize } from '@vueuse/core'
import * as d3 from "d3"
import { WebglPlot, ColorRGBA, WebglLine,WebglSquare} from "webgl-plot";

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
    },
    trackId: {
        type: String,
        required: true
    }
})

const option = computed(()=> {
    return props.option
})
const emit = defineEmits(['zoomTo'])

// const cvs_holder = ref(null)
// const canvas = ref(null)
// const corenavStore = usecorenavStore()
// const { chrom, min, max, start, end, isLoaded, chromSizes, chromBands } = storeToRefs(corenavStore)
const canvasContainer = ref(null)
const canvasRef = ref(null)
// const canvas = ref(null)
const canvasReady = ref(false)
const showSpin = ref(false)
const chrom = computed(
    () => props.location.chrom
)

const start = computed(
    () => props.location.start
)

const end = computed(
    () => props.location.end
)

const min = computed(
    () => props.location.min
)

const max = computed(
    () => props.location.max
)

const urls = [option.value.url]


const { width, height } = useElementSize(canvasContainer)


function largestTriangleThreeBucket(data, threshold, xProperty, yProperty) {
    /**
     * This method is adapted from the 
     * "Largest Triangle Three Bucket" algorithm by Sveinn Steinarsson
     * In his 2013 Masters Thesis - "Downsampling Time Series for Visual Representation"
     * http://skemman.is/handle/1946/15343
     *
     * The MIT License
     *  
     * Copyright (c) 2013 by Sveinn Steinarsson
     *
     * Permission is hereby granted, free of charge, to any person obtaining a copy
     * of this software and associated documentation files (the "Software"), to deal
     * in the Software without restriction, including without limitation the rights
     * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
     * copies of the Software, and to permit persons to whom the Software is
     * furnished to do so, subject to the following conditions:
     * The above copyright notice and this permission notice shall be included in
     * all copies or substantial portions of the Software.
     * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
     * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
     * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
     * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
     * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
     * THE SOFTWARE.
     * --------------------------------------------------------------------------------------------------------
     */
    yProperty = yProperty || 0;
    xProperty = xProperty || 1;

    var m = Math.floor,
        y = Math.abs,
        f = data.length;

    if (threshold >= f || 0 === threshold) {
        return data;
    }

    var n = [],
        t = 0,
        p = (f - 2) / (threshold - 2),
        c = 0,
        v,
        u,
        w;

    n[t++] = data[c];

    for (var e = 0; e < threshold - 2; e++) {
        for (var g = 0,
            h = 0,
            a = m((e + 1) * p) + 1,
            d = m((e + 2) * p) + 1,
            d = d < f ? d : f,
            k = d - a; a < d; a++) {
            g += +data[a][xProperty], h += +data[a][yProperty];
        }

        for (var g = g / k,
            h = h / k,
            a = m((e + 0) * p) + 1,
            d = m((e + 1) * p) + 1,
            k = +data[c][xProperty],
            x = +data[c][yProperty],
            c = -1; a < d; a++) {
            "undefined" != typeof data[a] &&
                (u = .5 * y((k - g) * (data[a][yProperty] - x) - (k - data[a][xProperty]) * (h - x)),
                    u > c && (c = u, v = data[a], w = a));
        }

        n[t++] = v;
        c = w;
    }

    n[t++] = data[f - 1];

    return n;
}

const _makeInitialRequest = (canvasEle, xdata) => {

    var xvalues = [],
        l = start.value,
        r = end.value,
        w = canvasEle.offsetWidth,
        step = (r - l) / w;

    // var ylog = _get(_get(opts._options, "yaxis", {}), "log");
    // const ylog = false
    // for (var k in xdata) {
    //     var values = [],
    //         data = xdata[k];

    //     // modifier
    //     // var negate = _get(opts._sries, k, {}).negate;
    //     const negate = false

    //     for (var i = 0; i < w; i++) {
    //         var v = data[i];
    //         if (ylog && v > 0) v = Math.log(v) / Math.log(ylog);
    //         if (negate) v = -v;
    //         values.push([i * step + l, v]);
    //     }

    //     xvalues.push($.extend(_get(opts._series, k, {}), { data: values }));
    // }
    const xvalues2 = xdata.map(obj => {
        const average = (obj.start + obj.end) / 2;
        const score = obj.score;
        return { pos: average, score: score };
        // return [average,score]
    });

    const xvalues3 = [{
        color: option.value.series[0].lineStyle.color,
        data: xvalues2
    }]
    // console.log(xvalues3)
    //_drawPlot(canvasEle, xvalues3);
    canvasReady.value = true;

    // const offscreen = canvasEle.transferControlToOffscreen()
    return {
        // canvasEle: canvasEle,
        drawData: xvalues3
    }

}

function _get(dict, key, altval) {
    return (dict == null) ? altval : (dict[key] == null ? altval : dict[key]);
}

const filteredData = ref([]);
const cacheKey = ref('');
// const filename = url.substring(url.lastIndexOf('/') + 1);

// const file = new BigWig({
//     filehandle: new RemoteFile(url)
// }
// )
console.log(urls)
// const local = new LocalFile('/some/file/path/file.txt')

const files = urls.map(url => {
    const filehandle = new RemoteFile(url)
    return new BigWig({
        filehandle: filehandle
    })
})

function calculateScale(start, end, viewportWidth) {
    // Calculate the size of the genomic region
    const regionSize = end - start;

    // Calculate the number of base pairs per pixel that would fit in the viewport
    const bpPerPixel = regionSize / viewportWidth;

    // Set a minimum scale factor of 1, to avoid dividing by 0 or a negative number
    const minScale = 1;

    // Calculate the scale factor based on the number of base pairs per pixel
    const scale = Math.max(minScale, 1 / bpPerPixel);

    return scale;
}

// const socket = new WebSocket("ws://localhost:8088");
// const message = ref('')
//     socket.onmessage = (event) => {
//       message.value = event.data;
//       console.log()
//       console.log(message.value)
//     };

//     socket.onopen = (event) => {
//       socket.send('Hello R Server!');
//     };

const hexToRGB = hex => {
  let alpha = false,
    h = hex.slice(hex.startsWith('#') ? 1 : 0);
  if (h.length === 3) h = [...h].map(x => x + x).join('');
  else if (h.length === 8) alpha = true;
  h = parseInt(h, 16);
  return (
    'rgb' +
    (alpha ? 'a' : '') +
    '(' +
    (h >>> (alpha ? 24 : 16)) +
    ', ' +
    ((h & (alpha ? 0x00ff0000 : 0x00ff00)) >>> (alpha ? 16 : 8)) +
    ', ' +
    ((h & (alpha ? 0x0000ff00 : 0x0000ff)) >>> (alpha ? 8 : 0)) +
    (alpha ? `, ${h & 0x000000ff}` : '') +
    ')'
  );
};




let color;
onMounted(() => {


    watch([()=>option.value.series,() => width.value, () => chrom.value, () => start.value, () => end.value], () => {

        canvasRef.value.width =width.value
        canvasRef.value.height = height.value
        const wglp = new WebglPlot(canvasRef.value);
        wglp.removeAllLines();
        // console.log(canvasRef.value.width, canvasRef.value.height)
        showSpin.value = true
        const scale = calculateScale(start.value, end.value, 1000);
        // console.log(scale)

        // An array of Promises that each call file.getFeatures() and return the result
        const featurePromises = files.map(file => {
            console.log(chrom.value, start.value, end.value,scale)
            return file.getFeatures(chrom.value, start.value, end.value, { scale: scale });
        });
        
        for (let i = 0; i < featurePromises.length; i++) {
            featurePromises[i].then(res => {

                // console.log(res)
                let dat = _makeInitialRequest(canvasContainer.value, res).drawData[0].data

                console.log(dat.length)
                if (dat.length > 1000) {
                    dat = largestTriangleThreeBucket(dat, 100000, 'pos', 'score')
                }
                // console.log(dat)
                // if (!color) {
                //     color = new ColorRGBA(Math.random(), Math.random(), Math.random(), 1);
                // }
                // console.log(option)
                const colorA  = option.value.series[0].lineStyle.color.match(/\d+/g).map(Number)
                const color =  new ColorRGBA(colorA[0]/255, colorA[1]/255,colorA[2]/255,1)
                //console.log(color)
                // console.log(dat)
                //console.log(dat)
                const Y = d3.map(dat, d => d.score);
                const yDomain = [0, d3.max(Y)];
                const yScale = d3.scaleLinear(yDomain, [-1,1]);

                // const X = d3.map(dat, d => d.score);
                const xDomain = [start.value, end.value];
                const xScale = d3.scaleLinear(xDomain, [-1,1 ]);


                for (let j = 0; j < dat.length; j++) {
                    // console.log(dat[j].pos, dat[j].score)
                    //line.setX(j, xScale(dat[j].pos))
                    // line.arrangeX();

                    //line.setY(j, yScale(dat[j].score))

                    const line = new WebglSquare(color);
                    line.setSquare(xScale(dat[j].pos)-0.01, 0.5-0.01, xScale(dat[j].pos)+0.01, 0.5+0.01)
                    wglp.addSurface(line)

                    // line.constY(0.5)
                }
                // console.log(line)
                //console.log(wglp.linesData)
            })
        }

        function newFrame() {
            wglp.update();
            requestAnimationFrame(newFrame);
        }
        requestAnimationFrame(newFrame);
        showSpin.value = false
    }, { immediate: true,deep:true });


})

</script>