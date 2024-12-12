<template>
    <div>
      <div class="n-layout-page-header">
        <n-card :bordered="false" title="Load a track from a valid URL">
          Fill in track id, track type and track URL.
        </n-card>
      </div>
      <n-card :bordered="false" class="mt-4 proCard">
        <n-grid cols="1 s:1 m:3 l:3 xl:3 2xl:3" responsive="screen">
          <n-grid-item offset="0 s:0 m:1 l:1 xl:1 2xl:1">
            <n-form
              :label-width="120"
              :model="formValue"
              :rules="rules"
              label-placement="left"
              ref="formRef"
              class="py-8"
            >
              <n-form-item label="Track ID" path="trackID">
                <n-input v-model:value="formValue.id" placeholder="Please fill in a track ID" />
              </n-form-item>
              <n-form-item label="Track URL" path="trackURL">
                <n-input v-model:value="formValue.url" placeholder="Please fill in a track url" />
              </n-form-item>
              <!-- <n-form-item label="Track " path="mobile">
                <n-input placeholder="电话号码" v-model:value="formValue.mobile" />
              </n-form-item> -->
              <n-form-item label="File format" path="trackType">
                <n-select
                  placeholder="Please choose a track type"
                  :options="TrackTypeList"
                  v-model:value="formValue.format"
                  @update:value="formValue.display = ''"
                />
              </n-form-item>
              <n-form-item label="Display style" path="trackDisplay">
                <!-- <n-input v-model:value="formValue.display" placeholder="Please fill in track Display style" /> -->
                <n-select 
                  placeholder="Please choose a track type"
                  :options="displayStyle.filter(item => item.format === formValue.format)[0].style || []"
                  v-model:value="formValue.display"
                />
              
              </n-form-item>

              <!-- <n-form-item label="预约事项" path="matter">
                <n-select
                  placeholder="请选择预约事项"
                  :options="matterList"
                  v-model:value="formValue.matter"
                  multiple
                />
              </n-form-item> -->
              <!-- <n-form-item label="性别" path="sex">
                <n-radio-group v-model:value="formValue.sex" name="sex">
                  <n-space>
                    <n-radio :value="1">男</n-radio>
                    <n-radio :value="2">女</n-radio>
                  </n-space>
                </n-radio-group>
              </n-form-item> -->
              <!-- <n-form-item label="预约备注" path="remark">
                <n-input
                  v-model:value="formValue.remark"
                  type="textarea"
                  placeholder="请输入预约备注"
                />
              </n-form-item> -->
 
              <div style="margin-left: 80px">
                <n-space>
                  <n-button @click="formSubmit">Submit</n-button>
                  <n-button @click="resetForm">Reset</n-button>
                </n-space>
              </div>
            </n-form>
          </n-grid-item>
        </n-grid>
      </n-card>
    </div>
  </template>
  
  <script lang="ts" setup>
    import { ref, unref, reactive,computed } from 'vue';
    import { useMessage } from 'naive-ui';
    // import { BasicUpload } from '@/components/Upload';
    // import { useGlobSetting } from '@/hooks/setting';
  
    // const globSetting = useGlobSetting();
  import addTrack from './AddTrack.js'
 
    const TrackTypeList = [
      {
        label: 'hic',
        value: 'hic'
      },{
        label: 'bedpe',
        value: 'bedpe'
      },{
        label: 'bigwig',
        value: 'bigwig'
      }, 
      {
        label: 'bed',
        value: 'bed'
      },
      // {
      //   label: 'heatmap',
      //   value: 'heatmap'
      // },
      {
        label: 'fasta',
        value: 'fasta'
      },
      {
        label: 'geneAnno',
        value: 'geneAnno'
      }
    ]
  

const displayStyle = ref([
  {
    format: 'bedpe',
    style: [
      {
      label: 'basicCurve',
      value: 'basicCurve'
      },
      {
        label: 'flatCurve',
        value: 'flatCurve'
      },
      {
        label: 'block',
        value: 'block'
      },{
        label: 'network',
        value: 'network'
      }
    ]
  },
  {
    format: 'hic',
    style: [
      {
        label: 'square',
        value: 'square'
      },
      {
        label: 'triangle',
        value: 'triangle'
      }
    ]
  },
  {
    format: 'bigwig',
    style:[
      {
        label: 'coverage',
        value: 'coverage'
      }
    ]
  },{
    format: 'geneAnno',
    style:[
      {
        label: 'UCSC',
      value: 'UCSC'
      }
    ]
  },
  {
    format: 'bed',
    style: [
      {
        label: 'block',
        value: 'block'
      }
    ]
  },{
    format: 'fasta',
    style: [
      {
        label: 'sequence',
        value:'sequence'
      }
    ]
  }
])
const disableDisplayStyle = computed(()=>{
  return displayStyle.value.some(item => item.format === formValue.format)

})

const rules = {
      trackID: {
        required: true,
        message: 'Please fill in a track ID',
        trigger: 'blur',
      },
      // trackType: {
      //   required: true,
      //   message: 'Please choose a track type',
      //   trigger: ['blur', 'change'],
      // },
      trackURL: {
        required: true,
        message: 'Please fill in a track URL',
        trigger: 'blur',
      }
    };
  
    const formRef: any = ref(null);
    const message = useMessage();
    // const { uploadUrl } = globSetting;
  
    const defaultValueRef = () => ({
      id: '',
      format: 'bedpe',
      url: '',
      display: ''
    });
  
    let formValue = reactive(defaultValueRef());
    // const uploadList = ref([
    //   'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
    // ]);
    // const uploadHeaders = reactive({
    //   platform: 'miniPrograms',
    //   timestamp: new Date().getTime(),
    //   token: 'Q6fFCuhc1vkKn5JNFWaCLf6gRAc5n0LQHd08dSnG4qo=',
    // });
  
    function formSubmit() {
      formRef.value.validate((errors) => {
        if (!errors) {
          message.success('验证成功');
          console.log(formValue)
          // addTrack(formValue.value)
        } else {
          message.error('验证失败，请填写完整信息');
        }
      });
      addTrack(formValue)
    }
  
    function resetForm() {
      formRef.value.restoreValidation();
      formValue = Object.assign(unref(formValue), defaultValueRef());
    }
  
    // function uploadChange(list: string[]) {
    //   console.log(list);
    // }
  </script>
  