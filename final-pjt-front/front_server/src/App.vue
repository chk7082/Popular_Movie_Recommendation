<template>
  <div id="app" class="mb-5">
    <!-- 네비게이션 바 start -->
    <nav class="d-flex justify-content-between align-items-center">
      <!-- 왼쪽 로고 + 여러 탭 start -->
      <div>
        <img alt="넷플릭스 로고" src="@/assets/logo.png" @click="toHome" style="cursor: pointer;">
        &nbsp; &nbsp;
        <router-link to="/">홈</router-link> &nbsp; | &nbsp;
        <router-link to="/community/">커뮤니티</router-link>
      </div>
      <!-- 왼쪽 로고 + 여러 탭 end -->

      <!-- 오른쪽 로고들 start -->
      <div>
        <img alt="돋보기" src="@/assets/돋보기.png">
        &nbsp;
        &nbsp;
        <img alt="종" src="@/assets/종.png">
        &nbsp;
        &nbsp;
        <img alt="빨간 네모" src="@/assets/빨간 네모.png">
        &nbsp;
        &nbsp;
      </div>
      <!-- 오른쪽 로고들 end -->
    </nav>
    <!-- 네비게이션 바 end -->

    <!-- 라우터 뷰 start -->
    <router-view/>
    <!-- 라우터 뷰 end -->
  </div>
</template>

<script>
export default {
  name: "App",
  methods: {
    toHome() {
      // 로고 클릭 시, 이미 홈에 있지 않다면, 홈으로 이동
      if(this.$route.path!=='/') {
        this.$router.push('/')
      }
    },
  }
}

</script>

<style>
@font-face {
  font-family: 's-core-dream';
  src: url('@/assets/fonts/20956085_SCDream5_OTF.otf')
}

#app {
  font-family: s-core-dream, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 20px;
  font-size: 24px;
}

nav a {
  
  font-weight: bold;
  color: #808080;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: white;
  text-decoration: none;
}
/* .logo{
 cursor: pointer; 
} */
</style>
