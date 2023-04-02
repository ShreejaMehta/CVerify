<template>
  <div class="file-upload">
    <div class="row">
      <!-- <div class="flex xs12">
        <va-card>
          <va-card-title>{{ t('fileUpload.advancedMediaGallery') }}</va-card-title>
          <va-card-content>
            <va-file-upload v-model="advancedGallery" type="gallery" file-types=".png, .jpg, .jpeg, .gif" dropzone />
          </va-card-content>
        </va-card>
      </div> -->
      <div class="flex xs12">
        <va-card>
          <va-card-title> Upload Resume </va-card-title>
          <va-card-content>
            <!-- <va-file-upload v-model="advancedList" dropzone @change = "handleFileUpload" /> -->
            <va-input v-model="advancedList" class="mb-6" placeholder="Enter File Path" />
            <button @click="handleFileUpload">Upload</button>
            <!-- <button @click="handleFileUpload">Upload</button> -->
          </va-card-content>
        </va-card>
      </div>
      <!-- <div class="flex xs12">
        <va-card>
          <va-card-title>{{ t('fileUpload.single') }}</va-card-title>
          <va-card-content>
            <va-file-upload v-model="single" type="single" />
          </va-card-content>
        </va-card>
      </div> -->
      <!-- <div class="flex xs12">
        <va-card>
          <va-card-title>{{ t('fileUpload.mediaGallery') }}</va-card-title>
          <va-card-content>
            <va-file-upload v-model="gallery" type="gallery" file-types=".png, .jpg, .jpeg, .gif" />
          </va-card-content>
        </va-card>
      </div> -->
      <!-- <div class="flex xs12">
        <va-card>
          <va-card-title>{{ t('fileUpload.uploadList') }}</va-card-title>
          <va-card-content>
            <va-file-upload v-model="list" />
          </va-card-content>
        </va-card>
      </div> -->
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue'
  import { useI18n } from 'vue-i18n'
  import axios from 'axios'

  const { t } = useI18n()

  const endpoint = 'http://localhost:6969/parse'
  // const advancedGallery = ref([])
  const advancedList = ref<string>('')
  // const single = ref([])
  // const gallery = ref([])
  // const list = ref([])

  // const handleFileUpload = async (filepath: string) => {
  //   // const formData = new FormData()
  //   // formData.append('filepath', filepath)
  //   // console.log(formData)
  //   // fetch(endpoint, {
  //   //   method: 'POST',
  //   //   body: formData,
  //   // })
  //   //   .then((response) => response.json())
  //   //   .then((data) => console.log(data))
  //   //   .catch((error) => console.error(error))
  //   const data = { filepath: filepath }
  //   axios
  //     .post(endpoint, data)
  //     .then((response) => {
  //       console.log(response)
  //     })
  //     .catch((error) => {
  //       console.error(error)
  //     })
  // }
  // const handleFileUpload = () => {
  //   const formData = new FormData()
  //   formData.append('filepath', advancedList.value)
  //   axios
  //     .post(endpoint, formData)
  //     .then((response) => console.log(response))
  //     .catch((error) => console.error(error))
  // }
  // const handleFileUpload = (event: any) => {
  //   const filePath = event.files[0].path
  //   axios.post(endpoint,{filePath})
  //   .then(response =>{
  //     console.log(response)
  //   })
  //   .catch(error => {
  //     console.error(error)
  //   })
  // }
  const filePath = ref('')

  const handleFileUpload = async () => {
    const data = { file: filePath.value }
    axios
      .post(endpoint, data)
      .then((response) => console.log(response))
      .catch((error) => console.error(error))
  }
</script>
