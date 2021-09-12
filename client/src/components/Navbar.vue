<template>
  <a-menu v-model="activeIndex" mode="horizontal" class="text-right">
    <a-menu-item v-for="(label, menu) in menus" :key="menu" @click="goTo(menu)">
      {{ label }}
    </a-menu-item>
    <a-icon class="icon" type="github" @click="goToGitHub" />
  </a-menu>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      menus: {
        "/home": "Home",
        "/movie": "Movie",
        "/rating": "Rating",
      },
      activeIndex: ["/home"],
    };
  },

  methods: {
    goTo(path) {
      if (path != this.activeIndex) {
        this.$router.push(path);
        this.activeIndex = [path];
      }
    },

    goToGitHub() {
      window.open("https://github.com/JANICECY/vue-top-movies");
    },
  },

  // updatae active menu when page freshes
  created() {
    this.activeIndex = [this.$route.path];
  },

  //   watch for route changes and update active menu
  watch: {
    immediate: true,
    $route(to, from) {
      this.activeIndex = [to.path];
    },
  },
};
</script>

<style scoped lang='css'>
.icon {
  margin: auto 20px auto 10px;
  font-size: 20px;
}
</style>