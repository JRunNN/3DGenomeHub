<template>
	<div class="page">
		<div class="main-grid gap-5">

			<!-- main col -->
			<div class="main-col">
				<div class="flex flex-col gap-5 h-full">

					<div class="flex main-chart-wrap">
						<n-card :bordered="true" >
      <n-skeleton text v-if="loading" :repeat="2" />
      <template v-else>
		<div class="w-full px-8 md:px-8 xl:px-8 py-2 lg:py-2 ">
			<p class="mb-2 text-l text-gray-500 dark:text-gray-400 leading-10 text-justify">
		<span>
			EXPRESSO has been published in <strong><em>Nucleic Acids Research</em></strong> as <strong>NAR Breakthrough Article</strong>. If you are using EXPRESSO, please cite:
		</span>
		</p>
		<p class="mb-2 text-l text-gray-500 dark:text-gray-400 leading-10 text-justify">
		<span>
			Cai,L., Qiao,J., Zhou,R., Wang,X., Li,Y., Jiang,L., Zhou,Q., Li,G., Xu,T. and Feng,Y. (2024) EXPRESSO: a multi-omics database to explore multi-layered 3D genomic organization. Nucleic Acids Research, 10.1093/nar/gkae999.
		</span>
		</p>
		<p class="mb-2 text-l text-gray-500 dark:text-gray-400 leading-10 text-justify">
		<span>
			We would love to hear your suggestions. Please ask your questions <a href="https://github.com/lycai05/EXPRESSO/issues"><strong>here</strong></a>, and we will respond as soon as possible.
		</span>
		</p>
		</div>
      </template>

  </n-card>
</div>
					<!-- big chart -->
					<div class="flex main-chart-wrap">
						<Intro class="h-full"></Intro>
					</div>


					<div class="flex grow">
<BodySiteBarChart></BodySiteBarChart>
					</div>

<div class="flex justify-between gap-5 mt-6">
	<CardAnalysis></CardAnalysis>
		<CardVisualization></CardVisualization>
		<CardApi></CardApi>
</div>
				</div>
			</div>

		</div>
	</div>
</template>

<script lang="ts" setup>
import { useThemeStore } from "@/stores/theme"
import { computed } from "vue"
import Intro from "./Intro.vue"
import CardAnalysis from "./CardAnalysis.vue"
import CardVisualization from "./CardVisualization.vue"
import CardApi from "./CardApi.vue"

const SessionsIcon = "carbon:user-multiple"
const UsersIcon = "carbon:user"
const ReportsIcon = "carbon:report"
const ErrorIcon = "carbon:debug"
const ViewsIcon = "carbon:view"
const ActivityIcon = "carbon:activity"
const UploadsIcon = "carbon:cloud-upload"

const themeStore = useThemeStore()

import BodySiteBarChart from './BodySiteBarChart.vue'

const style = computed<{ [key: string]: any }>(() => themeStore.style)
const textSecondaryColor = computed<string>(() => style.value["--fg-secondary-color"])

const chartBg = computed<string>(() =>
	themeStore.isThemeDark ? style.value["--secondary1-color"] : style.value["--secondary1-color"]
)
</script>

<style lang="scss" scoped>
.page {
	.main-grid {
		display: grid;
		grid-template-columns: repeat(1, 1fr);
		grid-template-rows: repeat(1, 1fr);
		grid-template-areas: "main main side";

		@media (max-width: 1200px) {
			display: flex;
			flex-direction: column;

			.timeline-wrap {
				min-height: 400px;
				display: flex;
				flex-direction: column;

				.n-card {
					flex-grow: 1;
				}
			}
		}
	}

	.main-col {
		grid-area: main;
		container-type: inline-size;

		// .main-chart-wrap {
		// 	height: 450px;
		// }

		.four-cards-wrap {
			display: grid;
			grid-template-columns: repeat(4, minmax(0, 1fr));
			grid-template-rows: repeat(1, minmax(0, 1fr));

			@container (max-width: 1000px) {
				grid-template-columns: repeat(2, minmax(0, 1fr));
				grid-template-rows: repeat(2, minmax(0, 1fr));
			}

			@container (max-width: 460px) {
				grid-template-columns: repeat(1, minmax(0, 1fr));
				grid-template-rows: repeat(4, minmax(0, 1fr));
			}
		}
	}

	.side-col {
		grid-area: side;
	}
}
</style>
