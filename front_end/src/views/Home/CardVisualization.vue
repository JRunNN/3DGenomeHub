<template>
	<n-card hoverable>
		<template #cover>
			<div class="p-10">
			<img src="@/assets/images/visualization.png" width="900" height="400" />
			</div>
		</template>
		<template #header>
			<span>In-house genome browser</span>
			<!-- <span class="ml-3 text-secondary-color">$644,00</span> -->
		</template>
		<!-- <template #header-extra>
			<Icon class="mr-3" :size="20" color="#FF0156" :name="HeartIcon"></Icon>
			<Icon :size="20" :name="ShareIcon"></Icon>
		</template> -->
		<template #default>
			<p>
				Visualize various 3D genomic features
				<br />
				<br />
				Visualize contact matrix, compartments, contac domains, stripes, chromatin loops
			</p>
		</template>
		<template #action>
			<div class="flex items-center justify-between">
				<!-- <n-button type="primary" quaternary>Details</n-button> -->
				<n-button type="primary" @click="$router.push({ name: 'Sample', params: { id: 'GSM4072698' } })">
					<!-- <Icon class="mr-3" :name="CartIcon"></Icon> -->
					Try customed visualization
				</n-button>
			</div>
		</template>
	</n-card>
</template>

<script setup lang="ts">
import { NCard, NButton, NText } from "naive-ui"
import Icon from "@/components/common/Icon.vue"
import { useRouter } from "vue-router";
const router = useRouter()
const CartIcon = "tabler:shopping-cart"
const HeartIcon = "ion:heart"
const ShareIcon = "carbon:share"
</script>
