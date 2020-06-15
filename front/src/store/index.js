import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_name: '',
    base_url: '',
    isLoggedin: false
  },
  mutations: {
    urlSave (state, url) {
      state.base_url = url
    },
    usernameSave (state, username) {
      state.user_name = username
    },
    Login (state) {
      state.isLoggedin = true
    },
    Logout (state) {
      state.isLoggedin = false
    }
  },
  actions: {

  },
  modules: {
  }
})
