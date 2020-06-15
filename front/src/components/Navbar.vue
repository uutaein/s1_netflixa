<template>
  <nav>
    <v-app-bar color="#625265" app flat>
      <v-app-bar-nav-icon id="drawerIcon" @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-uppercase white--text">
        <span class="font-weight-light">영화</span>
        <span>츄천츄천</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer app v-model="drawer" color="#B59AC5">
      <v-layout column align-center>
        <v-flex class="my-5">
        </v-flex>
      </v-layout>

      <v-list flat>
        <v-list-item v-for="link in links" :key="link.route" link :to="link.route">
          <v-list-item-icon>
            <v-icon class="white--text">{{link.icon}}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="white--text">{{link.text}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
export default {
  data: function () {
    return {
      drawer: false,
      links: [
        { icon: 'mdi-home', text: 'Home', route: '/' },
        {
          icon: 'mdi-filmstrip',
          text: '영화 추천받기',
          route: '/recommend'
        },
        {
          icon: 'mdi-trophy',
          text: '최고의 영화들'
          // route: '/top-rated-movies'
        },

        {
          icon: 'mdi-video-vintage',
          text: '영화 목록',
          route: '/movies'
        },
        {
          icon: 'mdi-film',
          text: '영화 추가',
          route: '/movies/create'
        },
        {
          icon: 'mdi-account-circle',
          text: '내 계정',
          route: '/account'
        },
        {
          icon: 'mdi-login',
          text: '로그인',
          route: '/login'
        },
        {
          icon: 'mdi-account-edit',
          text: '계정 만들기',
          route: '/signup'
        },
        {
          icon: 'mdi-grease-pencil',
          text: '리뷰 남기기',
          route: '/reviews/create'
        },
        {
          icon: 'mdi-comment-text-multiple-outline',
          text: '리뷰 보기',
          route: '/reviews'
        }

      ]
    }
  }
}
</script>

<style>

</style>
