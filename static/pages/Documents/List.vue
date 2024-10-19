<script>
import NextBtn from "@/components/buttons/nextBtn.vue";
import PrevBtn from "@/components/buttons/prevBtn.vue";
import SideBarText from "@/components/SideBarText.vue";
import FamousPersonItem from "@/pages/FamousPersonsPage/FamousPersonItem.vue";
import DocumentItem from "@/pages/Documents/DocumentItem.vue";

export default {
  name: "List",
  components: {DocumentItem, FamousPersonItem, SideBarText, PrevBtn, NextBtn},
  data(){
    return{
      title:"документы",
      docs:[
        {title: "План ассоциации узбеков РК Дустлик на 2018 год"},
        {title: "План ассоциации узбеков РК Дустлик на 2018 год"},
        {title: "План ассоциации узбеков РК Дустлик на 2018 год"},
        {title: "План ассоциации узбеков РК Дустлик на 2018 год"},
        {title: "План ассоциации узбеков РК Дустлик на 2018 год"},
      ]
    }
  }
}
</script>

<template>
  <div class="w-full relative">
    <div class="h-full absolute top-0 left-0">
      <SideBarText :title="title"/>
    </div>

    <div class="w-full" style="padding: 64px 0">
      <div class="mx-auto" style="width:65%;">
        <p class="font-gilroy mb-20" style="font-weight: 500; font-size: 40px">Важные документы</p>
        <p class="text-base leading-8" style="margin-bottom: 60px; color: #575F6C">Идея создания и разработка данного Портала принадлежит председателю узбекского этнокультурного центра города Астана Ш.Пулатову при непосредственной поддержки спонсоров и партнеров из числа ниже указанных компаний и организаций. Отельную благодарность выражаем этнокультурному центру города Алматы в лице председателя А.Исматуллаева за поддержку и выражение солидарности в воплощении данной инициативы.</p>
        <p class="leading-8 mb-8" style="font-weight: 500; font-size: 32px">Уставы</p>
        <div class="flex flex-col gap-3" style="margin-bottom: 60px">
          <div v-for="doc in docs" :key="doc.id">
            <DocumentItem :title="doc.title" />
          </div>
        </div>
        <p class="leading-8 mb-8" style="font-weight: 500; font-size: 32px">Планы на 2025 год</p>
        <div class="flex flex-col gap-3">
          <div v-for="doc in docs" :key="doc.id">
            <DocumentItem :title="doc.title" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>