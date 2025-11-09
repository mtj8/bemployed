<template>
  <div class="flex flex-col items-start justify-start gap-6 overflow-y-scroll p-10">
    <h3 class="text-3xl font-bold">Dashboard</h3>

    <div class="flex w-full items-start justify-between gap-6">
      <div class="flex grow flex-col items-center justify-center gap-6">
        <DashboardHackathonCard v-for="hackathon in currentHackathons.slice(0, 5)" :key="hackathon.uuid" :hackathon="hackathon" />
      </div>

      <div class="flex w-72 shrink-0 flex-col items-center justify-center gap-6">
        <div class="bg-bg-darker flex h-82 w-full flex-col items-center justify-start gap-2 rounded-lg p-2">
          <NuxtLink
            :to="`/profile/${friend.uuid}`"
            class="bg-bg-base hover:bg-bg-lighter flex w-full items-center justify-start gap-3 rounded-lg px-4 py-2 transition"
            v-for="friend in friends.slice(0, 5)"
            :key="friend.uuid"
          >
            <UserProfileCircle :gradient="friend.profileGradient" />

            <div class="flex flex-col items-start justify-center">
              <p class="">{{ friend.displayName }}</p>
              <p class="text-text-lighter text-xs">@{{ friend.username }}</p>
            </div>
          </NuxtLink>
        </div>

        <div class="bg-bg-darker h-20 w-full"></div>
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
