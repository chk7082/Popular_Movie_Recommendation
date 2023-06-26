<template>
  <div class="home">
    <!-- 메인 표지 start -->
    <div class="w-100">
      <img alt="메인 표지" src="@/assets/메인 표지.png" class="w-100">
    </div>
    <!-- 메인 표지 end -->

    <!-- 캐러셀 모음 담을 블럭 start -->
    <div class="carousel-container text-light">
      <!-- 장르 구분 없는 캐러셀 start -->
      <TotalCarousel class="my-5" />
      <!-- 장르 구분 없는 캐러셀 end -->

      <!-- v-for로 장르별 캐러셀 start -->
      <GenreCarousel class="my-5" v-for="(genre, index) in genres" :key="`genre-${index}`" :genre_name="genre.name"/>
      <!-- v-for로 장르별 캐러셀 end -->
    </div>
    <!-- 캐러셀 모음 담을 블럭 end -->
  </div>
</template>

<script>
import TotalCarousel from '@/components/TotalCarousel.vue'
import GenreCarousel from '@/components/GenreCarousel.vue'

import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      genres: null,
    }
  },
  components: {
    TotalCarousel,
    GenreCarousel,
  },
  methods: {
    getGenres() {
      const getGenreURL = `${this.$store.state.api_url}/api/v1/total_genre/`

      axios({
        method: 'get',
        url: getGenreURL,
      })
      .then((response) => {
        // console.log(response)
        this.genres = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  created() {
    this.getGenres()
  },
}
</script>

<style scoped>

.carousel-container {
  padding: 40px;
}

</style>
