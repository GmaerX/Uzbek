<script>
export default {
  name: "SideBarText",
  props:{
    title:'',
    isBackground: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<template>
  <aside class="side-bar" :style="{ backgroundColor: isBackground ? '#0072AB' : 'white' }">
    <p class="font-gilroy mx-auto" :style="{ color: isBackground ? 'white' : '#CFD3DA' }">{{ title }}</p>
  </aside>
</template>

<style scoped>
.side-bar {
  width: 160px;
  height: 100%;
  border-right: 1px solid #EBEEF0;
  position: relative;

  p {
    text-align: center;
    font-size: 32px;
    font-weight: 500;
    text-transform: uppercase;
    writing-mode: vertical-rl;
    margin-bottom: 0;
    position: absolute;
    top: 64px;
    left: 50%;
    transform: translateX(-50%) rotate(180deg);
  }
}
</style>