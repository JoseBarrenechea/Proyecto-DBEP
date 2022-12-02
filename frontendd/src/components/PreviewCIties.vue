<template>
<li><div>
    <img src="{{ image }}" alt="" /><br>
    <a> {{name}}</a>
    <a> of {{ country }}</a>
    <a> {{ visits }}</a>
</div></li>
</template>

<script>
export default {
    name: "PreviewCities",
    props: [
      "name",
      "country",
      "visits",
      "image"
    ]
}
</script>

<style scoped>

  a {
    width: 100%;
    font: 30px sans-serif;
    display: grid;
    place-content: center;
  }

  li {
    list-style: none;
    margin: 0 80px 0 80px;
  }

  img { height: 340px; }

  div {
    border-radius: 30px;
    background-color: white;
  }

</style>