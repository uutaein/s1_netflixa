
<template>
  <v-app>
    <v-container fluid>
      <v-row justify="center">
        <v-col cols="10" sm="10" md="10">
          <v-card class="mx-auto mt-12">
            <h1 class="ml-5">리뷰 남기기</h1>
            <v-row>
              <v-col cols="4">
                <v-img class="ml-12" :src="reviewData.moviesrc" height="35vh" width="30vh"></v-img>
              </v-col>
              <v-col cols="8">
                <v-text-field
                  label="영화 제목"
                  name="title"
                  prepend-icon="mdi-movie"
                  type="text"
                  class="mt-12"
                  readonly
                  disabled
                  v-model="reviewData.movietitle"
                ></v-text-field>
                <v-text-field
                  label="글 제목"
                  name="title"
                  prepend-icon="mdi-format-title"
                  type="text"
                  class="mt-4"
                  v-model="reviewData.title"
                  required
                ></v-text-field>
                <v-rating v-model="reviewData.score" length="10" background-color="#F6D985" small color="#F6D985"></v-rating>
                <div>
                  <span class="caption">평점</span>
                  <span class="font-weight-bold">{{ reviewData.score }}</span>
                </div>
              </v-col>
            </v-row>

            <v-textarea
              solo
              name="input-7-4"
              label="내용을 적어주세요"
              prepend-icon="mdi-clipboard-text"
              class="ml-12 mr-12"
              required
              v-model="reviewData.content"
            ></v-textarea>
            <!-- <v-select chips v-bind:items="genre" v-model="movieData.genres" item-text="name" item-value="id" multiple hint="장르를 모두 선택해주세요"></v-select> -->
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click="updateReview()" text color="#1F8AD8">리뷰 수정</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: 'UpdateReview',
  data () {
    return {
      reviewData: {
        title: null,
        content: null,
        score: 5,
        movietitle: '',
        moviesrc: ''
      }

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
      this.$http.get(apiUrl)
        .then(res => {
          console.log(res)
          this.reviewData.title = res.data.title
          this.reviewData.content = res.data.content
          this.reviewData.score = res.data.score
          this.reviewData.movietitle = res.data.movietitle
          this.reviewData.moviesrc = res.data.moviesrc
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateReview () {
      const baseUrl = this.$store.state.base_url
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const apiUrl = baseUrl + '/reviews/' + this.id + '/update/'
      this.$http.post(apiUrl, this.reviewData, config)
        .then(res => {
          this.$router.go(-1)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
