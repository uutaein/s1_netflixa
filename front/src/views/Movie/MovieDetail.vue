<template>
  <v-container>
    <v-flex class="pa-7">
      <v-card>
        <v-img :src="imageURL + movie.backdrop_path" class="white--text align-end" height="30vh"></v-img>
        <v-row>
          <h1 class="ml-8">{{movie.title}}</h1>
          <v-btn text @click="like_movie()" icon large>
            <v-snackbar v-model="like_popup" :timeout="like_timeout">
              {{ like_res }}
              <template v-slot:action="{ attr }">
                <v-btn color="indigo" text v-bind="attr" @click="like_popup = false">Close</v-btn>
              </template>
            </v-snackbar>
            <v-icon medium :color="heart_color">mdi-heart</v-icon>
          </v-btn>
        </v-row>
        <v-spacer></v-spacer>
        <v-row class="px-3 ml-3">
          <p class="borderP">개봉일: {{movie.release_date}}</p>
          <v-rating
            v-model="movie.half_rate"
            half-increments
            readonly
            medium
            background-color="#F6D985"
            color="#F6D985"
          ></v-rating>
          <v-chip-group>
            <v-chip outlined pill v-for="movie in movie_genre" :key="movie">{{ movie }}</v-chip>
          </v-chip-group>
        </v-row>
        <v-divider class="minDiv mt-2 mb-5"></v-divider>
        <div class="ml-3" style="height : 20vh">
          <h3>줄거리</h3>
          {{movie.overview}}
        </div>
        <v-divider class="minDiv mb-5"></v-divider>
        <div class="d-flex justify-end">
          <v-btn x-large text :to="'/reviews/create/' + id" color="#74B4A0" dark>리뷰쓰기</v-btn>
          <v-btn x-large text to="/movies/" color="#74B4A0">목록으로</v-btn>
        </div>
      </v-card>
    </v-flex>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

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
      heart_color: 'gray',
      movie_genre: []
    }
  },
  mounted () {
    this.id = this.$route.params.id
    this.getDetail()
  },
  computed: {
    ...mapState(['genre'])
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
        // 장르 배열에 넣기
        for (const i of res.data.genres) {
          const idx = this.genre.findIndex(x => x.id === i)
          console.log(this.genre[idx].name)
          this.movie_genre.push(this.genre[idx].name)
        }
        /// end of 장르 배열에 넣기
        res.data.half_rate = res.data.vote_average / 2
        this.movie = res.data
        this.$store.commit('selectedMovie', {
          title: this.movie.title,
          src: this.imageURL + this.movie.poster_path
        })
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
