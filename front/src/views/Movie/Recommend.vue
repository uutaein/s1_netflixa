<template v-if="loading">
  <v-layout v-if="loading">
       <v-container style="height: 400px;">
      <v-row
        class="fill-height"
        align-content="center"
        justify="center"
      >
        <v-col
          class="text-center"
          cols="12"
        >
         <h1 class="ml-5">당신을 위한 영화를 찾아내는 중입니다.</h1>
        </v-col>
        <v-col cols="6">
          <v-progress-linear
            color="#1F8AD8"
            indeterminate
            rounded
            height="6"
          ></v-progress-linear>
        </v-col>
      </v-row>
    </v-container>
  </v-layout>
  <v-layout v-else>
      <v-container>
    <media-nav
      :pageTitle="pageTitle"
      :sortCriteria="sortCriteria"
      @popularity="sortBy('popularity')"
      @vote_average="sortBy('vote_average')"
      @release_date="sortBy('release_date')"
    ></media-nav>
    <media-grid :movies="paginatedData" ></media-grid>
    <div class="text-center" v-if="showPagination">
      <v-pagination color="secondary" v-model="pageNum" :length="this.movieSize"></v-pagination>
    </div>
  </v-container>
  </v-layout>
</template>

<script>
import MediaGrid from '@/components/MediaGrid.vue'
import MediaNav from '@/components/MediaNav.vue'

export default {
  name: 'MovieRecommend',
  components: {
    mediaGrid: MediaGrid,
    mediaNav: MediaNav
  },
  props: {
    pageSize: { type: Number, required: false, default: 8 }
  },
  data () {
    return {
      movies: [],
      pageTitle: '당신을 위한 영화',
      imageURL: 'https://image.tmdb.org/t/p/w1280/',
      sortCriteria: 'Most Popular',
      sortedBy: 'popularity',
      pageNum: 1,
      movieSize: null,
      showPagination: false,
      loading: true
    }
  },
  mounted () {
    this.getRecommends()
  },
  computed: {
    paginatedData () {
      const start = (this.pageNum - 1) * this.pageSize
      const end = start + this.pageSize
      return this.movies.slice(start, end)
    }
  },
  methods: {
    async getRecommends () {
      setTimeout(() => {
        this.loading = false
      }, 3000)
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/movies/' + 'recommend/'
      try {
        const res = await this.$http.get(apiUrl, config)
        for (const i of res.data) {
          i.created_at = String(i.created_at).substring(0, 10)
          i.half_rate = i.vote_average / 2
          i.poster_path = this.imageURL + i.poster_path
          i.backdrop_path = this.imageURL + i.backdrop_path
        }
        this.movies = res.data
        const listLength = this.movies.length
        const listSize = this.pageSize
        const page = Math.floor((listLength - 1) / listSize) + 1
        this.movieSize = page
      } catch (err) {
        console.error(err)
      } finally {
        this.sortBy(this.sortedBy)
        this.showPagination = true
      }
    },
    sortBy (prop) {
      if (prop === 'popularity') {
        this.sortCriteria = 'Most Popular'
      } else if (prop === 'vote_average') {
        this.sortCriteria = 'Highest Rated'
      } else if (prop === 'release_date') {
        this.sortCriteria = 'Release Date'
      }
      this.sortedBy = prop
      this.movies.sort((a, b) => (a[prop] > b[prop] ? -1 : 1))
    }
  }
}
</script>

<style>

</style>
