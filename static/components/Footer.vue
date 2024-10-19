<script>
export default {
  name: "FooterPage",
  data() {
    return {
      lists: ["О нас", "Регионы", "Документы", "Пресс Центр", "Личности"],
      contents1: ["История","Культура и традиции","Наука и литература","Известные личности","Молодежные организации","Образование"],
      contents2: [],
    }
  },
  methods: {
    openDonate() {
      this.$router.push('/donates')
    }
  }
}
</script>

<template>
<footer class="flex w-full flex-col justify-center items-center gap-2.5" style="padding: 56px 108px; background: #F7F8FA">
  <div class="flex items-start self-stretch" style="gap:56px">
    <div class="flex flex-col items-start gap-10 self-stretch" v-for="list in lists" :key="list.id">
      <div class="flex flex-col items-start gap-6" style="flex: 1 0 0">
        <p class="self-stretch uppercase font-medium">{{list}}</p>
        <div>
          <ul>
            <li v-for="content in contents1" class="flex flex-col items-start gap-4 self-stretch">
              {{content}}
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="flex flex-col items-start gap-6" style="flex: 1 0 0">
      <p class="self-stretch uppercase font-medium">Контакты</p>
      <div>
        <ul>
          <li v-for="content in contents2">
            {{content}}
          </li>
        </ul>
      </div>
    </div>
    <div @click="openDonate">
      донаты
    </div>
  </div>
</footer>
</template>

<style scoped>
p {
  color: #333;
  font-size: 16px;
}
</style>