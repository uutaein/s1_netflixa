
<template>
  <div>
    <section id='top'>
      <v-row class="px-3" align="center">
      <h1 class="mt-7 ml-4 display-1 font-weight-light">영화 리뷰</h1>
      <h5 class="font-weight-light"></h5>
      </v-row>
      <v-divider id='topdivider'></v-divider>
      <v-row class="d-none d-md-flex font-weight-black px-3">
        <v-col cols='3'>영화</v-col>
        <v-col cols='6'>제목</v-col>
        <v-col cols='1'>작성일시</v-col>
        <v-col cols='1'>작성자</v-col>
        <v-col cols="1">평점</v-col>
      </v-row>
      <v-row class="d-flex d-md-none font-weight-black px-3">
        <v-col cols='8'>제목</v-col>
        <v-col cols='4'>작성자</v-col>
      </v-row>
    </section>
    <v-divider class='middivider'></v-divider>
    <section id='content'>
      <div v-for="post in paginatedData" :key="post.id">
        <v-btn
        :to="'/reviews/' + post.id"
        height="auto"
        text
        block
        >
          <v-row class="d-none d-md-flex px-3">
            <v-col cols='3'>{{post.movietitle}} </v-col>
            <v-col cols='6'>{{post.title}}</v-col>
            <v-col cols='1'>{{post.created_at}} </v-col>
            <v-col cols='1'>{{post.user.username}}</v-col>
            <v-col cols="1">{{post.score}}</v-col>
          </v-row>
          <v-row class="d-flex d-md-none px-3">
            <v-col class="text-truncate" cols='8'>{{post.title}}</v-col>
            <v-col cols='4'>{{post.username}}</v-col>
          </v-row>
        </v-btn>
        <v-divider :class="[post % 3 === 0 ? 'middivider' : '']"></v-divider>
      </div>
    </section>
    <div class="text-center my-5">
        <v-pagination :length="this.size" v-model="pageNum" color="#74B4A0">
        </v-pagination>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewList',
  props: {
    pageSize: { type: Number, required: false, default: 12 }
  },
  data () {
    return {
      posts: [],
      pageNum: 1,
      size: null,
      user: this.$store.state.user_id
    }
  },
  computed: {
    paginatedData () {
      const start = (this.pageNum - 1) * this.pageSize
      const end = start + this.pageSize
      return this.posts.slice(start, end)
    }
  },
  mounted () {
    this.getReviews()
  },
  methods: {
    getReviews () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/reviews/'
      this.$http.get(apiUrl)
        .then(res => {
          console.log(res)
          this.posts = res.data
          for (const i of res.data) {
            i.created_at = String(i.created_at).substring(0, 10)
          }
          const listLength = this.posts.length
          const listSize = this.pageSize
          const page = Math.floor((listLength - 1) / listSize) + 1
          this.size = page
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang="stylus">
#topdivider
  border-top-width 2px
  border-top-color #000
.middivider
  border-top-width 2px
</style>
