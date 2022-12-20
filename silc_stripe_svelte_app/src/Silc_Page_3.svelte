
Messages

<script>
    import { onDestroy } from 'svelte';
    import {onMount} from 'svelte';
    import{sleep} from './sc_util/gen_util.svelte';
    import { ss_jq } from './sc_util/ss_jq.svelte';  
    
    import { sg_auth, sg_loc } from './silc_store';    

    import { msgNavOptions } from  './nav_comp/msg_nav.svelte';
    
    function log_comp_destroy(){
        console.log("LOG Silc MSG Comp destroy called")
    }
      onDestroy(() => log_comp_destroy()); 
    
      const unsub = sg_auth.subscribe(val =>{
        console.log("[App.svelte] page 3 auth unsub call")
    })
        onDestroy( unsub )       
    

  onMount(async function() {
console.log("msg onMount")
  });


let selected = msgNavOptions[0];
let intSelected = 0;
  function changeComponent(event) {
	selected = msgNavOptions[event.srcElement.id];
	intSelected = event.srcElement.id;
}

</script>

<link rel='stylesheet' href='http://localhost:1110/sc_msg_nav_css/'>


Username
	<div>{ $sg_auth }</div>

	User Loc
	<div>{ $sg_loc }</div>


<div class="msg_wrap">

    <div class="navcolor sv_nav_row">
	{#each msgNavOptions as option, i}
		<div class="msg-nav-item">
			<button 
			class={intSelected==i ? 
			 "msg-nav-link active" : "msg-nav-link"}
			 on:click={changeComponent} 
			 id={i} role="tab">{option.page}
			</button>
		</div>
		{/each}
	</div>

  <div class="nav-item-srow">
		
		<div class="page-left"></div>

		<div class="nav-selected-row">
			<div class="nav-selected-page">
				<!-- <h1>{selected.page}</h1> -->
				<svelte:component this={selected.component}/>
			</div>
		</div>
		
		<div class="page-right"></div>
	</div>
</div>


   

