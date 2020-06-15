
<template>
  <v-app>
    <v-container fluid>
      <v-row justify="center">
        <v-col cols="10" sm="10" md="10">
          <v-card class="d-inline-block-auto mx-auto mt-12">
            <v-container>
              <v-row justify="space-between">
                <v-col cols="auto">
                  <v-card-text>
                    <v-form>
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
                        <v-date-picker v-model="movieDate.release_date" no-title scrollable>
                          <v-spacer></v-spacer>
                          <v-btn text color="primary" @click="date_menu = false">Cancel</v-btn>
                          <v-btn text color="primary" @click="$refs.menu.save(date)">OK</v-btn>
                        </v-date-picker>
                      </v-menu>

                    </v-form>
                  </v-card-text>
                </v-col>
              </v-row>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="signup({signupData})" color="primary">Signup</v-btn>
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
        password1: null,
        password2: null
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
