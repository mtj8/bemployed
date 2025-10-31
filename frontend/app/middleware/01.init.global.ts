export default defineNuxtRouteMiddleware(async (to) => {
  const nuxtApp = useNuxtApp();
  const userStore = useUserStore();

  if (userStore.isAuth && to.meta.redirectIfAuth) return await navigateTo(`/home`, { redirectCode: 301 });

  // * only run on initial page load
  // https://nuxt.com/docs/guide/directory-structure/middleware#when-middleware-runs
  if (!import.meta.client || !nuxtApp.isHydrating || !nuxtApp.payload.serverRendered) return;

  // TODO: add init call
  userStore.isAuth = true;
  userStore.user = {
    uuid: "gweyge98wgh9ew",
    displayName: "XxX_LeetCoder_XxX",
    username: "l33tcoder",
    email: "l33tcoder@gmail.com",
    school: "Monsters University",
    level: 2,
    xp: 67
  };
  userStore.currentHackathons = [
    {
      uuid: "hack1",
      name: "Hackathon One",
      description: "This is the first hackathon.",
      startDate: 1700000000,
      endDate: 1700086400,
      participants: 150
    },
    {
      uuid: "hack2",
      name: "Hackathon Two",
      description: "This is the second hackathon.",
      startDate: 1700172800,
      endDate: 1700259200,
      participants: 100
    }
  ];

  if (!userStore.isAuth && to.meta.requiresAuth) return await navigateTo("/login", { redirectCode: 301 });
  else if (userStore.isAuth && to.meta.redirectIfAuth) return await navigateTo("/home", { redirectCode: 301 });
});
