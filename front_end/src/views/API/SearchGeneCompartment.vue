<template>
    <n-card class="mb-8">
        <template #header>
            <div class="text-2xl">
                Search Compartments E1 score of samples
            </div>
        </template>
        <div class="mb-4">
            <n-space align="center">
                <n-tag type="info">
                    GET
                </n-tag>
                <n-code :code="` /gene/{gene_name}/compartment`"
                    language="shell" inline />
            </n-space>
        </div>
        <APICodeExample title="Example 1: Search compartment E1 value of gene NEAT1">
            <template #code1="{ js }">
                {{ js(`
                https://expresso.sustech.edu.cn/api/gene/NEAT1/compartment
                `) }}
            </template>
            <template #code2="{ js }">
                {{ js(`
[
    {
        "sample_name": "GSM2109212",
        "value": 0.7705,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },
    {
        "sample_name": "GSM2109213",
        "value": 0.8124,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },
    {
        "sample_name": "GSM2109214",
        "value": 0.9269,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },
    {
        "sample_name": "GSM2109215",
        "value": 0.7442,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },
    {
        "sample_name": "GSM2109218",
        "value": 0.9333,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },
    {
        "sample_name": "GSM2109219",
        "value": 0.8255,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },
    {
        "sample_name": "GSM2109220",
        "value": 0.9058,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },
    {
        "sample_name": "GSM2109221",
        "value": 1.0021,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },
    {
        "sample_name": "GSM2109222",
        "value": 0.8414,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },
    {
        "sample_name": "GSM2109223",
        "value": 0.6001,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },
    {
        "sample_name": "GSM2109224",
        "value": 0.9705,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },
    {
        "sample_name": "GSM2109225",
        "value": 0.8794,
        "tissue": "Brain",
        "health_status": "Healthy",
        "biomaterial_type": "iPSC/iPSC derived"
    },...]
                `) }}
            </template>
        </APICodeExample>
    </n-card>
</template>

<script lang="ts" setup>
import { NCard, NSpace, NText, NCode, NTag } from "naive-ui"
import Icon from "@/components/common/Icon.vue"
const ExternalIcon = "tabler:external-link"
const LinkIcon = "carbon:link"
import { RouterLink } from "vue-router"
import APICodeExample from "./APICodeExample.vue";
</script>
