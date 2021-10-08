<template>
  <div id="wrapper">
    <h2 class="header text-center">Rating Distribution</h2>
    <bar-chart :chartdata="ratingData" :width="800" :height="400" id="chart" />
    <h2 class="header text-center">Genre Distribution</h2>
    <bar-chart :chartdata="genreData" :width="800" :height="400" id="chart" />

    <h2 class="header text-center">Word Cloud</h2>
    <div id="word-cloud">
      <wordcloud
        :data="cloudWords"
        nameKey="name"
        valueKey="value"
        :color="colors"
        :showTooltip="false"
      >
      </wordcloud>
    </div>
  </div>
</template>


<script>
import BarChart from "../components/BarChart";
import axios from "axios";
import wordcloud from "vue-wordcloud";

export default {
  name: "Rating",
  components: { BarChart, wordcloud },
  props: ["movies"],
  data() {
    return {
      colors: [
        "#3498db",
        "#1abc9c",
        "#2ecc71",
        "#3498db",
        "#9b59b6",
        "#34495e",
        "#16a085",
        "#2980b9",
        "#8e44ad",
        "#2c3e50",
        "#bdc3c7",
        "#c0392b",
        "#f39c12",
      ],
      ratingData: {},
      genreData: {},
      cloudWords: [],
    };
  },
  mounted() {
    const getColors = (num) => {
      const result = [];
      for (let i = 0; i < num; i++) {
        const ranNum = Math.floor(Math.random() * this.colors.length);
        result.push(this.colors[ranNum]);
      }
      return result;
    };
    axios.get("/api/movie/imdb/genres").then((res) => {
      this.cloudWords = res.data;
      this.genreData = {
        labels: res.data.map((i) => i._id),
        datasets: [
          {
            label: "Top genres",
            backgroundColor: getColors(res.data.length),
            data: res.data.map((i) => i.value),
          },
        ],
      };
    });

    axios.get("/api/movie/imdb/ratings").then((res) => {
      this.ratingData = {
        labels: res.data.map((i) => i._id),
        datasets: [
          {
            label: "Occurance",
            backgroundColor: "#3498db",
            data: res.data.map((i) => i.count),
          },
        ],
      };
    });
  },
};
</script>

<style scoped>
.header {
  font-size: 2em;
  margin: 30px 0;
  font-weight: bold;
}

#chart {
  width: 800px;
  height: 400px;
  margin: 0 auto;
}
</style>