import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [ {
      path: "",
      name: "home1",
      component: () => import("../views/HomePage.vue"),
    }, {
      path: "/home",
      name: "home2",
      component: () => import("../views/HomePage.vue"),
    }, {
      path: "/touristplaces",
      name: "touristplaces",
      component: () => import("../views/TouristPlaces.vue"),
    }, {
      path: "/profile/:name",
      name: "profile",
      component: () => import("../views/ProfileView.vue"),
    },
  ],
});

export default router;