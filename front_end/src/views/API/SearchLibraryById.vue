<template>
                <n-card  class="mb-8">
                    <template #header>
                        <div class="text-2xl">
                            Search a specific library by id
                        </div>
                    </template>
                    <div class="mb-4">
                        <n-space align="center">
                            <n-tag type="info">
                                GET
                            </n-tag>
                            <n-code :code="` /dataset/{gsm_id}`" language="shell" inline />
                        </n-space>
                    </div>
                    <APICodeExample title="Example 1: Search dataset GSM4072698">
                        <template #code1="{ js }">
                            {{ js(`
                            https://expresso.sustech.edu.cn/api/sample/GSM4072698
                            `) }}
                        </template>
                        <template #code2="{ js }">
                            {{ js(`
                            {
                                "id": "GSM4072698",
                                "data_source": "GEO",
                                "data_type": "in-situ Hi-C",
                                "tissue": "Colon",
                                "health_status": "Cancer",
                                "biomaterial_type": "Tissue",
                                "enzyme_linker": "MboI",
                                "factor": "NA",
                                "cell_line_name": "NA"
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
