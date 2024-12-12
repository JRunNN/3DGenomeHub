import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import { Buffer } from 'buffer'
globalThis.Buffer = Buffer
globalThis.fetch.bind(globalThis)

import PrimeVue from 'primevue/config';

// import fetch from 'unfetch';


import { create,
  NCollapse,
  NCheckbox,
  NCollapseItem,
  NCheckboxGroup,
  NSpace,
  NDataTable,
  NMessageProvider,
  NTag,
  NSelect,
  NCard,
  NDescriptionsItem,
    NScrollbar,
    NAlert,
    NSpin,
    NDropdown,
    NDescriptions,
    NGrid,
    NGridItem,
    NIcon,
    NText,
    NSlider,
    NInputNumber,
    NTabs,
    NTabPane,
    NStatistic,
    NGi,
    NModal,
    NButtonGroup,
    NButton,
    NBreadcrumb,
    NBreadcrumbItem,
    NList,
    NListItem,
    NSkeleton,
    NDynamicTags,
    NAutoComplete,
    NCascader,
    NTooltip,
    NDrawer,
    NDrawerContent,
    NDivider,
    NColorPicker,
    NSwitch,
    NH2,
    NH3,
    NP,
    NCarousel,
    NRadioGroup,
    NRadio,
    NForm,
    NFormItem,
    NInput,
    NProgress
  } from "naive-ui";

import './assets/main.css'

// import '@/brodwer/static/css/jquery-ui.gis-basic.css'
// import '@/browser/static/style.css'
import 'jquery-ui-dist/jquery-ui.min.js'

const naive = create({
  components: [NCollapse, NCheckbox, NCollapseItem, NCheckboxGroup, NSpace, NDataTable, NMessageProvider, NTag,
    NSelect, NCard, NDescriptionsItem, NScrollbar, NAlert, NSpin, NDropdown, NDescriptions,     NGrid,
    NGridItem,NIcon,NText,NSlider, NInputNumber,NTabs,NTabPane, NStatistic, NGi, NModal, NButton, NButtonGroup,NBreadcrumb,NBreadcrumbItem,NList,NListItem,NSkeleton,NDynamicTags,
  NAutoComplete, NCascader,NTooltip, NDrawer, NDrawerContent, NDivider, NColorPicker,NSwitch, NH2, NH3, NP, NCarousel, NRadioGroup, NRadio, NForm, NFormItem, NInput, NProgress]
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(naive)


app.use(PrimeVue)
import "primevue/resources/themes/nano/theme.css";

app.mount('#app')
window.$vue = app

const defaultTitle: string = 'ActiveLoops'

router.beforeEach((data) => {
  document.title = ((data.meta.title && `${data.meta.title}-${defaultTitle}`) ||
    defaultTitle) as string
})


// import { Buffer } from 'buffer'


// globalThis.Buffer = Buffer

import CurvTrack from '@/browser/tracks/CurvTrack/CurvTrack.vue'
import CurvTrackConfig from '@/browser/tracks/CurvTrack/config.vue'
import PclsTrack from '@/browser/tracks/PclsTrack/PclsTrack.vue'
import PclsTrackConfig from '@/browser/tracks/PclsTrack/config.vue'
import GeneTrack from '@/browser/tracks/GeneTrack/GeneTrack.vue'
import GeneTrackConfig from '@/browser/tracks/GeneTrack/config.vue'
import HicTrack from '@/browser/tracks/HicTrack/HicTrack.vue'
import HicTrackConfig from '@/browser/tracks/HicTrack/config.vue'
import InterChromCurvTrack from '@/browser/tracks/InterChromCurvTrack/InterChromCurvTrack.vue'
import InterChromCurvTrackConfig from '@/browser/tracks/InterChromCurvTrack/config.vue'
import SclsTrack from '@/browser/tracks/SclsTrack/SclsTrack.vue'
import SclsTrackConfig from '@/browser/tracks/SclsTrack/config.vue'
import VirtualCTrack from '@/browser/tracks/VirtualCTrack/VirtualCTrack.vue'
import VirtualCTrackConfig from '@/browser/tracks/VirtualCTrack/config.vue'
import VirtualCTrackController from '@/browser/tracks/VirtualCTrack/controller.vue'

import LineGTrack from '@/browser/tracks/LineGTrack/LineGTrack.vue'
import LineGTrackConfig from '@/browser/tracks/LineGTrack/config.vue'

import HeatmapGTrack from '@/browser/tracks/HeatmapGTrack/HeatmapGTrack.vue'
import HeatmapGTrackConfig from '@/browser/tracks/HeatmapGTrack/config.vue'
import SeqTrack from '@/browser/tracks/SeqTrack/SeqTrack.vue'
import SeqTrackConfig from '@/browser/tracks/SeqTrack/config.vue'

import NetworkTrack from '@/browser/tracks/NetworkTrack/NetworkTrack.vue'
import NetworkTrackConfig from '@/browser/tracks/NetworkTrack/config.vue'

app.component('CurvTrackConfig', CurvTrackConfig)
app.component('CurvTrack', CurvTrack)

app.component('PclsTrackConfig', PclsTrackConfig)
app.component('PclsTrack', PclsTrack)

app.component('GeneTrackConfig', GeneTrackConfig)
app.component('GeneTrack', GeneTrack)

app.component('HicTrackConfig', HicTrackConfig)
app.component('HicTrack', HicTrack)

app.component('InterChromCurvTrackConfig', InterChromCurvTrackConfig)
app.component('InterChromCurvTrack', InterChromCurvTrack)

app.component('SclsTrackConfig', SclsTrackConfig)
app.component('SclsTrack', SclsTrack)

app.component('VirtualCTrackConfig', VirtualCTrackConfig)
app.component('VirtualCTrack', VirtualCTrack)
app.component('VirtualCTrackController', VirtualCTrackController)

app.component('LineGTrackConfig', LineGTrackConfig)
app.component('LineGTrack', LineGTrack)

app.component('HeatmapGTrackConfig', HeatmapGTrackConfig)
app.component('HeatmapGTrack', HeatmapGTrack)

app.component('SeqTrackConfig', SeqTrackConfig)
app.component('SeqTrack', SeqTrack)

app.component('NetworkTrackConfig', NetworkTrackConfig)
app.component('NetworkTrack', NetworkTrack)