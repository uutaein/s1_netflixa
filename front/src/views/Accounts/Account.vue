<template>
  <div>
    <v-container text-center>
      <v-row>
        <v-col cols="4">
          <v-card
            class="pt-12"
            height='88vh'>
          <v-avatar
            class="profile"
            color="grey"
            size="200"
            tile
          >
            <v-img centered src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
          </v-avatar>
              <v-list-item-content>
              <v-list-item-title class="title">Marcus Obrien</v-list-item-title>
              <v-list-item-subtitle>Network Engineer</v-list-item-subtitle>
            </v-list-item-content>
          </v-card>

        </v-col>
        <v-col cols="8">
          <v-card height='88vh'>

          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {

}
</script>

<style>
   #landing-page {
     /*background-image: url('../assets/hands_joined_team.jpeg');*/
    background-color: #8f2c2c;
    height: 100vh;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;
  }
</style>
