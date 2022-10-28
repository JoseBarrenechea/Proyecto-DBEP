<template>
  <header>
      <h1>Welcome to the site</h1>
      <h5>Sign up for free today</h5>
      <button>Get started</button>
  </header>
  <HelloWorld msg="Aerolinea UTEC"/>
  <HelloWorld msg="Aerolinea UTEC"/>
  <HelloWorld msg="Aerolinea UTEC"/>
</template>

 <!-- tamanio de la ventana: 1920 1080 -->

<script>
import HelloWorld from './components/HelloWorld.vue'
export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>

html {
  background: rgb(243, 229, 128);
  margin: 0px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #50422c;
  background-color: #bddeeb;
  margin-top: 10px;
}

header {
  height: 160px;
  width: 100%;
  position: fixed;
  background-image:
    linear-gradient(to bottom, #e4dddd80 70%, rgb(0, 0, 0, 0) 100%),
    url("./assets/avion.png");
  background-repeat: no-repeat;
  background-size:  50cm 160px;
  background-position: center;
}
</style>
