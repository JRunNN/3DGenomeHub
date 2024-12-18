<template>
	<n-card hoverable>
		<template #cover>
			<div class="p-10">
			<img src="https://placehold.co/600x200"  />
			</div>
		</template>
		<template #header>
			<span>Upload bed files with multiple genomic regions</span>
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
				<n-button type="primary"  @click="handleClick">
					<!-- <Icon class="mr-3" :name="CartIcon"></Icon> -->
					Upload file or Paste text
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

const handleClick = ()=>{
	router.push({path: '/annotation'})
}
</script>
