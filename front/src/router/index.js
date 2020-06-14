import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
// movie
import Home from '../views/Home.vue'
import Recommend from '@/views/Recommend.vue'
import MyMovie from '@/views/MyMovie.vue'

// account
import Account from '@/views/Account.vue'
import Login from '@/views/Login.vue'
import Signup from '@/views/Signup.vue'

// reviews
import CreateReview from '@/views/Review/CreateReview.vue'
import ReviewList from '@/views/Review/ReviewList.vue'

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
    path: '/mymovie',
    name: 'MyMovie',
    component: MyMovie
  },
  {
    path: '/reviews/create',
    name: 'CreateReview',
    component: CreateReview
  },
  {
    path: '/reviews',
    name: 'ReviewList',
    component: ReviewList
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
