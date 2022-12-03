<template>
  <div id="espace"></div>

  <div class="photo-user"><img  src=""/></div>
 <div>aaa</div>
</template>

<script>
export default { 
  name: "ProfileView",
  props: [
    "name", "lastname"
  ]
}
</script>

<style scoped>

  #espace {  height: 7cm; }
  
  .photo-user {
    margin: 30px 0 0 4.5cm;
    background-color: blueviolet;
    border-radius: 50%;
    height: 300px;
    width: 300px;
  }

</style>