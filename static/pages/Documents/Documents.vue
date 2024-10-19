<script>
import List from "@/pages/Documents/List.vue";
import Projects from "@/pages/Documents/Projects.vue";

export default {
  name: "Documents",
  components: {Projects, List}
}
</script>

<template>
<div>
  <List/>
  <Projects/>
</div>
</template>

<style scoped>

</style>