import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_id: '',
    user_name: '',
    base_url: '',
    isLoggedin: false,
    isSuperUser: false,
    genre: ''
  },
  mutations: {
    urlSave (state, url) {
      state.base_url = url
    },
    usernameSave (state, username) {
      state.user_name = username
    },
    useridSave (state, userID) {
      state.user_id = userID
    },
    Login (state) {
      state.isLoggedin = true
    },
    Logout (state) {
      state.isLoggedin = false
      state.user_name = ''
      state.user_id = ''
    },
    LoginState (state, cookies) {
      state.isLoggedin = cookies.iskey
      state.user_name = cookies.name
      state.user_id = cookies.id
    },
    GetGenre (state, genreData) {
      state.genre = genreData
    }
  },
  actions: {

  },
  modules: {
  }
})
