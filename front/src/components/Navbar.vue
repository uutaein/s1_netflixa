<template>
  <nav>
    <v-app-bar color="#625265" app flat>
      <v-app-bar-nav-icon id="drawerIcon" @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-uppercase white--text">
        <span class="font-weight-light">영화</span>
        <span>츄천츄천</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- login dialog -->
      <v-dialog v-model="login_dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn text v-bind="attrs" v-on="on">
            <v-icon color="white" large>mdi-account-circle</v-icon>
          </v-btn>
        </template>
        <v-card>
          <v-toolbar color="#1F8AD8" dark flat>
            <v-toolbar-title>로그인</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn text @click="login_dialog = false"><v-icon>mdi-close</v-icon></v-btn>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                label="ID를 입력하세요"
                name="login"
                prepend-icon="mdi-account"
                type="text"
                v-model="login_username"
                required
              ></v-text-field>

              <v-text-field
                label="비밀번호를 입력하세요"
                name="password"
                prepend-icon="mdi-lock"
                type="password"
                v-model="login_password"
                required
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text color="#1F8AD8" @click="login_dialog = false;signup_dialog = true">회원가입</v-btn>
            <v-btn text color="#1F8AD8" @click="login({login_username, login_password})">로그인</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <!-- signup dialog -->
      <v-dialog v-model="signup_dialog" persistent max-width="600px">
              <v-card>
              <v-toolbar
                color="#1F8AD8"
                dark
                flat
              >
                <v-toolbar-title>회원가입</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-btn text @click="signup_dialog = false"><v-icon>mdi-close</v-icon></v-btn>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="username"
                    name="username"
                    prepend-icon="mdi-account"
                    type="text"
                    v-model="signup_username"
                  ></v-text-field>

                  <v-text-field
                    label="Password"
                    name="passwd"
                    prepend-icon="mdi-lock"
                    type="password"
                    v-model="signup_passwd"
                  ></v-text-field>
                  <v-text-field
                    label="Password 확인"
                    name="passcd"
                    prepend-icon="mdi-lock"
                    type="password"
                    v-model="signup_passcf"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn text @click="signup({signup_username, signup_passwd, signup_passcf})" color="#1F8AD8">회원 가입</v-btn>
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
export default {
  data () {
    return {
      drawer: false,
      // dialog 위한 정보
      login_dialog: false,
      signup_dialog: false,
      // login 위한 정보
      login_username: null,
      login_password: null,
      // signup 위한 정보
      signup_username: null,
      signup_passwd: null,
      signup_passcf: null,

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
          icon: 'mdi-login',
          text: '로그인',
          route: '/login'
        },
        {
          icon: 'mdi-account-edit',
          text: '계정 만들기',
          route: '/signup'
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
      this.$cookies.set('auth-token', token)
      this.$store.commit('Login')
      this.$store.commit('usernameSave', this.username)
    },
    async login (loginData) {
      try {
        const res = await this.$http.post(this.$store.state.base_url + '/rest-auth/login/', loginData)
        this.setCookie(res.data.key)
        this.login_dialog = false
      } catch (err) {
        console.error(err)
      }
    },
    async signup (signupData) {
      try {
        const res = await this.$http.post(this.$store.state.base_url + '/rest-auth/signup/', signupData)
        this.setCookie(res.data.key)
        this.signup_dialog = false
      } catch (err) {
        console.error(err)
      }
    }
  }
}
</script>

<style>
</style>
