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
            </v-list-item-content>
          </v-card>
        </v-col>
        <v-col cols="8">
          <v-card height='84vh'>
              <v-flex>
                <h2 class="pt-3">나의 영화</h2>
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
      user: this.$store.state.user_name
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
