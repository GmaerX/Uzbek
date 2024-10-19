<script>
import Section1 from "@/pages/MainPage/Section1.vue";
import Section2 from "@/pages/MainPage/Section2.vue";
import Section3 from "@/pages/MainPage/Section3.vue";
import Section4 from "@/pages/MainPage/Section4.vue";
import Section5 from "@/pages/MainPage/Section5.vue";
import Section6 from "@/pages/MainPage/Section6.vue";
export default {
  name: "MainPage",
  components: {
    Section6,
    Section5,
    Section4,
    Section3,
    Section2,
    Section1
  }
}
</script>

<template>
  <div class="w-full">
    <Section1 />
    <Section2 />
    <Section3 />
    <Section4/>
    <Section5 />
    <Section6 />
  </div>
</template>

<style scoped>

</style>