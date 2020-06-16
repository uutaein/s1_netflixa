
<template>
  <v-app>
    <v-container fluid>
      <v-row justify="center">
        <v-col cols="10" sm="10" md="10">
          <v-card class="d-inline-block-auto mx-auto mt-12">
            <h1 class="ml-5">영화 수정</h1>
            <v-container>
              <v-row class="space-between">
                <v-col cols="3">
                  <v-text-field
                    label="title"
                    name="title"
                    prepend-icon="mdi-format-title"
                    type="text"
                    v-model="movieData.title"
                  ></v-text-field>

                  <v-text-field
                    label="original_title"
                    name="original_title"
                    prepend-icon="mdi-format-title"
                    type="text"
                    v-model="movieData.original_title"
                  ></v-text-field>
                  <v-switch v-model="movieData.adult" class="mx-2" label="Adult"></v-switch>

                  <v-menu
                    ref="menu"
                    v-model="date_menu"
                    :close-on-content-click="false"
                    :return-value.sync="movieData.release_date"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="movieData.release_date"
                        label="release date"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="movieData.release_date" no-title scrollable>
                      <v-spacer></v-spacer>
                      <v-btn text color="primary" @click="date_menu = false">Cancel</v-btn>
                      <v-btn
                        text
                        color="primary"
                        @click="$refs.menu.save(movieData.release_date)"
                      >OK</v-btn>
                    </v-date-picker>
                  </v-menu>
                </v-col>
                <v-col cols="3">
                  <v-img width="20vh" height="20vh" :src="movieData.poster_path"></v-img>
                  <v-text-field
                    label="poster_front"
                    name="poster_front"
                    prepend-icon="mdi-file-image"
                    type="text"
                    v-model="movieData.poster_path"
                  ></v-text-field>
                  <v-img width="20vh" height="20vh" :src="movieData.backdrop_path"></v-img>
                  <v-text-field
                    label="poster_backdrop"
                    name="poster_backdrop"
                    prepend-icon="mdi-folder-image"
                    type="text"
                    v-model="movieData.backdrop_path"
                  ></v-text-field>
                </v-col>

                <v-col cols="6">
                  <v-textarea solo name="input-7-4" label="줄거리를 적어주세요" v-model="movieData.overview"></v-textarea>
                  <v-select chips v-bind:items="genre" v-model="movieData.genres" item-text="name" item-value="id" multiple hint="장르를 모두 선택해주세요"></v-select>
                </v-col>
              </v-row>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="updateMovie()" text color="#1F8AD8">수정하기</v-btn>
              </v-card-actions>
            </v-container>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'UpdateMovie',
  data () {
    return {
      movieData: {
        title: '',
        original_title: '',
        release_date: new Date().toISOString().substr(0, 10),
        adult: false,
        overview: '',
        original_language: 'KR',
        poster_path: '',
        backdrop_path: '',
        genres: [],
        popularity: 0,
        vote_count: 0,
        vote_average: 0
      },
      date_menu: false
    }
  },
  computed: {
    ...mapState(['genre'])
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
        this.movieData.title = res.data.title
        this.movieData.original_title = res.data.original_title
        this.movieData.release_date = res.data.release_date
        this.movieData.adult = res.data.adult
        this.movieData.overview = res.data.overview
        this.movieData.original_language = res.data.original_language
        this.movieData.poster_path = res.data.poster_path
        this.movieData.backdrop_path = res.data.backdrop_path
        this.movieData.genres = res.data.genres
        this.movieData.popularity = res.data.popularity
        this.movieData.vote_count = res.data.vote_count
        this.movieData.vote_average = res.data.vote_average
      } catch (err) {
        console.error(err)
      }
    },
    async updateMovie () {
      try {
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        const baseUrl = this.$store.state.base_url
        const apiUrl = baseUrl + '/movies/' + this.id + '/update/'
        await this.$http.post(apiUrl, this.movieData, config)
        this.$router.push({ name: 'MovieDetail', params: { id: this.id } })
      } catch (err) {
        console.error(err)
      }
    }
  }

}
</script>

<style>
</style>
