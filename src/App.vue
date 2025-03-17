<script setup>
import { computed, onMounted, ref, watch } from 'vue';
import axios from 'axios';


const textField =ref('')
const audioUrl = ref('')

const convertText = async ()=>{
    console.log("button presseed")
    try {
        const response = await axios.post('http://127.0.0.1:5000/api',
            {text :textField.value},
            {responseType:"blob"}
        )
        audioUrl.value = URL.createObjectURL(new Blob([response.data], { type: "audio/mpeg" }));
        console.log("its working")
    }catch (error){
        console.log("You got error",error)
    }
}



</script>

<template>
 

<input type="text" v-model="textField" class=" bg-black text-white">

<button type="submit" @click="convertText" class=" bg-green-200 text-black">Submitt</button>

<a v-if="audioUrl" :href="audioUrl">The Audio url</a>
<audio v-if="audioUrl" :src="audioUrl" controls></audio>

    
    






</template>

