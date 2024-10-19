<script>
import SideBarText from "@/components/SideBarText.vue";

export default {
  name: "Donats",
  components: {SideBarText},
  data(){
    return {
      title: "Донаты"
    }
  }
}
</script>

<template>
  <div class="w-full relative">
    <div class="h-full absolute top-0 left-0">
      <SideBarText :title="title"/>
    </div>

    <div class="mx-auto cursor-pointer" style="width:65%; padding: 64px 0">
      <h2 class="font-gilroy mb-2" style="font-weight: 500; font-size: 40px; line-height: 52px">
        Хотите помочь нуждающимся?
      </h2>
      <p style="color:#575F6C" class="text-base leading-8">
        Заполните все формы ниже, и отправьте донат.
      </p>
      <div class="w-full grid grid-cols-2 my-10" style="border-radius: 8px; border: 1px solid #EBEEF0;overflow: hidden">
        <router-link
            to="/donates/1"
            class="item"
            :class="{ active: $route.path === '/donates/1' }">Через карту</router-link>

        <router-link
            to="/donates/2"
            class="item"
            :class="{ active: $route.path === '/donates/2' }">Через KASPI QR</router-link>

      </div>
      <div>
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<style scoped>
.item {
  @apply py-2.5 px-6 text-base mx-auto w-full text-center uppercase;
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