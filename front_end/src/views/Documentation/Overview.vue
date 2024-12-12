<template>
    <CardWrapper v-slot="{ expand, isExpand, reload }" class="h-full grow w-full">
        <CardActions :expand="expand" :isExpand="isExpand" :reload="reload" class="h-full" title="Search samples"
            :segmented="{
                content: true,
                footer: true
            }">
            <template #header>
                <n-h3>Introduction</n-h3>
            </template>
            <template #header-extra>
            </template>
            <template #default>
                <div v-html="compiledMarkdown" class="markdown"></div>

            </template>
    
        </CardActions>
    </CardWrapper>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';

import { NTag } from "naive-ui"
import { marked } from 'marked';
import axios from 'axios';
const compiledMarkdown = ref('');

onMounted(async () => {
  try {
    // 修改URL为你的Markdown文件的远程URL
    const response = await axios.get('https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/docs/Intro.md');
    let markdown = response.data;
    // 如果Markdown中的图片路径不是完整的URL，你需要在这里进行转换
    const baseUrl = 'https://3dgenomehub.oss-cn-shenzhen.aliyuncs.com/docs/assets/images/';
    markdown = markdown.replace(/!\[([^\]]*)\]\((\.\/assets\/images\/([^)]+))\)/g, `![$1](${baseUrl}$3)`);
    compiledMarkdown.value = marked(markdown);
  } catch (error) {
    console.error('Failed to load markdown', error);
  }
});
</script>
<style >
.markdown {
  line-height: 1.6;
  font-family: sans-serif;
  /* padding: 20px; */
}

/* 单独设置标题的行距 */
.markdown > h1,
.markdown > h2,
.markdown > h3,
.markdown > h4,
.markdown > h5,
.markdown >  h6 {
  line-height: 1.4; /* 标题行距通常比正文小 */
  margin-top: 20px; /* 添加上边距使标题更清晰 */
  margin-bottom: 20px; /* 添加下边距 */
}

/* 段落间距 */
.markdown p {
  margin-bottom: 10px; /* 每个段落下方的间距 */
}
</style>