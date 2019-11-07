import Vue from 'vue'
import Vuex from 'vuex'

import blogList from './blogList/index.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    blogList
  }
})
