<template>
    <n-card class="mb-8">
        <template #header>
            <div class="text-2xl">
                Search Domain and boundary profile of genes            </div>
        </template>
        <div class="mb-4">
            <n-space align="center">
                <n-tag type="info">
                    GET
                </n-tag>
                <n-code :code="` /gene/{gene_name}/domain`"
                    language="shell" inline />
            </n-space>
        </div>
        <APICodeExample title="Example 1: Search Domain and boundary profile of gene NEAT1">
            <template #code1="{ js }">
                {{ js(`
                    https://expresso.sustech.edu.cn/api/gene/NEAT1/domain
                `) }}
            </template>
            <template #code2="{ js }">
                {{ js(`
                [
                    {
                        "sample_name": "GSM1023732",
                        "value": "d",
                        "tissue": "Skin",
                        "health_status": "Healthy",
                        "biomaterial_type": "Cell Line"
                    },
                    {
                        "sample_name": "GSM1023733",
                        "value": "d",
                        "tissue": "Skin",
                        "health_status": "Healthy",
                        "biomaterial_type": "Cell Line"
                    },
                    {
                        "sample_name": "GSM1023734",
                        "value": "d",
                        "tissue": "Skin",
                        "health_status": "Non-Cancer Disease",
                        "biomaterial_type": "Cell Line"
                    },
                    {
                        "sample_name": "GSM1023735",
                        "value": "d",
                        "tissue": "Skin",
                        "health_status": "Non-Cancer Disease",
                        "biomaterial_type": "Cell Line"
                    },
                    {
                        "sample_name": "GSM1267196",
                        "value": "d",
                        "tissue": "hESC derived",
                        "health_status": "Healthy",
                        "biomaterial_type": "Cell Line"
                    },
                    {
                        "sample_name": "GSM1267197",
                        "value": "d",
                        "tissue": "hESC derived",
                        "health_status": "Healthy",
                        "biomaterial_type": "Cell Line"
                    },
                    {
                        "sample_name": "GSM1267198",
                        "value": "d",
                        "tissue": "hESC derived",
                        "health_status": "Healthy",
                        "biomaterial_type": "Cell Line"
                    },
                    {
                        "sample_name": "GSM1267199",
                        "value": "d",
                        "tissue": "hESC derived",
                        "health_status": "Healthy",
                        "biomaterial_type": "Cell Line"
                    },
                    {
                        "sample_name": "GSM1267200",
                        "value": "d",
                        "tissue": "hESC derived",
                        "health_status": "Healthy",
                        "biomaterial_type": "Cell Line"
                    },
                    {
                        "sample_name": "GSM1267201",
                        "value": "d",
                        "tissue": "hESC derived",
                        "health_status": "Healthy",
                        "biomaterial_type": "Cell Line"
                    },
                    {
                        "sample_name": "GSM1267202",
                        "value": "d",
                        "tissue": "hESC derived",
                        "health_status": "Healthy",
                        "biomaterial_type": "Cell Line"
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
