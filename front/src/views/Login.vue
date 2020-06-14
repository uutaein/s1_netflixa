<template>
  <v-app>

      <v-container
        fluid
      >
        <v-row
          justify="center"
        >
          <v-col
            cols="12"
            sm="10"
            md="10"
          >
            <v-card class="mt-12" height="50vh">
              <v-toolbar
                color="primary"
                dark
                flat
              >
                <v-toolbar-title>로그인</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="ID를 입력하세요"
                    name="login"
                    prepend-icon="mdi-account"
                    type="text"
                    v-model="username"
                  ></v-text-field>

                  <v-text-field
                    label="비밀번호를 입력하세요"
                    name="password"
                    prepend-icon="mdi-lock"
                    type="password"
                    v-model="password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <router-link :to="{name : 'Signup' }">
                    <v-btn color="primary">Signup</v-btn>
                </router-link>
                <v-btn
                    @click="login({username, password})"
                    >Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

  </v-app>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'

export default {
  data () {
    return {
      username: null,
      password: null
    }
  },
  methods: {
    setCookie (token) {
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },
    async login (loginData) {
      try {
        const res = await axios.post(SERVER_URL + '/rest-auth/login/', loginData)
        this.setCookie(res.data.key)
        this.$router.push({ name: 'Home' })
      } catch (err) {
        console.error(err)
      }
    }
  }
}
</script>

<style>

</style>
