<template>
    <n-card class="mb-8">
        <template #header>
            <div class="text-2xl">
                Search contact domains from samples
            </div>
        </template>
        <div class="mb-4">
            <n-space align="center">
                <n-tag type="info">
                    GET
                </n-tag>
                <n-code :code="` /domains?sample_name={sample_name}`"
                    language="shell" inline />
            </n-space>
        </div>
        <APICodeExample title="Example 1: Search Boundary and domain genes of sample GSM4072698">
            <template #code1="{ js }">
                {{ js(`
                https://expresso.sustech.edu.cn/api/domains?sample_name=GSM4072698
                `) }}
            </template>
            <template #code2="{ js }">
                {{ js(`
                {
                    "itemCount": 54718,
                    "items": [
                        {
                            "sample_name": "GSM4072698",
                            "gene_id": "PERM1",
                            "value": "b"
                        },
                        {
                            "sample_name": "GSM4072698",
                            "gene_id": "AL031282.2",
                            "value": "b"
                        },
                        {
                            "sample_name": "GSM4072698",
                            "gene_id": "SLC35E2A",
                            "value": "b"
                        },
                        {
                            "sample_name": "GSM4072698",
                            "gene_id": "TMEM52",
                            "value": "b"
                        },
                        {
                            "sample_name": "GSM4072698",
                            "gene_id": "AL391845.1",
                            "value": "b"
                        },
                        {
                            "sample_name": "GSM4072698",
                            "gene_id": "PRKCZ",
                            "value": "b"
                        },
                        {
                            "sample_name": "GSM4072698",
                            "gene_id": "MORN1",
                            "value": "b"
                        },
                        {
                            "sample_name": "GSM4072698",
                            "gene_id": "RER1",
                            "value": "b"
                        },
                        {
                            "sample_name": "GSM4072698",
                            "gene_id": "ACTRT2",
                            "value": "b"
                        },
                        {
                            "sample_name": "GSM4072698",
                            "gene_id": "C1orf174",
                            "value": "b"
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
