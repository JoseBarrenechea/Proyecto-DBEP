<template>
  <div id="espace"></div>
  <div class="portada">
    <div class="message">
      ÚNETE CON NOSOTROS Y EXPLORA EL MUNDO<br>
      Cada dia nuevos vuelos disponibles<br>
      s 
    </div>
    <img src="" alt="">
  </div>
  <h1 id="city-visit" style="color:white">Ciudades mas visitadas</h1>
  <br>
  <div class="slider-cuidades">
    <ul>
      <li><div>
          <img src="../assets/logoutec.png" alt="" /><br>
          <a> cuidad1</a>
        </div>
      </li>
      <li><div>
          <img src="../assets/logoutec.png" alt="" /><br>
          <a> cuidad2</a>
        </div>
      </li>
      <li><div>
          <img src="../assets/logoutec.png" alt="" /><br>
          <a> cuidad3</a>
        </div>
      </li>
      <li><div>
          <img src="../assets/logoutec.png" alt="" /><br>
          <a> cuidad4</a>
        </div>
      </li>
      <li><div>
          <img src="../assets/logoutec.png" alt="" /><br>
          <a> cuidad5</a>
        </div>
      </li>
      <li><div>
          <img src="../assets/logoutec.png" alt="" /><br>
          <a> cuidad6</a>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default { name: "TouristPlaces", }
</script>

<style scoped>

  #espace {  height: 4cm; }
  
  /* mensaje de portada */
  .portada {
    display: flex;
    background-color: rgb(0, 255, 238);
    margin: 0 2% 0 2%;
    height: 12cm;
  }

      .message {
        width: 50%;
        display: flex;
        background-color: #1d698f;
        justify-content: center;
        text-align: center;
        align-items: center;
      }

  #city-visit {
    display: grid;
    place-content: center;
    font-size: 40px;
    font-family: sans-serif;
    text-shadow: 2px 3px 0px #898999;
    line-height: 1.2;
  }

  /* mostrar imagenes de ciudades */
  .slider-cuidades {
    margin: 0 2% 40px 2%;
    padding-left: 20px;
    background-color: #898999;
    overflow: hidden;
    height: 500px;
  }

      .slider-cuidades a {
        width: 100%;
        font: 30px sans-serif;
        display: grid;
        place-content: center;
      }

      .slider-cuidades ul {
        margin-top: 50px;
        display: flex;
        animation: change 13s infinite alternate ease-in-out;
      }

      .slider-cuidades li {
        list-style: none;
        margin: 0 80px 0 80px;
      }

      .slider-cuidades img { height: 340px; }

      .slider-cuidades div {
        border-radius: 30px;
        background-color: white;
      }

  @keyframes change {
    0% { margin-left: 0%; }
    25% { margin-left: 0%; }

    75% { margin-left: -150% ;}
    100% { margin-left: -150% ;}
  }
</style>
