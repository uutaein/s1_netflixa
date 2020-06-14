import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
// views
import Home from '../views/Home.vue'
import Account from '@/views/Account.vue'
import Login from '@/views/Login.vue'
import Signup from '@/views/Signup.vue'
import Recommend from '@/views/Recommend.vue'
import MyMovie from '@/views/MyMovie.vue'

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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
