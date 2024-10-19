<script>
import NewsList from "@/pages/PressCenter/NewsList.vue";
import Gallery from "@/pages/PressCenter/Gallery.vue";
import SideBarText from "@/components/SideBarText.vue";
import VideoList from "@/pages/AboutUs/VideoList.vue";

export default {
  name: "Education",
  components: {VideoList, SideBarText, Gallery, NewsList},
  data() {
    return {
      title: "Регионы",
    }
  }
}
</script>

<template>
  <div class="w-full relative">
    <div class="h-full absolute top-0 left-0">
      <SideBarText :title="title"/>
    </div>

    <div class="w-full">
      <div class="section mx-auto" style="width:65%;">
        <div style="padding: 80px 0;">
          <div class="slider-container mb-14">
            <img
                class="w-full h-full rounded"
                src="@/assets/images/img.png"
                alt="Культура и традиция"
            />
          </div>
          <div>
            <h3 class="font-gilroy mb-10" style="font-size: 40px; font-weight: 500">
              Образование
            </h3>
            <span style="color: #575F6C" class="text-base leading-8">
        Идея создания и разработка данного Портала принадлежит председателю узбекского этнокультурного центра города Астана Ш.Пулатову при непосредственной поддержки спонсоров и партнеров из числа ниже указанных компаний и организаций. Отельную благодарность выражаем этнокультурному центру города Алматы в лице председателя А.Исматуллаева за поддержку и выражение солидарности в воплощении данной инициативы. <br><br>
        Идея создания и разработка данного Портала принадлежит председателю узбекского этнокультурного центра города Астана Ш.Пулатову при непосредственной поддержки спонсоров и партнеров из числа ниже указанных компаний и организаций. Отельную благодарность выражаем этнокультурному центру города Алматы в лице председателя А.Исматуллаева за поддержку и выражение солидарности в воплощении данной инициативы. <br><br>
        Идея создания и разработка данного Портала принадлежит председателю узбекского этнокультурного центра города Астана Ш.Пулатову при непосредственной поддержки спонсоров и партнеров из числа ниже указанных компаний и организаций. Отельную благодарность выражаем этнокультурному центру города Алматы в лице председателя А.Исматуллаева за поддержку и выражение солидарности в воплощении данной инициативы.
      </span>
          </div>
        </div>
      </div>
      <div class="section mx-auto" style="width:65%;">
        <NewsList/>
      </div>
      <div class="section mx-auto" style="width:65%;">
        <VideoList/>
      </div>
      <div class="section mx-auto" style="width:65%;">
        <Gallery/>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>