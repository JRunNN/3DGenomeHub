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
                <n-code :code="` /compartments?sample_name={sample_name}`"
                    language="shell" inline />
            </n-space>
        </div>
        <APICodeExample title="Example 1: Search Compartments E1 score of sample GSM2109214">
            <template #code1="{ js }">
                {{ js(`
                https://expresso.sustech.edu.cn/api/compartments?sample_name=GSM2109214
                `) }}
            </template>
            <template #code2="{ js }">
                {{ js(`
                {
                    "itemCount": 57133,
                    "items": [
                        {
                            "sample_name": "GSM2109214",
                            "gene_id": "SCML2P2",
                            "value": 0.2084
                        },
                        {
                            "sample_name": "GSM2109214",
                            "gene_id": "BTBD1",
                            "value": 0.6438
                        },
                        {
                            "sample_name": "GSM2109214",
                            "gene_id": "DHDDS",
                            "value": 0.493
                        },
                        {
                            "sample_name": "GSM2109214",
                            "gene_id": "BTBD2",
                            "value": 0.6037
                        },
                        {
                            "sample_name": "GSM2109214",
                            "gene_id": "AC254629.1",
                            "value": 0.7354
                        },
                        {
                            "sample_name": "GSM2109214",
                            "gene_id": "BTBD3",
                            "value": -0.2
                        },
                        {
                            "sample_name": "GSM2109214",
                            "gene_id": "MEIS1-AS2",
                            "value": 0.2492
                        },
                        {
                            "sample_name": "GSM2109214",
                            "gene_id": "AC022384.1",
                            "value": 1.1488
                        },
                        {
                            "sample_name": "GSM2109214",
                            "gene_id": "AL139423.1",
                            "value": 0.6802
                        },
                        {
                            "sample_name": "GSM2109214",
                            "gene_id": "MEIS1-AS3",
                            "value": 0.2492
                        }
                    ]
                }
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
