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
                      <i class="fas fa-user-alt" style="font-size: 100px"> </i>
                    </va-avatar>
                  </h2>
                  <p class="va-text-center"></p>
                </div>
                <div class="flex xs6 xl3">
                  <va-card-title>Basic Details</va-card-title>
                  <va-card-content>Name: {{ candidate.name }} </va-card-content>
                  <va-card-content>Email: {{ candidate.email }}</va-card-content>
                  <va-card-content>Github: {{ candidate.github }}</va-card-content>
                  <p class="va-text-center no-wrap"></p>
                </div>
              </div>
            </va-card-content>
          </va-card>
        </div>
        <div class="flex">
          <br />
          <va-card class="xs12 sm6 md12">
            <va-card-title>Github Data</va-card-title>
            <!-- Fetch data from Github API-->
            <va-card-content>
              <h2 class="va-h2 ma-0" :style="{ color: colors.primary }"></h2>
              <p class="no-wrap">Completed Pull Requests</p>
            </va-card-content>
          </va-card>
        </div>
      </div>
      <div class="flex xs12 sm6 md12 xl12">
        <va-card class="row row-seperated">
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
  import { useColors } from 'vuestic-ui'
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
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
    userName: '',
    avatarUrl: '',
  })
  onMounted(async () => {
    try {
      const response = await axios.get('http://localhost:6969/candidate/1')
      // const data = await response.json()
      candidate.value = response.data
      console.log(candidate.value)
      // const res = await axios.get(`https://api.github.com/users/`)
      // console.log(res.data)
      // gh.value = res.data
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

