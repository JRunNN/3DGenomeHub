<template>
    <n-card content-style="padding: 20px">
        <n-carousel show-arrow autoplay>
            <div>
                <p>sdds</p>
                <img class="carousel-img" src="../../assets/GM12878_tracks.jpg">

            </div>
            <!-- <img class="carousel-img" src="https://naive-ui.oss-cn-beijing.aliyuncs.com/carousel-img/carousel2.jpeg">
            <img class="carousel-img" src="https://naive-ui.oss-cn-beijing.aliyuncs.com/carousel-img/carousel3.jpeg">
            <img class="carousel-img" src="https://naive-ui.oss-cn-beijing.aliyuncs.com/carousel-img/carousel4.jpeg"> -->
            <template #arrow="{ prev, next }">
                <div class="custom-arrow">
                    <button type="button" class="custom-arrow--left" @click="prev">
                        <svg class="w-[16px] h-[16px] text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5H1m0 0 4 4M1 5l4-4"/>
  </svg>
                    </button>
                    <button type="button" class="custom-arrow--right" @click="next">
                        <svg class="w-[16px] h-[16px] text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
  </svg>
                    </button>
                </div>
            </template>
            <template #dots="{ total, currentIndex, to }">
                <ul class="custom-dots">
                    <li v-for="index of total" :key="index" :class="{ ['is-active']: currentIndex === index - 1 }"
                        @click="to(index - 1)" />
                </ul>
            </template>
        </n-carousel>
    </n-card>
</template>
<script lang="ts" setup>
</script>
<style scoped>
.carousel-img {
  width: 100%;
  height: 448px;
  object-fit: cover;
}

.custom-arrow {
  display: flex;
  position: absolute;
  bottom: 25px;
  right: 10px;
}

.custom-arrow button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  margin-right: 12px;
  /* color: #fff; */
  /* background-color: rgba(255, 255, 255, 0.1); */
  background-color: #00529B; /* a cold, business-like blue */
  color: #FFFFFF; /* white */
  border-width: 0;
  border-radius: 8px;
  transition: background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.custom-arrow button:hover {
    background-color: #003C70; /* a darker shade of blue for distinction */
}

.custom-arrow button:active {
  transform: scale(0.95);
  transform-origin: center;
}

.custom-dots {
  display: flex;
  margin: 0;
  padding: 0;
  position: absolute;
  bottom: 20px;
  left: 20px;
}

.custom-dots li {
  display: inline-block;
  width: 12px;
  height: 4px;
  margin: 0 3px;
  border-radius: 4px;
  background-color: #00529B; /* a cold, business-like blue */
  transition: width 0.3s, background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.custom-dots li.is-active {
  width: 40px;
  background-color: #8B0000; /* deep red, muted to maintain a professional appearance */
}
</style>
