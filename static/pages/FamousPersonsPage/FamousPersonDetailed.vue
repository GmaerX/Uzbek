<script>
import FooterPage from "@/components/Footer.vue";
import MainHeader from "@/components/Header.vue";
import MainPage from "@/pages/MainPage/MainPage.vue";

export default {
  name: "FamousPersonDetailed",
  components: {MainPage, FooterPage, MainHeader},
  methods: {
    closeModal() {
      this.$router.push('/famous-persons')
    },
  },
}
</script>

<template>
  <div class="flex flex-col h-screen w-full">
    <header class="w-full">
      <main-header/>
    </header>
    <div class="w-full flex-grow overflow-auto">
      <div class="fixed top-0 left-0 bg-black w-full h-full opacity-70" style="z-index: 20" @click="closeModal"></div>
      <div class="bg-white fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 rounded" style="z-index: 30">
        <div class="flex">
          <div style="padding: 64px 40px" class="flex-shrink-0">
            <img src="@/assets/images/img_1.png" class="rounded">
          </div>
          <div class="p-6 w-full flex flex-col">
            <div class="w-full flex justify-end">
              <button @click="closeModal">
                <span style="color:#0072AB; font-size: 20px">
                  X
                </span>
              </button>
            </div>
            <div>
              <p class="font-gilroy" style="font-weight: 500; font-size: 40px; line-height: 52px">Пулатов Шерзод Аббозович</p>
              <span style="color:#575F6C" class="text-base leading-8">Председатель, член АНК, член НЭС АНК</span>
            </div>
            <div class="mt-8 overflow-y-auto h-full">
                <span>
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias, blanditiis commodi dolores ea ex exercitationem fugit impedit nesciunt, nisi obcaecati odio possimus quisquam recusandae reiciendis repellat sed sequi suscipit voluptatibus.
                </span>
                </div>
          </div>
        </div>
      </div>
    </div>
    <footer class="w-full">
      <FooterPage></FooterPage>
    </footer>
  </div>
</template>

<style scoped>

</style>