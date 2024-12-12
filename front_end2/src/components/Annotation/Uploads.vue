<template>
        <div v-if="true" class="flex items-center justify-center w-full">
      <label for="dropzone-file" @click="selectFile"
        class="bg-white flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
        <div v-if="!uploading">
          <div class="flex flex-col items-center justify-center pt-5 pb-6" @dragover.prevent="handleDragOver"
            @dragenter.prevent="handleDragEnter" @dragleave.prevent="handleDragLeave" @drop.prevent="handleDrop">
            <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2" />
            </svg>
            <p class="mb-2 text-2xl text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span>
              or
              drag and drop</p>
            <p class="text-xs text-gray-500 dark:text-gray-400">Support bedpe file (MAX. number of chromatin loops:
              5000)
            </p>
          </div>
          <input id="dropzone-file" type="file" class="hidden" @change="selectFile" />
        </div>
        <template v-else>

          <div class="flex flex-col w-3/5">
            <n-progress class="w-16" type="line" indicator-placement="inside" :percentage="progressBarContent.percent"
              processing :height="40" :border-radius="8" :fill-border-radius="0" />

          </div>
          <div>
            {{ progressBarContent.notation }}
          </div>
        </template>

      </label>
    </div>
    <div v-if="progressBarContent.percent === 100">
      <div class="mt-8 items-center justify-between p-4 mb-4 space-y-4 bg-white rounded dark:bg-gray-700 sm:flex sm:space-y-0">
                    <div>
                        <div class="text-2xl font-bold text-gray-900 dark:text-white">{{ fileNames }}</div>
                        <div class="text-sm text-gray-500 dark:text-gray-400">{{ fileSizes }}</div>
                    </div>
                    <button  @click="submitAnnotation(taskId)" class="inline-flex items-center justify-center w-full px-5 py-3 text-base font-medium text-center text-white rounded-lg sm:w-auto bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900">
                        <!-- <svg class="w-5 h-5 mr-2 -ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path>
                        </svg> -->
                        Annotate
                      </button>
                </div>
      <!-- <button type="button"
              class="mr-4 text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              @click="submitAnnotation(taskId)"></button> -->
    </div>

</template>
<script lang="ts" setup>
import axios from 'axios';
import { h, defineComponent, ref, computed, reactive } from 'vue'
import { NButton, useMessage } from 'naive-ui'
import type { DataTableColumns } from 'naive-ui'
import { useRouter, useRoute } from 'vue-router'
const router = useRouter()


const message = useMessage()
const isDragOver = ref(false);
const handleDragOver = (event) => {
  isDragOver.value = true;
  // Normally, we need to prevent the default to allow a drop
  event.preventDefault();
};

const handleDragEnter = (event) => {
  isDragOver.value = true;
};

const handleDragLeave = (event) => {
  isDragOver.value = false;
};

const fileNames = ref('')
const fileSizes = ref('')

const handleDrop = (event) => {
  isDragOver.value = false;
  const files = event.dataTransfer.files;
  if (files.length > 0) {
    selectedFile.value = files[0];
    if (selectedFile.value) {
    fileNames.value = selectedFile.value.name;
    fileSizes.value = (selectedFile.value.size / 1024).toFixed(2) + ' KB';
  }
    uploadFile();
  }
};




const selectedFile = ref(null)
const uploading = ref(false)
const progressBarContent = ref({
  percent: 0,
  notation: 'Start File uploading'

})
const result = ref(null)

const selectFile = (event) => {
  selectedFile.value = event.target.files[0];
  if (selectedFile.value) {
    fileNames.value = selectedFile.value.name;
    fileSizes.value = (selectedFile.value.size / 1024).toFixed(2) + ' KB';
  }
  uploadFile()
}

const taskId = ref('')

const uploadFile = () => {
  if (!selectedFile.value) return;
  
  uploading.value = true;
  const formData = new FormData();
  formData.append('file', selectedFile.value);
  axios.post(import.meta.env.VITE_BASE_URL + '/annotations/upload/', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    },
    onUploadProgress: progressEvent => {
      progressBarContent.value.percent = parseInt(Math.round((progressEvent.loaded * 100) / progressEvent.total)) / 10;
    }
  })
    .then(response => {
      // Upload complete, start checking for the result
      uploading.value = false;
      // overallProgress.value = 'annotation'
      taskId.value = response.data.task_id;
console.log(response)
      progressBarContent.value.percent = 100
      progressBarContent.value.notation = 'Uploading completed'

    })
    .catch(error => {
      console.error('Upload failed:', error);
      uploading.value = false;
    });
}

const submitAnnotation = (taskId) =>{
  router.push(`task-info/${taskId}`)
}
</script>