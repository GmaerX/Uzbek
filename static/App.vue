<script>
export default {
  computed:{
    isModalRoute() {
      return this.$route.name === 'MemberAssociation';
    },
  }
}
</script>
<template>
  <div>
    <div v-if="!isModalRoute">
      <router-view />
    </div>
    <div v-else>
      <router-view />
    </div>
  </div>
</template>

<style>
</style>
