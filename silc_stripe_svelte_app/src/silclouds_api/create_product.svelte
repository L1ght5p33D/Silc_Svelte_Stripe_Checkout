
<script context="module" >


import { getContext, onDestroy } from 'svelte';
import { ss_jq } from '../sc_util/ss_jq.svelte';  
import {  sg_auth } from '../silc_store';



export const  insert_prod_node = () => {
  var pnamein = document.getElementById("prod_in_ui").value
  var pdescin = document.getElementById("desc_in_ui").value
  var ppricein = document.getElementById("price_in_ui").value
}

var n_a_v;
// cannot unsubscribe get called twice ...
const unsub_sg_auth = sg_auth.subscribe(val =>{
	  console.log("[create_product.svelte] sg_auth writer sub fire val ~ ", val)
    n_a_v = val
	})
  // cannot call
		// onDestroy( unsub_sg_auth )



export const cpp_ax = () => {
console.log("get glob silcAuth")
  console.log("sa ~", n_a_v)

  console.log("create product post async jq with sg_auth ~ " ,n_a_v ,
"key ~ ", JSON.parse(n_a_v)["ukey"])
var auname = JSON.parse(n_a_v)["uname"]

console.log("get auname ~ " + auname.toString())
if (auname == "init auth"){
  console.log("get auth init ~ log in to create product")
  window.alert("must log in to create product")
  return "fail"
}
var aukey = JSON.parse(n_a_v)["ukey"]
console.log("get aukey ~ " + aukey.toString())
var prodname = document.getElementById("prod_in").value;
var proddesc = document.getElementById("desc_in").value;
var prodprice = document.getElementById("prod_in").value;
var prod_data_obj = {"prodname": prodname, 
                      "proddesc":proddesc,
                       "prodprice": prodprice,
                        "uname": auname,
                        "key": aukey,
                      }

console.log("make prod data ~ "+JSON.stringify(prod_data_obj))
ss_jq.post( {
    type:"POST",
    url: "http://localhost:1110/silc_product_create/",
    crossDomain: true,
    data: JSON.stringify(prod_data_obj),
      success:  function(data) {
  console.log("Return cpp_ax jq resp ~")
  var ddata = JSON.stringify(data)
    console.log("jq resp data " + ddata)
  //  sg_auth.set(ddata)
  } } )

}

</script>