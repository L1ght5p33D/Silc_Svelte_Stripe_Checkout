<script>

import { onDestroy } from 'svelte';
import { store_val_0_writer } from './silc_store.js';


function log_comp_destroy(){
	console.log("LOG COMPONENT destroy called")
}

// subscribe returns unsubscribe to call onDestroy 
// would have to memory profile or look at src to see
// const unsubscribe = store_val_0_writer.subscribe(value => {
// 		store_val_0_local_val = value;
// 	});
// 	onDestroy(unsubscribe);

onDestroy(() => log_comp_destroy());


	export let tpropval;
	
	function reset() {
		console.log("RESET store val called " )
        store_val_0_writer.set("store val called from RESET")
	}

	function set(){
		console.log("SET store val called " )

		var ts = Date().toString();
		store_val_0_writer.set("store val called from SET " + ts)
	}

</script>
	can use { tpropval } anywhere
	<br>

	<button  on:click={ set }>
	Set G Store Val
</button>