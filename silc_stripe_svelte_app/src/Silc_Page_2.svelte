
<script context="module">

import { onDestroy } from 'svelte';
import {onMount} from 'svelte';
import { cpp_ax, insert_prod_node } from './silclouds_api/create_product.svelte';
	
import { sg_auth } from './silc_store';  


var prod_item = [{"pName":"testpnamefornow"}]



	</script>

 <!-- <div>Username: { JSON.parse($sg_auth)["uname"] } </div> -->

<div id="pay_info_nav_tab_wrap" class="nav_comp">
</div>

<div id="settings_nav_tab_wrap" class="nav_comp">
</div>

<div class="prod_wrap">
   
   <div class="prod_center">
   <div class="sn_item">Create New Silc Product</div>
         <div class="create_product_form">
         <input id="prod_in" type="text" value="Product Name">
         <br>
         <input id="desc_in" type="text" value="Description">
         <br>
         <input id="price_in" type="text" value="Price">
      <button on:click={ cpp_ax( $sg_auth ) }> Create Product</button> 
 </div>
 
 <div class="sn_item">Insert List </div>
      <div class="create_product_form">
      <input id="prod_in_ui" type="text" value="Product Name">
      <input id="desc_in_ui" type="text" value="Description">
      <input id="price_in_ui" type="number" value="Price">
      <button  on:click={insert_prod_node} >Post Product </button>
 </div>

 <div id="insert_prod_node_parent">
 </div>

      <div>Products</div>
         <div id="prod_tscroll_wrap" class="scrolling-wrapper">
            {#each prod_item as pi}
               <div class="prod_si_wrap">
                  <div class="prod_title">{ pi["pName"] }</div>
               </div>
            {/each}
         </div>

   </div>
 </div>





