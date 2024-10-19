<template>
  <div class="slider-logo flex">
    <div class="logos gap-10">
      <img src="@/assets/icons/logo1.svg" alt="Logo 7" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'AutoCarousel',
  data() {
    return {
      items: [
        { src: require('@/assets/icons/logo1.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo2.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo3.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo4.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo5.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo6.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo7.svg'), alt: 'Logo 7' },
        { src: require('@/assets/icons/logo8.svg'), alt: 'Logo 7' },
      ],
    };
  },
};
</script>

<style scoped>
.logos {
}
img {
  width: 100%;
  max-width: 120px;
}
</style>
