
console.log(" init silclouds auth ")

var sc_g_auth = "init_auth";

var whost = window.location.href

console.log("strip w host to gsc host ~ " + whost)
var whost_stripped = whost.split("://")[1].split("/")[0].split(":")[0]
console.log("stripped hostname ~ " + whost_stripped)

window.gsc_host = whost_stripped;


// silclouds server (for shop client, login/register, and static css)
window.scs_host = "http://localhost:1110"
// window.scs_host = "https://vsilc.com"

// client hostname, not used usually, 5000 for local svelte server or CDN
window.scc_host = "http://localhost:5000"
// window.scc_host = "https://silclouds.com"

console.log(" init silclouds auth ")


var sc_g_auth = "init_auth";


//setCookie(c1, 30);
//setCookie(c2, 30);
//setCookie(c3, 30)

// Oct 2021 18:44:07 G
var init_auth_cook = JSON.stringify({'silc_auth':"{'uname':'initt_uname','key':'init_hashedkey'}"})
// how to stay logged
//setCookie(tauth_cook, 30)

// Check User Auth response
var cua_resp = "no_cookie"; 
console.log("Set cua resp no cookie")
console.log("call check user auth")
check_user_auth("silc_auth")

console.log("get cua resp ~ ", cua_resp.toString())



function get_silc_cookie(cName) {
                console.log("call get silc cookie")
      const name = cName + "=";
      const cDecoded = decodeURIComponent(document.cookie); //to be careful
      console.log("DECODE cookie ~ " + cDecoded)

      if (cDecoded == ""){
              console.log("cookie is Null String")
              return "no_cookie"
      }
      
      return cDecoded;
}


// return "no_cookie" or the cookie string
function check_user_auth(si_ck_name){
        console.log("run CHECK USER AUTH")
        var get_ck = get_silc_cookie(si_ck_name)
        cua_resp = "no_cookie";
        if (get_ck == undefined || 
                get_ck == "" ||
                get_ck == "no_cookie" ) {
        
                        console.log("Cookie not set, check location for auth")
                        console.log(window.location.host)
                        console.log(window.location.href)
        if (window.location.href.includes("/shop_client/") != true &&
        window.location.href.includes("/create_account/") != true 
        ){
        console.log("kick unauthorized user to shop client")
                window.location.href = "/shop_client/"  
		
                }
        }

        console.log("auth passed, setting cookie auth and globals")
	// set auth check resp async here later
                // if (get_ck != )
                console.log( "SI cookie get ~ " + get_ck.toString())
                cua_resp = get_ck
		sc_g_auth = get_ck
                window.sc_g_auth = sc_g_auth 
             
        
        return cua_resp;
}




function setCookie(cookie_data, expDays) {
        console.log("call set silc cookie")
        let date = new Date();
        date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        let si_ck = cookie_data + ";" + expires + ";" + "path=/";
        console.log("set si cookie ~ " + si_ck)
        document.cookie = si_ck;
}


// cookie from svelte app
// set_sa_cookie = function() {
//         console.log("set_auth_cookie called ~ ")
//         var un_in = document.getElementById("ad_log_un").value
//         console.log("get ad log un val ~ " + un_in)
//         // var auth_cook = JSON.stringify({ "silc_auth":{ "uname":un_in, "ukey":"HASHKEY_cookie"}})
//     var auth_un_cook = "silc_auth=" + JSON.stringify(
//         {"uname": un_in,
//             "ukey": "HASHKEY"})
//         console.log("call set silc cookie ~ " + auth_un_cook)
//             let date = new Date();
//             var expDays=30
//             date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
//             const expires = "expires=" + date.toUTCString();
    
//         var au_ck = auth_un_cook + expires
//         console.log("set window silcauth cookie ~ " + au_ck) 
//             document.cookie = au_ck;
    
//             console.log("set window silcauth cookie complete")
//     }





// update component auth tab
// only call from pages with <div class="auth_header"> component
function uc_auth_tab(){
        console.log("update auth tab with check user auth resp ~" +
                cua_resp.toString())
        if (cua_resp == "no_cookie"){
			console.log("auth not set")
		}
        else if(cua_resp != "no_cookie"){
                var logged_uname = JSON.parse(cua_resp)["silc_auth"]["uname"]

        var ui_auth_tab = document.getElementById("acc_un_out")
		 	if (ui_auth_tab == undefined){
                console.log("cant find acc_un_out auth tab")
       			 }
		
		else{
                ui_auth_tab.innerHTML = logged_uname
        }
         
        }
}



function driver_dash_portal_click(){
        var logged_in = false;
        // do request with uname/key if have cookie, otherwise alert

			// var cr = check_user_auth()
        if (cua_resp == "no_cookie"){
              console.log('user not logged kick to /shop_client ')
                window.location.href = "/shop_client/"  
        }
        else{
                console.log("cookie set auth passed ( CHECK FLOW  LATER)")
                window.location.href  = "/driver_dashboard/"
        }
}



uc_auth_tab()

