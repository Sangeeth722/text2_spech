<script setup>
import { computed, onMounted, ref, watch } from 'vue';
import axios from 'axios';


const language = ref('')
const stationDetails = ref('')
const loading = ref(false)


const getData = async()=>{
    loading.value =true
    
    
    
    try {
        const response = await axios.post('https://radioappbackendpython.onrender.com/api', {tag:language.value})
        stationDetails.value = await response.data
        console.log(stationDetails.value)
        
    }catch(error){
        console.log("get error", error)
    }finally{
        loading.value = false
        
    }
}



</script>

<template>
    <input type="text" name="" id="" class="block  p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 mx-24  md:w-2/3" text-black v-model="language" placeholder="eg Malayalam ,Rock">


    <button @click="getData" type="submit" class=" bg-green-600 text-white px-4 py-2 rounded-lg shadow-md hover:bg-green-700 transform  transition duration-300 ease-in-out hover:scale-105 active:scale-95 ml-24 my-2 md:ml-96" :disabled="loading" > {{ loading ? 'Loading...':"Explore Stations" }}</button>

    

    <div  v-if="stationDetails.length"  class=" grid grid-cols-2 gap-8 md:grid-cols-4">
       
        <div v-for="(station , index) in stationDetails">
                
           
            <div class=" flex pt-3" >
                <img v-if="station.favicon" :src="station.favicon" alt="" class=" w-5 h-5  mr-4">
            <h3 class=" font-bold font-mono text-xl">
                {{ station.name }}
            </h3>

            </div>
            <p><strong>Country:</strong> {{ station.country }}</p>
            <p><strong>Languages:</strong> {{ station.language }}</p>
            <p><strong>State:</strong> {{ station.state }}</p>
        <p><strong>Bitrate:</strong> {{ station.bitrate ? station.bitrate + ' kbps' : 'Unknown' }}</p>
        <p><strong>Codec:</strong> {{ station.codec }}</p>
        
      

        <audio :src="station.url_resolved
        " controls class=" w-3/4 border-2 border-gray-700 rounded-lg bg-gray-800 p-2"
        >
        </audio>


       
            
   

        </div>
        

    
   
    </div>
<div v-else>
    <p v-if="loading" class="text-center text-lg font-semibold text-gray-700 animate-pulse md:mr-96 pt-4">
    Hold on, our radio ninjas are searching...
</p>

<p v-else-if="language.length" class="text-center text-lg font-semibold text-gray-700 md:mr-96 pt-4">
    No signal detected! Even aliens can't find this station. 🛸📡
</p>

<p v-else class="text-center text-lg font-semibold text-gray-700 md:mr-96 pt-4">
    Type something to discover awesome radio stations!
</p>

</div>

    





</template>


<style>
button:hover {
    transform: scale(1.05);
    transition: all 0.3s ease-in-out;
}

</style>