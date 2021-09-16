<template>
  <a-table class="movie-table" :columns="columns" :data-source="data">
    <a
      slot="name"
      slot-scope="text, record"
      target="_blank"
      :href="`https://www.imdb.com/${record.detail_path}`"
    >
      <img class="cover" :src="`${record.poster_path}`" alt="cover" />
      <span>{{ text }}</span>
    </a>

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
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      data: [],
      columns: [
        {
          title: "Rank",
          dataIndex: "key",
          key: "key",
        },
        {
          title: "Title",
          dataIndex: "title",
          key: "title",
          // width: 80,
          scopedSlots: { customRender: "name" },
        },
        {
          title: "Genre",
          dataIndex: "genre",
          key: "genre",
          // width: 80,
          // scopedSlots: { customRender: "name" },
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
      this.data = res.data.map((item, index) => ({ ...item, key: index + 1 }));
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


.movie-table {
  padding: 3% 2%;
}
</style>