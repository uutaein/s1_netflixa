
<template>
  <v-app>
    <v-container fluid>
      <v-row justify="center">
        <v-col cols="10" sm="10" md="10">
          <v-card class="d-inline-block-auto mx-auto mt-12">
            <h1 class="ml-5">리뷰 남기기</h1>
            <v-row>
              <v-col cols="6">
                <v-text-field
                  label="글 제목"
                  name="title"
                  prepend-icon="mdi-format-title"
                  type="text"
                  v-model="reviewData.title"
                ></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-rating v-model="reviewData.score" length="10" background-color="pink lighten-2" small color="pink"></v-rating>
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
              v-model="reviewData.content"
            ></v-textarea>
            <!-- <v-select chips v-bind:items="genre" v-model="movieData.genres" item-text="name" item-value="id" multiple hint="장르를 모두 선택해주세요"></v-select> -->

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click="createReview()" text color="#1F8AD8">영화 등록</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: 'CreateReview',
  data () {
    return {
      reviewData: {
        title: null,
        content: null,
        score: 5
      }
    }
  },
  mounted () {
    this.id = this.$route.params.id
  },
  methods: {
    async createReview () {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const baseUrl = this.$store.state.base_url
      const apiUrl = baseUrl + '/reviews/' + 'create/' + this.id + '/'
      try {
        const res = await this.$http.post(apiUrl, this.reviewData, config)
        this.$router.push({
          name: 'ReviewDetail',
          params: { id: res.data.id }
        })
      } catch (err) {
        console.error(err)
      }
    }
  }
}
</script>

<style>
</style>
