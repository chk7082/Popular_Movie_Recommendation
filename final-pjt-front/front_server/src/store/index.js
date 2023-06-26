import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    api_url: 'http://127.0.0.1:8000',
    poster_base_path: 'https://image.tmdb.org/t/p/original',
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
