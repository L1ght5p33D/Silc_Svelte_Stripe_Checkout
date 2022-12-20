

<script context="module">

import {  sg_auth } from './silc_store';

// get silc auth cookie
export const get_sa_cookie = function(){
console.log(" call check auth cookie ")
	let cookies = document.cookie
		// console.log("auth cookie ~ " + cookies.toString()); 
        if (cookies){
            // console.log("Found doc cookies ~ ", cookies.toString())
         return cookies;
        }
	else {
		console.log(" DOC COOKIES undefined for now ...O AUTH")
        return "no_ck"
	}

	}

export const set_sa_cookie = function() {
    console.log("set_auth_cookie called ~ ")
    var un_in = document.getElementById("ad_log_un").value
    console.log("get ad log un val ~ " + un_in)
    // var auth_cook = JSON.stringify({ "silc_auth":{ "uname":un_in, "ukey":"HASHKEY_cookie"}})
var auth_un_cook = "silc_auth=" + JSON.stringify(
    {"uname": un_in,
        "ukey": "HASHKEY"})
    console.log("call set silc cookie ~ " + auth_un_cook)
        let date = new Date();
        var expDays=30
        date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();

    var au_ck = auth_un_cook + expires
    console.log("set window silcauth cookie ~ " + au_ck) 
        document.cookie = au_ck;

        console.log("set window silcauth cookie complete")
}

export const remove_auth_cookie = function(){
        console.log("rem auth cookie calle ~")

        var auth_writer_obj = {"uname":"init auth"}
        sg_auth.set( JSON.stringify(auth_writer_obj) )
        console.log("location host" + location.host)
        console.log("location hostname" + location.hostname)

        var d = new Date();
                d.setDate(d.getDate() - 1);
                var expires = "expires="+d;
                
        document.cookie = "silc_auth=loggedOut;"+ expires +";path=/";

}

export const redirect_no_auth = function(){
    console.log("redirect auth to pub")
    window.location.href="http://localhost:1110/shop_client/"
}
</script>
