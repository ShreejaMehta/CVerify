<template>
  <div class="dashboard">
    <va-card>
      <va-card-title>List of candidates</va-card-title>
      <va-card-content>
        <div class="table-wrapper">
          <table class="va-table va-table--striped va-table--hoverable">
            <thead>
              <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Number</th>
                <th>Skills</th>
                <th>Github</th>
                <th>LinkedIn</th>
                <th>Urls</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="c in candidates" :key="c.id">
                <td>{{ c.name }}</td>
                <td>{{ c.email }}</td>
                <td>{{ c.number }}</td>
                <td>{{ c.skills.join(', ') }}</td>
                <td>{{ c.github }}</td>
                <td>{{ c.linkedIn }}</td>
                <td>{{ c.urls.join(' ') }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </va-card-content>
    </va-card>
  </div>
</template>

<script setup lang="ts">
  import { ref, onMounted } from 'vue'

  import DashboardCharts from './DashboardCharts.vue'
  import DashboardInfoBlock from './DashboardInfoBlock.vue'
  import DashboardTabs from './DashboardTabs.vue'
  import DashboardMap from './DashboardMap.vue'
import axios from 'axios'
  const dashboardMap = ref()
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
  }
  const candidates = ref<Candidate[]>([])

  onMounted(async () => {
    try {
      const response = await axios.get('http://localhost:6969/summary/100')
      // const data = await response.json()
      candidates.value = response.data
    } catch (error) {
      console.error(error)
    }
  })
  function addAddressToMap({ city, country }: { city: { text: string }; country: string }) {
    dashboardMap.value.addAddress({ city: city.text, country })
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
