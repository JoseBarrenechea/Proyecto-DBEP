<template>
  <div id="espace"></div>
  <div class="transfonde">
    <div class="box-logging">
      <button id="close" @click="login=false" >X</button>
      AAAAA

    </div>
  </div>
</template>

<script>
export default {
    name: "SignUpView"
}
</script>

<style>

  #espace {  height: 5cm; }


  .transfonde {
    background-color: rgb(0, 77, 52);
    position: fixed;
    width: 100%;
    height: 100%;
    /* height: 10cm; */
    padding: 20% 30% 25% 30%;
  }
  
  .box-logging {
    background-color: aquamarine;
    height: 14cm;
  }

  .close { float: right; }
</style>