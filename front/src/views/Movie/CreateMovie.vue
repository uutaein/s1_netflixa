
<template>
  <v-app>
    <v-container fluid>
      <v-row justify="center">
        <v-col cols="10" sm="10" md="10">
          <v-card class="d-inline-block-auto mx-auto mt-12">
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
                  <v-switch v-model="adult" class="mx-2" label="Adult"></v-switch>

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
                </v-col>
              </v-row>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="signup({signupData})" color="primary">영화 등록</v-btn>
              </v-card-actions>
            </v-container>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: 'CreateMovie',
  data () {
    return {
      movieData: {
        title: '',
        original_title: '',
        release_date: new Date().toISOString().substr(0, 10),
        adult: 'false',
        overview: '',
        original_language: '',
        poster_path: '',
        backdrop_path: '',
        genres: []
      },
      date_menu: false
    }
  },
  methods: {
    async createMovie () {
      try {
        const res = await this.$http.post(
          this.$store.state.base_url + '/rest-auth/signup/',
          this.signupData
        )
        this.setCookie(res.data.key)
        this.$router.push({ name: 'Home' })
      } catch (err) {
        console.error(err)
      }
    }
  }
}
</script>

<style>
</style>
