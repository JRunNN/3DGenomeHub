<template>
	<div class="card p-fluid">
        <DataTable :value="customers" lazy paginator :first="0" :rows="10" v-model:filters="filters" ref="dt" dataKey="id"
            :totalRecords="totalRecords" :loading="loading" @page="onPage($event)" @sort="onSort($event)" @filter="onFilter($event)" filterDisplay="row"
            :globalFilterFields="['name','country.name', 'company', 'representative.name']"
            v-model:selection="selectedCustomers" :selectAll="selectAll" @select-all-change="onSelectAllChange" @row-select="onRowSelect" @row-unselect="onRowUnselect" tableStyle="min-width: 75rem">
            <Column selectionMode="multiple" headerStyle="width: 3rem"></Column>
            <Column field="id" header="ID" filterMatchMode="startsWith" sortable>
                <template #filter="{filterModel,filterCallback}">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()" class="p-column-filter" placeholder="Search"/>
                </template>
            </Column>
            <Column field="disease" header="Disease" filterField="disease" filterMatchMode="contains" sortable>
                <template #filter="{filterModel,filterCallback}">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()" class="p-column-filter" placeholder="Search"/>
                </template>
            </Column>
            <Column field="bodySites" header="BodySites" filterMatchMode="contains" sortable>
                <template #filter="{filterModel,filterCallback}">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()" class="p-column-filter" placeholder="Search"/>
                </template>
            </Column>
            <Column field="assay" header="Assay" filterField="assay" sortable>
                <template #filter="{filterModel,filterCallback}">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()" class="p-column-filter" placeholder="Search"/>
                </template>
            </Column>
            <Column field="factor" header="Factor" filterField="factor" sortable>
                <template #filter="{filterModel,filterCallback}">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()" class="p-column-filter" placeholder="Search"/>
                </template>
            </Column>
            <Column field="action" header="Action" filterField="action" sortable>
                <template #filter="{filterModel,filterCallback}">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()" class="p-column-filter" placeholder="Search"/>
                </template>
            </Column>
        </DataTable>
	</div>
</template>
<script setup>
// import { ref, onMounted } from 'vue';

import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';   // optional
import Row from 'primevue/row';   
import InputText from 'primevue/inputtext'

import { onMounted, ref, reactive, watch, computed, h, nextTick } from 'vue';
import { useRouter, useRoute } from 'vue-router'
// import { NButton } from 'naive-ui'
import axios from 'axios';
// import { type } from 'os';
import { v4 as uuid } from 'uuid'
import { useTrackStore } from '../../browser/store/TrackStore/TrackStore'
import { useSessionStore } from '../../browser/store/SessionStore/SessionStore'
const trackStore = useTrackStore();
const sessionStore = useSessionStore();

const diseaseStatus = ref([])
const bodySites = ref([])
const assays = ref([])
// const cellId = ref([])
const loadingRef = ref(true)
const dataRef = ref([])
const from = ref(0)
const to = ref(0)
const currentPage = ref(1)
const pageSize = ref(10)
const initializedData = ref([])
const itemCount = ref(0)
const paginationReactive = computed(() => ({
    page: currentPage.value,
    pageCount: 1,
    pageSize: pageSize.value,
    itemCount: itemCount.value
}))
let includeInitialData = true
const cellId = ref('')



const dt = ref();
const loading = ref(false);
const totalRecords = ref(0);
const customers = ref();
const selectedCustomers = ref();
const selectAll = ref(false);
const filters = ref({
    'name': {value: '', matchMode: 'contains'},
    'country.name': {value: '', matchMode: 'contains'},
    'company': {value: '', matchMode: 'contains'},
    'representative.name': {value: '', matchMode: 'contains'},
});
const lazyParams = ref({});
// const columns = ref([
//     {field: 'name', header: 'Name'},
//     {field: 'country.name', header: 'Country'},
//     {field: 'company', header: 'Company'},
//     {field: 'representative.name', header: 'Representative'}
// ]);

const loadLazyData = () => {
    loading.value = true;

    setTimeout(() => {
            customers.value = [{
    id: 1000,
    name: 'James Butt',
    country: {
        name: 'Algeria',
        code: 'dz'
    },
    company: 'Benton, John B Jr',
    date: '2015-09-13',
    status: 'unqualified',
    verified: true,
    activity: 17,
    representative: {
        name: 'Ioni Bowcher',
        image: 'ionibowcher.png'
    },
    balance: 70663
}]
            totalRecords.value = 100;
            loading.value = false;

    }, Math.random() * 1000 + 250);
};

const onPage = (event) => {
    console.log(lazyParams.value,event)
    lazyParams.value = event;
    loadLazyData();
};
const onSort = (event) => {
    console.log(lazyParams.value,event)
    lazyParams.value = event;
    loadLazyData();
};
const onFilter = () => {
    console.log(lazyParams.value,event)
    lazyParams.value.filters = filters.value ;
    loadLazyData();
};
const onSelectAllChange = (event) => {
    selectAll.value = event.checked;

    if (selectAll) {
        CustomerService.getCustomers().then(data => {
            selectAll.value = true;
            selectedCustomers.value = data.customers;
        });
    }
    else {
        selectAll.value = false;
        selectedCustomers.value = [];
    }
};
const onRowSelect = () => {
    selectAll.value = selectedCustomers.value.length === totalRecords.value;
};
const onRowUnselect = () => {
    selectAll.value = false;
};


onMounted(() => {
    loading.value = true;

    lazyParams.value = {
        first: dt.value.first,
        rows: dt.value.rows,
        sortField: null,
        sortOrder: null,
        filters: filters.value
    };

    loadLazyData();
});

</script>

<style>
</style>