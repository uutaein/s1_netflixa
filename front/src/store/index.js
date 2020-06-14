import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userInfo: null,
    isLogin: false,
    isLoginError: false
  },
  mutations: {
    loginSuccess (state, payload) {
      state.isLogin = true
      state.isLoginError = false
      state.userInfo = payload
    },
    loginError (state) {
      state.isLogin = false
      state.isLoginError = true
      state.userInfo = null
    },
    logout (state) {
      state.isLogin = false
      state.isLoginError = false
      state.userInfo = null
    }
  },
  actions: {
    async login (dispatch, loginObj) {
      try {
        const res = axios.post('https://localhost:8080/' + '/rest-auth/signup/' + loginObj)
        localStorage.setItem('access_token', res.data.token)
        this.dispatch('getMemberInfo')
        router.push({ name: 'Home' })
      } catch (err) {
        console.error(err)
      }
    }
  },
  modules: {
  }
})
