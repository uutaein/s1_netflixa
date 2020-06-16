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
    this.getGenre()
    this.$store.commit('LoginState', { iskey: this.$cookies.isKey('auth-token'), name: this.$cookies.get('username'), id: this.$cookies.get('userid') })
  },
  methods: {
    async getGenre () {
      try {
        const res = await this.$http.get('http://api.themoviedb.org/3/genre/movie/list?api_key=714dd2d169d0ac88cf9e118b870d7c1c&language=ko-KR')
        this.$store.commit('GetGenre', res.data.genres)
      } catch (err) {
        console.log(err)
      }
    }
  },
  store
}
</script>
