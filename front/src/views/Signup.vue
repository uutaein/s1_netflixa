
<template>
  <v-app>

      <v-container
      fluid
      >
        <v-row
          justify="center"
        >
          <v-col
            cols="12"
            sm="10"
            md="10"
          >
            <v-card class="mt-12">
              <v-toolbar
                color="primary"
                dark
                flat
              >
                <v-toolbar-title>SignUp</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="username"
                    name="username"
                    prepend-icon="mdi-account"
                    type="text"
                    id="username"
                    v-model="signupData.username"
                  ></v-text-field>

                  <v-text-field
                    id="password1"
                    label="Password"
                    name="password1"
                    prepend-icon="mdi-lock"
                    type="password"
                    v-model="signupData.password1"
                  ></v-text-field>
                  <v-text-field
                    id="password2"
                    label="Password 확인"
                    name="password2"
                    prepend-icon="mdi-lock"
                    type="password"
                    v-model="signupData.password2"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="signup" color="primary">Signup</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

  </v-app>
</template>

<script>
export default {
  name: 'SignupView',
  data () {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null
      }
    }
  },
  methods: {
    signup () {
      this.$emit('submit-signup-data', this.signupData)
    }
  }
}
</script>

<style>

</style>
