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
import axios, { AxiosError } from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vuestic-ui'
const router = useRouter()

const { init: toast } = useToast()

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
    axios
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
        if (resp.status !== 200 || resp.data['candidate_id'] === undefined) {
          toast({ message: `Failed to upload resume ${file.name}`, color: 'danger' })
          return
        }
        candidateList.value.push({
          fileName: file.name,
          candidateId: resp.data['candidate_id'],
        })
		toast({ message: `Upload success: ${file.name}`, color: 'success' })
      })
      .catch((err: AxiosError | Error) => {
		if(axios.isAxiosError(err)) {
			if(err.status === 400) {
				toast({ message: `Unable to upload ${file.name}. ${err.message}`, color: 'danger' })
			}
			else if (err.status == 422) {
				toast({ message: `Unable to upload ${file.name}. INVALID FILE TYPE`, color: 'danger' })
			}
			else {
				toast({ message: `Unable to upload ${file.name}. is the server up?`, color: 'danger' })
			}
		}
		else {
	 		toast({ message: `Unable to upload ${file.name}. Unkown Error`, color: 'danger' })
		}
      })
  }
}
</script>
