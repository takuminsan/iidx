<template>
  <div class="hello">aaa</div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import axios from "axios";

// @Options({
//   props: {
//     msg: String,
//   },
// })
export default class MusicList extends Vue {
  // created() {

  // }

  mounted() {
    axios.get("music-list/").then((response) => console.log(response));
  }

  // updated() {

  // }

  // destroyed() {

  // }
}
</script>
