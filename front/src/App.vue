<template>
  <v-app>
    <app-navbar></app-navbar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import store from '@/store'

export default {
  name: 'App',

  components: {
    appNavbar: Navbar
  },

  data: () => ({
    //
  }),
  mounted () {
    this.$store.commit('urlSave', 'http://localhost:8000') // url 정해주기
  },
  store
}
</script>
