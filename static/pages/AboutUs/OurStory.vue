<script>
import NextBtn from "@/components/buttons/nextBtn.vue";
import PrevBtn from "@/components/buttons/prevBtn.vue";

export default {
  name: "OurStory",
  components: {PrevBtn, NextBtn},
  data() {
    return {
      currentSlide: 0,
      slidesPerView: 3,// Текущий активный слайд
      slides: [
        {
          year: "1995 год",
          description:
              "Общественное объединение «Узбекский национальный культурный центр города Астана»...",
          image: require('@/assets/images/1.png'),
        },
        {
          year: "1996 год",
          description:
              "В этот год центр достиг новых успехов и провел множество мероприятий...",
          image: require('@/assets/images/1.png'),
        },
        {
          year: "1997 год",
          description: "С начала 1997 года началась активная работа с молодёжью...",
          image: require('@/assets/images/1.png'),
        },
        {
          year: "1997 год",
          description: "С начала 1997 года началась активная работа с молодёжью...",
          image: require('@/assets/images/1.png'),
        },
      ],
    };
  },
  methods: {
    scrollLeft() {
      if (this.currentSlide > 0) {
        this.currentSlide--;
      } else {
        this.currentSlide = Math.ceil(this.slides.length / this.slidesPerView) - 1;
      }
      this.updateSliderPosition();
    },
    // Прокрутка вправо
    scrollRight() {
      if (this.currentSlide < Math.ceil(this.slides.length / this.slidesPerView) - 1) {
        this.currentSlide++;
      } else {
        this.currentSlide = 0;
      }
      this.updateSliderPosition();
    },
    // Переход к конкретному слайду
    goToSlide(index) {
      this.currentSlide = index;
      this.updateSliderPosition();
    },
    // Обновление позиции слайдера
    updateSliderPosition() {
      const sliderWidth = this.$refs.slider.offsetWidth / this.slidesPerView;
      this.$refs.slider.style.transform = `translateX(-${this.currentSlide * sliderWidth * this.slidesPerView}px)`;
    },
  },
}
</script>

<template>
  <div class="slider-container">
    <div class="w-full flex items-center justify-between" style="margin-bottom: 56px;">
      <h2 class="font-gilroy slider-title">Наша история</h2>
      <div class="flex gap-4 items-center">
        <prev-btn @click="scrollLeft" />
        <next-btn @click="scrollRight" />
      </div>
    </div>
    <div class="relative overflow-hidden w-full">
      <div class="slider-content flex gap-6 overflow" ref="slider">
        <div class="slide group relative flex" v-for="(slide, index) in slides" :key="index">
          <div>
            <img :src="slide.image" alt="Slide Image" class="w-full h-full object-cover items-center" />
          </div>
          <div style="background-color: #0072AB;" class="overflow-hidden absolute inset-0 opacity-0 group-hover:opacity-80 flex flex-col justify-end items-center text-center transition-opacity duration-500 p-6">
          </div>
          <div class="absolute inset-0 opacity-0 group-hover:opacity-100 flex flex-col justify-end items-center text-center transition-opacity duration-700 p-6">
            <p class="font-gilroy text-start" style="font-size: 24px; font-weight: 500; color: white">{{ slide.year }}</p>
            <span class="text-white mt-2 text-start" style="font-size: 14px">{{ slide.description }}</span>
          </div>
        </div>
      </div>
    </div>
    <div class="flex justify-center mt-8">
      <span
          v-for="(slide, index) in Math.ceil(slides.length / slidesPerView)"
          :key="index"
          :class="['dot', { active: currentSlide === index }]"
          @click="goToSlide(index)"
      ></span>
    </div>
  </div>
</template>



<style scoped>
.slider-container {
  padding: 0 0 80px 0;
  position: relative;
  max-width: 100%;
}

.slider-title {
  font-weight: 500;
  font-size: 40px;
}

.slider-content {
  transition: transform 0.5s ease-in-out;
}

.slide {
  min-width: 33.33%;
  justify-content: space-between;
  align-items: center;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: rgba(0, 0, 0, 0.3);
  margin: 0 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.dot.active {
  background-color: #0072ab;
}
</style>

