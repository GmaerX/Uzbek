<script>
import NextBtn from "@/components/buttons/nextBtn.vue";
import PrevBtn from "@/components/buttons/prevBtn.vue";
import GalleryItem from "@/pages/PressCenter/GalleryItem.vue";

export default {
  name: "Interview",
  components: {GalleryItem, PrevBtn, NextBtn},
  methods: {
    goToYoutube() {
      window.open('https://www.youtube.com/watch?v=qGSx8ZsGYGI&ab_channel=%D0%9A%D0%B8%D0%BD%D0%BE%D0%BF%D0%BE%D0%B8%D1%81%D0%BA', '_blank');
    }
  }
}
</script>

<template>
  <div style="padding: 0 0 80px 0" class="flex">
    <div class="w-full">
      <h2 class="font-gilroy mb-6" style="font-weight: 500; font-size: 40px">
        Интервью
      </h2>
      <p style="color:#575F6C" class="mb-6 leading-8">
        Благотворительные инициативы общества собирают с каждым разом всё больше участников, которые приносят лекарства, одежду, продукты, игрушки. Эти простые вещи обладают добавочной ценностью — они несут в себе тепло, заботу и стремление облегчить и украсить жизнь людей, находящихся в трудной жизненной ситуации.
      </p>
      <span style="color:#575F6C; font-style: italic">
        Пулатов Шерзод Аббозович
      </span>
      <div class="flex gap-4 items-center justify-between mt-10">
        <button class="px-6 py-2.5 rounded text-white font-medium" style="background-color: #0072AB" @click="goToYoutube">Посмотреть</button>
        <div class="flex items-center gap-6">
          <prev-btn/>
          <next-btn/>
        </div>
      </div>
    </div>
    <div class="w-full h-full overflow-hidden" style="margin-left: 188px; border-radius: 8px">
      <img src="@/assets/images/img_4.png" alt="" class="w-full">
    </div>
  </div>
</template>

<style scoped>

</style>