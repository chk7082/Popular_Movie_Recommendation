<template>
  <div class="text-light" style="margin: 20px 10%; ">    
    <div>
      <h1>게시글 수정</h1>
      <!-- <form @submit.prevent="createArticle">
        <label for="title">제목 : </label>
        <input type="text" id="title" v-model.trim="title"><br>
        <label for="content">내용 : </label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
        <input type="submit" id="submit">
      </form> -->
      <div style="margin: 30px 20%;">
        <div> 
          <form @submit.prevent="createArticle" class="mt-3">
            <div align="left" class="form-group my-4">
              <label for="title" class="mb-2 fs-4">제목</label>
              <input v-model="title" type="text" class="form-control" id="title" placeholder="제목을 입력하세요">
            </div>
            <!-- <div class="form-group">
              <label for="author"> 작성자 </label>
              <input type="text" class="form-control" id="author" placeholder="작성자를 입력하세요">
            </div> -->
            <div align="left" class="form-group my-4">
              <label for="content" class="mb-2 fs-4"> 내용 </label>
              <textarea v-model="content" class="form-control" id="content" placeholder="내용을 입력하세요" style="height: 250px;"></textarea>
            </div>
          </form>
          <button @click="updateArticle" type="button" class="btn btn-primary" id="btn-save">등록</button>
          &nbsp;
          <a :href="`/community/articles/${$route.params.article_id}`" role="button" class="btn btn-secondary">취소</a>
        </div>
      </div>
      
    </div>
  </div>


</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UpdateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    updateArticle() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content){
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/articles/article_detail/${this.$route.params.article_id}/`,
        data: {title, content},
      })
      .then(() => {
        // console.log(res)
        this.$router.push(`/community/articles/${this.$route.params.article_id}/`)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getThisArticle(article_id) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/article_detail/${article_id}/`,
      })
      .then((response) => {
        // console.log(res)
        this.title = response.data.title
        this.content = response.data.content
        // console.log('여기까지 오는군')
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created() {
    this.getThisArticle(this.$route.params.article_id)
  },

}
</script>

<style>

</style>