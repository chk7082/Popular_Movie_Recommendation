<template>
  <div class="d-flex w-100 h-100 align-items-center justify-content-center" @click.stop="closeModal">
    <div @click.stop>
      <div class="rounded" style="width: 650px; background-color: #222222">
        <div class="p-3">
          <h5 class="modal-title">이런 <span v-if="!genre_name">인기</span>  <span v-if="genre_name">{{ genre_name }}</span> 영화 어떠세요?</h5>
        </div>
        <hr class="m-0">
        <div>
          <h4 class="my-3">{{ selected.title }}</h4>
          <div>
            <img :src="`${poster_base_path}${selected.poster_path}`" 
              alt="poster" class="rounded"
              style="cursor: pointer; height: 25rem;"
              @click.stop="goToDetail(selected.id)"
            >
          </div>
          <div class="mt-4 mx-5 fs-5">
            <h5 class="text-white-50">{{ selected.tagline }}</h5>
          </div>
          <br>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'MovieModal',
  data() {
    return {
      
    }
  },
  computed: {
    poster_base_path() {
      return this.$store.state.poster_base_path
    }
  },
  props: {
    selected: Object,
    genre_name: String,
  },
  methods: {
    goToDetail(movie_id) {
      this.$router.push(`/detail/${movie_id}/`)
    },
    closeModal() {
      // console.log('클릭 테스트')
      this.$emit('close-modal')
    },
  },
  created() {
    console.log()
  },
}
</script>

<style>

</style>