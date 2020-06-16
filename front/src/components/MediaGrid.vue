<template>
  <v-layout row wrap>
    <v-flex xs12 sm6 md4 lg3 v-for="movie in movies" :key="movie.id">
      <v-card hover class="ma-3"  height="35vh">
        <v-layout column align-center fill-height class="text-center">
          <v-img height="25vh" class="white--text align-end" :src="imageURL + movie.poster_path">
          <v-card-title class="font-weight-light" color="white">{{movie.title || movie.name}}</v-card-title>
          </v-img>
          <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <v-btn text color="#FBA285" :to=" '/movies/' + movie.id">DETAIL</v-btn>

          </v-card-actions>
          <!-- <v-progress-circular
            color="#B6DAE4"
            rotate="-90"
            width="8"
            :value="movie.vote_average * 10"
            class="font-weight-heavy my-5"
          ></v-progress-circular> -->

          <!-- <v-card-text>
            <v-expansion-panels focusable>
              <v-expansion-panel id="synopsis">
                <v-expansion-panel-header>Synopsis</v-expansion-panel-header>
                <v-expansion-panel-content>{{movie.overview}}</v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
          </v-card-text> -->
          <v-card-text>{{movie.overview}}</v-card-text>
        </v-layout>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: ['movies', 'imageURL'],
  data () {
    return {}
  }
}
</script>

<style scoped>
</style>
