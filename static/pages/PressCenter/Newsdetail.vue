<script>
import VideoMaterial from "@/pages/PressCenter/VideoMaterial.vue";

export default {
  name: "Newsdetail",
  components: {VideoMaterial},
  props: ['id'],
  data() {
    return {
      newsId: null,
      newsItem: null
    };
  },
}
</script>

<template>
<div class="w-full flex justify-center py-20">
  <div class="section mx-auto" style="width:65%;">
    <div class="flex mb-12">
      <span class="route">Главная</span>
      <span class="mx-4 route">/</span>
      <span class="route">НОВОСТИ</span>
      <span class="mx-4 route">/</span>
      <span class="text-base uppercase" style="letter-spacing:2px; width:190px;white-space: nowrap;overflow: hidden;text-overflow: ellipsis; font-weight: 500">Шавкат Мирзиёев лично поздравил с победой таэквондиста Улугбека Рашитова и боксера Хасанбоя Дусматова — видео</span>
    </div>
    <div class="w-full flex justify-between">
      <div class="flex flex-col gap-y-10 w-full" style="margin-right: 128px">
        <div>
          <img src="@/assets/images/img_3.png" alt="" class="rounded w-full">
        </div>
        <div>
          <h3 class="font-gilroy" style="font-weight: 500; font-size: 40px; line-height: 52px">
            Шавкат Мирзиёев лично поздравил с победой таэквондиста Улугбека Рашитова и боксера Хасанбоя Дусматова — видео
          </h3>
        </div>
        <div>
          <p>
            Глава государства поговорил с таэквондистом Улугбеком Рашитовым и боксером Хасанбоем Дусматовым, которые завоевали золотые медали на Олимпиаде в Париже.
            <br><br>
            Президент горячо поздравил спортсменов и с большим удовлетворением отметил, что завоевание нашей сборной двух золотых олимпийских медалей за один день стало историческим событием для узбекского спорта. Шавкат Мирзиёев также подчеркнул, что смелые и уверенные выступления наших ребят, их высокое мастерство и мужество стали примером подлинного героизма, показали, на что способна молодежь Нового Узбекистана, придали огромную силу и чувство гордости народу. Президент выразил признательность их тренерам, родителям и близким.
            <br><br>
            В свою очередь Улугбек Рашитов и Хасанбой Дусматов искренне поблагодарили главу государства за особое внимание и высокое доверие, за условия, созданные для спортсменов, и заявили, что посвящают свои победы Новому Узбекистану.
          </p>
        </div>
        <div class="flex items-center justify-between">
          <button class="rounded text-white font-medium uppercase px-3 py-2" style="background-color: #0072AB">Олимпиада</button>
          <p style="color:#575F6C" class="text-base uppercase font-medium">Вчера 22:13</p>
        </div>
      </div>
      <div style="width: 35%">
        <p class="font-gilroy mb-10" style="font-weight: 500; font-size: 32px; line-height: 38px">Другие новости</p>
        <video-material/>
        <video-material class="mt-6"/>
        <video-material class="mt-6"/>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped>
.route {
  color: #CFD3DA;
  font-weight: 500;
  @apply uppercase;
}
</style>