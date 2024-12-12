<script setup lang="ts">
import { computed } from 'vue'
import { RouterView } from 'vue-router'
import { useRouter, useRoute } from 'vue-router';

const route = useRoute();
const router = useRouter();

const generator: any = (routerMap) => {
  return routerMap.map((item) => {
    const currentMenu = {
      ...item,
      label: item.meta.title,
      key: item.name,
      disabled: item.path === '/',
    };
    // 是否有子菜单，并递归处理
    // if (item.children && item.children.length > 0) {
    //   // Recursion
    //   currentMenu.children = generator(item.children, currentMenu);
    // }
    return currentMenu;
  });
};

const breadcrumbList = computed(() => {
  console.log(route.matched)
  return generator(route.matched);
});

const dropdownSelect = (key) => {
  router.push({ name: key });
};

</script>

<template>
  <div class="w-10/12 min-w-[800px]  p-4">
    <!-- <div
        class="mr-1 layout-header-trigger layout-header-trigger-min"
        v-if="headerSetting.isReload"
        @click="reloadPage"
      >
        <n-icon size="18">
          <ReloadOutlined />
        </n-icon>
      </div> -->




    <!-- 面包屑 -->
    <div class="mb-4">
      <n-breadcrumb v-if="true" separator=">">
        <template v-for="routeItem in breadcrumbList" :key="routeItem.name === 'Redirect' ? void 0 : routeItem.name">
          <!-- {{ routeItem }} -->
          <n-breadcrumb-item clickable="true" href="/">
            <n-icon size="18" class="mr-2 mb-0.5">
              <svg class="w-5 h-5 " aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                viewBox="0 0 20 20">
                <path
                  d="m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z" />
              </svg>
            </n-icon>
            <span class="">Home</span>
          </n-breadcrumb-item>
          <n-breadcrumb-item clickable="true" :href="routeItem.path"
            v-if="routeItem.meta.title && routeItem.meta.title != 'Home'">
            <n-dropdown v-if="routeItem.children.length" :options="routeItem.children" @select="dropdownSelect">
              <span class="link-text">
                <component v-if="routeItem.meta.icon" :is="routeItem.meta.icon" />
                {{ routeItem.meta.title }}
              </span>
            </n-dropdown>

            <span class="inline-block" v-else>
              <!-- <component v-if="routeItem.meta.icon" :is="routeItem.meta.icon" /> -->
              {{ routeItem.meta.title }}
            </span>
            <!-- {{ routeItem }} -->
          </n-breadcrumb-item>

        </template>
      </n-breadcrumb>
    </div>
    <RouterView />
  </div>
</template>