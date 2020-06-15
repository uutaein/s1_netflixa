import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_id: '',
    base_url: ''
  },
  mutations: {
    urlSave (state, url) {
      state.base_url = url
    },
    idSave (state, id) {
      state.user_id = id
    }
  },
  actions: {

  },
  modules: {
  }
})
