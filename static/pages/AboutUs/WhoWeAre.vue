<script>
import SideBar from "@/pages/MainPage/SideBar.vue";

export default {
  name: "WhoWeAre",
  components: {SideBar},
  data() {
    return {
      page: "01",
    };
  },
}
</script>

<template>
  <div style="padding: 80px 0">
    <h2 class="font-gilroy mb-10" style="font-weight: 500; font-size: 40px">
        Кто мы?
      </h2>
      <p style="color: #575F6C;" class="text-base leading-8">
        Идея создания и разработка данного Портала принадлежит председателю узбекского этнокультурного центра города Астана Ш.Пулатову при непосредственной поддержки спонсоров и партнеров из числа ниже указанных компаний и организаций. Отельную благодарность выражаем этнокультурному центру города Алматы в лице председателя А.Исматуллаева за поддержку и выражение солидарности в воплощении данной инициативы.
      </p>
  </div>
</template>

<style scoped>
</style>