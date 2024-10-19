<script>
import NextBtn from "@/components/buttons/nextBtn.vue";
import PrevBtn from "@/components/buttons/prevBtn.vue";

export default {
  name: "CultureAndTradition",
  components: {PrevBtn, NextBtn},
  data(){
    return {
      currentSlide: 0,
      images: [
        require('@/assets/images/img.png'),
        require('@/assets/images/img.png'),
        require('@/assets/images/img.png')
      ],
    };
  },
  methods: {
    prevSlide() {
      if (this.currentSlide > 0) {
        this.currentSlide--;
      } else {
        this.currentSlide = this.images.length - 1;
      }
    },
    nextSlide() {
      if (this.currentSlide < this.images.length - 1) {
        this.currentSlide++;
      } else {
        this.currentSlide = 0;
      }
    },
  },
}
</script>

<template>
  <div style="padding: 80px 0;">
    <div style="margin-bottom: 56px" class="w-full flex items-center justify-between">
      <h2 class="font-gilroy" style="font-weight: 500; font-size: 40px">
        Культура и традиция
      </h2>
      <div class="flex gap-4 items-center">
        <prev-btn @click="prevSlide"/>
        <next-btn @click="nextSlide"/>
      </div>
    </div>
    <div class="slider-container mb-14">
      <transition name="fade" mode="out-in">
        <img
            class="w-full h-full rounded"
            :src="images[currentSlide]"
            :key="currentSlide"
            alt="Культура и традиция"
        />
      </transition>
    </div>
    <div>
      <h3 class="font-gilroy mb-10" style="font-size: 40px; font-weight: 500">
        Филиалы “ЕПУК”
      </h3>
      <span style="color: #575F6C" class="text-base leading-8">
        Идея создания и разработка данного Портала принадлежит председателю узбекского этнокультурного центра города Астана Ш.Пулатову при непосредственной поддержки спонсоров и партнеров из числа ниже указанных компаний и организаций. Отельную благодарность выражаем этнокультурному центру города Алматы в лице председателя А.Исматуллаева за поддержку и выражение солидарности в воплощении данной инициативы. <br><br>
        Идея создания и разработка данного Портала принадлежит председателю узбекского этнокультурного центра города Астана Ш.Пулатову при непосредственной поддержки спонсоров и партнеров из числа ниже указанных компаний и организаций. Отельную благодарность выражаем этнокультурному центру города Алматы в лице председателя А.Исматуллаева за поддержку и выражение солидарности в воплощении данной инициативы. <br><br>
        Идея создания и разработка данного Портала принадлежит председателю узбекского этнокультурного центра города Астана Ш.Пулатову при непосредственной поддержки спонсоров и партнеров из числа ниже указанных компаний и организаций. Отельную благодарность выражаем этнокультурному центру города Алматы в лице председателя А.Исматуллаева за поддержку и выражение солидарности в воплощении данной инициативы.
      </span>
    </div>
  </div>
</template>

<style scoped>
.slider-container {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter, .fade-leave-to  {
  opacity: 0;
}
</style>