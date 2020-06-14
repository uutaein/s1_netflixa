<template>
  <v-content>
    <v-container v-for="article in articles" :key="`article_${article.id}`">
        <v-card
            color="#385F73"
            dark
            class="mx-auto my-6"
            max-width="1000"
        >
        <v-card-title class="display-2">{{article.title}}</v-card-title>
        <v-card-subtitle class="headline">
            {{article.content}}
        </v-card-subtitle>
        <v-text class="p-1"> 작성일: {{article.created_at}}</v-text>
        </v-card>
    </v-container>
  </v-content>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'ReviewList',
  data () {
    return {
      articles: []
    }
  },
  methods: {
    async fetchArticles () {
      try {
        const res = await axios.get(SERVER_URL + '/reviews')
        this.articles = res.data
      } catch (err) {
        console.error(err)
      }
    }
  },
  created () {
    this.fetchArticles()
  }
}
</script>

<style>

</style>
