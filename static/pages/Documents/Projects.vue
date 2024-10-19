<script>
import SideBarText from "@/components/SideBarText.vue";
import DocumentItem from "@/pages/Documents/DocumentItem.vue";
import PrevBtn from "@/components/buttons/prevBtn.vue";
import NextBtn from "@/components/buttons/nextBtn.vue";
import ProjectItem from "@/pages/Documents/ProjectItem.vue";

export default {
  name: "Projects",
  components: {ProjectItem, NextBtn, PrevBtn, DocumentItem, SideBarText},
  data(){
    return{
      title:"Проекты",
    }
  }
}
</script>

<template>
  <div class="w-full relative">
    <div class="h-full absolute top-0 left-0">
      <SideBarText :title="title" :is-background="true"/>
    </div>

    <div class="w-full" style="padding: 64px 0">
      <div class="mx-auto" style="width:65%;">
        <div class="flex items-center justify-between mb-14">
          <p class="font-gilroy" style="font-weight: 500; font-size: 40px">Проекты на 2025 год</p>
          <div class="flex items-center gap-6">
            <prev-btn/>
            <next-btn/>
          </div>
        </div>
        <div class="w-full grid grid-cols-2 gap-6">
          <ProjectItem/>
          <ProjectItem/>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>