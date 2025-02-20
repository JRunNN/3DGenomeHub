<template>
    <div v-if="state === 'start'">
      <div
        class="h-64 bg-white flex flex-col w-full border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
        <div v-if="!uploading">
          <textarea id="description" v-model="inputText" rows="4"
            class="h-full bg-white block p-2.5 w-full text-sm text-gray-900 rounded-lg focus:ring-primary-500 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
            placeholder="Paste your bed format data here...
Example format:
chr1  1000  2000 
chr2  5000  6000"></textarea>
        </div>
      </div>
      <div class="mt-4 flex justify-between items-center">
        <p class="text-xs text-gray-500 dark:text-gray-400">
          Maximum 5000 chromatin loops
        </p>
        <button @click="handleSubmit" :disabled="!inputText.trim()"
          class="px-4 py-2 text-sm font-medium text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 disabled:opacity-50 disabled:cursor-not-allowed">
          Submit
        </button>
      </div>
    </div>
  
    <div v-else-if="state === 'uploading'">
      <div class="flex flex-col w-3/5">
        <n-progress class="w-16" type="line" indicator-placement="inside" :percentage="progressBarContent.percent"
          processing :height="40" :border-radius="8" :fill-border-radius="0" />
      </div>
      <div>
        {{ progressBarContent.notation }}
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import {computed, ref} from 'vue'
  import axios from 'axios'
  import {useMessage} from 'naive-ui'
  import {useRouter} from 'vue-router'

  const router = useRouter()
  const message = useMessage()
  
  const state = ref('start')
  const inputText = ref('')
  const uploading = ref(false)
  const progressBarContent = ref({
    percent: 0,
    notation: 'Processing input...'
  })
  
  const taskId = ref('')
  
  // Computed properties for displaying file info
  const fileNames = computed(() => 'input.bedpe')
  const fileSizes = computed(() => {
    const bytes = new TextEncoder().encode(inputText.value).length
    return (bytes / 1024).toFixed(2) + ' KB'
  })
  
  const validateInput = (text: string) => {
    if (!text.trim()) {
      message.error('Please enter some data')
      return false
    }
  
    const lines = text.trim().split('\n')
    if (lines.length > 5000) {
      message.error('Maximum 5000 chromatin loops allowed')
      return false
    }
  
    for (const line of lines) {
      const fields = line.trim().split(/\s+/)

  
      // Additional validation for chromosome names and positions
      // if (!fields[0].startsWith('chr') || !fields[3].startsWith('chr')) {
      //   message.error('Chromosome names should start with "chr"')
      //   return false
      // }
  
      // Validate that positions are numbers
      // for (let i of [1, 2, 4, 5]) {
      //   if (isNaN(Number(fields[i]))) {
      //     message.error('Positions must be numeric values')
      //     return false
      //   }
      // }
    }
  
    return true
  }
  const handleSubmit = async () => {
    if (!validateInput(inputText.value)) {
      return
    }

    state.value = 'uploading'
    uploading.value = true

    try {
      const lines = inputText.value.trim().split('\n')
      // 提取用户输入的文本数据
      const payload = {
        queries: lines.map(line => line.trim()), // 将输入的文本内容作为 JSON 参数
      }
      console.log("输入的数据为：", payload.queries)

      // 发送 POST 请求，将输入数据传递到后端
      const response = await axios.get('http://127.0.0.1:8000/api/results/get_text_input_overview/', payload.queries, {
        headers: {
          'Content-Type': 'application/json',
        },
      })

      const result = response.data // 从响应中提取数据
      message.success('Data processed successfully!')
    } catch (error) {
      console.error('Request failed:', error)
      message.error('Request failed, please try again.')
      state.value = 'start'
      uploading.value = false
    }
  }
  
  // Reset function
  const resetForm = () => {
    inputText.value = ''
    state.value = 'start'
    uploading.value = false
    progressBarContent.value = {
      percent: 0,
      notation: 'Processing input...'
    }
  }
  </script>
  
  <style scoped>
  textarea {
    resize: none;
    height: 100%;
    font-family: monospace;
  }
  
  textarea::placeholder {
    white-space: pre;
  }
  </style>