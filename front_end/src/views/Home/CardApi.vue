<template>
	<n-card hoverable>
		<template #cover>
			<div class="p-10">
				<img src="@/assets/images/api.png" width="900" height="400" />
			</div>
		</template>
		<template #header>
			<span>Easy API access</span>
			<!-- <span class="ml-3 text-secondary-color">$644,00</span> -->
		</template>
		<!-- <template #header-extra>
			<Icon class="mr-3" :size="20" color="#FF0156" :name="HeartIcon"></Icon>
			<Icon :size="20" :name="ShareIcon"></Icon>
		</template> -->
		<template #default>
			<p>
				Progammatic access to datasets in EXPRESSO database
				<br />
				<br />
				Search sample and genes, download files
			</p>
		</template>
		<template #action>
			<div class="flex items-center justify-between">
				<!-- <n-button type="primary" quaternary>Details</n-button> -->
				<n-button type="primary" @click="handleClick">
					<!-- <Icon class="mr-3" :name="CartIcon"></Icon> -->
					Go To API page
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
	// console.log('click')
	router.push({path: '/Api'})
}
</script>
