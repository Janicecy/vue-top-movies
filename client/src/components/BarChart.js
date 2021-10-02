import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
  data() {
    return {
        options: {
          }
    }
  },
  props: {
    chartdata: {
        type: Object,
        default: null
      },
    //   options: {
    //     type: Object,
    //     default: null
    //   }
  },

  watch: {
    chartdata: {
        immediate: true, 
        handler (newChartData, oldVal) {
            this.renderChart(newChartData, this.options);
          // do your stuff
        }
    }
  },

  mounted() {
    // Overwriting base render method with actual data.
    this.renderChart(this.chartdata, this.options);
  },
};