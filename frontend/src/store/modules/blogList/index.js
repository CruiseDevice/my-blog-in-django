import axios from 'axios'

const state = {

}

const mutations = {

}

const actions = {
  fetchblogs ({commit}) {
    axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/',
        headers: {
            // Authorization: 'Token ' + TOKEN,
            'Content-Type': 'application/json'
        }
    })
    .then((response) => {
        console.log(response)
    })
  }
}

const getters = {

}

const blogListModule = {
  state,
  mutations,
  actions,
  getters
}

export default blogListModule
