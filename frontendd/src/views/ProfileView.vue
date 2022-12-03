<template>
  <div id="espace"></div>

  <div class="photo-user"><img  src=""/></div>
  
 <div> {{ name }}</div>
</template>

<script>
export default { 
  name: "ProfileView",
  data() {
    return {
      name: this.$route.params.name
    }
  },
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