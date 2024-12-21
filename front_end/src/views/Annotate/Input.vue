<template>
    <n-tabs type="line" animated>
<!--        <n-tab-pane name="uploads" tab="FILE UPLOADS">-->
<!--            <FileUpload></FileUpload>-->
<!--        </n-tab-pane>-->
        <n-tab-pane name="textinput" tab="TEXT INPUT">
            <TextInput></TextInput>
        </n-tab-pane>

    </n-tabs>
</template>
<script setup>
import FileUpload from './FileUpload.vue';
import TextInput from './TextInput.vue';
</script>