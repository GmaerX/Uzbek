<script>
import NewsItem from "@/pages/PressCenter/NewsItem.vue";
import NextBtn from "@/components/buttons/nextBtn.vue";
import PrevBtn from "@/components/buttons/prevBtn.vue";
import VideoMaterial from "@/pages/PressCenter/VideoMaterial.vue";

export default {
  name: "VideoList",
  components: {VideoMaterial, PrevBtn, NextBtn, NewsItem},
  data(){
    return{
      video:[1,2,3]
    }
  }
}
</script>

<template>
  <div style="padding: 100px 0;">
    <div style="margin-bottom: 56px" class="w-full flex items-center justify-between">
      <h2 class="font-gilroy" style="font-weight: 500; font-size: 40px">
        Видео материалы
      </h2>
      <div class="flex gap-4 items-center">
        <prev-btn/>
        <next-btn/>
      </div>
    </div>
<!--    <div style="grid-template-columns: repeat(3, 1fr);display: grid;gap: 24px;">-->
    <div class="grid grid-cols-3 gap-6" style="">
      <div v-for="n in video" :key="n.id" class="">
        <VideoMaterial />
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>