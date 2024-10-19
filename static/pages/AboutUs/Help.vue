<script>
import PrevBtn from "@/components/buttons/prevBtn.vue";
import NextBtn from "@/components/buttons/nextBtn.vue";

export default {
  name: "Help",
  components: {NextBtn, PrevBtn}
}
</script>

<template>
  <div class="w-full" style="padding: 0 0 80px">
    <div class="flex" style="border: 1px solid #EBEEF0; border-radius:8px">
      <div class="w-full p-16" style="">
        <p class="font-gilroy mb-6" style="font-weight: 500; font-size: 40px">
          Помощь нуждающимся
        </p>
        <p class="leading-8 text-base" style="color: #575F6C">
          Благотворительные инициативы общества собирают с каждым разом всё больше участников, которые приносят лекарства, одежду, продукты, игрушки. Эти простые вещи обладают добавочной ценностью — они несут в себе тепло, заботу и стремление облегчить и украсить жизнь людей, находящихся в трудной жизненной ситуации.
        </p>
        <div class="mt-10 flex justify-between">
          <button class="uppercase font-medium text-base py-4 px-6 text-white" style="border-radius: 6px; border: 1px solid #CFD3DA; background-color: #0072AB">подробнее</button>
          <div class="flex gap-6 items-center">
            <prev-btn/>
            <next-btn/>
          </div>
        </div>
      </div>
      <div class="w-full" style="">
        <img src="@/assets/images/img_2.png" class="w-full h-full">
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>