<script>
import SideBarText from "@/components/SideBarText.vue";

export default {
  name: "ContactsPage",
  components: {SideBarText},
  data(){
    return {
      title: "Контакты"
    }
  }
}
</script>

<template>
  <div class="w-full relative" style="padding: 64px 0">
    <div class="h-full absolute top-0 left-0">
      <SideBarText :title="title"/>
    </div>
    <div class="mx-auto cursor-pointer " style="width:65%; margin-bottom: 40px;">
      <div class="w-full grid grid-cols-2" style="border-radius: 8px; border: 1px solid #EBEEF0;overflow: hidden">
        <router-link
            to="/contacts/republic-contacts"
            class="item"
            :class="{ active: $route.path === '/contacts/republic-contacts' }">Республиканские Контакты</router-link>

        <router-link
            to="/contacts/regions-contacts"
            class="item"
            :class="{ active: $route.path === '/contacts/regions-contacts' }">региональные контакты</router-link>

      </div>
    </div>
    <div class="mx-auto" style="width:65%">
      <router-view></router-view>
    </div>
  </div>
</template>

<style scoped>
.item {
  @apply py-2.5 px-6 text-base mx-auto w-full text-center uppercase;
  font-weight: 500;
}
.item + .item {
  border-left: 1px solid #EBEEF0
}
.active {
  background-color: #0072AB;
  color: white;
}
</style>