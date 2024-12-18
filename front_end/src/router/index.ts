import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: "/",
			redirect: "/home"
		},
		{
			path: "/home",
			name: "home",
			component: () => import("@/views/Home/index.vue"),
			meta: { title: "Home" }
		},
		{
			path: "/browse",
			name: "browse",
			redirect: "/browse/human",
			meta: { title: "Home" },
			children: [
				{
					path: "human",
					name: "Human",
					component: () => import("@/views/Browse/index.vue"),
				},
				{
					path: "mouse",
					name: "Mouse",
					component: () => import("@/views/Browse/mouse.vue"),
					// props: true,  // Enable props for route params
					meta: {
						title: "Loop annotation details",
						showBreadCrumb: false
					}
				}
			]
		},
		{
			path: "/annotation",
			name: "Annotation",
			redirect: { name: "Input" },
			component: () => import("@/views/Annotate/index.vue"),
			meta: {
				title: "Loop annotation",
				showBreadCrumb: true
			},
			children: [
				{
					path: "input",
					name: "Input",
					component: () => import("@/views/Annotate/Input.vue"),
					meta: {
						title: "Upload Files",
						showBreadCrumb: false
					}
				},
				{
					path: "task-info/:taskId",
					name: "AnnotationDetail",
					component: () => import("@/views/Annotate/AnnotationDetail.vue"),
					// props: true,  // Enable props for route params
					meta: {
						title: "Loop annotation details",
						showBreadCrumb: false
					}
				}
			]
		},
		{
			path: "/api",
			name: "api",
			component: () => import("@/views/API/index.vue"),
			meta: { title: "API" }
		},
		{
			path: "/Datasets",
			name: "datasets",
			component: () => import("@/views/Datasets/index.vue"),
			meta: { title: "Home" }
		},
		{
			path: "/Documentation",
			name: "Documentation",
			component: () => import("@/views/Documentation/index.vue"),
			meta: { title: "Documentation" }
		}
	]
})

// router.beforeEach(route => {
// 	return authCheck(route)
// })

export default router
