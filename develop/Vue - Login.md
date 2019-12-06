# Vue Login

```html
<template>
  <v-layout class="text-center basic">
    <v-form class="form-signin" @submit.prevent = "userSignIn">
      <img class = "mb-4" src = "@/assets/login.jpg" alt="" width="72" height="72">
      <v-text-field
        name="ID"
        label="ID"
        id="ID"
        type="text"
        v-model="ID"
        class="form-control pa-0"
        required
      ></v-text-field>
      <v-text-field
        name="password"
        label="Password"
        id="password"
        type="password"
        v-model="password"
        required
        class="form-control pa-0"
      ></v-text-field>
      <!-- <div class = "checkbox mb-3">
	  
	  </div> -->
      <v-btn block large color = "grey darken-1" class = "white--text" type="submit">
		  Sign In
      </v-btn>
    </v-form>
  </v-layout>
</template>

<script>
import api from '@/services/Api'
import router from '@/router'
export default {
  name: 'LoginPage',
  data() {
    return {
      ID: '',
      password: ''
    }
  },
  components: {},
  methods: {
    userSignIn() {
      if (this.ID == '' || this.password == '') {
        alert('ID가 입력되지 않았습니다.')
      } else {
        api.Login(this.ID, this.password)
      }
    }
  },
  mounted() {
    console.log(this.$store.state)
  }
}
</script>

<style scoped>

.basic {
  height : 100%;
  display: -ms-flexbox;
  display: -webkit-box;
  display: flex;
  -ms-flex-align: center;
  -ms-flex-pack: center;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
>>>.form-signin > .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
>>>.form-signin > .form-control:focus {
  z-index: 2;
}
>>>.form-signin > .v-input[type="text"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
>>>.form-signin > .v-input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>
```

