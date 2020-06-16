<template>
  <v-container>
    <v-flex class="pa-7">
      <div>
        <v-row>
          <h1 class="ml-3">{{movie.title}}</h1>
          <v-spacer></v-spacer>
          <v-btn
            @click="like_movie()"
            icon
          >
            <v-snackbar v-model="like_popup" :timeout="like_timeout">
              {{ like_res }}
              <template v-slot:action="{ attr }">
                <v-btn color="indigo" text v-bind="attr" @click="like_popup = false">Close</v-btn>
              </template>
            </v-snackbar>
            <v-icon medium>mdi-heart</v-icon>
          </v-btn>
        </v-row>
        <v-row class="px-3">
          <span class="borderP">개봉일: {{movie.release_date}}</span>
          <span class="borderP">평점: {{movie.vote_average}}</span>
        </v-row>
      </div>
      <v-divider class="minDiv mt-2 mb-5"></v-divider>
      <div>
        <div>
          <xmp>{{movie.overview}}</xmp>
          <br />
        </div>
        <v-divider class="minDiv mb-5"></v-divider>
        <div class="d-flex justify-end">
          <v-btn to="/movies" color="#74B4A0" dark>목록으로</v-btn>
        </div>
      </div>
    </v-flex>
  </v-container>
</template>

<script>
export default {
  name: 'MovieDetail',
  data () {
    return {
      movie: {},
      user: this.$store.state.user_name,
      is_liked: false,
      like_popup: false,
      like_timeout: 2000,
      like_res: '시발'
    }
  },
  mounted () {
    this.id = this.$route.params.id
    this.getDetail()
  },
  methods: {
    async getDetail () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/movies/' + this.id + '/'
      try {
        const res = await this.$http.get(apiUrl)
        this.movie = res.data
      } catch (err) {
        console.error(err)
      }
    },
    async like_movie () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/reviews/' + this.id + '/like'
      try {
        const res = await this.$http.get(apiUrl)
        console.log(res)
      } catch (err) {
        console.error(err)
      } finally {
        this.like_popup = true
      }
    }
  }
}
</script>

<style lang="stylus">
xmp {
  white-space: pre-wrap;
  word-wrap: break-word;
}

.minDiv {
  border-top-width: 2px;
}
</style>
