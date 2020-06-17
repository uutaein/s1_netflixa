<template>
  <v-container>
    <v-flex class="pa-7">
      <div>
        <v-card>
          <v-layout column align-center fill-width class="text-left">
          <v-img :src="imageURL + movie.backdrop_path" class="white--text align-end" height="30vh">
            <v-card-title class="font-weight-light" large color="white">{{movie.title || movie.name}}</v-card-title>
          </v-img>
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
            <v-icon medium :color="heart_color">mdi-heart</v-icon>
          </v-btn>
          </v-layout>
        </v-card>
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
          <v-btn :to="'/reviews/create/' + id" color="#74B4A0" dark>리뷰쓰기</v-btn>
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
      imageURL: 'https://image.tmdb.org/t/p/w1280/',
      user: this.$store.state.user_name,
      is_liked: false,
      like_popup: false,
      like_timeout: 2000,
      like_res: '',
      heart_color: 'gray'
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
        if (res.data.like_users.includes(this.$store.state.user_id)) {
          this.is_liked = true
          this.heart_color = 'pink'
        }
        this.movie = res.data
        this.$store.commit('selectedMovie', { title: this.movie.title, src: this.imageURL + this.movie.poster_path })
      } catch (err) {
        console.error(err)
      }
    },
    async like_movie () {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/movies/' + this.id + '/like/'
      try {
        await this.$http.get(apiUrl, config)
        this.is_liked = !this.is_liked
        if (this.is_liked === true) {
          this.like_res = '좋아요 하셨습니다'
          this.heart_color = 'pink'
        } else {
          this.like_res = '좋아요 취소 하셨습니다'
          this.heart_color = 'gray'
        }
      } catch (err) {
        console.error(err)
        this.like_res = '에러가 발생했습니다. 나중에 다시 시도하세요'
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
