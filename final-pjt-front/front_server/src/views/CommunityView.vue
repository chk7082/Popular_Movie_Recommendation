<template>
  <div class="text-light" style="margin: 20px 10%; ">
    <!-- 나무비위키 헤더 start -->
    <div class="d-flex align-items-center justify-content-between">
      <img alt="게시글 작성" class="invisible" src="@/assets/게시글 작성.png" @click="createArticle" style="cursor: pointer;" width="100">
      <h1>나무비위키</h1>
      <img alt="게시글 작성" src="@/assets/게시글 작성.png" @click="createArticle" style="cursor: pointer;" width="100">
    </div>
    <!-- 나무비위키 헤더 end -->
    <br>
    <div v-for="(article, index) in articles" :key="`article-${index}`" class="my-5" style="cursor: pointer;" @click="goToArticleDetail(article.id)">
      <!-- 첫번째 줄 start -->
      <div class="d-flex mb-3 align-items-center justify-content-between">
        <div align="left" class="fs-3 w-50">
          {{ article.title }}
        </div>

        <div align="right" class="fs-6 text-white-50 w-50">
          생성 시각 : {{ dateTime(article.created_at) }}
        </div>

      </div>
      <!-- 첫번째 줄 end -->

      <!-- 두번째 줄 start -->
      <div class="d-flex align-items-center justify-content-between">
        <div align="left" class="fs-6 text-white-50 w-50" style="height: 25px; display: inline-block; overflow: hidden; ">
          {{ article.content }}
        </div>

        <div align="right" class="fs-6 text-white-50 w-50">
          최근 수정 시각 : {{ dateTime(article.updated_at) }}
        </div>

      </div>
      <!-- 두번째 줄 end -->
      <hr>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
  name: 'CommunityView',
  data() {
    return {
      articles: null,
    }
  },
  methods: {
		getArticleList() {
			const getArticleListURL = `${this.$store.state.api_url}/api/v1/articles/article_list/`

			axios({
				method: 'get',
				url: getArticleListURL,
			})
			.then((response) => {
				this.articles = response.data
        // console.log(this.articles)
			})
			.catch((error) => {
				console.log(error)
			})
		},
    dateTime(value) {
      return moment(value).format('YYYY-MM-DD HH:mm:ss')
    },
    createArticle() {
      if(this.$route.path!=='/create') {
        this.$router.push('/create')
      }
    },
    goToArticleDetail(article_id) {
      this.$router.push(`/community/articles/${article_id}`)
    },
	},
	created() {
		this.getArticleList()
	},
}
</script>

<style>

</style>