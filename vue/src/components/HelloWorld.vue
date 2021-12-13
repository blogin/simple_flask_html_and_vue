<template>
  <div class="hello">
    <input type="text" v-model="text">
    <button @click="qqq()">get</button>
    <div>{{res}}</div>
  </div>
</template>

<script>
import Axios from 'axios'
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return{
      text: "",
      res: ""
    }
  },
  methods: {
    qqq(){
      console.log(this.text)
      Axios.post('http://127.0.0.1:5000/', {rrr:this.text})
        .then((resp) => {
          console.log(resp)
          this.res = resp.data
        })
        .catch((error) => {
          console.log("setUserLogin error => ", error);
        })
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
