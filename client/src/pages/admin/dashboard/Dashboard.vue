<template>
  <div class="dashboard">
    <va-card>
      <va-card-title>List of candidates</va-card-title>
      <va-card-content>
        <div class="va-table va-table--striped va-table--hoverable">
          <va-data-table :items="candidates" :columns="columns" :clickable="true" @row:click="handleClick">
            <template #header(status)="{ label }">
              <va-chip size="small">
                {{ label }}
              </va-chip>
            </template>
            <template #cell(status)="{ value }">
              <v-if>
                <va-chip size="small" :color="getStatusColor(value)">
                  {{ value }}
                </va-chip>
              </v-if>
            </template>
          </va-data-table>
        </div>
      </va-card-content>
    </va-card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

import { useToast } from 'vuestic-ui'
const { init } = useToast()

const router = useRouter()
interface Candidate {
  id: number
  name: string
  number: string
  email: string
  skills: string[]
  education: string[]
  github: string
  linkedIn: string
  urls: string[]
  status: string
}
const candidates = ref<Candidate[]>([])
const columns = [
  { key: 'id', sortable: true },
  { key: 'name', sortable: true },
  { key: 'email', sortable: true },
  { key: 'status', width: 80 },
]

const handleClick = (event: any) => {
  console.log(event.itemIndex)
  const id = event.itemIndex + 1
  // const routes = [{ path: `/user/user-info/ :${event.itemIndex + 1}`, redirect: { name: 'user-info' }, props: true }]
  router.push({ path: `/user-info/${id}` })
}
function getStatusColor(status: string) {
  if (status === 'Accepted') {
    return 'success'
  }

  if (status === 'processing') {
    return 'info'
  }
  return 'danger'
}

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:6969/summary/100')
    candidates.value = response.data
  } catch (error) {
    init({ message: 'Failed to fetch from server!', color: 'danger' })
    /* console.error(error) */
  }
})
</script>

<style lang="scss">
.row-equal .flex {
  .va-card {
    height: 100%;
  }
}

.dashboard {
  .va-card {
    margin-bottom: 0 !important;
    &__title {
      display: flex;
      justify-content: space-between;
    }
  }
}
</style>
