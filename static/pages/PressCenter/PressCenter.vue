<script>
import SideBarText from "@/components/SideBarText.vue";
import NewsList from "@/pages/PressCenter/NewsList.vue";
import VideoList from "@/pages/AboutUs/VideoList.vue";
import Gallery from "@/pages/PressCenter/Gallery.vue";
import Interview from "@/pages/PressCenter/Interview.vue";

export default {
  name: "PressCenter",
  components: {Interview, Gallery, VideoList, NewsList, SideBarText},
  data(){
    return {
      title:"ПРЕСС ЦЕНТР",
    }
  }
}
</script>

<template>
  <div class="w-full relative">
    <div class="h-full absolute top-0 left-0">
      <SideBarText :title="title"/>
    </div>

    <div class="w-full">
      <div class="section mx-auto" style="width:65%;">
        <NewsList/>
      </div>
      <div class="section mx-auto" style="width:65%;">
        <VideoList/>
      </div>
      <div class="section mx-auto" style="width:65%;">
        <Gallery/>
      </div>
      <div class="section mx-auto" style="width:65%;">
        <Interview/>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<style scoped>

</style>