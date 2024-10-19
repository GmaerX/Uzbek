<script>
import NextBtn from "@/components/buttons/nextBtn.vue";
import PrevBtn from "@/components/buttons/prevBtn.vue";
import FamousPersonItem from "@/pages/FamousPersonsPage/FamousPersonItem.vue";
import SideBarText from "@/components/SideBarText.vue";

export default {
  name: "RegionsPage",
  components: {SideBarText, FamousPersonItem, PrevBtn, NextBtn},
  data() {
    return{
      title:"Регионы"
    }
  }
}
</script>

<template>
<div>
  <div class="w-full relative">
    <div class="h-full absolute top-0 left-0">
      <SideBarText :title="title"/>
    </div>

    <div class="w-full" style="padding:80px 0">
      <div style="width:65%; margin-bottom: 40px;" class="flex justify-between mx-auto">
        <h2 class="font-gilroy" style="font-size: 40px; line-height: 52px; font-weight: 500">Этнокультурный центр узбеков Казахстана</h2>
      </div>
      <div class="relative bg-blue-50 mx-auto" style="width: 1224px; height: 940px">
        <div class="absolute top-0 left-0">
          <p class="text-sm" style="color: #575F6C">Sed ut perspiciatis unde omnis iste natus error sit <br> voluptatem accusantium doloremque laudantium,<br> totam rem aperiam.</p>
        </div>
      </div>
    </div>
    <div class="mx-auto cursor-pointer " style="width:65%; margin-bottom: 40px;">
      <div class="w-full grid grid-cols-3" style="border-radius: 8px; border: 1px solid #EBEEF0;overflow: hidden">
        <router-link
            to="/regions/guide"
            class="item"
            :class="{ active: $route.path === '/regions/guide' }">Руководство</router-link>

        <router-link
            to="/regions/information"
            class="item"
            :class="{ active: $route.path === '/regions/information' }">Информация</router-link>

        <router-link
            to="/regions/contacts-info"
            class="item"
            :class="{ active: $route.path === '/regions/contacts-info' }">Контакты</router-link>
      </div>
    </div>
    <div class="mx-auto" style="width:65%">
      <router-view></router-view>
    </div>
  </div>
</div>
</template>

<style scoped>
.item {
  @apply py-2.5 px-6 text-base mx-auto w-full text-center;
  font-weight: 500;
}
.item + .item {
  border-left: 1px solid #EBEEF0
}
.active {
  background-color: #0072AB;
  color: white;
}
</style>