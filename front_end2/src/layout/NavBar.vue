<script lang="ts" setup>
import {ref} from 'vue'
import {useMessage} from 'naive-ui'

const showMenu = ref(false)
const message = useMessage()

const links = [
  {name: 'Home', path: '/',},
  {name: 'Data List', path: '/datalist'},
  // {
  //   name: 'Search', path: '/search?type=loops',
  // },
  {name: 'Active Browser', path: '/genome-browser'},
  {name: 'Cancer CRE', path: '/cancer-cre',
  // submenu: [
  // {label: 'Loop sets annotation', path: '/analysis/annotations'},
  // {label: 'Differential loops analysis', path: '/analysis/4c-virtual-plot'},
  // {label: 'Transcription factor analysis', path: '/analysis/4c-virtual-plot'},
  // {label: 'Virtual 4C plot', path: '/analysis/4c-virtual-plot'},
  // ]
},
{
  name: 'Analysis', path: '/annotation/uploads',
},
  {name: 'Download', path: '/download'},
  {name: 'Documentation', path: '/documentation'}
]

const handleSelect = (path: string) => {
  message.info(path)
}
</script>

<template>
  <nav
      class="nav-bar fixed w-full z-20 top-0 left-0  h-16 text-white">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <router-link class="flex items-center" to="/">
  <img alt="Expresso Logo" class="h-8 w-16" src="../assets/logo.svg">
  <span class="self-center text-2xl whitespace-nowrap text-white">EXPRESSO</span>
</router-link>
      <div class="flex md:order-2">
        <!-- <button
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            type="button">
          Get started
        </button> -->
        <button aria-controls="navbar-sticky" aria-expanded="false"
                class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                data-collapse-toggle="navbar-sticky" type="button">
          <span class="sr-only">Open main menu</span>
          <svg aria-hidden="true" class="w-5 h-5" fill="none" viewBox="0 0 17 14" xmlns="http://www.w3.org/2000/svg">
            <path d="M1 1h15M1 7h15M1 13h15" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                  stroke-width="2"/>
          </svg>
        </button>
      </div>
      <div id="navbar-sticky" class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1">
        <ul class="flex flex-col p-4 md:p-0 mt-4 font-medium rounded-lg  md:flex-row md:space-x-8 md:mt-0 ">
          <li v-for="link in links"
              class=" text-lg	block py-2 pl-3 pr-4  rounded hover:text-gray-400 md:hover:bg-transparent  md:p-0  dark:hover:bg-gray-700  md:dark:hover:bg-transparent"
          >
            <template v-if="link.submenu">
              <n-dropdown :options="link.submenu" size="large" trigger="hover" @select="handleSelect">
                <div class="flex justify-between items-center">
                  <router-link
                      :key="link.name"
                      :to="link.path"
                  >{{ link.name }}
                  </router-link>
                  <n-icon size="20">
                    <svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"
                         xmlns:xlink="http://www.w3.org/1999/xlink">
                      <g fill="none">
                        <path
                            d="M3.146 5.646a.5.5 0 0 1 .708 0L8 9.793l4.146-4.147a.5.5 0 0 1 .708.708l-4.5 4.5a.5.5 0 0 1-.708 0l-4.5-4.5a.5.5 0 0 1 0-.708z"
                            fill="currentColor"></path>
                      </g>
                    </svg>
                  </n-icon>
                </div>

              </n-dropdown>
            </template>
            <template v-else>
              <router-link
                  :key="link.name"
                  :to="link.path"
              >{{ link.name }}
              </router-link>
            </template>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<style>
.nav-bar {
  background-color: #1B4098;
}
</style>