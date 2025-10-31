<template>
  <RouterLink :to="link.path" class="hover:bg-bg-lighter flex w-full items-center justify-start gap-2 rounded-lg px-3 py-2.5 transition" :class="{ 'bg-neutral-700 hover:bg-neutral-700!': isActive }">
    <img class="size-6" :src="link.icon" aria-hidden="true" />
    <p>{{ link.name }}</p>
  </RouterLink>
</template>

<script setup lang="ts">
const props = defineProps<{
  link: SidebarLink;
  isActive: boolean;
}>();
</script>

<style scoped></style>
