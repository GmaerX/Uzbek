<script>
import SideBar from "@/pages/MainPage/SideBar.vue";
import moreDetail from "@/components/buttons/moreDetail.vue"

export default {
  name: "Section2",
  components: {SideBar, moreDetail},
  data () {
    return {
      page: "02",
      title:"подробнее"
    }
  },
  methods: {
    GotoAboutUs(){
      this.$router.push({ name: 'AboutUs' });
    },
  }
}
</script>

<template>
  <div class="w-full flex">
    <div>
      <SideBar :page="page" :icon="false"/>
    </div>
    <div class="w-full" style="padding-left: 188px">
      <div class="py-16 border-0 border-t border-solid border-gray-200" style="width: 75%">
        <div style="margin-bottom: 72px">
          <h2 class="font-gilroy" style="font-size: 40px; font-weight: 500; padding-bottom: 56px">О нас</h2>
          <div class="flex gap-10">
            <div class="w-1/2" style="color: #575F6C">
              Идея создания и разработка данного Портала принадлежит председателю узбекского этнокультурного центра города Астана Ш.Пулатову при непосредственной поддержки спонсоров и партнеров из числа ниже указанных компаний и организаций. Отельную благодарность выражаем этнокультурному центру города Алматы в лице председателя А.Исматуллаева за поддержку и выражение солидарности в воплощении данной инициативы.
            </div>
            <div class="w-1/2" style="color: #575F6C">Единый Портал Узбеков Казахстана создан под эгидой Ассамблеи народа Казахстана с целью продвижения деятельности узбекских этнокультурных объединений всех уровней, в том числе Ассоциации этнокультурных общественных объединений узбеков РК "Дустлик".</div>
          </div>
        </div>
        <div>
          <moreDetail :title="title" @click="GotoAboutUs"/>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>