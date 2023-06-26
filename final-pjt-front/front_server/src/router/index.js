import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DetailView from '../views/DetailView.vue'
import CommunityView from '../views/CommunityView.vue'
import CreateView from '../views/CreateView.vue'
import UpdateView from '../views/UpdateView.vue'
import ArticleDetail from '../views/ArticleDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/detail/:movie_id',
    name: 'detail',
    component: DetailView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/community/articles/:article_id',
    name: 'article_detail',
    component: ArticleDetail
  },
  {
    path: '/community/articles/:article_id/update',
    name: 'article_update',
    component: UpdateView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
