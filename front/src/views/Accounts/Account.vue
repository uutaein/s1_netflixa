<template>
  <div>
    <v-container text-center>
      <v-row>
        <v-col cols="4">
          <v-card
            class="pt-12"
            height='84vh'>
          <v-avatar
            class="profile"
            color="grey"
            size="200"
            tile
          >
            <v-img centered src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
          </v-avatar>
              <v-list-item-content>
              <v-list-item-title class="title">{{ userData.username }}</v-list-item-title>
              <v-list-item-subtitle>
                <v-btn
                @click="follow()"
                icon
              >
                <v-snackbar v-model="follow_popup" :timeout="follow_timeout">
                  {{ follow_res }}
                  <template v-slot:action="{ attr }">
                    <v-btn color="indigo" text v-bind="attr" @click="follow_popup = false">Close</v-btn>
                  </template>
                </v-snackbar>
                <v-icon medium :color="heart_color">mdi-heart</v-icon>
              </v-btn>
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-card>
        </v-col>
        <v-col cols="8">
          <v-card height='84vh'>
              <v-flex>
                <h2 class="pt-3">나의 영화</h2>
                <v-carousel hide-delimiters style="box-shadow: 0px 0px" height="auto">
                  <v-carousel-item v-for="i in 2" :key="i" max-height="30vh" >
                    <v-layout row>
                      <v-flex sm4 v-for="j in userData.like_movies" :key="j" pl-2 pr-2>
                        <v-card>
                          <v-img
                            src="https://cdn.vuetifyjs.com/images/cards/desert.jpg"
                            aspect-ratio="2"
                          ></v-img>
                          <v-card-title primary-title>
                            <div>
                              <h3 class="headline mb-0">{{j}}</h3>
                              <div> Card text </div>
                            </div>
                          </v-card-title>
                        </v-card>
                      </v-flex>
                    </v-layout>
                  </v-carousel-item>
                </v-carousel>
              </v-flex>
            <h2 class="pt-3">작성 리뷰</h2>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'account',
  data () {
    return {
      userData: {},
      user: this.$store.state.user_name,
      is_followed: false,
      follow_popup: false,
      follow_timeout: 2000,
      follow_res: '',
      heart_color: 'gray'
    }
  },
  methods: {
    async getDetail () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/accounts/' + this.userID + '/'
      try {
        const res = await this.$http.get(apiUrl)
        this.userData = res.data
      } catch (err) {
        console.error(err)
      }
    },
    async follow () {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/accounts/' + this.userData.id + '/follow/'
      try {
        await this.$http.get(apiUrl, config)
        this.is_followed = !this.is_followed
        if (this.is_followed === true) {
          this.follow_res = '팔로우 하셨습니다'
          this.heart_color = 'pink'
        } else {
          this.follow_res = '팔로우 취소 하셨습니다'
          this.heart_color = 'gray'
        }
      } catch (err) {
        console.error(err)
        this.follow_res = '에러가 발생했습니다. 나중에 다시 시도하세요'
      } finally {
        this.follow_popup = true
      }
    }
  },
  mounted () {
    this.userID = this.$store.state.user_id
    this.getDetail()
  }
}
</script>

<style>
   #landing-page {
     /*background-image: url('../assets/hands_joined_team.jpeg');*/
    background-color: #8f2c2c;
    height: 100vh;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;
  }
</style>
