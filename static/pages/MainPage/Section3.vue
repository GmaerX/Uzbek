<script>
import SideBar from "@/pages/MainPage/SideBar.vue";
import moreDetail from "@/components/buttons/moreDetail.vue";
export default {
  name: "Section3",
  components: {moreDetail, SideBar},
  data() {
    return {
      page: "03",
      title:"узнать больше"
    };
  }
}
</script>

<template>
<div class="w-full flex">
  <div>
    <SideBar :page="page" :is-background="true"/>
  </div>
  <div class="w-full" style="background: #F7F8FA; padding: 64px 0 64px 188px;">
    <div style="width: 1224px; padding-bottom: 56px" class="flex justify-between">
      <h2 class="font-gilroy" style="font-size: 40px; line-height: 52px; font-weight: 500">Культура и традиция</h2>
      <router-link :to="{ name: 'AboutUs', hash: '#section-2' }">
        <moreDetail :title="title"/>
      </router-link>
    </div>
    <div style="width: 1224px; height: 640px; border-radius: 6px" class="content-end relative">
      <img src="@/assets/images/img.png" alt="" class="w-full h-full">
      <div class="absolute bottom-0 left-0 p-10">
        <div class="text-white font-medium text-2xl mb-4">Культура и традиция</div>
        <div class="font-normal text-base leading-8" style="color: rgba(255, 255, 255, 0.7);">Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptate</div>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>