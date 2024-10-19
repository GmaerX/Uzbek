<script>
export default {
  name: "FamousPersonItem",
  methods:{
    PersonDetail() {
      this.$router.push({ name: 'person-detail' })
    },
  }
}
</script>

<template>
<div style="border: 1px solid #EBEEF0; border-radius: 8px; overflow: hidden;" class="flex">
  <div style="width: 15%">
    <img src="@/assets/images/img_1.png" alt="" class="w-full h-full">
  </div>
  <div style="padding: 0 60px" class="flex items-center w-full">
    <div>
      <p class="font-gilroy" style="font-weight: 500; font-size: 32px; line-height: 38px">Пулатов Шерзод Аббозович</p>
      <span class="text-lg" style="color:#575F6C">Председатель, член АНК, член НЭС АНК</span>
      <div class="mt-6">
        <button @click="PersonDetail" class="uppercase font-medium text-base py-2.5 px-4 text-white" style="border-radius: 6px; border: 1px solid #CFD3DA; background-color: #0072AB">подробнее</button>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>