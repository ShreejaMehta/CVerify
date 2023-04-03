<template>
  <div class="file-upload">
    <div class="row">
      <div class="flex xs12">
        <va-card>
          <va-card-title>{{ t('fileUpload.advancedUploadList') }}</va-card-title>
          <va-card-content>
            <va-file-upload v-model="advancedList" dropzone />
          </va-card-content>
        </va-card>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue'

  const advancedList = ref([])

</script>
