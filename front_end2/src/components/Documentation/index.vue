<template>
  <n-card  style="margin-bottom: 16px">
    <n-tabs type="line" placement="left" 
    animated
    >
      <n-tab-pane name="Data List" tab="Data List">
        <p class="mb-4 text-xl font-light text-gray-500">

        DataList is the place where all data is displayed, and users can also filter the data according to their needs.
        </p>
        <img class="mx-auto" src="../../assets/doc/DataList.png">

      </n-tab-pane>
      <n-tab-pane name="Cell Type" tab="Cell Type">
        <p class="mb-4 text-xl font-light text-gray-500">
        Visualize and explore chromatin interactions in each cell type. Each cell type page contains three sections: (1) Basic cell information; (2) Active Browser with loaded tracks from relevant cell types; and (3) Chromatin interaction data from the relevant cell types in tabular format.
      </p>
        <img class="mx-auto" src="../../assets/doc/CellType_CellInfo.png">
        <img class="mx-auto" src="../../assets/doc/CellType_GenomeBrowser.png">
        <img class="mx-auto" src="../../assets/doc/CellType_Table.png">
      </n-tab-pane>
      <n-tab-pane name="Active Browser" tab="Active Browser">
        <p class="mb-4 text-xl font-light text-gray-500">
        You can open track loading panel to add hosted tracks to Active Browser. In the browser, you can navigate using the chromosome view bar interactively. You can also config track styles.
      </p>
        <img class="mx-auto" src="../../assets/doc/ActiveBrowser_AddTrack.png">
        <img class="mx-auto" src="../../assets/doc/ActiveBrowser_LoadTrack.png">
        <img class="mx-auto" src="../../assets/doc/ActiveBrowser_ConfigTrack.png">
      </n-tab-pane>
      <n-tab-pane name="Cancer 3D genome" tab="Cancer 3D genome">
        <img class="mx-auto" src="../../assets/doc/Cancer3D_entry.png">

      </n-tab-pane>
      <n-tab-pane name="News" tab="News">
        <section class="mt-6">
      <n-grid cols="1 s:1 m:1 l:1 xl:1 2xl:1" responsive="screen" :x-gap="12" :y-gap="8">
        <!-- <n-grid-item>
        <FrontPageCarousel />
      </n-grid-item> -->
        <n-grid-item>
          <DevTimeLine />
        </n-grid-item>
      </n-grid>
    </section>
      </n-tab-pane>
    </n-tabs>
  </n-card>
</template>
<script lang="ts" setup>
</script>
<style>
</style>