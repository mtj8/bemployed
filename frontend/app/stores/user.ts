export const useUserStore = defineStore("userStore", () => {
  const user = ref<User>();
  const isAuth = ref(false);

  return { user, isAuth };
});
