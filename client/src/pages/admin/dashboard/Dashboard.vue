<template>
  <div class="dashboard">
    <va-card>
      <va-card-title>List of candidates</va-card-title>
      <va-card-content>
        <div class="va-table va-table--striped va-table--hoverable">
          <!-- <table class="va-table va-table--striped va-table--hoverable">
            <thead>
              <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="c in candidates" :key="c.id">
                <td>{{ c.name }}</td>
                <td>{{ c.email }}</td>
                <td><va-badge :text="c.status" :color="getStatusColor(c.status)" /></td>
              </tr>
            </tbody>
          </table> -->
          <va-data-table :items="candidates" :columns="columns" :clickable="true" @row:click="handleClick">
          </va-data-table>
        </div>
      </va-card-content>
    </va-card>
  </div>
</template>

<script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { routerViewLocationKey } from 'vue-router'
  import { isTemplateElement } from '@babel/types'
  import router from '../../../router'
import { userInfo } from 'os'
import UserInfo from '../../user/UserInfo.vue'
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
 
  const handleClick = (event: any) => {
    console.log(event)
    const routes = [{ path: '/user/user-info', component: UserInfo, props: true }]
  }
  const columns = [
    { key: 'id', sortable: true },
    { key: 'name', sortable: true },
    { key: 'email', sortable: true },
    { key: 'status', width: 80 },
  ]

  onMounted(async () => {
    try {
      const response = await axios.get('http://localhost:6969/summary/100')
      // const data = await response.json()
      candidates.value = response.data
    } catch (error) {
      console.error(error)
    }
  })
  function getStatusColor(status: string) {
    if (status === 'Accepted') {
      return 'success'
    }

    if (status === 'processing') {
      return 'info'
    }
    return 'danger'
  }
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
