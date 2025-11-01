<template>
  <div class="flex flex-col items-center justify-center overflow-y-scroll">
    <h2 class="text-3xl font-bold">hey user</h2>
    <p>upcoming hackathons</p>
    <p>find new hackathons button</p>
    <p>idk</p>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  requiresAuth: true,
  redirectIfAuth: false,
  layout: "dashboard"
});
</script>

<style scoped></style>
