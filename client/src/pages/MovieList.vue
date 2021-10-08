<template>
  <div class="movie-table">
    <h1 class="header">IMDB TOP 250</h1>
    <a-table :columns="columns" :data-source="movies">
      <a
        slot="name"
        slot-scope="text, record"
        target="_blank"
        :href="`https://www.imdb.com/${record.detail_path}`"
      >
        <img class="cover" :src="`${record.poster_path}`" alt="cover" />
        <span>{{ text }}</span>
      </a>

      <span slot="genres" slot-scope="genres">
        {{ genres.join(", ") }}
      </span>

      <span slot="directors" slot-scope="directors">
        <a
          class="a-name"
          v-for="director in directors"
          :key="director"
          :href="`https://en.wikipedia.org/wiki/${director}`"
          target="_blank"
        >
          {{ director }}
        </a>
      </span>

      <span slot="stars" slot-scope="stars">
        <a
          class="a-name"
          v-for="star in stars"
          :key="star"
          :href="`https://en.wikipedia.org/wiki/${star}`"
          target="_blank"
        >
          {{ star }}
        </a>
      </span>

      <span slot="rating" slot-scope="rating, record">
        <a-icon type="star" class="star-icon" theme="filled" />
        <span
          ><b>{{ rating }} ({{ record.user_review_count }})</b></span
        >
      </span>
    </a-table>

    <Rating v-if="movies[0]" :movies="movies" />
  </div>
</template>

<script>
import axios from "axios";
import Rating from "./Rating";

export default {
  components: { Rating },
  data() {
    return {
      movies: [],
      columns: [
        {
          title: "Rank",
          dataIndex: "key",
          key: "key",
          sorter: (a, b) => a.key - b.key,
        },
        {
          title: "Title",
          dataIndex: "title",
          key: "title",
          // width: 80,
          scopedSlots: { customRender: "name" },
        },
        {
          title: "Genres",
          dataIndex: "genres",
          key: "genres",
          // width: 80,
          scopedSlots: { customRender: "genres" },
        },
        {
          title: "Directors",
          dataIndex: "directors",
          key: "directors",
          scopedSlots: { customRender: "directors" },
        },

        {
          title: "Stars",
          dataIndex: "stars",
          key: "stars",
          scopedSlots: { customRender: "stars" },
        },

        {
          title: "Plot",
          dataIndex: "plot",
          key: "plot",
          width: 500,
        },

        {
          title: "Rating",
          dataIndex: "rating",
          key: "rating",
          scopedSlots: { customRender: "rating" },
        },
      ],
    };
  },

  created() {
    axios.get("/api/movie/imdb").then((res) => {
      this.movies = res.data.map((item, index) => ({
        ...item,
        key: index + 1,
      }));
    });
  },
};
</script>

<style scoped>
.star-icon {
  margin-right: 5px;
  color: rgb(245 196 24);
}

.cover {
  margin-right: 10px;
}

.a-name {
  display: block;
}

.header {
  font-size: 2em;
  /* margin: 30px 0; */
  font-weight: bold;
}


.movie-table {
  padding: 1% 2%;
}
</style>