<template>
  <n-collapse arrow-placement="right" :default-expanded-names="expanded ? name : null" accordion>
    <!-- 右侧 -->
    <template #header-extra>
      <div @click="click">
        <slot name="header"></slot>
      </div>
    </template>

    <n-collapse-item :title="name" :name="name">
      <slot></slot>
    </n-collapse-item>
  </n-collapse>
  <n-divider style="margin: 4px 0px 4px 0px;"></n-divider>

</template>

<script setup lang="ts">
defineProps({
  name: {
    type: String,
    required: true
  },
  expanded: {
    type: Boolean,
    required: false,
    default: false
  }
})

// const name = new Date().getTime()

const click = (e:MouseEvent) => {
  e.preventDefault()
  e.stopPropagation()
}
</script>
