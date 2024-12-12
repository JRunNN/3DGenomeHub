<template>
    <n-card class="mb-8">
        <template #header>
            <div class="text-2xl">
                Search stripes from genes
            </div>
        </template>
        <div class="mb-4">
            <n-space align="center">
                <n-tag type="info">
                    GET
                </n-tag>
                <n-code :code="` /stripes?gene_id={gene_id}`"
                    language="shell" inline />
            </n-space>
        </div>
        <APICodeExample title="Example 1: Search stripes from gene NEAT1">
            <template #code1="{ js }">
                {{ js(`
                https://expresso.sustech.edu.cn/api/stripes?gene_id=NEAT1                `) }}
            </template>
            <template #code2="{ js }">
                {{ js(`
                {
                    "itemCount": 1248065,
                    "items": [
                        {
                            "chrom1": "chr16",
                            "pos1": 34570001,
                            "pos2": 34595000,
                            "chrom2": "chr16",
                            "pos3": 34570001,
                            "pos4": 36490000,
                            "id": "ENCFF021YUU",
                            "pvalue": 0.001,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "AC018558.1,AC018558.2,AC018558.3,AC018558.4,AC018558.5,AC023824.1,AC023824.2,AC023824.3,AC023824.4,AC023824.5,AC023824.6,AC092325.1,AC106785.1,AC106785.2,AC116553.1,AC116553.2,AC135776.1,AC135776.2,AC135776.3,AC135776.4,AGGF1P4,AGGF1P5,AGGF1P6,AGGF1P7,AGG",
                            "h3k27ac_1": "NA",
                            "h3k27ac_2": "NA",
                            "h3k27me3_1": "NA",
                            "h3k27me3_2": "NA",
                            "ctcf_1": "NA",
                            "ctcf_2": "NA"
                        },
                        {
                            "chrom1": "chr3",
                            "pos1": 93465001,
                            "pos2": 93485000,
                            "chrom2": "chr3",
                            "pos3": 91760001,
                            "pos4": 93485000,
                            "id": "ENCFF021YUU",
                            "pvalue": 0.001,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "NA",
                            "h3k27ac_1": "NA",
                            "h3k27ac_2": "NA",
                            "h3k27me3_1": "NA",
                            "h3k27me3_2": "NA",
                            "ctcf_1": "NA",
                            "ctcf_2": "NA"
                        },
                        {
                            "chrom1": "chr1",
                            "pos1": 2650001,
                            "pos2": 2685000,
                            "chrom2": "chr1",
                            "pos3": 2650001,
                            "pos4": 4490000,
                            "id": "ENCFF021YUU",
                            "pvalue": 0.001,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "AC242022.1,AC242022.2,ACTRT2,AL008733.1,AL136528.1,AL136528.2,AL355602.1,AL365330.1,AL512383.1,AL512413.1,AL513320.1,AL589702.1,AL590438.1,AL592464.1,AL592464.2,AL805961.1,AL805961.2,ARHGEF16,C1orf174,CCDC27,CEP104,DFFB,EEF1DP6,LINC00982,LINC01134,LINC013",
                            "h3k27ac_1": "NA",
                            "h3k27ac_2": "NA",
                            "h3k27me3_1": "NA",
                            "h3k27me3_2": "NA",
                            "ctcf_1": "NA",
                            "ctcf_2": "NA"
                        },
                        {
                            "chrom1": "chr2",
                            "pos1": 90380001,
                            "pos2": 90400000,
                            "chrom2": "chr2",
                            "pos3": 89795001,
                            "pos4": 90400000,
                            "id": "ENCFF021YUU",
                            "pvalue": 0.001,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "AC233263.1,AC233263.2,AC233263.6,IGKV1D-12,IGKV1D-13,IGKV1D-16,IGKV1D-17,IGKV1D-22,IGKV1D-27,IGKV1D-32,IGKV1D-33,IGKV1D-35,IGKV1D-37,IGKV1D-39,IGKV1D-42,IGKV1D-43,IGKV1D-8,IGKV1OR2-118,IGKV2D-10,IGKV2D-14,IGKV2D-18,IGKV2D-19,IGKV2D-23,IGKV2D-24,IGKV2D-26,",
                            "h3k27ac_1": "NA",
                            "h3k27ac_2": "NA",
                            "h3k27me3_1": "NA",
                            "h3k27me3_2": "NA",
                            "ctcf_1": "NA",
                            "ctcf_2": "NA"
                        },
                        {
                            "chrom1": "chr8",
                            "pos1": 85640001,
                            "pos2": 85660000,
                            "chrom2": "chr8",
                            "pos3": 85640001,
                            "pos4": 87490000,
                            "id": "ENCFF021YUU",
                            "pvalue": 0.001,
                            "gene_anno_1": "REXO1L3P,REXO1L8P",
                            "gene_anno_2": "AC023194.1,AC023194.2,AC023194.3,AC084128.1,AC090572.1,AC090572.2,AC090572.3,AC100801.1,AC103760.1,AC232323.1,AC232323.2,ATP6V0D2,CNBD1,CNGB3,CPNE3,GOLGA2P1,MIOXP1,NTAN1P2,PSKH2,REXO1L10P,REXO1L11P,REXO1L12P,REXO1L1P,REXO1L2P,REXO1L3P,REXO1L4P,REXO1L5P,RE",
                            "h3k27ac_1": "NA",
                            "h3k27ac_2": "NA",
                            "h3k27me3_1": "NA",
                            "h3k27me3_2": "NA",
                            "ctcf_1": "NA",
                            "ctcf_2": "NA"
                        },
                        {
                            "chrom1": "chr17",
                            "pos1": 26590001,
                            "pos2": 26625000,
                            "chrom2": "chr17",
                            "pos3": 25505001,
                            "pos4": 26625000,
                            "id": "ENCFF021YUU",
                            "pvalue": 0.001,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "NA",
                            "h3k27ac_1": "NA",
                            "h3k27ac_2": "NA",
                            "h3k27me3_1": "NA",
                            "h3k27me3_2": "NA",
                            "ctcf_1": "NA",
                            "ctcf_2": "NA"
                        },
                        {
                            "chrom1": "chr21",
                            "pos1": 8215001,
                            "pos2": 8250000,
                            "chrom2": "chr21",
                            "pos3": 8215001,
                            "pos4": 9365000,
                            "id": "ENCFF021YUU",
                            "pvalue": 0.003,
                            "gene_anno_1": "MIR6724-2,RF01518,RNA5-8SN2",
                            "gene_anno_2": "CR381572.1,CR381572.2,CR381653.1,CR381670.1,CR392039.1,CR392039.2,CR392039.3,CR392039.4,CR392039.5,FP236383.1,FP236383.2,FP236383.3,FP671120.4,LINC01666,MIR3648-2,MIR3687-2,MIR6724-2,MIR6724-3,MIR6724-4,MTCO1P1,RF01518,RF01518,RF01518,RNA5-8SN2,RNA5-8SN2,",
                            "h3k27ac_1": "NA",
                            "h3k27ac_2": "NA",
                            "h3k27me3_1": "NA",
                            "h3k27me3_2": "NA",
                            "ctcf_1": "NA",
                            "ctcf_2": "NA"
                        },
                        {
                            "chrom1": "chr7",
                            "pos1": 56360001,
                            "pos2": 56380000,
                            "chrom2": "chr7",
                            "pos3": 56360001,
                            "pos4": 57490000,
                            "id": "ENCFF021YUU",
                            "pvalue": 0.001,
                            "gene_anno_1": "AC093392.2,CICP8,SEPT14P24",
                            "gene_anno_2": "AC069152.1,AC092175.1,AC092423.1,AC092447.1,AC092447.10,AC092447.2,AC092447.3,AC092447.4,AC092447.5,AC092447.6,AC092447.7,AC092447.8,AC092447.9,AC093392.2,AC095038.1,AC095038.2,AC095038.3,AC099654.1,AC099654.10,AC099654.11,AC099654.12,AC099654.13,AC099654",
                            "h3k27ac_1": "NA",
                            "h3k27ac_2": "NA",
                            "h3k27me3_1": "NA",
                            "h3k27me3_2": "NA",
                            "ctcf_1": "NA",
                            "ctcf_2": "NA"
                        },
                        {
                            "chrom1": "chr16",
                            "pos1": 34575001,
                            "pos2": 34595000,
                            "chrom2": "chr16",
                            "pos3": 33505001,
                            "pos4": 34595000,
                            "id": "ENCFF021YUU",
                            "pvalue": 0.001,
                            "gene_anno_1": "NA",
                            "gene_anno_2": "AC133561.1,AC133561.2,AC133561.3,AC133561.4,AC136428.1,AC136428.2,AC136428.3,AC136428.4,AC136932.1,AC136944.1,AC136944.2,AC136944.3,AC136944.4,AC140658.1,AC140658.2,AC140658.3,AC140658.4,AC140658.5,AC140658.6,AC140658.7,AC142384.1,ARHGAP23P1,BCAP31P1,BCLA",
                            "h3k27ac_1": "NA",
                            "h3k27ac_2": "NA",
                            "h3k27me3_1": "NA",
                            "h3k27me3_2": "NA",
                            "ctcf_1": "NA",
                            "ctcf_2": "NA"
                        },
                        {
                            "chrom1": "chr4",
                            "pos1": 9330001,
                            "pos2": 9365000,
                            "chrom2": "chr4",
                            "pos3": 8620001,
                            "pos4": 9365000,
                            "id": "ENCFF021YUU",
                            "pvalue": 0.001,
                            "gene_anno_1": "USP17L25,USP17L26,USP17L27,USP17L28,USP17L29,USP17L30,USP17L5,USP17L9P",
                            "gene_anno_2": "AC073648.1,AC073648.2,AC073648.3,AC073648.4,AC073648.5,AC073648.6,AC116612.1,AC209005.1,ALG1L14P,ENPP7P10,FAM86KP,FAM90A26,HMX1,SNRPCP16,UNC93B8,USP17L10,USP17L11,USP17L12,USP17L13,USP17L14P,USP17L15,USP17L16P,USP17L17,USP17L18,USP17L19,USP17L20,USP17L21,",
                            "h3k27ac_1": "NA",
                            "h3k27ac_2": "NA",
                            "h3k27me3_1": "NA",
                            "h3k27me3_2": "NA",
                            "ctcf_1": "NA",
                            "ctcf_2": "NA"
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
