<script>
import WhoWeAre from "@/pages/AboutUs/WhoWeAre.vue";
import SideBar from "@/pages/MainPage/SideBar.vue";
import OurStory from "@/pages/AboutUs/OurStory.vue";
import CultureAndTradition from "@/pages/AboutUs/CultureAndTradition.vue";
import Section4 from "@/pages/MainPage/Section4.vue";
import FamousPersons from "@/pages/AboutUs/FamousPersons.vue";
import YouthOrganizations from "@/pages/AboutUs/YouthOrganizations.vue";
import EducationAndSport from "@/pages/AboutUs/EducationAndSport.vue";
import Help from "@/pages/AboutUs/Help.vue";

export default {
  name: "AboutUs",
  components: {
    Help,
    EducationAndSport,
    YouthOrganizations, FamousPersons, Section4, CultureAndTradition, OurStory, SideBar, WhoWeAre},
  data (){
    return {
      sections: ['кто мы','наша история','культура','личности','молодежные организации','образование и спорт','помощь',],
      currentSection: 0,
    }
  },
  mounted() {
    const observer = new IntersectionObserver(this.handleIntersection, {
      threshold: 0.3,
    });

    const sectionElements = document.querySelectorAll('.section');
    sectionElements.forEach((section) => observer.observe(section));
  },
  methods: {
    handleIntersection(entries) {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          const sectionId = entry.target.id.split('-')[1];
          this.currentSection = parseInt(sectionId);
        }
      }
    },
  },
}
</script>

<template>
  <div class="w-full flex relative">
    <div style="width: 160px; height: 100%; border-right: 1px solid #EBEEF0; position: absolute; top:0" class="">
      <div style="position: sticky; top:120px;">
        <ul>
          <li v-for="(section, index) in sections" :key="index" class="cursor-pointer">
            <div :class="['circle mb-8 mx-auto', { active: currentSection === index }]">
            </div>
          </li>
        </ul>
      </div>
    </div>

    <div class="w-full">
      <div class="text-box flex-wrap" style="width:140px; position: fixed; top:140px; left: 120px; padding: 12px 24px;">
        {{ sections[currentSection] }}
      </div>
      <div id="section-0" class="section mx-auto" style="width:65%;">
        <WhoWeAre></WhoWeAre>
      </div>
      <div id="section-1" class="section mx-auto" style="width:65%;">
        <OurStory></OurStory>
      </div>
      <div class="w-full" style="background-color: #F7F8FA">
        <div class="section mx-auto" id="section-2" style="width:65%;">
          <CultureAndTradition></CultureAndTradition>
        </div>
      </div>
      <div id="section-3" class="section mx-auto" style="width:65%;">
        <FamousPersons/>
      </div>
      <div id="section-4" class="section mx-auto" style="width:65%;">
        <YouthOrganizations/>
      </div>
      <div id="section-5" class="section mx-auto" style="width:65%;">
        <EducationAndSport/>
      </div>
      <div id="section-6" class="section mx-auto" style="width:65%;">
        <Help/>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<style scoped>
.circle {
  width: 25px;
  height: 25px;
  border: 1px solid #EBEEF0;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: background-color 0.3s ease;
}
.sidebar-text {
  padding: 20px;
  font-size: 14px;
  color: #333;
}
.circle::before {
  content: '';
  width: 10px;
  height: 10px;
  background-color: #575F6C;
  border-radius: 50%;
}

.circle.active {
  border-color: rgba(0, 114, 171, 0.2);
  width: 30px;
  height: 30px;
}

.circle.active::before {
  border: 1px solid rgba(0, 114, 171, 0.25);
  background-color: #0072AB;
}
.text-box {
  background-color: #ffff;
  border: 1px solid #E0E3E8;
  border-radius: 8px;
  font-size: 16px;
  color: #575F6C;
  font-weight: 500;
  text-align: center;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
</style>