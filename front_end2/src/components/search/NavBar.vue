<template>
    <div class="mb-4 p-3 bg-white  relative flex rounded-lg items-center">


        <!-- <div class="  w-20 mr-3 text-l">
            <n-select v-model:value="chrom" :options="chromValues" :consistent-menu-width="false" />

        </div> -->

        <!-- ==================== -->

        <!-- search bar -->
        <div class="flex flex-grow items-center">
            <!-- <label for="simple-search" class="sr-only">Search</label> -->
            <input type="text" id="simple-search"
                class="relative m-0  block min-w-0 flex-auto  rounded-l border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-1.5 text-base font-normal text-neutral-700 outline-none transition duration-300 ease-in-out focus:border-primary focus:text-neutral-700 focus:shadow-te-primary focus:outline-none"
                placeholder="Search" required v-model="currentLocString">
            <!-- <button
                class="relative flex items-center mr-3 px-4 py-2.5
                                text-white
                                rounded-r bg-blue-700 transition duration-150 ease-in-out hover:bg-primary-700 hover:shadow-lg focus:bg-primary-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-primary-800 active:shadow-lg"
                type="button" id="location-search" data-te-ripple-init data-te-ripple-color="light"
                @click="$emit('toggleGenomicRegionPanel')">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 4.5l15 15m0 0V8.25m0 11.25H8.25" />
                </svg>



            </button> -->
        </div>
        <!-- ========== -->

        <!-- shift button -->
        <div class="inline-flex rounded-md shadow-sm ml-2" role="group">
            <button type="button"
                class="text-blue-700 border border-blue-700 hover:bg-blue-700 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-l text-sm text-center inline-flex items-center p-2 w-9 h-9"
                @click="$emit('shift', $event, -1)">
                <svg fill="currentColor" class="h-6 w-6" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"
                    aria-hidden="true">
                    <path clip-rule="evenodd" fill-rule="evenodd"
                        d="M17 10a.75.75 0 01-.75.75H5.612l4.158 3.96a.75.75 0 11-1.04 1.08l-5.5-5.25a.75.75 0 010-1.08l5.5-5.25a.75.75 0 111.04 1.08L5.612 9.25H16.25A.75.75 0 0117 10z">
                    </path>
                </svg>
            </button>
            <button type="button"
                class="text-blue-700 border-t border-b border-r border-blue-700 hover:bg-blue-700 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-r text-sm text-center inline-flex items-center mr-3 p-2 w-9 h-9"
                @click="$emit('shift', $event, 1)">
                <svg fill="currentColor" class="h-6 w-6" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"
                    aria-hidden="true">
                    <path clip-rule="evenodd" fill-rule="evenodd"
                        d="M3 10a.75.75 0 01.75-.75h10.638L10.23 5.29a.75.75 0 111.04-1.08l5.5 5.25a.75.75 0 010 1.08l-5.5 5.25a.75.75 0 11-1.04-1.08l4.158-3.96H3.75A.75.75 0 013 10z">
                    </path>
                </svg>
            </button>
        </div>

        <!-- zoom in and out buttons -->
        <div class="inline-flex rounded-md shadow-sm mr-2" role="group">
            <button type="button"
                class="text-blue-700 border border-blue-700 hover:bg-blue-700 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-l text-sm text-center inline-flex items-center p-2 w-9 h-9"
                @click="$emit('zoomIn')">
                <svg fill="currentColor" class="h-6 w-6" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"
                    aria-hidden="true">
                    <path
                        d="M9 6a.75.75 0 01.75.75v1.5h1.5a.75.75 0 010 1.5h-1.5v1.5a.75.75 0 01-1.5 0v-1.5h-1.5a.75.75 0 010-1.5h1.5v-1.5A.75.75 0 019 6z">
                    </path>
                    <path clip-rule="evenodd" fill-rule="evenodd"
                        d="M2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9zm7-5.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11z">
                    </path>
                </svg>
            </button>
            <button type="button" class="text-blue-700 
                                border-t border-b border-r border-blue-700 
                                hover:bg-blue-700 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 
                                font-medium rounded-r text-sm  text-center inline-flex items-center 
                                mr-3 p-2 w-9 h-9" @click="$emit('zoomOut')">
                <svg fill="currentColor" class="h-6 w-6" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"
                    aria-hidden="true">
                    <path d="M6.75 8.25a.75.75 0 000 1.5h4.5a.75.75 0 000-1.5h-4.5z"></path>
                    <path clip-rule="evenodd" fill-rule="evenodd"
                        d="M9 2a7 7 0 104.391 12.452l3.329 3.328a.75.75 0 101.06-1.06l-3.328-3.329A7 7 0 009 2zM3.5 9a5.5 5.5 0 1111 0 5.5 5.5 0 01-11 0z">
                    </path>
                </svg>
            </button>
        </div>

        <!-- vertical line -->
        <!-- <div class="inline-flex rounded-md shadow-sm" role="group">
            <button type="button"
                class="text-blue-700 border border-blue-700 hover:bg-blue-700 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded text-sm text-center inline-flex items-center p-2 w-10 h-10"
                @click="">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
            </button>
        </div> -->

        <!-- screenshot button -->
        <!-- <div class="inline-flex rounded-md shadow-sm mx-2" role="group">
            <button type="button"
                class="text-blue-700 border border-blue-700 hover:bg-blue-700 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded text-sm text-center inline-flex items-center p-2"
                @click="">
                Screennshot
            </button>
        </div> -->


        <!-- // current view  -->
        <div class=" flex flex-col justify-center items-center">
            <p class="text-xl">{{ BASIC_intComma(span) }} bp</p>
        </div>
        <n-tooltip placement="top-start" trigger="hover" :delay=1000>
    <template #trigger>
        <button class="ml-12">

  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" 
       class="w-6 h-6 cursor-pointer transform transition-transform duration-500 hover:scale-110 active:scale-95 text-blue-500" 
       @click="handleArrowClick">
    <circle cx="12" cy="12" r="11" fill="none" stroke="currentColor" class="transition-all duration-200 hover:stroke-blue-700"/>
    <path stroke-linecap="round" stroke-linejoin="round" :transform="'rotate(' + rotation + ', 12, 12)'" 
          d="M13.5 17l-4.5-4.5 4.5-4.5" class="transition-all duration-200"/>
  </svg>
</button>
</template>
    Click to expand Genomic Regions selection widget
  </n-tooltip>
    </div>
</template>

<script lang="ts" setup>
import { ref, computed, watch, defineProps } from 'vue';
import { BASIC_intComma } from '@/browser/utils/utils'

const props = defineProps({
    asm: {
        type: String,
        required: true
    },
    chrom: {
        type: String,
        required: true
    },
    min: {
        type: Number,
        required: true
    },
    max: {
        type: Number,
        required: true
    },
    start: {
        type: Number,
        required: true
    },
    end: {
        type: Number,
        required: true
    },
    chromSizes: {
        type: Object,
        required: true
    },
    chromNames: {
        type: Array,
        required: true
    }
})

const emit = defineEmits(['update:chrom', 'update:start', 'update:end', 'update:min', 'update:max', 'shift', 'zoomIn', 'zoomOut', 'zoomTo', 'toggleGenomicRegionPanel'])
const asm = ref(props.asm)


const chrom = computed({
    get: () => props.chrom,
    set: (value) => {
        emit('update:chrom', value)
    }
})

const chromValues = ref(props.chromNames.map((item) => {
    return {
        label: item,
        value: item
    }
}))

const start = computed(
    () => props.start
)

const end = computed(
    () => props.end
)

// input search
const stringToLoc = (searchString) => {
    const [chromosome, location] = searchString.split(":");
    console.log('chromosome: ', chromosome)
    const [start, end] = location.split("-");
    const startInt = parseInt(start.replace(/,/g, ""));
    const endInt = parseInt(end.replace(/,/g, ""));
    return { chrom: chromosome, start: startInt, end: endInt };
}

const currentLocString = ref('')

watch([() => props.chrom, () => props.start, () => props.end], () => {
    currentLocString.value = props.chrom + ':' + BASIC_intComma(props.start) + '-' + BASIC_intComma(props.end)
}, { immediate: true })


const handleLocationSearch = function () {

    const { chrom, start, end } = stringToLoc(currentLocString.value)
    // emit('update:chrom', chrom)
    // emit('update:start', start)
    // emit('update:end', end)
    //corenavStore.zoomTo(chrom, start, end);
    emit('zoomTo', chrom, start, end)
    // console.log('search location:  ', chromosome, startInt, endInt)

}

// currently viewed genomic regions in bp
const span = computed(() => {
    return end.value - start.value + 1
})


let rotation = ref(0)
let isClockwise = true
const handleArrowClick = () => {
    rotation.value += isClockwise ? -90 : 90;
    isClockwise = !isClockwise;
    emit('toggleGenomicRegionPanel')
}


</script>

<style>
#basic_navbar {
    z-index: 500;
}

#basic_navbar .brand img {
    margin-top: -5px;
    margin-bottom: -4px;
}

#basic_navbar .navbar-inner {
    border-radius: 0;
}

#basic_navbar li.panel-toggle.panel-hide a.show {
    display: block;
}

#basic_navbar li.panel-toggle.panel-hide a.hide {
    display: none;
}

#basic_navbar li.panel-toggle.panel-show a.show {
    display: none;
}

#basic_navbar li.panel-toggle.panel-show a.hide {
    display: block;
}
</style>