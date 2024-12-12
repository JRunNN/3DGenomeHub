<template>
    <!-- <div style="height:600px">
        <h1>cytoscape-cose-bilkent demo (compound)</h1>
        <button id="randomize" type="button">Randomize</button>
        <button id="layoutButton" type="button">CoSE-Bilkent</button>
        <div id="cy"></div>
        <n-alert title="可以没有边框" type="info" :bordered="true">
      {{ selectedInfo }}
    </n-alert>
    </div> -->
    <div ref="canvasContainer"  :style="props.style" style="height:600px">
        <!-- <n-spin v-show="showSpin" class="absolute left-1/2 top-1/2"></n-spin> -->
        <div id="cy"></div>
        <n-alert title="" type="default" :bordered="true">
      {{ selectedInfo }}
    </n-alert>
    </div>
</template>
  
<script setup lang="ts">
// You might need to adjust these imports depending on your build setup
import cytoscape from 'cytoscape';
import coseBilkent from 'cytoscape-cose-bilkent';
import { onMounted, watch, ref, computed } from 'vue'
import { TabixIndexedFile } from '@gmod/tabix'
import { RemoteFile } from 'generic-filehandle'
import { useMessage } from 'naive-ui'
const message = useMessage()

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
const option = computed(() => {
    return props.option
})
// const trackId = ref(props.trackId)
const isVisible = ref(true)
const selectedInfo = ref('')
let visibilityWidth = 1000000

const showSpin = ref(false)
cytoscape.use(coseBilkent);
const url = props.option.url

const file = new TabixIndexedFile({
    filehandle: new RemoteFile(url),
    tbiFilehandle: new RemoteFile(url + '.tbi')
})
const canvasReady = ref(false)
onMounted(() => {
    const cy = cytoscape({
        container: document.getElementById('cy'),

        ready: function () {
            this.nodes().forEach(function (node) {
                let width = [30, 70, 110];
                let size = width[Math.floor(Math.random() * 3)];
                node.css("width", size);
                node.css("height", size);
            });
            this.layout({ name: 'cose-bilkent', animationDuration: 1000 }).run();
        },

        style: [
            {
                selector: 'node',
                style: {
                    'background-color': '#ad1a66'
                }
            },

            {
                selector: ':parent',
                style: {
                    'background-opacity': 0.333
                }
            },

            {
                selector: 'edge',
                style: {
                    'width': 3,
                    'line-color': '#ad1a66'
                }
            }
        ],

        elements: [{ group: 'nodes', data: { id: 'n0' } },
        { group: 'nodes', data: { id: 'n1' } },
        { group: 'nodes', data: { id: 'n2' } },
        { group: 'nodes', data: { id: 'n3' } },
        { group: 'nodes', data: { id: 'n4', parent: 'n37' } },
        { group: 'nodes', data: { id: 'n5' } },
        { group: 'nodes', data: { id: 'n6' } },
        { group: 'nodes', data: { id: 'n7', parent: 'n37' } },
        { group: 'nodes', data: { id: 'n8', parent: 'n37' } },
        { group: 'nodes', data: { id: 'n9', parent: 'n37' } },
        { group: 'nodes', data: { id: 'n10', parent: 'n38' } },
        { group: 'nodes', data: { id: 'n12' } },
        { group: 'nodes', data: { id: 'n13' } },
        { group: 'nodes', data: { id: 'n14' } },
        { group: 'nodes', data: { id: 'n15' } },
        { group: 'nodes', data: { id: 'n16' } },
        { group: 'nodes', data: { id: 'n17' } },
        { group: 'nodes', data: { id: 'n18' } },
        { group: 'nodes', data: { id: 'n19' } },
        { group: 'nodes', data: { id: 'n20' } },
        { group: 'nodes', data: { id: 'n21' } },
        { group: 'nodes', data: { id: 'n22' } },
        { group: 'nodes', data: { id: 'n23' } },
        { group: 'nodes', data: { id: 'n24', parent: 'n39' } },
        { group: 'nodes', data: { id: 'n25', parent: 'n39' } },
        { group: 'nodes', data: { id: 'n26', parent: 'n42' } },
        { group: 'nodes', data: { id: 'n27', parent: 'n42' } },
        { group: 'nodes', data: { id: 'n28', parent: 'n42' } },
        { group: 'nodes', data: { id: 'n29', parent: 'n40' } },
        { group: 'nodes', data: { id: 'n31', parent: 'n41' } },
        { group: 'nodes', data: { id: 'n32', parent: 'n41' } },
        { group: 'nodes', data: { id: 'n33', parent: 'n41' } },
        { group: 'nodes', data: { id: 'n34', parent: 'n41' } },
        { group: 'nodes', data: { id: 'n35', parent: 'n41' } },
        { group: 'nodes', data: { id: 'n36', parent: 'n41' } },
        { group: 'nodes', data: { id: 'n37' } },
        { group: 'nodes', data: { id: 'n38' } },
        { group: 'nodes', data: { id: 'n39', parent: 'n43' } },
        { group: 'nodes', data: { id: 'n40', parent: 'n42' } },
        { group: 'nodes', data: { id: 'n41', parent: 'n42' } },
        { group: 'nodes', data: { id: 'n42', parent: 'n43' } },
        { group: 'nodes', data: { id: 'n43' } },
        { group: 'edges', data: { id: 'e0', source: 'n0', target: 'n1' } },
        { group: 'edges', data: { id: 'e1', source: 'n1', target: 'n2' } },
        { group: 'edges', data: { id: 'e2', source: 'n2', target: 'n3' } },
        { group: 'edges', data: { id: 'e3', source: 'n0', target: 'n3' } },
        { group: 'edges', data: { id: 'e4', source: 'n1', target: 'n4' } },
        { group: 'edges', data: { id: 'e5', source: 'n2', target: 'n4' } },
        { group: 'edges', data: { id: 'e6', source: 'n4', target: 'n5' } },
        { group: 'edges', data: { id: 'e7', source: 'n5', target: 'n6' } },
        { group: 'edges', data: { id: 'e8', source: 'n4', target: 'n6' } },
        { group: 'edges', data: { id: 'e9', source: 'n4', target: 'n7' } },
        { group: 'edges', data: { id: 'e10', source: 'n7', target: 'n8' } },
        { group: 'edges', data: { id: 'e11', source: 'n8', target: 'n9' } },
        { group: 'edges', data: { id: 'e12', source: 'n7', target: 'n9' } },
        { group: 'edges', data: { id: 'e13', source: 'n13', target: 'n14' } },
        { group: 'edges', data: { id: 'e14', source: 'n12', target: 'n14' } },
        { group: 'edges', data: { id: 'e15', source: 'n14', target: 'n15' } },
        { group: 'edges', data: { id: 'e16', source: 'n14', target: 'n16' } },
        { group: 'edges', data: { id: 'e17', source: 'n15', target: 'n17' } },
        { group: 'edges', data: { id: 'e18', source: 'n17', target: 'n18' } },
        { group: 'edges', data: { id: 'e19', source: 'n18', target: 'n19' } },
        { group: 'edges', data: { id: 'e20', source: 'n17', target: 'n20' } },
        { group: 'edges', data: { id: 'e21', source: 'n19', target: 'n20' } },
        { group: 'edges', data: { id: 'e22', source: 'n16', target: 'n20' } },
        { group: 'edges', data: { id: 'e23', source: 'n20', target: 'n21' } },
        { group: 'edges', data: { id: 'e25', source: 'n23', target: 'n24' } },
        { group: 'edges', data: { id: 'e26', source: 'n24', target: 'n25' } },
        { group: 'edges', data: { id: 'e27', source: 'n26', target: 'n38' } },
        { group: 'edges', data: { id: 'e29', source: 'n26', target: 'n39' } },
        { group: 'edges', data: { id: 'e30', source: 'n26', target: 'n27' } },
        { group: 'edges', data: { id: 'e31', source: 'n26', target: 'n28' } },
        { group: 'edges', data: { id: 'e33', source: 'n21', target: 'n31' } },
        { group: 'edges', data: { id: 'e35', source: 'n31', target: 'n33' } },
        { group: 'edges', data: { id: 'e36', source: 'n31', target: 'n34' } },
        { group: 'edges', data: { id: 'e37', source: 'n33', target: 'n34' } },
        { group: 'edges', data: { id: 'e38', source: 'n32', target: 'n35' } },
        { group: 'edges', data: { id: 'e39', source: 'n32', target: 'n36' } },
        { group: 'edges', data: { id: 'e40', source: 'n16', target: 'n40' } }
        ]
    });

    cy.on('click', 'node', function(evt){
      console.log( 'clicked ' + evt.target.id() );
      selectedInfo.value = `Selected interaction anchor ${evt.target.id()}`

});

cy.on('click', 'edge', function(event){
    // console.log( 'clicked ' +evt.target.source() + ' --- ' + evt.target.target() );
    console.log(event.target.connectedNodes())
    // selectedInfo.value 
    const connectedNodes= event.target.connectedNodes();
    const connectedAnchor1 = connectedNodes[0]
    const connectedAnchor2 = connectedNodes[1]
    console.log(connectedAnchor1.id())
    selectedInfo.value = `Selected interaction between ${connectedAnchor1.id()} and ${connectedAnchor2.id()}` 

});
    watch([() => option.value.series, () => chrom.value, () => start.value, () => end.value], async (newStart, newEnd) => {
        if (end.value - start.value < visibilityWidth) {
            showSpin.value = true
            // colors = option.value.series[0].itemStyle.color || "black"
            // lineColor = option.value.series[0].lineStyle.color || "black"
            // isVisible.value = true
            // canvasReady.value = false
            // console.log("start or end value changes, drawPlotX")
            let lines = []
            let edgeIdCounter = 0;

            await file.getLines(chrom.value, start.value, end.value, function (line, fileOffset) {
                const splitData = line.split(/;/)
                const arr = splitData[0].split(/[\s,:-]+/)
                const chrom = arr[0]
                const start = Number(arr[1])
                const end = Number(arr[2])
                const chrom2 = arr[3]
                const start2 = Number(arr[4])
                const end2 = Number(arr[5])

                let anchor1
                let anchor2
                if (splitData.length === 1) {
                     anchor1 = `${chrom}:${start}-${end}`;
                     anchor2 = `${chrom2}:${start2}-${end2}`;
                } else if (splitData.length === 2) {
                    if (splitData[1].split('|')) {
                        const anchor = splitData[1].split('|')
                    // Check and assign anchor1 and anchor2 based on conditions
                     anchor1 = (anchor[0] === '.' || anchor[0] === 'N' || anchor[0].trim() === '') ? `${chrom}:${start}-${end}` : anchor[0];
                     anchor2 = (anchor[1] === '.' || anchor[1] === 'N' || anchor[1].trim() === '') ? `${chrom2}:${start2}-${end2}` : anchor[1];

                    } else {
                        message.error(`Delimiter '|' not found in the second part of the line: "${line}"`)
                    }
                }

                // Check if anchors already exist
                let anchor1Exists = lines.some(item => item.data.id === anchor1);
                let anchor2Exists = lines.some(item => item.data.id === anchor2);

                // If they don't exist, add them as nodes
                if (!anchor1Exists) {
                    lines.push({ group: 'nodes', data: { id: anchor1 } });
                }
                if (!anchor2Exists) {
                    lines.push({ group: 'nodes', data: { id: anchor2 } });
                }
                // lines.push(addedData)
                // Create an edge between anchor1 and anchor2
                let edgeId = `e${edgeIdCounter++}`;
                lines.push({ group: 'edges', data: { id: edgeId, source: anchor1, target: anchor2 } });
            })
            console.log(lines)
            cy.elements().remove(); cy.add(lines);
            const layout = cy.layout({
                name: 'cose-bilkent',
                animate: 'end',
                animationEasing: 'ease-out',
                animationDuration: 1000,
                randomize: true
            });

            layout.run();

        } else {
            isVisible.value = false
            canvasReady.value = true
        }


    }, { immediate: true, deep: true });




    // Event listeners for buttons
    // document.getElementById("layoutButton").addEventListener("click", () => {
    //     const layout = cy.layout({
    //         name: 'cose-bilkent',
    //         animate: 'end',
    //         animationEasing: 'ease-out',
    //         animationDuration: 1000,
    //         randomize: true
    //     });

    //     layout.run();
    // });

    // document.getElementById("randomize").addEventListener("click", () => {
    //     const layout = cy.layout({
    //         name: 'random',
    //         animate: true,
    //         animationDuration: 1000,
    //         animationEasing: 'ease-out'
    //     });

    //     layout.run();
    // });
})

</script>
  
<style scoped>
#cy {
    width: 100%;
    height: 90%;
    z-index: 999;
}

h1 {
    opacity: 0.5;
    font-size: 1em;
}

button {
    margin-right: 10px;
}
</style>