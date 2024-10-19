<script>
import MainPage from "@/pages/MainPage/MainPage.vue"
import MainHeader from "@/components/Header.vue";
import FooterPage from "@/components/Footer.vue";
export default {
  name: "FullPage",
  components: {FooterPage, MainHeader, MainPage}
}
</script>

<template>
  <div class="flex flex-col h-screen w-full">
    <header class="w-full">
      <main-header/>
    </header>
    <div class="w-full flex-grow overflow-auto">
<!--    <MainPage />-->
      <transition name="fade" mode="out-in">
        <router-view />
      </transition>
      <footer class="w-full">
        <FooterPage></FooterPage>
      </footer>
    </div>
  </div>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>