import tailwindcss from "@tailwindcss/vite";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
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
      title: "free jobs",
      meta: [
        { charset: "UTF-8" },
        { name: "viewport", content: "width=device-width, initial-scale=1.0" },
        { name: "mobile-web-app-capable", content: "yes" },
        { property: "og:title", content: "free jobs" },
        { property: "og:site_name", content: "free jobs llc" },
        { property: "og:type", content: "website" },
        { name: "description", content: "i want a job too" },
        { property: "og:description", content: "i want a job too" }
      ],
      // link: [{ rel: "icon", type: "image/png", href: "/seagull.png" }],
      htmlAttrs: {
        lang: "en"
      }
    }
  }
});
