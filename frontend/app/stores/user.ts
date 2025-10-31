export const useUserStore = defineStore("userStore", () => {
  const user = ref<User>();
  const isAuth = ref(false);

  const friends = ref<User[]>([]);
  const currentHackathons = ref<Hackathon[]>([]);

  return { user, isAuth, friends, currentHackathons };
});
