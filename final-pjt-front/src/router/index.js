import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/movies/Home'
import Signup from '@/views/accounts/Signup'
import Signin from '@/views/accounts/Signin'
import Profile from '@/views/accounts/Profile'
import Community from '@/views/community/Community'
import ArticleForm from '@/views/community/ArticleForm'
import ArticleDetail from '@/views/community/ArticleDetail'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/signin',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/accounts/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/community/articleform',
    name: 'ArticleForm',
    component: ArticleForm
  },
  {
    path: '/community/articledetail',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
