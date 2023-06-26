<template>
  <div class="total-carousel-container">
    <!-- 캐러셀 설명 start -->
    <div class="d-flex align-items-center justify-content-between">
      <h1 class="carousel-explanation ms-5 mb-2">인기 {{genre_name}} 영화</h1>
      <img alt="이거어때" src="@/assets/이거어때.png" height="50" class="ms-5 mb-2 mt-2" style="cursor: pointer;" @click="randomRecommendation">
    </div>
    <!-- 캐러셀 설명 end -->

    <!-- 캐러셀 start  -->
    <carousel :per-page="6" :paginationEnabled="false">
      <slide v-for="(movie, index) in movies" :key="`total-movie-${index}`">
        <img :src="`${poster_base_path}${movie.poster_path}`" 
          alt="poster" class="mx-5 rounded" 
          @click="goToDetail(movie.id)"
          @dragstart="temp"
          style="cursor: pointer; width: 90%; height: 100%"
        >
      </slide>
    </carousel>
    <!-- 캐러셀 end -->

    <!-- Modal start -->
    <MovieModal v-if="showModal" class="movie-modal" :selected="selected" :genre_name="genre_name" @close-modal="closeModal"/>  
    <!-- Modal end -->
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';
import axios from 'axios'
import _ from 'lodash'
import MovieModal from '@/components/MovieModal.vue'

export default {
  name: "TotalCarousel",
  components: {
    Carousel,
    Slide,
    MovieModal,
  },
  props: {
    genre_name: String,
  },
  data() {
    return {
      movies: null,
      is_that_click_drag: false,
      selected: Object.create(null),
      showModal: false,
    }
  },
  computed: {
    poster_base_path() {
      return this.$store.state.poster_base_path
    }
  },
  methods: {
    getMovies() {
      const getMovieURL = `${this.$store.state.api_url}/api/v1/top_100_movie_list/${this.genre_name}`

      axios({
        method: 'get',
        url: getMovieURL,
      })
      .then((response) => {
        this.movies = response.data
        // console.log(this.movies)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    goToDetail(movie_id) {
      if (this.is_that_click_drag) {
        this.is_that_click_drag = false
      } else {
        this.$router.push(`/detail/${movie_id}/`)
      }
    },
    temp() {
      // console.log('마우스 움직이는 중')
      this.is_that_click_drag = true
    },
    randomRecommendation() {
      this.selected = _.sample(this.movies)
      this.showModal = true
    },
    closeModal() {
      this.showModal = false
    }
  },
  created() {
    this.getMovies()
  }
}
</script>

<style scoped>

.total-carousel-container {
  padding: 20px;
}

.carousel-explanation {
  font-size: 24px;
}

.movie-modal {
  position: fixed;
  margin: auto auto;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
}

</style>