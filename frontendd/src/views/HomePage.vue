<template>
  <!-- <h1 class="green">{{ msg }}</h1> -->
  <div style="height: 7cm;"></div>
  <div class="back-content">
    <h1 class="about-us" style="color:black">About us:</h1>

    <div class="content-home-1">
      <div class="descripcion" style="color:black">
        <!-- contenido -->
        UTEC's Airlines es una aerolínea que te permite viajar tanto a nivel nacional como internacional. La finalidad de esta aerolínea es mostrarte y
        poder llevarte a los mejores y hermosos lugares turísticos que existen en Latinoamérica.
      </div>
      <div class="images-present">
        <div id="img-a1">
          <img src="" alt="" />
        </div>
        <div id="img-a2">
          <img src="" alt="" />
        </div>
        <div id="img-a3">
          <img src="" alt="" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default { name: "HomePage", }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .back-content {
    background-color: hsl(240, 2%, 51%, 0.5);
    box-shadow:
       inset 0 -3em 3em rgba(0,0,0,0.1),
             0 0  0 2px rgb(255,255,255),
             1em 1em 1em rgba(0,0,0,0.3);
    border-radius: 10px;
    padding: 30px 0 0 0;
    margin: 0 2% 0 2%;
  }
  .about-us {
    display: grid;
    place-content: center;
    font-size: 55px;
    text-shadow: 2px 3px 0px #898999;
    line-height: 1.2;
  }

  .content-home-1 {
    display: flex;
    margin-bottom: 100px;
  }
      .descripcion {
        margin: 60px 0 60px 90px;
        width: 40%;
        display: grid;
        border-radius: 3px;
        background-color: rgba(189,189,189,0.1);
        font-size: 32px;
        place-content: center;
        padding: 40px 30px 40px 30px;
      }

      .images-present {
        margin: 60px 0px 60px 50px;
        width: 60%;
        height: 400px;
        display: flex;
        padding-top: 30px;
      }

      #img-a1, #img-a2, #img-a3 { 
        background-color: aquamarine;
        width: 200px;
        height: 300px;

        margin: 12px;
      }

</style>
