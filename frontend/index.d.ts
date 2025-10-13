// https://nuxt.com/docs/guide/directory-structure/pages#typing-custom-metadata

declare module "#app" {
  interface PageMeta {
    /** Whether or not the page requires authentication. */
    requiresAuth: boolean;
    /** If the user is authenticated, whether or not to redirect the user to dashboard. */
    redirectIfAuth: boolean;
  }
}

export {};
