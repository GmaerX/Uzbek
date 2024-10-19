<script>
import SideBar from "@/pages/MainPage/SideBar.vue";
import moreDetail from "@/components/buttons/moreDetail.vue";
import NextBtn from "@/components/buttons/nextBtn.vue";
import PrevBtn from "@/components/buttons/prevBtn.vue";
import AutoCarousel from "@/pages/MainPage/AutoCarousel.vue";

export default {
  name: "Section6",
  components: {AutoCarousel, PrevBtn, NextBtn, SideBar, moreDetail},
  data() {
    return {
      page: "06",
      title:"узнать больше",
      items: [
        { src: require('@/assets/icons/logo1.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo2.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo3.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo4.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo5.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo6.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo7.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo8.svg'), alt: 'Logo 7' },
      ],
    };
  },
}
</script>

<template>
<div class="w-full flex">
  <div>
    <SideBar :page="page" :icon="false"/>
  </div>
  <div class="w-full">
    <div class="w-full" style="padding: 80px 0 80px 188px;">
      <div style="width: 1224px; padding-bottom: 40px" class="flex justify-between">
        <h2 class="font-gilroy" style="font-size: 40px; line-height: 52px; font-weight: 500">Наши партнеры</h2>
        <div class="flex items-center gap-6">
          <prev-btn/>
          <next-btn/>
        </div>
      </div>
    </div>
    <div class="w-full">
      <auto-carousel/>
    </div>
  </div>
</div>
</template>

<style scoped>
</style>