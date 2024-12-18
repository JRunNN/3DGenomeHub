import { renderIcon } from "@/utils"
import { h } from "vue"
import { RouterLink } from "vue-router"
import { type MenuMixedOption } from "naive-ui/es/menu/src/interface"

const BlankIcon = "carbon:document-blank"
const TypographyIcon = "fluent:text-font-16-regular"
const MultiLanguageIcon = "ion:language-outline"
const GroupIcon = "carbon:tree-view"
const IconsIcon = "fluent:icons-24-regular"

import dashboard from "./dashboard"
import calendars from "./calendars"
import apps from "./apps"
import cards from "./cards"
import getComponents from "./components"
import tables from "./tables"
import layout from "./layout"
import maps from "./maps"
import editors from "./editors"
import charts from "./charts"
import toolbox from "./toolbox"
import authentication from "./authentication"
const DocsIcon = "ion:book-outline"
const DashboardIcon = "carbon:database-messaging"
const ChartIcon = "carbon:chart-histogram"
const DownloadIcon = "carbon:document-download"
const SearchIcon = "carbon:search"
const AnalysisIcon = "carbon:text-link-analysis"
const APIIcon = "carbon:api-1"
const HomeIcon = "carbon:home"
const BrowseIcon = "carbon:content-view"
const HumanIcon = "mdi:head-outline"
const MouseIcon = "mingcute:mickeymouse-line"
const AnnotateIcon = "clarity:process-on-vm-line"


export default function getItems(mode: "vertical" | "horizontal", collapsed: boolean): MenuMixedOption[] {
	return [
		// dashboard,
		// calendars,
		// ...apps,
		{
			key: "divider-1",
			type: "divider",
			props: {
				style: {
					//marginLeft: "32px"
				}
			}
		},
		{
		label: () =>
			h(
				RouterLink,
				{
					to: {
						name: "home"
					}
				},
				{ default: () => "Home" }
			),
			key: "home",
			icon: renderIcon(HomeIcon)
		},
		{
			label: () =>
				h(
					RouterLink,
					{
						to: {
							name: "browse"
						}
					},
					{ default: () => "Browse" }
				),
				key: "browse",
				icon: renderIcon(BrowseIcon),
				children: [
					{
						icon: renderIcon(HumanIcon),
						label: () =>
							h(
								RouterLink,
								{
									to: {
										name: "Human"
									}
								},
								{ default: () => "Human" }
							),
						key: "Human"
					},
					{
						icon: renderIcon(MouseIcon),
						label: () =>
							h(
								RouterLink,
								{
									to: {
										name: "Mouse"
									}
								},
								{ default: () => "Mouse" }
							),
						key: "Mouse"
					}
				]
		},
		{
			label: () =>
				h(
					RouterLink,
					{
						to: {
							name: "Annotation"
						}
					},
					{ default: () => "Annotate" }
				),
				key: "annotate",
				icon: renderIcon(AnnotateIcon)
			},
			{
				label: () =>
					h(
						RouterLink,
						{
							to: {
								name: "api"
							}
						},
						{ default: () => "REST API" }
					),
					key: "api",
					icon: renderIcon(APIIcon)
				},
				{
					label: () =>
						h(
							RouterLink,
							{
								to: {
									name: "datasets"
								}
							},
							{ default: () => "Datasets" }
						),
						key: "Datasets",
						icon: renderIcon(DashboardIcon)
					},

				{
					label: () =>
						h(
							RouterLink,
							{
								to: {
									name: "Documentation"
								}
							},
							{ default: () => "Documentation" }
						),
						key: "Documentation",
						icon: renderIcon(DocsIcon)
					}
	]
}
