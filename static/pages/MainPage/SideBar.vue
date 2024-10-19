<script>
export default {
  name:"SideBar",
  props: {
    page: String,
    icon: {
      type: Boolean,
      default: true,
    },
    isBackground: {
      type: Boolean,
      default: false
    },
  },
}
</script>
<template>
  <aside class="side-bar" :style="{ backgroundColor: isBackground ? '#0072AB' : 'white' }">
    <p :style="{ color: isBackground ? '#fff' : '#CFD3DA'}" class="font-gilroy">{{ page }}</p>
    <svg width="16" height="89" viewBox="0 0 16 89" fill="none" xmlns="http://www.w3.org/2000/svg" v-if="icon">
      <path d="M7.2929 88.7071C7.68342 89.0976 8.31659 89.0976 8.70711 88.7071L15.0711 82.3431C15.4616 81.9526 15.4616 81.3195 15.0711 80.9289C14.6805 80.5384 14.0474 80.5384 13.6569 80.9289L8 86.5858L2.34315 80.9289C1.95262 80.5384 1.31946 80.5384 0.928936 80.9289C0.538411 81.3195 0.538411 81.9526 0.928936 82.3431L7.2929 88.7071ZM7 4.37114e-08L7 88L9 88L9 -4.37114e-08L7 4.37114e-08Z" :style="{ fill: isBackground ? '#fff' : '#CFD3DA' }"/>
    </svg>
  </aside>
</template>
<style scoped>
.side-bar {
  width: 160px;
  height: 100%;
  padding: 64px 0;
  border-right: 1px solid #EBEEF0;
  @apply flex flex-col justify-between items-center flex-shrink-0 self-stretch;

  p {
    text-align: center;
    font-size: 32px;
    font-weight: 500;
    text-transform: uppercase;
  }
  svg {
    stroke-width: 2px;
  }
}
</style>