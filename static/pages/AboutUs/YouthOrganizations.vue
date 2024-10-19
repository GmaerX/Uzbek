<script>
export default {
  name: "YouthOrganizations"
}
</script>

<template>
  <div class="w-full" style="padding: 0 0 80px">
    <h2 class="font-gilroy" style="font-weight: 500; font-size:40px">
      Молодежные организации
    </h2>
    <div class="flex flex-col gap-5">
      <div class="flex gap-5">
        <div class="image-block_1 izo relative group">
          <img src="@/assets/images/img.png" alt="Image 1" style="width: 100%; height: 100%"/>
          <div class="izo-item absolute inset-0 opacity-0 group-hover:opacity-80 flex flex-col justify-end items-center text-center transition-opacity duration-500 p-6">
          </div>
          <div class="absolute inset-0 opacity-0 group-hover:opacity-100 flex flex-col justify-end transition-opacity duration-700 p-6">
            <span class="font-gilroy text-start mb-4" style="font-size: 24px; font-weight: 500; color: white">Организация “Текст”</span>
            <span class="text-white mt-2 text-start mb-6 font-normal" style="font-size: 14px">
              Единый Портал Узбеков Казахстана создан под эгидой Ассамблеи народа Казахстана с целью продвижения деятельности узбекских этнокультурных объединений всех уровней, в том числе Ассоциации этнокультурных общественных объединений узбеков РК "Дустлик".
            </span>
            <div>
              <router-link to="/organization-details">
                <button class="uppercase font-medium text-base py-4 px-6 bg-white" style="border-radius: 6px; border: 1px solid #CFD3DA">подробнее</button>
              </router-link>
            </div>
          </div>
        </div>
        <div class="image-block_1">
          <img src="@/assets/images/img.png" alt="Image 1" style="width: 100%; height: 100%"/>
        </div>
      </div>
      <div class="flex gap-5">
        <div class="image-block_2">
          <img src="@/assets/images/img.png" alt="Image 2" />
        </div>
        <div class="image-block_2">
          <img src="@/assets/images/img.png" alt="Image 3" />
        </div>
        <div class="image-block_2">
          <img src="@/assets/images/img.png" alt="Image 3" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.izo {
  border-radius: 6px;
  width: 288px;
  height: 384px;
  @apply bg-gray-100;

  .izo-item {
    background-color: #0072AB;
  }
}
.image-block_1, .image-block_2 > img {
  @apply rounded h-full w-full;
}
.image-block_1 {
  height: 340px;
  @apply bg-red-200;
}
.image-block_2 {
  height: 390px;
  @apply bg-red-200;
}
</style>