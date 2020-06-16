import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
// movie
import Home from '@/views/Movie/Home.vue'
import Recommend from '@/views/Movie/Recommend.vue'
import MovieList from '@/views/Movie/MovieList.vue'
import CreateMovie from '@/views/Movie/CreateMovie.vue'
import UpdateMovie from '@/views/Movie/UpdateMovie.vue'
import MovieDetail from '@/views/Movie/MovieDetail.vue'

// account
import Account from '@/views/Accounts/Account.vue'
import Login from '@/views/Accounts/Login.vue'
import Signup from '@/views/Accounts/Signup.vue'

// reviews
import ReviewList from '@/views/Review/ReviewList.vue'
import ReviewDetail from '@/views/Review/ReviewDetail.vue'
import CreateReview from '@/views/Review/CreateReview.vue'
import UpdateReview from '@/views/Review/UpdateReview.vue'

Vue.prototype.$http = axios
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/account',
    name: 'Account',
    component: Account
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieList
  },
  {
    path: '/movies/create',
    name: 'CreateMovie',
    component: CreateMovie
  },
  {
    path: '/movies/:id/update',
    name: 'UpdateMovie',
    component: UpdateMovie
  },
  {
    path: '/movies/:id',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/reviews',
    name: 'ReviewList',
    component: ReviewList
  },
  {
    path: '/reviews/create',
    name: 'CreateReview',
    component: CreateReview
  },
  {
    path: '/reviews/:id/update',
    name: 'UpdateReview',
    component: UpdateReview
  },
  {
    path: '/reviews/:id',
    name: 'ReviewDetail',
    component: ReviewDetail
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
