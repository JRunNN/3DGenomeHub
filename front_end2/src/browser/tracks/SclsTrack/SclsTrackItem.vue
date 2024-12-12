<template>
    <n-scrollbar v-if="isVisible">
        <div ref="canvasContainer" class="basic-canvas" :style="props.style">
            <canvas ref="canvas"></canvas>
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
import { ref, onMounted, watch, computed } from 'vue';
import { fetchBedFileData } from '../../service/base'
import { drawPlotX } from '../../hooks/BaseRowTrack'
import { useElementSize } from '@vueuse/core'
import { TabixIndexedFile } from '@gmod/tabix'
import { RemoteFile } from 'generic-filehandle'

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

// const corenavStore = usecorenavStore()


// const { chrom, min, max, start, end, isLoaded, chromSizes, chromBands } = storeToRefs(corenavStore)

const prepad = ref(0)
const postpad = ref(0)
const h = ref(8)
const canvasContainer = ref(null)
const canvas = ref(null)
const clickable = ref(false)
const hpad = ref(10) // distance between glyphs (used in intersection)
const showLabel = ref(false)
const label = ref(null)
const linklayer = ref(null)

const { width, height } = useElementSize(canvasContainer.value)

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

const url = props.option.url
// const trackId = ref(props.trackId)
const isVisible = ref(false)
let visibilityWidth = 10000000
const canvasReady = ref(false)
// function isCanvasBlank(canvas) {
//     return !canvas.getContext('2d')
//         .getImageData(0, 0, canvas.width, canvas.height).data
//         .some(channel => channel !== 0)
// }

// Define a function that takes two arguments:
// `element`: The DOM element for which we want to store data.
// `name` (optional): The string name of the property to set or retrieve,
//                    or an object of name-value pairs.
//                    If it's not provided or undefined, return all the data
//                    associated with the element as an object.
// function data(element, name) {
//     // Create a reference to the element's dataset, which stores attributes prefixed with "data-".
//     var dataset = element.dataset;

//     // If the second parameter is undefined, return all the data associated with the element.
//     if (name === undefined) {
//         // Create an empty object to store the data.
//         var result = {};

//         // Loop through all the properties of the dataset.
//         for (var prop in dataset) {
//             // Check if the property is an actual data-* attribute
//             if (/^data-\w+/.test(prop)) {
//                 // Get the property value by removing the "data-" prefix and converting the camel-cased name
//                 // to hyphen-separated form using a regular expression.
//                 var propName = prop.substr(5).replace(/-([a-z])/g, function (match, letter) {
//                     return letter.toUpperCase();
//                 });

//                 // Add the property and its value to the result object.
//                 result[propName] = dataset[prop];
//             }
//         }

//         // Return the result object.
//         return result;
//     }

//     // Handle the case where the name is a string.
//     if (typeof name === "string") {
//         // Check if the name represents a single property.
//         if (arguments.length === 2) {
//             // Retrieve the value of the specified property.
//             return dataset["data-" + name];
//         } else {
//             // Split the name into an array of property names.
//             var props = name.split(/\s+/);

//             // If there are no properties, return undefined.
//             if (props.length === 0) {
//                 return undefined;
//             }

//             // Create an object to store the values of the specified properties.
//             var result = {};

//             // Add each specified property and its value to the result object.
//             for (var i = 0; i < props.length; i++) {
//                 var propName = props[i].replace(/-([a-z])/g, function (match, letter) {
//                     return letter.toUpperCase();
//                 });
//                 result[props[i]] = dataset["data-" + propName];
//             }

//             // Return the result object.
//             return result;
//         }
//     }

//     // Handle the case where the name is an object.
//     if (typeof name === "object") {
//         // For each property in the object, set the corresponding data attribute on the element.
//         for (var prop in name) {
//             element.dataset["data-" + prop] = name[prop];
//         }
//     }
// }



// const _createLayer = (canvasHolder) => {
//     var canvas = canvasHolder.find(">canvas");
//     return $("<div>").css({
//         position: "absolute",
//         top: canvas.position().top,
//         left: canvas.position().start,
//         width: canvas.width() - 16,
//         height: canvas.height(),
//         'overflow-x': 'hidden',
//         'overflow-y': 'hidden',
//         margin: 0
//     }).mousewheel(function (ev, d, dx, dy) {
//         var top = canvasHolder.scrollTop();
//         canvasHolder.scrollTop(top - 36 * d);
//         if (top !== canvasHolder.scrollTop()) ev.preventDefault();

//     }).appendTo(canvasHolder);
// }


const _measureWidth = (canvas, w, scls, c, showLable) => {
    // determine which part of canvas will be used to draw given scls
    var ctx = canvas.getContext("2d"),
        cstart = Math.max(1, c(scls.start)),
        cend = Math.min(w, c(scls.end + 1)),
        actualWidth = Math.max(cend - cstart, showLable ? ctx.measureText(scls._text).width : 0);

    return { start: cstart, end: cstart + actualWidth };
}




const _makeLabel = (item, templ) => {
    if ((label.value == null || label.value === '') && templ == null) return '';
    if (templ != null) label.value = templ;

    // if (_.isString(label)) {
    //     return $.tmpl(label, item).text(); // use template (TODO: use compiled template)
    // } else if (_.isFunction(label)) {
    //     return label(item); // normal function
    // }
    if (typeof label === "string") {
        return $.tmpl(label, item).text();
    } else if (typeof label === "function") {
        return label(item);
    }
    return ''; // catch-all
}

const _addLinks = (parent, canvas, y, w, h, postpad, scls, c) => {
    // determine which part of canvas will be used to draw given scls
    var ctx = canvas.getContext("2d");

    var cstart = Math.max(1, c(scls.start)),
        cend = Math.min(w, c(scls.end + 1)),
        actualWidth = Math.max(cend - cstart, showLabel.value ? ctx.measureText(scls._text).width : 0);
    left = cstart;

    var elem = $("<div>").css({
        position: "absolute",
        top: y,
        left: left,
        //"background-color": "rgba(255, 0, 0, 0.3)",
        width: actualWidth,
        height: h + postpad,
        cursor: "pointer"
    }).attr({
        title: scls._tooltip
    }).appendTo(parent);
    return elem;
}

const _getColor = (colors, comp, item) => { // comp <- (line|outline|fill)
    if (colors == null) return 'black'; // paranoid check
    var defaultValue = colors._ || 'black', // if specific type is not found, use wildcard "_"
        c = colors[comp] || defaultValue;

    // if (!_.isFunction(c)) return c;
    if (typeof c !== "function") return c;

    var args = $.extend({
        comp: comp, // component type
        element: item,

        cluster: item, // for backward compatibility
        tag: item // for backward compatibility
    });
    return c(args) || defaultValue; // in case the function doesn't return valid value
}


const _drawAnchor = (ctx, x, y, w, h, l_, r_) => {
    var h_ = h / 2, w_ = h / 3,
        // whether the sides should protrude or not; possible values: (-1,0,1)
        l = l_ || 0, r = r_ || 0;
    ctx.save();
    ctx.clearRect(x, y, w, h);
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x + w, y);
    // ctx.lineTo(x + w + w_ * r, y + h_);
    ctx.lineTo(x + w, y + h);
    ctx.lineTo(x, y + h);
    // ctx.lineTo(x + w_ * l, y + h_);
    ctx.lineTo(x, y);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
}

const _drawItem = (canvas, x, y, w, h, scls, colors, c) => {
    console.log(scls)
    var ctx = canvas.getContext("2d"),
        hRatio = h / 8,
        cstart = Math.max(1, c(scls.start)),
        cend = Math.min(w, c(scls.end + 1));

    ctx.save();
    ctx.translate(0, y + h / 2);
    ctx.lineWidth = 1;

    ctx.strokeStyle = _getColor(colors, "outline", scls);
    ctx.fillStyle = _getColor(colors, "fill", scls);

    var prot = 1;
    if (scls.strand == "+") prot = 1; else if (scls.strand == "-") prot = -1;
    _drawAnchor(ctx, cstart, -3 * hRatio, cend - cstart, 6 * hRatio, prot, prot); // _drawClusterAnchor: function(ctx, x, y, w, h, l_, r_)

    if (showLabel.value) {
        // console.log('showLabel')
        // 5. write symbol/accession
        ctx.fillStyle = _getColor(colors, "text", scls);
        ctx.font = "normal 9px sans-serif";
        ctx.textAlign = "left";
        ctx.fillText(scls._text, cstart, 6 * hRatio + 6);
    }

    ctx.restore();
}

const _resize = () => {
    // by default, do nothing
    // only coverage-type tracks would want to redraw
}

const _adjustTitle = (modifier, onfinish) => {
    var track = this.element,
        opts = this.options;

    opts._title.css({
        width: track.height() - 12 // magic number
    });
    if (onfinish) onfinish();
}

// watch(items, (newItems) => {
//     console.log(newItems)
//     drawPlotX(newItems, false)
// })

// Example usage:
// var parser = new BED()
// let results
// const tracksStore = usetracksStore()

const data = ref([]);
const filteredData = ref([]);
const cacheKey = ref('');
// const url = '/data/BASIC_H1.S-anchor.bed';
const filename = url.substring(url.lastIndexOf('/') + 1);


const file = new TabixIndexedFile({
    filehandle: new RemoteFile(url),
    tbiFilehandle: new RemoteFile(url + '.tbi')
})



const option = computed(()=> {
    return props.option
})
onMounted(() => {
    watch([()=>option.value.series,() => chrom.value,() => start.value, () => end.value], async (newStart, newEnd) => {
        showSpin.value = true
        if (end.value - start.value < visibilityWidth) {
            isVisible.value = true
            canvasReady.value = false
            let lines = []
            await file.getLines(chrom.value, start.value, end.value, function(line, fileOffset) {
                // data.value = d;
                // console.log(d)
                // console.log(newKey)
                // filteredData.value = filterData(d);
                // console.log((filteredData.value)
                // console.log('filteredData', filteredData.value)
                // console.log(canvasContainer.value)
                // if (filteredData.value.length === 0) {
                //     console.log("No data in this region")
                //     isVisible.value = false
                //     return
                // }
                const arr = line.split(/[\s]+/)
                const addedData = {
                chrom: arr[0],
                start:  Number(arr[1]),
                end:  Number(arr[2])
            }
            lines.push(addedData)


            })
                             console.log(lines)
                            drawPlotX(canvas.value, lines, false, canvasContainer.value, h.value, prepad.value, postpad.value, showLabel.value, _drawItem, _measureWidth, start.value, end.value)
                // console.log('ddddddddddddddddddddd')
                canvasReady.value = true;
                showSpin.value = false;
        } else {
            isVisible.value = false
            canvasReady.value = true
        }
    }, { immediate: true });


    watch(() => width.value, () => {
        showSpin.value = true
        // console.log(eleWidth.value)
        // canvasContainer.value.style.width = eleWidth.value + 'px'
        if(width.value>0) {
        drawPlotX(canvas.value, filteredData.value, false, canvasContainer.value, h.value, prepad.value, postpad.value, showLabel.value, _drawItem, _measureWidth, start.value, end.value)
        }
        showSpin.value = false;
    })


})


</script>


<style scoped></style>