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
          <ColorfulBars />
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
    <!-- <div class="flex md12">
        <va-card>
          <va-card-title>{{ t('forms.mediumEditor.title') }}</va-card-title>
          <va-card-content class="d-flex justify-center">
            <va-medium-editor @initialized="handleEditorInitialization">
              <h1>Select Text To Open Editor</h1>
              <p>
                You enter into your favorite local bar looking
                <span class="default-selection"><b>good</b></span> as hell, but you know the only heads you want to
                turn—spicy & stylish alpha bitches — are heavily fixated on the D. The hot girl talks to you, but she
                only wants to be your best friend. Her nonthreatening and attentive best friend. Receiver of sexy
                selfies, listener of stories. Meanwhile, you attract unwanted attention from straight men, pudgy and
                greasy moths to your emotionally distant flame.
              </p>
              <p>
                Read the full article on
                <a href="https://medium.com/@dorn.anna/girl-no-you-dont-2e21e826c62c">Medium</a>
              </p>
            </va-medium-editor>
          </va-card-content>
        </va-card>
      </div> -->
    <!-- <div class=" flex xs8 md3">
        <va-avatar size="150px" font-size="30px">
          <i class="fas fa-user-alt" style="font-size: 80px"></i>
        </va-avatar> 
      </div>
      <va-card class="flex ">
        <va-card-title>Basic Details</va-card-title>
        <va-card-content>Name:{{  }}</va-card-content>
      </va-card> -->
  </div>
</template>

<script setup lang="ts">
  import { nextTick } from 'vue'
  import { useI18n } from 'vue-i18n'
  import type MediumEditor from 'medium-editor'
  import ColorfulBars from './Widgets/ColorfulBars.vue'
  import { useColors } from 'vuestic-ui'
  // import VaMediumEditor from '../../../../components/va-medium-editor/VaMediumEditor.vue'
  // const { t } = useI18n()
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
