<template>
  <div class="markup-tables flex">
    <!-- <va-card class="flex mb-4">
      <va-card-title>{{ t('tables.basic') }}</va-card-title>
      <va-card-content>
        <div class="table-wrapper">
          <table class="va-table">
            <thead>
              <tr>
                <th>{{ t('tables.headings.name') }}</th>
                <th>{{ t('tables.headings.email') }}</th>
                <th>{{ t('tables.headings.country') }}</th>
                <th>{{ t('tables.headings.status') }}</th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="user in users" :key="user.id">
                <td>{{ user.name }}</td>
                <td>{{ user.email }}</td>
                <td>{{ user.country }}</td>
                <td>
                  <va-badge :text="user.status" :color="getStatusColor(user.status)" />
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </va-card-content>
    </va-card> -->

    <va-card>
      <va-card-title>{{ t('Applicants') }}</va-card-title>
      <va-card-content>
        <div class="table-wrapper">
          <table class="va-table va-table--striped va-table--hoverable">
            <thead>
              <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Country</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users" :key="user.id">
                <td>{{ user.name }}</td>
                <td>{{ user.email }}</td>
                <td>{{ user.country }}</td>
                <td>
                  <va-badge :text="user.status" :color="getStatusColor(user.status)" />
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </va-card-content>
    </va-card>
    <va-card variant="tonal">
      <va-card-title>Application Status Summary</va-card-title>
      <va-card-content>
        <div class="flex xl6 xs12 lg6">
          <div class="row">
            <div v-for="(info, idx) in infoTiles" :key="idx" class="flex xs12 sm4">
              <va-card class="mb-4" :color="info.color">
                <va-card-content>
                  <h2 class="va-h2 ma-0" style="color: white">{{ countStatus(info.text) }}</h2>
                  <p style="color: white">{{ t(info.text) }}</p>
                </va-card-content>
              </va-card>
            </div>
          </div>
        </div>
      </va-card-content>
    </va-card>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue'
  import { useI18n } from 'vue-i18n'
  import data from '../../../../data/tables/markup-table/data.json'
  import { VaCard, VaCardContent, VaCardTitle } from 'vuestic-ui'
  import axios, { AxiosResponse } from 'axios'
  import Vue,{onMounted} from 'vue'
  import console from 'console'
  import VueAxios from 'vue-axios'

  const { t } = useI18n()
  const users = ref(data.slice(0, 10))
  var countStatus = (status: string) =>
    Object.values(data.slice(0, 10)).reduce(function (n, i) {
      return n + +(i.status === status)
    }, 0)

  const infoTiles = ref([
    {
      color: 'success',
      text: 'Accepted',
    },
    {
      color: 'info',
      text: 'processing',
    },
    {
      color: 'danger',
      text: 'rejected',
    },
  ])

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
  .markup-tables {
    .table-wrapper {
      overflow: auto;
    }

    .va-table {
      width: 100%;
    }
  }
</style>
