<template>
  <div class="bg-bg-darker flex h-full w-72 shrink-0 flex-col items-center justify-between px-3 pt-5 pb-3">
    <div class="flex w-full flex-col items-center justify-center gap-1">
      <SidebarPageLink v-for="link in pageLinks" :key="link.path" :link="link" :is-active="route.path === link.path" />
    </div>

    <div class="my-4 h-1 w-full rounded-full bg-neutral-700"></div>

    <div class="mb-5 h-full w-full overflow-y-scroll"></div>

    <SidebarUserCard />
  </div>
</template>

<script setup lang="ts">
const route = useRoute();
const router = useRouter();

const userStore = useUserStore();
const { currentHackathons } = storeToRefs(userStore);

const pageLinks = [
  {
    name: "Dashboard",
    icon: "/icons/bonfire.svg",
    path: "/home"
  },
  {
    name: "Past Hackathons",
    icon: "/icons/calendar.svg",
    path: "/profile/history"
  },
  {
    name: "Friends",
    icon: "/icons/people.svg",
    path: "/profile/friends"
  }
] as const satisfies SidebarLink[];
</script>

<style scoped></style>
