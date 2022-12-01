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
      // path: "/login",
      // name: "login",
      // component: () => import("../views/LoginPage.vue"),
    },
  ],
});

export default router;