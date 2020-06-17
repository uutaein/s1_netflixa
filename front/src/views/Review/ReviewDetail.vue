<template>
  <v-container>
    <v-flex class="pa-7">
      <div>
        <v-row>
          <h5>{{ post.movietitle }}</h5>
          </v-row>
          <v-row>
          <h1 class="ml-3">{{post.title}}</h1>
          <v-spacer></v-spacer>
          <v-btn
            v-if="this.$store.state.user_name != post.user.username"
            @click="like_review()"
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
        </v-row>
        <v-row class="px-3">
          <span class="borderP">작성일: {{post.updated_at}}</span>
          <span class="borderP">작성자: {{post.user.username}}</span>
        </v-row>
      </div>
      <v-divider class="minDiv mt-2 mb-5"></v-divider>
      <div>
        <div style="height: 25vh">
          <xmp>{{post.content}}</xmp>
          <br />
        </div>
        <v-divider class="minDiv mb-5"></v-divider>
        <div class="d-flex justify-end">
          <v-btn :to=" '/movies/' + post.movie">영화 정보 보기 </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            v-if="this.$store.state.user_name === post.user.username"
            @click="$router.push({ name: 'UpdateReview', params: { id: post.id }})"
            class="mr-3"
            color="light-blue"
            dark
          >수정</v-btn>
          <v-btn
            v-if="this.$store.state.user_name === post.user.username"
            @click="deleteDetail()"
            class="mr-3"
            color="pink"
            dark
          >삭제</v-btn>
          <v-btn to="/reviews" color="#74B4A0" dark>목록으로</v-btn>
        </div>
      </div>
      <Comment class="mt-10"></Comment>
    </v-flex>
  </v-container>
</template>

<script>
import Comment from '@/components/Comment'
export default {
  name: 'ReviewsDetail',
  components: {
    Comment
  },
  data () {
    return {
      post: {},
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
    getDetail () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/reviews/' + this.id + '/'
      this.$http
        .get(apiUrl)
        .then(res => {
          console.log(res)
          const createdAt = res.data.updated_at
          res.data.updated_at =
            createdAt.substring(0, 4) +
            '년 ' +
            createdAt.substring(5, 7) +
            '월 ' +
            createdAt.substring(8, 10) +
            '일'
          this.post = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    async deleteDetail () {
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/reviews/' + this.id + '/delete/'
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      try {
        await this.$http.get(apiUrl, config)
        this.$router.push({ name: 'ReviewList' })
      } catch (err) {
        console.log(err)
      }
    },
    async like_review () {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/reviews/' + this.id + '/like/'
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
