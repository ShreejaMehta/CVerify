<template>
  <form @submit.prevent="">
    <va-input
      v-model="email"
      class="mb-3"
      type="email"
      :label="t('auth.email')"
      :error="!!emailErrors.length"
      :error-messages="emailErrors"
    />
    <va-input
      v-model="password"
      class="mb-3"
      type="password"
      :label="t('auth.password')"
      :error="!!passwordErrors.length"
      :error-messages="passwordErrors"
    />
    <div class="auth-layout__options d-flex align-center justify-space-between">
      <va-checkbox v-model="keepLoggedIn" class="mb-0" :label="t('auth.keep_logged_in')" />
      <router-link class="ml-1 va-link" :to="{ name: 'recover-password' }">{{
        t('auth.recover_password')
      }}</router-link>
    </div>

    <div class="d-flex justify-center mt-3">
      <va-button class="my-0" @click="validate(email, password)">{{ t('auth.login') }}</va-button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import axios from 'axios'
import { useToast } from 'vuestic-ui'
import { useGlobalStore } from '../../../stores/global-store'
const { t } = useI18n()

const { init } = useToast()
const store = useGlobalStore()

const email = ref('')
const password = ref('')
const keepLoggedIn = ref(false)
const emailErrors = ref<string[]>([])
const passwordErrors = ref<string[]>([])
const router = useRouter()

const formReady = computed(() => !emailErrors.value.length && !passwordErrors.value.length)

function onsubmit() {
  if (!formReady.value) return

  emailErrors.value = email.value ? [] : ['Email is required']
  passwordErrors.value = password.value ? [] : ['Password is required']

  router.push({ name: 'dashboard' })
}
const serverUrl = import.meta.env.VITE_CVERIFY_SERVER_URL === '' ? 'http://localhost:6969' : import.meta.env.VITE_CVERIFY_SERVER_URL;
const endpoint = serverUrl + '/auth/login';


const data = ref([
  {
    username: String,
    password: String,
    logged_in: String,
  },
])
const validate = async (username: string, password: string) => {
  const data2 = { username: username, password: password }
  let resp = await axios
    .post(endpoint, data2)
    .then((resp) => {
      console.log(resp)
      if (resp.data.logged_in) {
        store.updateLoggedInStatus(true)
        router.push({ name: 'dashboard' })
        init({ message: 'Logged In!', color: 'success' })
      } else {
        init({ message: 'Invalid Username/Password', color: 'danger' })
        store.updateLoggedInStatus(false)
      }
    })
    .catch((error) => {
      init({ message: 'Internal server error 500, try again later!', color: 'danger' })
      console.error(error)
    })
}
</script>
