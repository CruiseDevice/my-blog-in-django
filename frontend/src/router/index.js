import Vue from 'vue'
import Router from 'vue-router'
import BlogList from '@/components/BlogList'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'BlogList',
      component: BlogList
    }
  ]
})
