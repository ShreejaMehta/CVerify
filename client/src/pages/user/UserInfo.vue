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
                      <img :src="gh.avatar_url" />
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
        </div>
      </div>

      <div class="flex">
        <va-card class="row row-separated">
          <va-card-title>Skills</va-card-title>
          <va-card-content>
            <div class="flex xs12">
              <va-chip-group>
                <va-chip v-for="skill in candidate.skills" :key="skill" color="primary" style="margin: 8px">
                  {{ skill }}
                </va-chip>
              </va-chip-group>
            </div>
          </va-card-content>
        </va-card>
      </div>
    </div>
    <br />
    <div class="flex items-center">
      <va-card>
        <va-card-title>Actions </va-card-title>
        <va-card-content>
          <va-button icon="arrow_forward" icon-color="#fff" class="flex" style="margin: 8px">
            Accept
          </va-button>
          <va-button icon="clear" color="danger" class="flex" style="margin: 8px"> Reject </va-button>
        </va-card-content>
      </va-card>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'

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
onMounted(async () => {
  const id = router.currentRoute.value.params.id
  try {
    const response = await axios.get(`http://localhost:6969/candidate/${id}`)
    candidate.value = response.data
    const name = candidate.value.github
    // const linkedin = candidate.value.linkedin
    const res = await axios.get(`https://api.github.com/users/${name}`)
    // console.log(res.data)
    gh.value = res.data
    const rep = await axios.get(`https://api.github.com/users/${name}/repos`)
    repos.value = rep.data

    // to fetch data from linkedin
    // const rem = await axios.get(`https://api.linkedin.com/v2/`)
    // console.log(rem.data)
    // console.log(repos.value[3].name)
  } catch (error) {
    console.error(error)
  }
})
</script>
<style></style>
