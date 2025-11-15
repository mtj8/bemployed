<template>
  <div class="flex flex-col items-start justify-start gap-6 overflow-y-scroll p-10">
    <h3 class="text-3xl font-bold">Dashboard</h3>

    <div class="flex w-full items-start justify-between gap-6">
      <div class="flex grow flex-col items-center justify-center gap-6">
        <DashboardHackathonCard v-for="hackathon in currentHackathons.slice(0, 5)" :key="hackathon.uuid" :hackathon="hackathon" />
      </div>

      <div class="flex w-72 shrink-0 flex-col items-center justify-center gap-6">
        <div class="bg-bg-darker flex h-82 w-full flex-col items-center justify-start gap-2 rounded-lg p-2">
          <DashboardFriendCard v-for="friend in friends.slice(0, 5)" :key="friend.uuid" :friend="friend" />
        </div>

        <NuxtLink class="bg-bg-darker w-full rounded-lg px-8 py-3 text-lg font-semibold" to="/hackathons">Find Hackathons</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  requiresAuth: true,
  redirectIfAuth: false,
  layout: "dashboard"
});

const userStore = useUserStore();
const { currentHackathons, friends } = storeToRefs(userStore);
</script>

<style scoped></style>
