<script>
import VideoMaterial from "@/pages/PressCenter/VideoMaterial.vue";
import NextBtn from "@/components/buttons/nextBtn.vue";
import PrevBtn from "@/components/buttons/prevBtn.vue";
import GalleryItem from "@/pages/PressCenter/GalleryItem.vue";

export default {
  name: "Gallery",
  components: {GalleryItem, PrevBtn, NextBtn, VideoMaterial},
  data(){
    return{
      photo: [1,2,3,4,5,6]
    }
  }
}
</script>

<template>
  <div style="padding: 0 0 100px 0;">
    <div style="margin-bottom: 56px" class="w-full flex items-center justify-between">
      <h2 class="font-gilroy" style="font-weight: 500; font-size: 40px">
        Фотогалерея
      </h2>
      <div class="flex gap-4 items-center">
        <prev-btn/>
        <next-btn/>
      </div>
    </div>
    <div style="grid-template-columns: repeat(3, 1fr);display: grid" class="gap-y-8 gap-x-6">
      <div v-for="n in photo" :key="n.id" class="">
        <GalleryItem />
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>