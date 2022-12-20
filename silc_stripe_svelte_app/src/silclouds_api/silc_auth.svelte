<script context="module" >

import { compute_slots } from "svelte/internal";
import { get_sa_cookie,  set_sa_cookie } from "../cookie_utils.svelte";
import {  sg_auth } from '../silc_store';


export const  auth_cookie_login = function(){

			console.log("auth cookie login call ~ ")

			// get cookie and see if its already set.. tell user already logged
			var gsc = get_sa_cookie()

			if (gsc != "no_ck" && gsc != ""){
				console.log("cookie already set ~ " , gsc)
				var gsc = JSON.parse(gsc.split("=")[1].split("expires")[0])
				var gsc_dec = JSON.stringify(gsc)
				console.log("try get gsc parsed DO NOT MOVE COOKIE EXPIRED ORDER ~ " + gsc_dec)
				
				console.log("get gsc uname ~ ", gsc["uname"])
				console.log("get gsc ukey ~ ", gsc["ukey"])
				
				var silc_auth_writer = {"uname":gsc["uname"], "ukey":gsc["ukey"]}
				
				sg_auth.set( JSON.stringify(silc_auth_writer) )
				
				window.SilcAuth = silc_auth_writer

				console.log("get silc auth")

			console.log("silc auth  ~ ", JSON.stringify(window.SilcAuth) )
			}
			else{
				console.log("cookie resp no_ck, not set")
				var auth_un_val = document.getElementById("ad_log_un").value;
				var auth_hk = "HASHKEY"
				}
}

export const  auth_header_login_click = function(){

			console.log("auth header login call ~ ")

			// get cookie and see if its already set.. tell user already logged
			var gsc = get_sa_cookie()

			console.log("get gsc cookie ~ " + gsc)

			if (gsc != "no_ck"){
				console.log("cookie already set ~ " , gsc)
			// window.alert("already logged in boot to login screen later")
	
			}

			else{console.log("cookie resp no_ck, not set")
				var auth_un_val = document.getElementById("ad_log_un").value;
				var auth_hk = "HASHKEY"
			}

			//TODO Auth POST here with confirm uname and key or redirect
			var post_auth_uk_check = true;
			if (post_auth_uk_check == true){
				console.log("Auth post response success, set cookie")
				set_sa_cookie()

				var auth_writer_obj = {"uname":auth_un_val, "ukey":auth_hk}
				sg_auth.set( JSON.stringify(auth_writer_obj) )
			}
			else{
				console.log("NO AUTH redirect out")
				redirect_no_auth()
			}
}




// 	ss_jq.post( {
//   type:"POST",
//   url: "http://localhost:1110/silc_auth_svck/",
//   crossDomain: true,
//   data: JSON.stringify({"tsome":"data"}),
//     success:  function(data) {
 
//  var ddata = JSON.stringify(data)
//    console.log("sas resp data" + ddata)

// }
// })


// Type: Function( PlainObject data, String textStatus, jqXHR jqXHR )
// var jqxhr = ss_jq.post( {
//   type:"POST",
//   url: "http://localhost:1110/get_account_user/",
//   crossDomain: true,
//   data: JSON.stringify({"tsome":"data"}),
//     success:  function(data) {
 
//  var ddata = JSON.stringify(data)
//    console.log("svvvp data " + ddata)
//  gad = ddata;
// },




</script>