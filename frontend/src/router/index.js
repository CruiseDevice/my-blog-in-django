import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import BlogList from '@/components/BlogList'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/',
      name: 'BlogList',
      component: BlogList
    }
  ]
})
