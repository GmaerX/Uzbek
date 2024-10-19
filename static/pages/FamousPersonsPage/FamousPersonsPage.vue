<script>
import EducationAndSport from "@/pages/AboutUs/EducationAndSport.vue";
import WhoWeAre from "@/pages/AboutUs/WhoWeAre.vue";
import FamousPersons from "@/pages/AboutUs/FamousPersons.vue";
import Help from "@/pages/AboutUs/Help.vue";
import OurStory from "@/pages/AboutUs/OurStory.vue";
import CultureAndTradition from "@/pages/AboutUs/CultureAndTradition.vue";
import YouthOrganizations from "@/pages/AboutUs/YouthOrganizations.vue";
import SideBarText from "@/components/SideBarText.vue";
import FamousPersonItem from "@/pages/FamousPersonsPage/FamousPersonItem.vue";
import PrevBtn from "@/components/buttons/prevBtn.vue";
import NextBtn from "@/components/buttons/nextBtn.vue";

export default {
  name: "FamousPersonsPage",
  components: {
    NextBtn,
    PrevBtn,
    FamousPersonItem,
    SideBarText,
    YouthOrganizations, CultureAndTradition, OurStory, Help, FamousPersons, WhoWeAre, EducationAndSport},
  data(){
    return {
      title: "известные личности",
    }
  }
}
</script>

<template>
  <div class="w-full relative">
    <div class="h-full absolute top-0 left-0">
      <SideBarText :title="title"/>
    </div>

    <div class="w-full" style="padding: 80px 0">
      <div class="mx-auto flex justify-between" style="width:65%; margin-bottom: 48px;">
        <p class="font-gilroy" style="font-weight: 500; font-size: 40px">Известные личности</p>
        <div class="flex gap-6 items-center">
          <prev-btn></prev-btn>
          <next-btn/>
        </div>
      </div>
      <div class="mx-auto" style="width:65%;">
        <FamousPersonItem class="mp"/>
        <FamousPersonItem class="mp"/>
        <FamousPersonItem class="mp"/>
        <FamousPersonItem class="mp"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
.mp + .mp {
  @apply mt-6;
}
</style>