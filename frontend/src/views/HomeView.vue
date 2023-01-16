<template>
  <div class="home">
    <MusicList />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import MusicList from "@/components/MusicList.vue";

@Options({
  components: {
    MusicList,
  },
})
export default class HomeView extends Vue {}
</script>
