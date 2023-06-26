<template>
  <div class="text-light">
		<!-- 라우터 링크에 변수가 들어갈때, 이를 뽑아서 사용할 수 있는 방법 -->
		<!-- https://router.vuejs.org/guide/essentials/dynamic-matching.html -->

		<!-- backdrop 이미지 start -->
    <div>
      <img v-if="movie_detail" :src="`${poster_base_path}${movie_detail.backdrop_path}`" alt="backdrop" style="width: 100%;">
		</div>
		<!-- backdrop 이미지 end -->

		<div v-if="movie_detail" style="margin: 40px 7%;">
			<!-- title start -->
			<!-- 한글 제목 -->
			<div class="d-flex align-items-center justify-content-between">
				<div class="d-flex align-items-center">
					<h1>{{ movie_detail.title }}</h1>
					&nbsp;&nbsp;&nbsp;
					<div class="text-white-50 fs-3">({{ movie_detail.release_date }})</div>
				</div>
				
				<!-- 평균 평점 start -->
				<div>
					<h3> <span style="color: #E50914;">★</span> {{ preprocessed_average_rating }} </h3>
				</div>
				<!-- 평균 평점 end -->
			</div>
			<!-- 원제목 -->
			<div class="d-flex mb-4 align-items-center justify-content-between">
				<div class="d-flex">
					<h6 class="text">{{ movie_detail.original_title }}</h6>
					&nbsp;&nbsp;&nbsp;
					<h6 class="text-white-50">런타임 : {{ runtime }}</h6>
				</div>
				<!-- genre start -->
				<div>
					<h6>
						장르 : 
						<span v-for="(genre, index) in movie_detail.genres" :key="`genre-name-${index}`">
							{{ genre.name }}
						</span>
					</h6>
				</div>
				<!-- genre end -->
			</div>
			<!-- title end -->

			<!-- tagline start -->
			<div align="left" class="mt-4">
        <h5 class="text-white-50">{{ movie_detail.tagline }}</h5>
      </div>
			<!-- tagline end -->
      <br>
      <!-- overview start -->
      <div align="left">
				<h5 class="mb-3">개요</h5>
        <h6>{{ movie_detail.overview }}</h6>
      </div>
      <!-- overview end -->
		
		<!-- 뒤로가기 버튼 start -->
		<div style="margin: 40px 7%;"></div>
			<img align="right" alt="뒤로가기 버튼" src="@/assets/뒤로가기.png" @click="toHome" style="cursor: pointer;" height="50">
			<br>
			<br>
			<br>
			<br>
		</div>
		<!-- 뒤로가기 버튼 end -->
  </div>
</template>

<script>
import axios from 'axios'

export default {
	name: "DetailView",
	data() {
		return {
			movie_detail: null,
			runtime: null,
			preprocessed_average_rating: null,
		}
	},
	computed: {
		poster_base_path() {
			return this.$store.state.poster_base_path
		}
	},
	methods: {
		getMovieDetail(movie_id) {
			const getMovieDetailURL = `${this.$store.state.api_url}/api/v1/movie_detail/${movie_id}/`

			axios({
				method: 'get',
				url: getMovieDetailURL,
			})
			.then((response) => {
				// console.log(response)
				this.movie_detail = response.data
				this.convertRunTime(response.data.runtime)
				this.preprocessAverageRating(response.data.vote_average)
			})
			.catch((error) => {
				console.log(error)
			})
		},
		convertRunTime(runtime) {
			const hour = Math.floor(runtime / 60)
			const minute = runtime - 60 * hour

			if (hour > 0) {
				this.runtime = `${hour}시간 ${minute}분`
			} else {
				this.runtime = `${minute}분`
			}
		},
		preprocessAverageRating(average_rating) {
			const dotPosition = average_rating.indexOf('.')
			this.preprocessed_average_rating = average_rating.substr(0, dotPosition+3)
		},
		toHome() {
			this.$router.push('/')
    },
	},
	created() {
		this.getMovieDetail(this.$route.params.movie_id)
	}
}
</script>

<style>
</style>