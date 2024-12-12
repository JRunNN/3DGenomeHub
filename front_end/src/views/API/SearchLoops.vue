<template>
    <n-card class="mb-8">
        <template #header>
            <div class="text-2xl">
                Search Chromatin loops from samples
            </div>
        </template>
        <div class="mb-4">
            <n-space align="center">
                <n-tag type="info">
                    GET
                </n-tag>
                <n-code :code="` /loops?sample_name={sample_name}`"
                    language="shell" inline />
            </n-space>
        </div>
        <APICodeExample title="Example 1: Search Chromatin loops from sample GSM4072698">
            <template #code1="{ js }">
                {{ js(`
                    https://expresso.sustech.edu.cn/api/loops?sample_name=GSM4072698
                `) }}
            </template>
            <template #code2="{ js }">
                {{ js(`
                    {
                        "itemCount": 3145,
                        "items": [
                            {
                                "chrom1": "chr1",
                                "start1": 117520000,
                                "end1": 117530000,
                                "chrom2": "chr1",
                                "start2": 117890000,
                                "end2": 117900000,
                                "sample_name": "GSM4072698",
                                "counts": 23.0,
                                "gene_anno_1": "NA",
                                "gene_anno_2": "NA"
                            },
                            {
                                "chrom1": "chr1",
                                "start1": 110620000,
                                "end1": 110630000,
                                "chrom2": "chr1",
                                "start2": 110780000,
                                "end2": 110790000,
                                "sample_name": "GSM4072698",
                                "counts": 37.0,
                                "gene_anno_1": "KCNA2",
                                "gene_anno_2": "NA"
                            },
                            {
                                "chrom1": "chr1",
                                "start1": 116360000,
                                "end1": 116370000,
                                "chrom2": "chr1",
                                "start2": 116480000,
                                "end2": 116490000,
                                "sample_name": "GSM4072698",
                                "counts": 37.0,
                                "gene_anno_1": "NA",
                                "gene_anno_2": "LINC01762"
                            },
                            {
                                "chrom1": "chr1",
                                "start1": 111500000,
                                "end1": 111510000,
                                "chrom2": "chr1",
                                "start2": 111650000,
                                "end2": 111660000,
                                "sample_name": "GSM4072698",
                                "counts": 37.0,
                                "gene_anno_1": "ADORA3",
                                "gene_anno_2": "KRT18P57,RNU6-151P"
                            },
                            {
                                "chrom1": "chr1",
                                "start1": 113140000,
                                "end1": 113150000,
                                "chrom2": "chr1",
                                "start2": 113680000,
                                "end2": 113690000,
                                "sample_name": "GSM4072698",
                                "counts": 37.0,
                                "gene_anno_1": "NA",
                                "gene_anno_2": "NA"
                            },
                            {
                                "chrom1": "chr1",
                                "start1": 116130000,
                                "end1": 116140000,
                                "chrom2": "chr1",
                                "start2": 116500000,
                                "end2": 116510000,
                                "sample_name": "GSM4072698",
                                "counts": 37.0,
                                "gene_anno_1": "NA",
                                "gene_anno_2": "AL390066.1"
                            },
                            {
                                "chrom1": "chr1",
                                "start1": 91990000,
                                "end1": 92000000,
                                "chrom2": "chr1",
                                "start2": 92290000,
                                "end2": 92300000,
                                "sample_name": "GSM4072698",
                                "counts": 25.0,
                                "gene_anno_1": "NA",
                                "gene_anno_2": "GLMN,RPAP2"
                            },
                            {
                                "chrom1": "chr1",
                                "start1": 94850000,
                                "end1": 94860000,
                                "chrom2": "chr1",
                                "start2": 95230000,
                                "end2": 95240000,
                                "sample_name": "GSM4072698",
                                "counts": 24.0,
                                "gene_anno_1": "SLC44A3-AS1",
                                "gene_anno_2": "AC092802.1,RWDD3"
                            },
                            {
                                "chrom1": "chr1",
                                "start1": 109540000,
                                "end1": 109550000,
                                "chrom2": "chr1",
                                "start2": 109770000,
                                "end2": 109780000,
                                "sample_name": "GSM4072698",
                                "counts": 58.0,
                                "gene_anno_1": "AL355310.3,GNAI3,GPR61",
                                "gene_anno_2": "NA"
                            },
                            {
                                "chrom1": "chr1",
                                "start1": 112800000,
                                "end1": 112810000,
                                "chrom2": "chr1",
                                "start2": 113070000,
                                "end2": 113080000,
                                "sample_name": "GSM4072698",
                                "counts": 27.0,
                                "gene_anno_1": "NA",
                                "gene_anno_2": "AL357055.3,LRIG2"
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
