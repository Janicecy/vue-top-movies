<template>
  <div id="app">
    <Navbar />
    <router-view></router-view>
    <div id="qeqw"></div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar";

export default {
  name: "App",
  components: {
    Navbar,
  },
  created() {},
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.d-flex {
  display: flex;
}

.flex-wrap {
  flex-wrap: wrap;
}

.space-evently {
  justify-content: space-evenly;
}

.text-right {
  text-align: right;
}

.text-center {
  text-align: center;
}
</style>
