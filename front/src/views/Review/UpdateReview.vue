<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" md="8" offset-md="2">
          <div>
            <h1 class="gamjaFont">리뷰 수정하기</h1>
          </div>
          <v-divider></v-divider>
          <v-form ref="form" v-model="valid">
            <v-text-field
            v-model="title"
            :counter="10"
            label="글 제목"
            ></v-text-field>
            <v-textarea
            v-model="content"
            label="글 내용"
            outlined
            ></v-textarea>
          </v-form>
          <v-row>
            <div class="ml-auto pa-2">
              <v-btn @click="updateReview()" color="#74b4a0" dark>
                수정하기
              </v-btn>
            </div>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'UpdateReview',
  data () {
    return {
      title: '',
      content: '',
      valid: true
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
          this.title = res.data.title
          this.content = res.data.content
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
      this.$http.post(apiUrl, { title: this.title, content: this.content }, config)
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
