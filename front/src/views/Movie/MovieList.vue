<template>
  <v-container>
    <media-nav
      :pageTitle="pageTitle"
      :sortCriteria="sortCriteria"
      @popularity="sortBy('popularity')"
      @vote_average="sortBy('vote_average')"
      @release_date="sortBy('release_date')"
    ></media-nav>
    <media-grid :movies="paginatedData" :imageURL="imageURL"></media-grid>
    <div class="text-center" v-if="showPagination">
      <v-pagination color="secondary" v-model="pageNum" :length="this.movieSize"></v-pagination>
    </div>
  </v-container>
</template>

<script>
import MediaGrid from '@/components/MediaGrid.vue'
import MediaNav from '@/components/MediaNav.vue'

export default {
  components: {
    mediaGrid: MediaGrid,
    mediaNav: MediaNav
  },
  props: {
    pageSize: { type: Number, required: false, default: 40 }
  },
  data: function () {
    return {
      movies: [],
      pageTitle: '영화 목록',
      imageURL: 'https://image.tmdb.org/t/p/w1280/',
      sortCriteria: 'Most Popular',
      sortedBy: 'popularity',
      pageNum: 1,
      movieSize: null,
      showPagination: false
    }
  },
  computed: {
    paginatedData () {
      const start = (this.pageNum - 1) * this.pageSize
      const end = start + this.pageSize
      return this.movies.slice(start, end)
    }
  },
  methods: {
    async getMovies () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/movies/'
      try {
        const res = await this.$http.get(apiUrl)
        for (const i of res.data) {
          i.created_at = String(i.created_at).substring(0, 10)
          i.half_rate = i.vote_average / 2
        }
        this.movies = res.data
        console.log(this.movies)
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
  },
  watch: {
    page: function (page) {
      this.getMovies()
    }
  },
  mounted () {
    this.getMovies()
  }
}
</script>

<style scoped>
</style>
