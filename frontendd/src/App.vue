<script>
import { RouterLink, RouterView } from "vue-router";
// import LoginPage from "./views/LoginPage.vue";
// import router from "./router/index.js";

export default {
  name: "App",
  components: {
    RouterLink,
    RouterView,
  },
  data() {
    return {
      loginAsk: false
    };
  },
  // methods: {},
  // created() {
  // },
};

// router.beforeEach((to, from) => {
//   console.log(this.$route.name);
//   // if (from.name === 'login')
//   //   this.$route.name = "login"
// });
</script>

<template>
  <!-- <div v-if="this.$route.name === 'login'"> -->
  <header>
    <div class="options-bar">
      <div id="options-left">
        <ul>
          <li><RouterLink to="/home"><button>Who are we?</button></RouterLink></li>
          <li><RouterLink to="/touristplaces"><button>Tourist Places</button></RouterLink></li>
          <li><button type="submit">Check-in</button></li>
        </ul>
      </div>
      <div id="options-right">
        <ul>
          <li><button type="submit">My profile</button></li> <!-- dependiente-->
          <li><button type="submit">My travels</button></li>
          <!-- <li><RouterLink v-if="login" to="/login"><button @click="login=true">Log in</button></RouterLink></li> -->
          <li><button type="submit" @click="loginAsk=true">Log in</button></li>
        </ul>
      </div>
    </div>

    <div class="present-logo">
      <img id="logoutec" src="./assets/logoutec.png" alt="LogoUtec" />
      <div id="title-on"> UTEC's AIRLINES </div>
    </div>
  </header>

  <div class="transfonde" v-if="loginAsk">
    <div class="box-logging">
      <div style="width:100%;"><button id="close" @click="loginAsk=false" >X</button></div>
      <div id="title-log">Login with our page!</div>
      <div style="clear:both"></div>
      AAAAA

    </div>
  </div>

  <RouterView />

  <footer>
    <ul>
      <li> aaaa</li>
      <li> aaaa</li>
    </ul>
  </footer>
</template>

 <!-- tamanio de la ventana: 1920 1080 -->

<style>

  html, body {
    margin: 0;
    background-image: radial-gradient(circle, #c9f5ff, #dbf6ff, #ebf8ff, #f8fbff, #ffffff); 
  }

    header {
      height: 220px;
      width: 100%;
      position: absolute;
      background-image: url("./assets/avion.png");
      background-repeat: no-repeat;
      background-size:  50.5cm 220px;
      background-position: center;
    }
  
  /* Titulo y logo */
  .present-logo {
    width: 100%;
    display: flex;
    padding: 82px 0 0 40px;
  }

      #logoutec {
        width: 110px;
        opacity: 50%;
        margin-right: 2 0px;
      }

      #title-on {
        font-size: 40px;
        padding: 2% 20px 0 20px;
        margin-bottom: 20px;
        color: white;
      }

  /* Barras de opciones */
  .options-bar {
    background-color: #0f0f2c80;
    width: 100%;
    display: flex;
    position: fixed;
    align-items: center;
  }

      #options-left { width: 70%; }

      #options-right { width: 28%; }

      li {
        display: inline;
        padding-left: 25px;
      }

      button {
        border-color: white;
        font-size: 18px;
        color: white;
        border-radius: 6px;
        background-color: transparent;
      }

  footer {
    background-color: rgb(75, 207, 255);
    padding-top: 5%;
    height: 50px;
  }

  .transfonde {
    background-color: hsl(0, 0%, 0%, 0.5);
    position: fixed;
    overflow: hidden;
    width: 100%;
    height: 100%;
    /* height: 10cm; */
    padding: 8% 20% 10% 15%;
  }
  
      .box-logging {
        background-color: rgb(96, 158, 186);
        height: 15.5cm;
        width: 30cm;
        padding: 5px 5px 5px 5px;
      }

      #close {
        color: black;
        background-color: transparent;
        width: 30px;
        float: right;
        box-shadow: 2px 3px 0px #898999;
        border-radius: 2px;
      }
  
  /* filter: contrast() */
  /* filter: grayscale(0%);   en un click  */
</style>
