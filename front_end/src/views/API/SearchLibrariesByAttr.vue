<template>
                <n-card class="mb-8">
                    <template #header>
                        <div class="text-2xl">
                            Search datasets by one or multiple conditions
                        </div>
                    </template>
                    <div class="mb-4">
                        <n-space align="center">
                            <n-tag type="info">
                                GET
                            </n-tag>
                            <n-code :code="` /datasets/tissue={string}&heatlth_status={string}&biomaterial={string}`"
                                language="shell" inline />
                        </n-space>
                    </div>
                    <APICodeExample title="Example 1: Search all datasets from cancer">
                        <template #code1="{ js }">
                            {{ js(`
                                https://expresso.sustech.edu.cn/api/samples?health_status=cancer&limit=10&offset=1     `) }}
                        </template>
                        <template #code2="{ js }">
                            {{ js(`
                            [
                            {
                                "id": "\nGSM5369938",
                                "data_source": "ENCODE",
                                "data_type": "ChIA-PET",
                                "tissue": "Colon",
                                "health_status": "Cancer",
                                "biomaterial_type": "Cell Line",
                                "enzyme_linker": "ACGCGATATCTTATCTGACT",
                                "factor": "RNAPII",
                                "cell_line_name": "HCT116"
                            },
                            {
                                "id": "\nGSM5369939",
                                "data_source": "ENCODE",
                                "data_type": "ChIA-PET",
                                "tissue": "Colon",
                                "health_status": "Cancer",
                                "biomaterial_type": "Cell Line",
                                "enzyme_linker": "ACGCGATATCTTATCTGACT",
                                "factor": "RNAPII",
                                "cell_line_name": "HCT116"
                            },
                            {
                                "id": "\nGSM5374056",
                                "data_source": "ENCODE",
                                "data_type": "ChIA-PET",
                                "tissue": "hESC derived",
                                "health_status": "Healthy",
                                "biomaterial_type": "Cell Line",
                                "enzyme_linker": "ACGCGATATCTTATCTGACT",
                                "factor": "RNAPII",
                                "cell_line_name": "AG04450"
                            },
                            {
                                "id": "\nGSM5379364",
                                "data_source": "ENCODE",
                                "data_type": "ChIA-PET",
                                "tissue": "Liver",
                                "health_status": "Cancer",
                                "biomaterial_type": "Cell Line",
                                "enzyme_linker": "ACGCGATATCTTATCTGACT",
                                "factor": "RNAPII",
                                "cell_line_name": "HepG2"
                            },
                            {
                                "id": "ENCLB439RJA",
                                "data_source": "ENCODE",
                                "data_type": "ChIA-PET",
                                "tissue": "Blood",
                                "health_status": "Healthy",
                                "biomaterial_type": "Cell Line",
                                "enzyme_linker": "ACGCGATATCTTATCTGACT",
                                "factor": "RNAPII",
                                "cell_line_name": "GM12878"
                            },
                            {
                                "id": "ENCLB897ZCQ",
                                "data_source": "ENCODE",
                                "data_type": "ChIA-PET",
                                "tissue": "Blood",
                                "health_status": "Healthy",
                                "biomaterial_type": "Cell Line",
                                "enzyme_linker": "ACGCGATATCTTATCTGACT",
                                "factor": "RNAPII",
                                "cell_line_name": "GM12879"
                            },
                            {
                                "id": "GSM1023732",
                                "data_source": "GEO",
                                "data_type": "in-situ Hi-C",
                                "tissue": "Skin",
                                "health_status": "Healthy",
                                "biomaterial_type": "Cell Line",
                                "enzyme_linker": "HindIII",
                                "factor": "NA",
                                "cell_line_name": "HGFDFN168"
                            },
                            {
                                "id": "GSM1023733",
                                "data_source": "GEO",
                                "data_type": "in-situ Hi-C",
                                "tissue": "Skin",
                                "health_status": "Healthy",
                                "biomaterial_type": "Cell Line",
                                "enzyme_linker": "HindIII",
                                "factor": "NA",
                                "cell_line_name": "AG08470"
                            },
                            {
                                "id": "GSM1023734",
                                "data_source": "GEO",
                                "data_type": "in-situ Hi-C",
                                "tissue": "Skin",
                                "health_status": "Non-Cancer Disease",
                                "biomaterial_type": "Cell Line",
                                "enzyme_linker": "HindIII",
                                "factor": "NA",
                                "cell_line_name": "HGADFN167"
                            },
                            {
                                "id": "GSM1023735",
                                "data_source": "GEO",
                                "data_type": "in-situ Hi-C",
                                "tissue": "Skin",
                                "health_status": "Non-Cancer Disease",
                                "biomaterial_type": "Cell Line",
                                "enzyme_linker": "HindIII",
                                "factor": "NA",
                                "cell_line_name": "HGADFN167"
                            },
                            {
                                "id": "GSM1267196",
                                "data_source": "GEO",
                                "data_type": "in-situ Hi-C",
                                "tissue": "hESC derived",
                                "health_status": "Healthy",
                                "biomaterial_type": "Cell Line",
                                "enzyme_linker": "HindIII",
                                "factor": "NA",
                                "cell_line_name": "hESC"
                            },...]
                            `) }}
                        </template>
                    </APICodeExample>
                    <APICodeExample title="Example 2: Search all datasets from liver or heart">
                        <template #code1="{ js }">
                            {{ js(`
                            /datasets/tissue=liver,heart
                            `) }}
                        </template>
                        <template #code2="{ js }">
                            {{ js(`
                            {
                            gsm_id: '',
                            health_status: '',

                            }
                            `) }}
                        </template>
                    </APICodeExample>
                    <APICodeExample
                        title="Example 3: Search all cancer datasets from heart and biomaterials are from tissue">
                        <template #code1="{ js }">
                            {{ js(`
                            /datasets/tissue=heart&health_status=cancer&biomaterial=tissue
                            `) }}
                        </template>
                        <template #code2="{ js }">
                            {{ js(`
                            {
                            gsm_id: '',
                            health_status: '',

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
