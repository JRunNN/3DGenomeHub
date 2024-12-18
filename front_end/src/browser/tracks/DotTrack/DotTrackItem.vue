<template>
  <div class="relative h-full w-full">

    <div v-if="isVisible">
      <div ref="canvasContainer" class="basic-canvas aspect-ratio" :style="props.style">
        <n-spin :show="showSpin" class="absolute left-1/2 top-1/2">
          <div></div>
        </n-spin>
      </div>
    </div>
    <div v-else>
      <div ref="canvasContainer" class="basic-canvas">
        <n-alert title="" type="warning">
          No data in this region.
        </n-alert>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watch, computed, defineProps } from 'vue';
import { useElementSize } from '@vueuse/core'
import * as d3 from "d3";
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
  style: {
    type: Object,
    required: true
  },
  dataLoaded: {
    type: Boolean,
    required: false
  }
})

const chrom = computed(
  () => props.location.chrom
)

const start = computed(
  () => props.location.start
)

const end = computed(
  () => props.location.end
)

const corenavStore = ref({
  asm: 'hg38',
  chrom: props.location.chrom,
  start: props.location.start,
  end: props.location.end,
  max: 0,
  min: 0,
  size: 0
})
const url = props.option.url

// const type = ref('square')
const isVisible = ref(true)
const showSpin = ref(false)

const canvasContainer = ref(null)
const { width, height } = useElementSize(canvasContainer)
const file = new TabixIndexedFile({
  filehandle: new RemoteFile(url),
  tbiFilehandle: new RemoteFile(url + '.tbi')
})


const type = ref('triangle')
function createTooltip(element, text) {
  // Create the tooltip div
  const tooltip = document.createElement('div');
  tooltip.className = 'tooltip';
  tooltip.textContent = text;

  // Append the tooltip to the body
  document.body.appendChild(tooltip);

  // Function to show the tooltip
  function showTooltip(e) {
    tooltip.style.opacity = '1';
    tooltip.style.top = `${e.pageY + 10}px`;
    tooltip.style.left = `${e.pageX + 10}px`;
  }
  // Function to hide the tooltip
  function hideTooltip() {
    tooltip.style.opacity = '0';
  }

  // Attach the event listeners
  element.addEventListener('mouseover', showTooltip);
  element.addEventListener('mousemove', showTooltip);
  element.addEventListener('mouseout', hideTooltip);
}


const plotHic = (dataset, canvasWidth, canvasHeight) => {
  const minCount = d3.min(dataset, function (d) { return d.score; })
  const maxCount = d3.max(dataset, function (d) { return d.score; });

  const margin = { top: 0, right: 0, bottom: 0, left: 0 },
    width = canvasWidth,
    height = canvasWidth;

  // const tooltip = d3.select("body").append("div")
  //   .attr("id", "tooltip")
  //   .style("opacity", 1);

  const xScale = d3.scaleLinear()
    .domain([start.value, end.value])
    .range([0, width]);

  const xScaleRef = xScale.copy();

  const yScale = d3.scaleLinear()
    .domain([start.value, end.value])
    .range([height, 0]);

  // Create a sequential color scale
  const colorScale = d3.scaleSequential()
    .domain([0, maxCount])
    .interpolator(d3.interpolateReds);

  const xAxis = d3.axisTop().scale(xScale);
  const yAxis = d3.axisLeft().scale(yScale);

  const tooltip = d3.select("#canvasContainer").append("div")
    .attr("id", "tooltip")
    .style("opacity", 0);

  // Canvas setup
  const canvas = d3.select(canvasContainer.value)
    .append("canvas")
    .attr("width", width)
    .attr("height", height)
    .style("left", margin.left + "px")
    .style("bottom", margin.bottom + "px")
    .style("position", "absolute");

  // const crosshairColor = 'rgba(170, 0, 0, 0.80)';
  // const crosshairWidth = 3;
  // const crosshairVisible = ref(false);

  // let canvasOverlay = d3.select(canvasContainer.value)
  //   .append("canvas")
  //   .attr("width", width)
  //   .attr("height", height)
  //   .style("left", margin.left + "px")
  //   .style("bottom", margin.bottom + "px")
  //   .style("position", "absolute")
  //   .on("mousemove", event => mousemove(event))
  //   .on("mouseout", event => mouseout(event));

  // const ctxOverlay = canvasOverlay.node().getContext("2d");
  // ctxOverlay.translate(width / 2, height / 2);
  // ctxOverlay.rotate(Math.PI / 4);
  // ctxOverlay.scale(1 / Math.sqrt(2), 1 / Math.sqrt(2));

  // const mouseout = (event) => {
  //   if (crosshairVisible.value) {
  //     ctxOverlay.clearRect(0, 0, canvasOverlay.node().width, canvasOverlay.node().height);
  //     crosshairVisible.value = false;
  //   }
  // }

  // function getTransformedCoordinates(mouseX, mouseY) {
  //   var x = mouseX - width / 2;
  //   var y = mouseY - height / 2;
  //   var angle = -Math.PI / 4;
  //   var scale = Math.sqrt(2);

  //   var transformedX = x * scale * Math.cos(angle) - y * scale * Math.sin(angle);
  //   var transformedY = x * scale * Math.sin(angle) + y * scale * Math.cos(angle);

  //   return { x: transformedX, y: transformedY };
  // }

  // function drawCrosshair(ctx, canvas, x, y) {
  //   var transformedCoords = getTransformedCoordinates(x, y);
  //   ctx.save();
  //   ctx.setTransform(1, 0, 0, 1, 0, 0);
  //   ctx.clearRect(0, 0, canvas.width, canvas.height);
  //   var endX = width / 2;
  //   var endY = height / 2;
  //   ctx.restore();

  //   ctx.beginPath();
  //   ctx.strokeStyle = 'blue';
  //   ctx.lineWidth = crosshairWidth;
  //   ctx.moveTo(transformedCoords.x, transformedCoords.y);
  //   ctx.lineTo(width, transformedCoords.y);
  //   ctx.stroke();

  //   ctx.beginPath();
  //   ctx.strokeStyle = 'blue';
  //   ctx.moveTo(transformedCoords.x, transformedCoords.y);
  //   ctx.lineTo(transformedCoords.x, height);
  //   ctx.stroke();

  //   return { x: transformedCoords.x, y: transformedCoords.y };
  // }

  // function updateCrosshairPosition(canvas, event) {
  //   var rect = canvas.getBoundingClientRect();
  //   var x0 = event.clientX - rect.left;
  //   var y0 = event.clientY - rect.top;
  //   const { x, y } = drawCrosshair(ctxOverlay, canvasOverlay.node(), x0, y0);

  //   var x1 = Math.round(xScale.invert(x));
  //   var y1 = Math.round(yScale.invert(y));

  //   if (x1 > xScaleRef.domain()[1]) x1 = xScaleRef.domain()[1];
  //   if (x1 < xScaleRef.domain()[0]) x1 = xScaleRef.domain()[0];
  //   if (y1 > yScale.domain()[1]) y1 = yScale.domain()[1];
  //   if (y1 < yScale.domain()[0]) y1 = yScale.domain()[0];

  //   const d = dataset.filter((item) => {
  //     return (Math.abs((item.start1 + item.end1) / 2 - x1) < width / 10) &&
  //       Math.abs(((item.start2 + item.end2) / 2 - y1) < width / 10);
  //   });

  //   if (!d[0]) {
  //     createTooltip(canvas, `${x1} - ${y1}: 0`);
  //   } else {
  //     createTooltip(canvas, `${d[0].start1} - ${d[0].start2}: ${d[0].score}`);
  //   }
  // }

  // const mousemove = (event) => {
  //   crosshairVisible.value = true;
  //   updateCrosshairPosition(canvasOverlay.node(), event);
  // }

  const svg = d3.select(canvasContainer.value)
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + [margin.left, margin.top] + ")");

  const ctx = canvas.node().getContext("2d");

  const renderXAxis = svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + yScale(0) + ")")
    .call(xAxis);

  const k = d3.event ? d3.event.transform.k : 1;
  const dw = 1 * k;

  ctx.translate(width / 2, height / 2);
  ctx.rotate(Math.PI / 4);
  ctx.scale(1 / Math.sqrt(2), 1 / Math.sqrt(2));

  // Draw data points
  dataset.forEach(function (d) {
    const x = xScale((d.start1 + d.end1) / 2);
    const y = yScale((d.start2 + d.end2) / 2);
    const fill = colorScale(d.score);

    ctx.beginPath();
    ctx.rect(x, y, 10, 10);
    ctx.fillStyle = fill;
    // ctx.strokeStyle = fill;
    ctx.fill();
    ctx.stroke();
  });

  // Add color legend
  const legendWidth = 200;
  const legendHeight = 20;

  // Create gradient for legend
  ctx.save();
  ctx.setTransform(1, 0, 0, 1, 0, 0);

  const legendGradient = ctx.createLinearGradient(20, 0, legendWidth + 20, 0);
  const steps = 10;

  // for (let i = 0; i < steps; i++) {
  //   const t = i / steps;
  //   legendGradient.addColorStop(t, colorScale(maxCount * t));
  // }

  // Draw legend rectangle
  ctx.fillStyle = legendGradient;
  ctx.fillRect(20, height - 40, legendWidth, legendHeight);

  // Add legend labels
  ctx.fillStyle = 'black';
  // ctx.font = '12px Arial';
  // ctx.fillText('0', 20, height - 45);
  // ctx.fillText(maxCount.toFixed(2), 20 + legendWidth, height - 45);

  ctx.restore();

  showSpin.value = false;
}

// import { useMiddlePanelWidth } from '../../hooks/useLayout'
const option = computed(() => {
  return props.option
})

let lines;
onMounted(async () => {
  watch([() => option.value.series, () => chrom.value, () => start.value, () => end.value], async () => {
    const canvases = canvasContainer.value.querySelectorAll('canvas');
    canvases.forEach(canvas => {
      canvas.parentNode.removeChild(canvas);
    });
    showSpin.value = true

    lines = []
    await file.getLines(chrom.value, start.value, end.value, function (line, fileOffset) {
      // const splitData = line.split(/;/)
      const arr = line.split(/[\s,:-]+/)
      // const anchor = splitData[1].split(/,/)
      const addedData = {
        chrom: arr[0],
        start1: Number(arr[1]),
        end1: Number(arr[2]),
        chrom2: arr[3],
        start2: Number(arr[4]),
        end2: Number(arr[5]),
        score: Number(arr[6])//,
        // anchor1: anchor[0],
        // anchor2: anchor[1]
      }
      if(addedData['score'] > 1){lines.push(addedData)}

    })
    // console.log(lines)
    // _makeInitialRequest(canvasContainer.value, lines, width.value)
    //  showSpin.value = true
    // canvasContainer.value.innerHTML = ''

    plotHic(lines, width.value, height.value)


  }, { immediate: true, deep: true });

  watch([() => width.value, () => props.style], () => {
    const canvases = canvasContainer.value.querySelectorAll('canvas');
    canvases.forEach(canvas => {
      canvas.parentNode.removeChild(canvas);
    });
    showSpin.value = true
    plotHic(lines, width.value, height.value)
  });

})
</script>
<style scoped>
.custom-rotate {
  transform: rotate(90deg);
}
</style>