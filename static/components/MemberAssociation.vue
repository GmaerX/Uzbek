<script>
import MainHeader from "@/components/Header.vue";
import FooterPage from "@/components/Footer.vue";
import MainPage from "@/pages/MainPage/MainPage.vue";

export default {
  name: "MemberAssociation",
  components: {MainPage, FooterPage, MainHeader},
  methods: {
    closeModal() {
      this.$router.push('/')
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
      <div class="bg-white fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 p-6" style="z-index: 30; border-radius: 8px; overflow: hidden">
        <div class="w-full flex justify-end">
          <button @click="closeModal" class="text-base uppercase" style="color:#0072AB">x</button>
        </div>
        <h2 class="font-gilroy" style="font-weight: 500; font-size: 40px; line-height: 52px">
          Хотите стать членом нашей Ассоциации?
        </h2>
        <p style="color:#575F6C" class="text-base leading-8">
          Заполните все формы ниже, и отправьте заявку.
        </p>
        <div class="mt-8">
          <form class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- ФИО -->
            <div>
              <label class="label" for="name">ВАШЕ ФИО:</label>
              <input type="text" id="name" class="w-full border border-gray-300 rounded p-2 bg-white" value="ПУЛАТОВ ШЕРЗОД АББОЗОВИЧ" readonly>
            </div>

            <!-- Дата Рождения -->
            <div>
              <label class="label" for="dob">ДАТА РОЖДЕНИЯ:</label>
              <input type="text" id="dob" class="w-full border border-gray-300 rounded p-2 bg-white" value="20.10.1000" readonly>
            </div>

            <!-- ИИН -->
            <div>
              <label class="label" for="iin">ВАШ ИИН:</label>
              <input type="text" id="iin" class="w-full border border-gray-300 rounded p-2 bg-white" value="2314123123123" readonly>
            </div>

            <!-- Телефон -->
            <div>
              <label class="label" for="phone">ВАШ ТЕЛЕФОН НОМЕР:</label>
              <input type="text" id="phone" class="w-full border border-gray-300 rounded p-2 bg-white" value="+77777777" readonly>
            </div>
          </form>
        </div>
      </div>
    </div>
    <footer class="w-full">
      <FooterPage></FooterPage>
    </footer>
  </div>
</template>

<style scoped>
.label {
  font-weight: 500;
  font-size: 16px;
  line-height: 23px;
  letter-spacing: 2px;
}
</style>