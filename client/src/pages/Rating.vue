<template>
  <div id="wrapper">
    <h2 class="header text-center">Movie Rating Distribution</h2>
    <bar-chart :chartdata="chartData" width="800" height="400" id="chart" />
  </div>
</template>


<script>
import BarChart from "../components/BarChart";
import axios from "axios";

export default {
  name: "Rating",
  components: { BarChart },
  data() {
    return {
      chartData: {},
    };
  },
  mounted() {
    axios.get("/api/movie/imdb/ratings").then((res) => {      
      this.chartData = {
        labels: res.data.map(i => i._id),
        datasets: [
          {
            label: "Movie Count",
            backgroundColor: "#f87979",
            data: res.data.map(i => i.movies.length),
          },
        ],
      }
    })
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