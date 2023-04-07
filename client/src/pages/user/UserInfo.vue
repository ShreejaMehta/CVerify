<template>
  <div class="medium-editor">
    <div class="row row-equal">
      <div class="row">
        <div class="flex xs12 xl3 md12">
          <va-card>
            <va-card-content>
              <div class="row row-separated">
                <div class="flex xs12">
                  <h2 class="va-h2 ma-0 va-text-center">
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
                  <p class="va-text-center no-wrap"></p>
                </div>
              </div>
            </va-card-content>
          </va-card>
          <br />
          <va-card class="flex">
            <va-card-content>
              <h2 class="va-h2 ma-0" :style="{ color: colors.info }">{{ gh.public_repos }}</h2>
              <p class="no-wrap">Public Repos</p>
            </va-card-content>
          </va-card>
          <br />
          <va-card class="flex">
            <va-card-content>
              <h2 class="va-h2 ma-0" :style="{ color: colors.primary }">123</h2>
              <p class="no-wrap">Total Commits</p>
            </va-card-content>
          </va-card>
          <br />
          <va-card class="flex flex-col gap-2">
            <va-card-title>Skills</va-card-title>
            <va-card-content>
              <va-progress-bar :model-value=gh.public_repos color="success" />
            </va-card-content>
          </va-card>
        </div>
        <div class="flex md9">
          <va-card>
            <va-card-title>Repositories</va-card-title>
            <!-- Fetch data from Github API-->
            <va-data-table :items="repos" :columns="columns" />
          </va-card>
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
