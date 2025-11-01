import tailwindcss from "@tailwindcss/vite";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  modules: ["@pinia/nuxt"],
  css: ["~/assets/main.css"],
  vite: {
    plugins: [tailwindcss()]
  },
  runtimeConfig: {
    public: {
      backend: ""
    }
  },
  app: {
    head: {
      title: "not discord",
      meta: [
        { charset: "UTF-8" },
        { name: "viewport", content: "width=device-width, initial-scale=1.0" },
        { name: "mobile-web-app-capable", content: "yes" },
        { property: "og:title", content: "not discord" },
        { property: "og:site_name", content: "not discord" },
        { property: "og:type", content: "website" },
        { name: "description", content: "this is NOT discord" },
        { property: "og:description", content: "this is NOT discord" }
      ],
      // link: [{ rel: "icon", type: "image/png", href: "/seagull.png" }],
      htmlAttrs: {
        lang: "en"
      }
    }
  }
});
