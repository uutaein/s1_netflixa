<template>
  <v-flex>
  <v-carousel hide-delimiters style="box-shadow: 0px 0px">
    <v-carousel-item v-for="i in 2" :key="i">
      <v-layout row>
        <v-flex sm4 v-for="j in 6" :key="j" pl-2 pr-2>
          <v-card>
            <v-img
              src="https://cdn.vuetifyjs.com/images/cards/desert.jpg"
              aspect-ratio="0.8"
            ></v-img>
            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-0">Card {{i}}-{{j}}</h3>
                <div> Card text </div>
              </div>
            </v-card-title>
          </v-card>
        </v-flex>
      </v-layout>
    </v-carousel-item>
  </v-carousel>
</v-flex>
</template>

<script>
export default {

}
</script>

<style>

</style>
