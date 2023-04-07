<template>
  <div class="medium-editor">
    <div class="row row-equal">
      <div class="row">
        <div class="flex xs12 xl3 md12">
          <va-card class="flex">
            <va-card-content>
              <div class="row row-separated">
                <div class="flex xs12">
                  <h2 class="va-h2 ma-5 va-text-center">
                    <va-avatar size="150px">
                      <!-- <i class="fas fa-user-alt" style="font-size: 100px"> </i> -->
                      <img v-bind:src="gh.avatar_url" />
                    </va-avatar>
                  </h2>
                  <p class="va-text-center"></p>
                </div>
                <div class="flex">
                  <va-card-title>Basic Details</va-card-title>
                  <va-card-content>Name: {{ candidate.name }} </va-card-content>
                  <va-card-content>Email: {{ candidate.email }}</va-card-content>
                  <va-card-content>Github: {{ candidate.github }}</va-card-content>

                </div>
              </div>
            </va-card-content>
          </va-card>
        </div>
        <div class="flex md9 xs12">
          <!-- Fetch data from Github API-->
          <!-- <va-data-table :items="repos" :columns="columns" /> -->
          <img
            :src="`http://github-profile-summary-cards.vercel.app/api/cards/stats?username=${candidate.github}&theme=github`"

          />

          <img
            :src="`http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=${candidate.github}&theme=github&exclude={exclude}`"

          />

          <img
            :src="`http://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=${candidate.github}&theme=github&exclude={exclude}`"

          />

          <img
            :src="`https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=${candidate.github}&theme=github`"
            style="width: 90%"
          />
          <!-- <img
              :src="`http://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=${candidate.github}&theme=github&utcOffset={utcOffset}`"
            /> -->
        </div>
      </div>

      <div class="flex xs12 sm6 md12 xl12">
        <va-card class="row row-separated">
          <va-card-content> LinkedIN </va-card-content>
        </va-card>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { nextTick } from 'vue'
import { useI18n } from 'vue-i18n'
import type MediumEditor from 'medium-editor'
import { useRouter } from 'vue-router'
import { useColors } from 'vuestic-ui'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { Interface } from 'readline'

const router = useRouter()
const candidate = ref({
  id: null,
  name: '',
  email: '',
  skills: [],
  education: [],
  github: '',
  linkedin: '',
  urls: [],
  status: '',
})
const gh = ref({
  login: '',
  avatar_url: '',
  public_repos: '',
})
interface Repos {
  name: string
  url: string
  forks: number
}
const repos = ref<Repos[]>([])
const githubProfileSummaryUrl = ref('')
const columns = [
  { key: 'name', sortable: true },
  { key: 'forks', sortable: true },
]
onMounted(async () => {
  const id = router.currentRoute.value.params.id
  try {
    const response = await axios.get(`http://localhost:6969/candidate/${id}`)
    candidate.value = response.data
    const name = candidate.value.github
    const res = await axios.get(`https://api.github.com/users/${name}`)
    // console.log(res.data)
    gh.value = res.data
    const rep = await axios.get(`https://api.github.com/users/${name}/repos`)
    repos.value = rep.data
    // console.log(repos.value[3].name) 
  } catch (error) {
    console.error(error)
  }
})

const { colors } = useColors()
function handleEditorInitialization(editor: typeof MediumEditor) {
  nextTick(() => highlightSampleText(editor))
}
function highlightSampleText(editor: typeof MediumEditor) {
  const sampleText = document.getElementsByClassName('default-selection')[0] as HTMLElement
  editor.selectElement(sampleText)
}
</script>
<style>
</style>