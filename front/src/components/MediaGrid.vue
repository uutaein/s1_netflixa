<template>
  <v-layout row wrap>
    <v-flex xs12 sm6 md4 lg3 v-for="movie in movies" :key="movie.id">
      <v-card hover class="ma-3"  height="50vh">
        <v-layout column align-center fill-height class="text-center">
          <v-img height="30vh" class="white--text align-end" :src="movie.poster_path">
          <v-card-title class="font-weight-light" color="white">{{movie.title || movie.name}}</v-card-title>
          </v-img>
          <v-rating
            v-model="movie.half_rate"
            half-increments
            readonly
            background-color="#F6D985"
            color="#F6D985"
          ></v-rating>
          <v-card-actions>
          <v-btn text color="#FBA285" :to=" '/movies/' + movie.id">DETAIL</v-btn>
          <v-btn v-if="update_permition" text color="#FBA285" :to=" '/movies/' + movie.id + '/update/' ">UPDATE</v-btn>
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
      update_permition: this.$store.state.isSuperUser
    }
  }
}
</script>

<style scoped>
</style>
