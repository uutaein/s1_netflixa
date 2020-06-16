<template>
  <v-layout row wrap>
    <v-flex xs12 sm6 md4 lg3 v-for="movie in movies" :key="movie.id">
      <v-card hover class="ma-3"  height="35vh">
        <v-layout column align-center fill-height class="text-center">
          <v-img height="25vh" class="white--text align-end" :src="imageURL + movie.poster_path">
          <v-card-title class="font-weight-light" color="white">{{movie.title || movie.name}}</v-card-title>
          </v-img>
          <v-rating
            v-model="movie.half_rate"
            half-increments
            readonly
            color="#F6D985"
          ></v-rating>
          <v-card-actions>
          <v-btn text color="#FBA285" :to=" '/movies/' + movie.id">DETAIL</v-btn>
          </v-card-actions>
        </v-layout>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: ['movies', 'imageURL'],
  data () {
    return {

    }
  }
}
</script>

<style scoped>
</style>
