<template>
  <nav>
    <v-app-bar color="#625265" app flat>
      <v-app-bar-nav-icon id="drawerIcon" @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-uppercase white--text">
        <span class="font-weight-light">영화</span>
        <span>츄천츄천</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <span style="color: white" v-if="isLoggedin">{{ userCheck }} 님 환영합니다</span>
      <v-btn v-if="isLoggedin" text color="white" @click="logout()">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
      <!-- login dialog -->
      <v-dialog v-if="!isLoggedin" v-model="login_dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn text v-bind="attrs" v-on="on">
            <v-icon color="white" large>mdi-account-circle</v-icon>
          </v-btn>
        </template>
        <v-card>
          <v-toolbar color="#1F8AD8" dark flat>
            <v-toolbar-title>로그인</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn text @click="login_dialog = false">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                label="ID를 입력하세요"
                name="login"
                prepend-icon="mdi-account"
                type="text"
                v-model="loginData.username"
                required
              ></v-text-field>

              <v-text-field
                label="비밀번호를 입력하세요"
                name="password"
                prepend-icon="mdi-lock"
                type="password"
                v-model="loginData.password"
                required
              ></v-text-field>
            </v-form>
            <v-alert v-if="loginFail" dense outlined type="error">아이디가 존재하지 않거나 비밀번호가 일치하지 않습니다</v-alert>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text color="#1F8AD8" @click="login_dialog = false;signup_dialog = true">회원가입</v-btn>
            <v-btn text color="#1F8AD8" @click="login()">로그인</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <!-- signup dialog -->
      <v-dialog v-model="signup_dialog" persistent max-width="600px">
        <v-card>
          <v-toolbar color="#1F8AD8" dark flat>
            <v-toolbar-title>회원가입</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn text @click="signup_dialog = false">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                label="username"
                name="username"
                prepend-icon="mdi-account"
                type="text"
                v-model="signupData.username"
              ></v-text-field>

              <v-text-field
                label="Password"
                name="passwd"
                prepend-icon="mdi-lock"
                type="password"
                v-model="signupData.password1"
              ></v-text-field>
              <v-text-field
                label="Password 확인"
                name="passcd"
                prepend-icon="mdi-lock"
                type="password"
                v-model="signupData.password2"
              ></v-text-field>
            </v-form>
            <v-alert v-if="signupFail" dense outlined type="error">동일한 아이디가 존재하거나 비밀번호가 일치하지 않습니다</v-alert>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text @click="signup()" color="#1F8AD8">회원 가입</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-app-bar>

    <v-navigation-drawer app v-model="drawer" color="#B59AC5">
      <v-layout column align-center>
        <v-flex class="my-5"></v-flex>
      </v-layout>

      <v-list flat>
        <v-list-item v-for="link in links" :key="link.route" link :to="link.route">
          <v-list-item-icon>
            <v-icon class="white--text">{{link.icon}}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="white--text">{{link.text}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      drawer: false,
      // dialog 위한 정보
      login_dialog: false,
      signup_dialog: false,
      // login 위한 정보
      loginData: {
        username: null,
        password: null
      },
      loginFail: false,
      // signup 위한 정보
      signupData: {
        username: null,
        password1: null,
        password2: null
      },
      signupFail: false,
      // routing
      links: [
        { icon: 'mdi-home', text: 'Home', route: '/' },
        {
          icon: 'mdi-filmstrip',
          text: '영화 추천받기',
          route: '/recommend'
        },
        {
          icon: 'mdi-trophy',
          text: '최고의 영화들'
          // route: '/top-rated-movies'
        },

        {
          icon: 'mdi-video-vintage',
          text: '영화 목록',
          route: '/movies'
        },
        {
          icon: 'mdi-film',
          text: '영화 추가',
          route: '/movies/create'
        },
        {
          icon: 'mdi-account-circle',
          text: '내 계정',
          route: '/account'
        },
        {
          icon: 'mdi-grease-pencil',
          text: '리뷰 남기기',
          route: '/reviews/create'
        },
        {
          icon: 'mdi-comment-text-multiple-outline',
          text: '리뷰 보기',
          route: '/reviews'
        }
      ]
    }
  },
  methods: {
    setCookie (token) {
      this.$cookies.set('auth-token', token.token)
      this.$cookies.set('username', token.name)
      this.$cookies.set('userid', token.id)
      this.$store.commit('Login')
    },
    getname () {
      axios.get(this.$store.state.base_url + '/accounts/' + this.loginData.username + '/')
        .then(res => { this.setCookie({ id: res.data.id }) })
        .catch(err => console.error(err))
    },
    async login () {
      try {
        const res = await this.$http.post(
          this.$store.state.base_url + '/rest-auth/login/',
          this.loginData
        )
        console.log(res)
        this.getname()
        this.setCookie({ token: res.data.key, name: this.loginData.username })
        this.$store.commit('usernameSave', this.loginData.username)
        this.$store.commit('useridSave', res.data.id)
        this.login_dialog = false
        this.loginFail = false
      } catch (err) {
        console.error(err)
        this.loginFail = true
      }
    },
    async logout () {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      try {
        await this.$http.post(
          this.$store.state.base_url + '/rest-auth/logout/', config, true
        )
        this.$store.commit('Logout')
        this.$cookies.remove('auth-token')
        this.$cookies.remove('username')
        this.$cookies.remove('userid')
      } catch (err) {
        console.error(err)
      }
    },
    async signup () {
      try {
        const res = await this.$http.post(
          this.$store.state.base_url + '/rest-auth/signup/',
          this.signupData
        )
        this.setCookie({ token: res.data.key, name: this.signupData.username })
        this.$store.commit('usernameSave', this.signupData.username)
        // this.$store.commit('useridSave', res.data.user.pk)
        this.signup_dialog = false
        this.signupFail = false
      } catch (err) {
        console.error(err)
        this.signupFail = true
      }
    }
  },
  computed: {
    isLoggedin () {
      return this.$store.state.isLoggedin
    },
    userCheck () {
      return this.$store.state.user_name
    }
  }
}
</script>

<style>
</style>
