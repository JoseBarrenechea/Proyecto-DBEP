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
      <div style="width:100%;">
        <button type="submit" id="close" @click="loginAsk=false">
          <div class="arrow"></div>
        </button>
      </div><br>
      <h1>Login Airline</h1>
      <form method="post">
        <label for="e">Your email</label>
        <input id="email" type="text" name="e" required="required" />
        <label for="p">Password</label>
        <input type="password" name="p" required="required" />
        <br><br>
        <button if="password" type="submit" class="btn btn-primary btn-block btn-large">Log in!</button>
      </form>
      <div style="clear:both"></div>

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
  /* @import url(https://fonts.googleapis.com/css?family=Open+Sans); */
  
  html, body {
    margin: 0;
    background-image: linear-gradient(to right bottom, #4a657f, #3d5f86, #35588d, #345092, #3b4694, #3f4192, #433b90, #48358e, #45368b, #423788, #3f3785, #3c3882);
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
    padding: 8% 22% 10% 34%;
  }
  
      .box-logging {
        background-image: linear-gradient(to right bottom, #6b4a7f, #5e4d7e, #524f7b, #485077, #405071, #3b4e6f, #364b6e, #31496c, #2d446f, #2b3e71, #2e3772, #332f71);
        height: 15cm;
        width: 15cm;
        padding: 10px 10px 10px 10px;
        position: absolute;
        box-shadow:
          inset 0 -3em 3em rgba(0,0,0,0.1),
                0 0  0 2px rgb(255,255,255),
                1em 1em 1em rgba(0,0,0,0.3);
        border-radius: 30px;
      }

      .box-logging form { padding: 4% 12% 4% 12%;  }

      .arrow {
        width: 10px;
        height: 10px;
        border: 5px solid;
        border-color: white transparent transparent white;
        transform: rotate(-225deg);
      }

      .box-logging h1 {
        color: #fff;
        text-shadow: 0 0 10px rgba(0,0,0,0.3);
        letter-spacing: 1px;
        text-align: center;
      }

      .box-logging input { 
        width: 70%; 
        height: 10px;
        margin-bottom: 30px; 
        background: rgba(50, 172, 225, 0.2);
        /* outline: none; */
        padding: 20px;
        font-size: 20px;
        color: rgb(145, 163, 197);
        border: 3px solid rgb(255, 255, 255);
        border-radius: 8px;
        transition: box-shadow .5s ease;
      }

      .box-logging label {
        color: white;
        font-size: 20px;
      }

      .box-logging input:focus { box-shadow: inset 0 -5px 45px }

      #close {
        color: white;
        background-color: rgba(214, 126, 26, 0.5);
        width: 60px;
        height: 40px;
        float: right;
        border-radius: 10px;
      }

      #close:hover {
        transition: box-shadow .5s ease;
        outline: none;
      }

      .btn {
        display: inline-block;
        *display: inline; 
        margin-bottom: 0; 
        padding: 9px 14px;
        font-size: 20px; 
        width: 100%; display:block;
        line-height: normal; 
        border: 7px solid #eceff4; text-shadow: 1px 1px 1px rgba(0,0,0,0.4); 
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.5);
        background-image: -webkit-linear-gradient(top, #59646a, #2c2f34); 
      }

      .btn:hover { 
        color: #ffff; 
        -decoration: none;
         background-color:#2c2f34;
         background-position: 0 -4px; 
         transition: background-position 0.1s linear;
      }

  /* filter: contrast() */
  /* filter: grayscale(0%);   en un click  */
</style>
