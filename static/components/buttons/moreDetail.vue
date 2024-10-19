<script>
export default {
  props:{
    title:{
      type: String,
      required: true
    }
  },
  name: "mareDetail",
}
</script>

<template>
  <div>
    <button class="uppercase text-base flex items-center gap-6" style="color: #0072AB">
      <div style="font-weight: 500; letter-spacing: 1.5px">{{ title }}</div>
      <div class="flex items-center">
        <svg width="45px" height="45px" viewBox="-2.4 -2.4 28.80 28.80" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#0072AB" transform="rotate(0)">
          <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
          <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round" stroke="#CFD3DA" stroke-width="0.096"></g>
          <g id="SVGRepo_iconCarrier">
            <path d="M11 16L15 12M15 12L11 8M15 12H3M4.51555 17C6.13007 19.412 8.87958 21 12 21C16.9706 21 21 16.9706 21 12C21 7.02944 16.9706 3 12 3C8.87958 3 6.13007 4.58803 4.51555 7" stroke="#0072AB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
          </g>
        </svg>
      </div>
    </button>
  </div>
</template>

<style scoped>

</style>