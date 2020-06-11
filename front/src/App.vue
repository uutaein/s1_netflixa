<template>
  <v-app>
    <app-navbar></app-navbar>
    <v-content>
      <router-view></router-view>
    </v-content>
    <v-footer>
      <app-footer></app-footer>
    </v-footer>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'App',

  components: {
    appNavbar: Navbar
  },

  data: () => ({
    //
  })
}
</script>
