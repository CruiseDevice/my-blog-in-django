/* eslint-disable */
import axios from 'axios'

const state = {
  posts: []
}

const mutations = {
  UPDATE_BLOG_POSTS(state, payload) {
    state.posts = payload
  }
}

const actions = {
  fetchblogs (state) {
    axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then((response) => {
        console.log(response.data)
        state.commit('UPDATE_BLOG_POSTS', response.data)
    })
  }
}

const getters = {
  getposts: state => state.posts
}

const blogListModule = {
  state,
  mutations,
  actions,
  getters
}

export default blogListModule
