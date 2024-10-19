<script>
import SideBar from "@/pages/MainPage/SideBar.vue"
export default {
  name: "Section1",
  components: {SideBar},
  data() {
    return {
      page: "01",
    }
  },
  methods: {
    openModal() {
      this.$router.push('/member-association')
    },
  }
}
</script>

<template>
  <div class="w-full flex">
    <div>
      <SideBar :page="page"/>
    </div>
    <div class="relative w-full">
      <div class="w-full flex justify-end" style="padding: 69px 0">
      <div>
        <img src="@/assets/images/1.png " alt="first">
      </div>
      <div class="ml-1">
        <div class="img-main">
          <img src="@/assets/images/2.png" alt="">
        </div>
        <div class="img-main">
          <img src="@/assets/images/3.png" alt="">
        </div>
        <div class="img-main">
          <img src="@/assets/images/4.png" alt="">
        </div>
      </div>
    </div>
      <div class="absolute top-1/2 transform -translate-y-1/2 backdrop-blur-container" style="padding: 40px 80px; border-radius: 0 8px 8px 0; border-left: 1px solid #0072AB; overflow: hidden;">
        <div class="relative z-10">
          <h1 class="font-gilroy title">
            «Ассоциация этнокультурных <br>
            объединений узбеков Республики <br>
            Казахстан «Дустлик»
          </h1>
          <p class="description">
            Для узбекской общины в Казахстане единство <br>
            это основа нашего общего будущего и залог процветания и развития нашего народа.
          </p>
        </div>
        <div>
          <button @click="openModal" class="join">
            стать членом ассоциации
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.img-main + .img-main {
  @apply mt-1;
}
.backdrop-blur-container {
  background-color: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
}
.title {
  font-size: 40px;
  line-height: 52px;
  font-weight: 500;
}
.description {
  @apply text-sm mt-6 mb-10;
  color:#575F6C;
  line-height: 32px;
}
.join {
  @apply uppercase text-base bg-white hover:bg-gray-50 py-4 px-6;
  border: 1px solid #CFD3DA;
  border-radius: 6px;
  font-weight: 500;
}
</style>