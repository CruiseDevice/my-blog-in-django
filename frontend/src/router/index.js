import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import BlogList from '@/components/BlogList'
import NotFound from '@/components/404'
import Post from '@/components/Post'

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
      path: '/blog',
      name: 'BlogList',
      component: BlogList
    },
    {
      path: '/blog/:post_id',
      name: 'Post',
      component: Post,
      props: true
    },
    {
      path: '*',
      component: NotFound
    }
  ]
})
