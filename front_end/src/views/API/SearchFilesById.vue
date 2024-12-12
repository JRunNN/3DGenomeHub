<template>
                <n-card  class="mb-8">
                    <template #header>
                        <div class="text-2xl">
                            Search downloadable files by id
                        </div>
                    </template>
                    <div class="mb-4">
                        <n-space align="center">
                            <n-tag type="info">
                                GET
                            </n-tag>
                            <n-code :code="` /files/{sample_name}`" language="shell" inline />
                        </n-space>
                    </div>
                    <APICodeExample title="Example 1: Search all files for library GSM2109214">
                        <template #code1="{ js }">
                            {{ js(`
                           https://expresso.sustech.edu.cn/api/files/GSM2109214
                            `) }}
                        </template>
                        <template #code2="{ js }">
                            {{ js(`
                            [
                            {
                            "gsm_id": "GSM2109214",
                            "file_name": "GSM2109214.chromatin_loops.tsv.gz",
                            "data_type": "hic",
                            "file_type": "loop"
                            },
                            {
                            "gsm_id": "GSM2109214",
                            "file_name": "GSM2109214.compartments.bed.gz",
                            "data_type": "hic",
                            "file_type": "compartment"
                            },
                            {
                            "gsm_id": "GSM2109214",
                            "file_name": "GSM2109214.contact_matrix.hic",
                            "data_type": "hic",
                            "file_type": "matrix"
                            },
                            {
                            "gsm_id": "GSM2109214",
                            "file_name": "GSM2109214.domain_boundaries.txt.gz",
                            "data_type": "hic",
                            "file_type": "domain"
                            },
                            {
                            "gsm_id": "GSM2109214",
                            "file_name": "GSM2109214.stripes.tsv.gz.gz",
                            "data_type": "hic",
                            "file_type": "stripe"
                            }
                            ]
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
