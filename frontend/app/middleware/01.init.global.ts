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
    uuid: "fuck-fuck-fuck-fuck",
    displayName: "XxX_LeetCoder_XxX",
    username: "l33tcoder",
    email: "l33tcoder@gmail.com",
    school: "Monsters University",
    level: 2,
    xp: 67
  };
  userStore.currentHackathons = [
    {
      uuid: "1111-1111-1111-1111",
      name: "2026 Annual MIT Hackathon",
      description: "the best ever",
      startDate: 1700000000,
      endDate: 1700086400,
      participants: 152
    },
    {
      uuid: "2222-2222-2222-2222",
      name: "Hack the North 2026",
      description: "hack the north",
      startDate: 1700500000,
      endDate: 1700586400,
      participants: 301
    },
    {
      uuid: "3333-3333-3333-3333",
      name: "2026 Global Hackathon",
      description: "go global",
      startDate: 1701000000,
      endDate: 1701086400,
      participants: 507
    },
    {
      uuid: "4444-4444-4444-4444",
      name: "Startup Weekend 2026",
      description: "build a startup",
      startDate: 1701500000,
      endDate: 1701586400,
      participants: 212
    },
    {
      uuid: "5555-5555-5555-5555",
      name: "Code for Good 2026",
      description: "code for a cause",
      startDate: 1702000000,
      endDate: 1702086400,
      participants: 253
    },
    {
      uuid: "6666-6666-6666-6666",
      name: "AI Innovators Hackathon 2026",
      description: "innovate with AI",
      startDate: 1702500000,
      endDate: 1702586400,
      participants: 413
    },
    {
      uuid: "7777-7777-7777-7777",
      name: "GreenTech Hackathon 2026",
      description: "hack for the planet",
      startDate: 1703000000,
      endDate: 1703086400,
      participants: 186
    },
    {
      uuid: "8888-8888-8888-8888",
      name: "HealthTech Hackathon 2026",
      description: "tech for health",
      startDate: 1703500000,
      endDate: 1703586400,
      participants: 229
    }
  ];

  if (!userStore.isAuth && to.meta.requiresAuth) return await navigateTo("/login", { redirectCode: 301 });
  else if (userStore.isAuth && to.meta.redirectIfAuth) return await navigateTo("/home", { redirectCode: 301 });
});
