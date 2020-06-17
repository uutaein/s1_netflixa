<template>
  <v-app id="inspire">
    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card class="elevation-12">
              <v-toolbar
                color="primary"
                dark
                flat
              >
                <v-toolbar-title>New Article</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Title"
                    name="title"
                    v-model="reviewData.title"
                    id="title"
                    type="text"
                    prepend-icon="mdi-format-title"
                  ></v-text-field>
                  <v-textarea
                    v-model="reviewData.content"
                    name="content"
                    id="content"
                    label="content"
                    value="Content"
                    hint="Hint text"
                    type="text"
                    prepend-icon="mdi-border-color"
                  ></v-textarea>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="createReview" color="primary">Submit!</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
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
    this.getDetail()
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
        this.$router.push({ name: 'ReviewDetail', params: { id: res.data.id } })
      } catch (err) {
        console.error(err)
      }
    }
    // checkLoggedIn() {
    //   if (!this.$cookies.isKey('auth-token')) {
    //     this.$router.push({ name: 'Login' })
    //   }
    // }
  }

  // created() {
  //   this.checkLoggedIn()
  // },
}
</script>

<style>
</style>
