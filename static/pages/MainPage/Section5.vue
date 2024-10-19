<script>
import SideBar from "@/pages/MainPage/SideBar.vue";
import moreDetail from "@/components/buttons/moreDetail.vue";
export default {
  name: "Section5",
  components: {moreDetail, SideBar},
  data() {
    return {
      page: "05",
      title:"узнать больше",
    }
  }
}
</script>

<template>
  <div class="w-full flex">
    <div>
      <SideBar :page="page"/>
    </div>
    <div class="w-full" style="padding: 80px 0 80px 188px;">
      <div style="width: 1224px; padding-bottom: 40px" class="flex justify-between">
        <h2 class="font-gilroy" style="font-size: 40px; line-height: 52px; font-weight: 500">Этнокультурный центр узбеков Казахстана</h2>
        <router-link to="/regions/guide">
          <moreDetail :title="title"/>
        </router-link>
      </div>
      <div class="relative bg-blue-50" style="width: 1224px; height: 940px">
        <div class="absolute top-0 left-0">
          <p class="text-sm" style="color: #575F6C">Sed ut perspiciatis unde omnis iste natus error sit <br> voluptatem accusantium doloremque laudantium,<br> totam rem aperiam.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>