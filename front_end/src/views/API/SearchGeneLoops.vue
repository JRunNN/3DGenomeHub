<template>
    <n-card class="mb-8">
        <template #header>
            <div class="text-2xl">
                Search Gene associated chromatin loops
            </div>
        </template>
        <div class="mb-4">
            <n-space align="center">
                <n-tag type="info">
                    GET
                </n-tag>
                <n-code :code="` /loops?gene_id=NEAT1`"
                    language="shell" inline />
            </n-space>
        </div>
        <APICodeExample title="Example 1: Search NEAT1 associated chromatin loops">
            <template #code1="{ js }">
                {{ js(`
                https://expresso.sustech.edu.cn/api/loops?gene_id=NEAT1
                `) }}
            </template>
            <template #code2="{ js }">
                {{ js(`
                {
                    "itemCount": 2103266,
                    "items": [
                        {
                            "chrom1": "chr1",
                            "start1": 171800000,
                            "end1": 171810000,
                            "chrom2": "chr1",
                            "start2": 171980000,
                            "end2": 171990000,
                            "sample_name": "GSM1267196",
                            "counts": 31.0,
                            "gene_anno_1": "AL031864.1",
                            "gene_anno_2": "NA"
                        },
                        {
                            "chrom1": "chr2",
                            "start1": 181750000,
                            "end1": 181760000,
                            "chrom2": "chr2",
                            "start2": 181890000,
                            "end2": 181900000,
                            "sample_name": "GSM1267196",
                            "counts": 36.0,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "AC009962.1,ITPRID2"
                        },
                        {
                            "chrom1": "chr21",
                            "start1": 38170000,
                            "end1": 38180000,
                            "chrom2": "chr21",
                            "start2": 38350000,
                            "end2": 38360000,
                            "sample_name": "GSM1267196",
                            "counts": 28.0,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "NA"
                        },
                        {
                            "chrom1": "chr3",
                            "start1": 187310000,
                            "end1": 187320000,
                            "chrom2": "chr3",
                            "start2": 187670000,
                            "end2": 187680000,
                            "sample_name": "GSM1267196",
                            "counts": 34.0,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "SST"
                        },
                        {
                            "chrom1": "chr7",
                            "start1": 122210000,
                            "end1": 122220000,
                            "chrom2": "chr7",
                            "start2": 122530000,
                            "end2": 122540000,
                            "sample_name": "GSM1267196",
                            "counts": 24.0,
                            "gene_anno_1": "AC015983.2",
                            "gene_anno_2": "NA"
                        },
                        {
                            "chrom1": "chr8",
                            "start1": 100710000,
                            "end1": 100720000,
                            "chrom2": "chr8",
                            "start2": 100830000,
                            "end2": 100840000,
                            "sample_name": "GSM1267196",
                            "counts": 29.0,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "RNU4-83P"
                        },
                        {
                            "chrom1": "chr9",
                            "start1": 72030000,
                            "end1": 72040000,
                            "chrom2": "chr9",
                            "start2": 72270000,
                            "end2": 72280000,
                            "sample_name": "GSM1267196",
                            "counts": 24.0,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "AL135924.1"
                        },
                        {
                            "chrom1": "chr1",
                            "start1": 89050000,
                            "end1": 89060000,
                            "chrom2": "chr1",
                            "start2": 89420000,
                            "end2": 89430000,
                            "sample_name": "GSM1267198",
                            "counts": 34.0,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "NA"
                        },
                        {
                            "chrom1": "chr10",
                            "start1": 27280000,
                            "end1": 27290000,
                            "chrom2": "chr10",
                            "start2": 27960000,
                            "end2": 27970000,
                            "sample_name": "GSM1267198",
                            "counts": 13.0,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "NA"
                        },
                        {
                            "chrom1": "chr12",
                            "start1": 63540000,
                            "end1": 63550000,
                            "chrom2": "chr12",
                            "start2": 63740000,
                            "end2": 63750000,
                            "sample_name": "GSM1267198",
                            "counts": 13.0,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "NA"
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
