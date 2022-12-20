


<script>
//example import
   // import SilcStoreComp from './SilcStoreComp.svelte';
import { store_val_0_writer } from './silc_store.js';
   
   import SilcAccComp from './SilcAccComp.svelte';
   
   </script>

<link rel='stylesheet' href='http://localhost:1110/sc_acc_css/'>

 <!-- store val can be accessed with dollar reserved char  -->
 <!-- Auto-subscription only works with store variables that -->
  <!-- are declared (or imported) at the top-level scope -->
   <!-- of a component. -->
<!-- Silc store auto sub ~  {$store_val_0_writer} -->

<div class="page_cnt">

   <div >
<h3 class="sc_acc_title" > Account </h3>
</div>
 <SilcAccComp></SilcAccComp>
</div>
