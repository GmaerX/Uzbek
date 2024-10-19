<script>
import NextBtn from "@/components/buttons/nextBtn.vue";
import PrevBtn from "@/components/buttons/prevBtn.vue";
import NewsItem from "@/pages/PressCenter/NewsItem.vue";

export default {
  name: "News",
  components: {NewsItem, PrevBtn, NextBtn},
  data() {
    return {
      news: [
        { id: 1, title: "News 1" },
        { id: 2, title: "News 2" },
        { id: 3, title: "News 3" },
        { id: 4, title: "News 4" },
        { id: 5, title: "News 5" },
        { id: 6, title: "News 6" },
      ],
    };
  },
  methods: {
    goToNewsDetail(id) {
      this.$router.push({ name: 'news-detail' }); // Переход на детальную страницу
    }
  }
}
</script>

<template>
  <div style="padding: 80px 0 0 0">
    <div style="margin-bottom: 56px" class="w-full flex items-center justify-between">
      <h2 class="font-gilroy" style="font-weight: 500; font-size: 40px">
        Последние новости
      </h2>
      <div class="flex gap-4 items-center">
        <prev-btn/>
        <next-btn/>
      </div>
    </div>
    <div style="grid-template-columns: repeat(3, 1fr);display: grid" class="gap-y-8 gap-x-6">
      <div v-for="n in news" :key="n.id" class="cursor-pointer" @click="goToNewsDetail(n.id)">
        <NewsItem :title="n.title"/>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>