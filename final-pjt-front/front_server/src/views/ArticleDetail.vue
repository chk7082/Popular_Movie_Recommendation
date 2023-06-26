<template>
  <div class="text-light d-flex justify-content-center" style="margin: 20px 0; ">
    <div>
      <!-- 디테일 start -->
      <div>
        <div>
          <h1 class="my-5">{{ article_detail.title }}</h1>
          <div class="card" style="width: 600px; height: 400px;">
            <div class="card-body" style="overflow-y: auto;">
              <h4 align="left">{{ article_detail.content }}</h4>
            </div>
          </div>
        </div>
      </div>
      <!-- 디테일 end -->
      <br>
      <div>
        <!-- 각종 버튼들 start -->
        <button @click="updateArticle(article_detail.id)" type="button" class="btn btn-primary" >수정</button>
        &nbsp;
        <button @click="deleteArticle(article_detail.id)" type="button" class="btn btn-danger" >삭제</button>
        &nbsp;
        <a href="/community" role="button" class="btn btn-secondary">뒤로가기</a>
        <!-- 각종 버튼들 end -->
      </div>
    </div>
  </div>
  
</template>

<script>
import axios from 'axios'

export default {
  name: 'ArticleDetail',
  data() {
    return {
      article_detail: null,
    }
  },
  methods: {
    getArticleDetail(article_id) {
      const getArticleDetailURL = `${this.$store.state.api_url}/api/v1/articles/article_detail/${article_id}/`
      
      axios({
        method: 'get',
        url: getArticleDetailURL,
      })
      .then((response) => {
        this.article_detail = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    },
    updateArticle(article_id) {
      // const updateArticleURL = `${this.$store.state.api_url}/api/v1/articles/article_detail/${article_id}/`

      // axios({
      //   method: 'put',
      //   url: updateArticleURL,
      // })
      // .then((response) => {
      //   this.article_detail = response.data
      // })
      // .catch((error) => {
      //   console.log(error)
      // })

      this.$router.push(`/community/articles/${article_id}/update`)
    },
    deleteArticle(article_id) {
      const deleteArticleURL = `${this.$store.state.api_url}/api/v1/articles/article_detail/${article_id}/`

      axios({
        method: 'delete',
        url: deleteArticleURL,
      })
      .then(() => {
        this.$router.push(`/community`)
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  created() {
    this.getArticleDetail(this.$route.params.article_id)
  }

}
</script>

<style>

</style>