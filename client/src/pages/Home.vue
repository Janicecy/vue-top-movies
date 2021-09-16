<template>
  <div class="text-center">
    <div class="header">
      <div class="header-text">
        <h1>Top 100 Movies Data Analytics</h1>
        <h3>Built with Vue2, Flask and Echarts.</h3>
      </div>
      <img id="header-img" src="../assets/header.jpg" alt="" />
    </div>

    <div class="d-flex flex-wrap space-evently category">
      <a-card hoverable class="box-card" @click.native="routeTo('movie')">
        <a-icon class="icon" theme="filled" type="video-camera" />
        <div class="num">100</div>
        <div class="text">Moives</div>
        <img class="logo" src="../assets/imdb_logo.png" alt="">
      </a-card>

      <a-card hoverable class="box-card" @click.native="routeTo('rating')">
        <a-icon class="icon" theme="filled" type="star" />
        <div class="num">100</div>
        <div class="text">Rating</div>
      </a-card>

      <a-card hoverable class="box-card">
        <a-icon type="area-chart" class="icon"  />
        <div class="num">100</div>
        <div class="text">Charts</div>
      </a-card>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    routeTo(name) {
      this.$router.push({ name });
    },
  },
};
</script>

<style scoped lang="css">
h1 {
  font-size: 2.5em;
  font-weight: bolder;
}

.header-text {
  background-color: #002e40;
  padding: 2%;
}

h1, h3 {
  color: white;
}

.header {
  margin-bottom: 100px;
}

#header-img {
  object-fit: cover;
  width: 100%;
  height: 200px;
}

.box-card {
  min-width: 350px;
  margin: 20px;
  cursor: pointer;
}

.num {
  font-size: 60px;
  font-weight: bolder;
  color: #409eff;
}

.box-card div {
  margin-bottom: 10px;
}

.category {
  background-color: #f4f4f5;
  padding: 3%;
  margin: 0 3%;
}

.text {
  font-weight: bold;
}

.logo {
    width: 50px;
}

.icon {
  font-size: 45px;
  display: block;
}
</style>