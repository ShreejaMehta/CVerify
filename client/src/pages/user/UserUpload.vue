<template>
  <div class="file-upload">
    <div class="row">
      <div class="flex xs12">
        <va-card>
          <va-card-title>Resume Upload</va-card-title>
          <va-card-content>
            <va-file-upload v-model="fileList" file-types=".pdf" dropzone @onchange="handleUpload" />
          </va-card-content>
          <!-- TODO: Center the Button -->
          <div class="row justify-center">
            <va-button v-if="fileList.length > 0" icon="upload" :onclick="handleUpload">Upload?</va-button>
          </div>
          <br />
        </va-card>
      </div>
    </div>
    <va-card>
      <va-card-title>Uploaded Resumes!</va-card-title>
      <va-card-content>
        <div class="va-table-responsive">
          <table class="va-table va-table--clickable">
            <thead>
              <tr>
                <th>FileName</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="candidate in candidateList" :key="candidate.candidateId" @click="handleOnClick(candidate)">
                <td>{{ candidate.fileName }}</td>
                <va-badge text="Analyzed" color="success" class="ma-2" />
              </tr>
            </tbody>
          </table>
        </div>
      </va-card-content>
    </va-card>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()
type Candidate = {
  fileName: string
  candidateId: number
}

const fileList = ref<any>([]) // Bad Coding practice
const candidateList = ref<Candidate[]>([])

const handleOnClick = (candidate: Candidate) => {
  console.log(candidate)
  // TODO: Redirect to the candidate page
  router.push({ path: `/user-info/${candidate.candidateId}` })
}

const handleUpload = async () => {
  for (let file of fileList.value) {
    // TODO: Add error handling for axios
    let resp = await axios
      .post(
        'http://localhost:6969/upload',
        {
          file: file,
        },
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        },
      )
      .then((resp) => {
        candidateList.value.push({
          fileName: file.name,
          candidateId: resp.data['candidate_id'],
        })
        console.log(candidateList.value)
      })
      .catch((err) => {
        console.log(err)
      })
  }
}
</script>
