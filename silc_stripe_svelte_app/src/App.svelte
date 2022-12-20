<script>
import { getAllContexts, onDestroy } from 'svelte';
import { navOptions } from  './Nav.svelte';

import { ss_jq } from './sc_util/ss_jq.svelte';  
import { silc_URL } from './silc_url_conf.svelte';
import { get_sa_cookie, redirect_no_auth, remove_auth_cookie } from './cookie_utils.svelte';
import { auth_cookie_login, auth_header_login_click } from './silclouds_api/silc_auth.svelte'
import { store_val_0_writer, sg_auth, sg_loc, sg_plat  } from './silc_store';

import {onMount} from 'svelte';


// Page for nav
let selected = navOptions[0];
let intSelected = 0;


// Dev Config Flag
// changeComponent(1)

// change the selected component 
//(the event.originalTarget.id is not accessible 
//in Chrome so switched to event.srcElement.id)
function changeComponent(event) {

	console.log("change comp event ~ " + event.toString())
	selected = navOptions[event.srcElement.id];
	intSelected = event.srcElement.id;
}

    const unsub_sg_auth = sg_auth.subscribe(val =>{
	  console.log("[App.svelte] sg auth unsub")
	})
	

function sa_od(){
	console.log("silclouds app ondestroy called")

	unsub_sg_auth()
}


onDestroy( sa_od )





var jqxhr = ss_jq.post( {
  type:"POST",
  url: "http://localhost:1110/get_account_user/",
  crossDomain: true,
  data: JSON.stringify({"tsome":"data"}),
    success:  function(data) {
 
 var ddata = JSON.stringify(data)
   console.log("sp data " + ddata)
//  sg_auth.set(ddata)
} } )


	
let lastKnownScrollPosition = 0;
let ticking = false;

let ls_dist = 0
let sts = Date.now()

// function si_scroll_ctl(scrollPos) {
// 	var new_date = Date.now()
// 	// console.log("new date ~" + new_date.toString())
// 	// console.log("sts ~ " + sts.toString())
// 	console.log("ls dist ~ " + ls_dist.toString())
// 	console.log("scroll Pos ~ " + scrollPos.toString())
// 		if (new_date - sts > 1000 &&  scrollPos - ls_dist > 10){
// 			console.log(	"LONG SCROLL IS LONG")
// 		}
// 		console.log("end long scroll routine")
// 	ls_dist = scrollPos;
// }

// window.addEventListener('scroll', function(e) {
// 	console.log("se")
//   lastKnownScrollPosition = window.scrollY;

//   if (!ticking) {
//     // console.log("not ticking")
// 	window.requestAnimationFrame(function() {
// 		// console.log("not ticking req anim frame")
// 		si_scroll_ctl(lastKnownScrollPosition);
//       ticking = false;
//     });

//     ticking = true;
//   }
// });


function sv_ham_menu_click(){
	console.log("sv ham menu call")
	// var menu_elem = document.getElementById("sv_nav_item_wrap");
	var menu_elem = document.getElementById("sv_nav_row");
	menu_elem.classList.toggle ("sv_nav_hide")

}

var nav_builtins = ""
nav_builtins = "<p>Browser CodeName: " + navigator.appCodeName + "</p>";
		nav_builtins+= "<p>Browser Name: " + navigator.appName + "</p>";
		nav_builtins+= "<p>Browser Version: " + navigator.appVersion + "</p>";
		nav_builtins+= "<p>Cookies Enabled: " + navigator.cookieEnabled + "</p>";
		nav_builtins+= "<p>Platform: " + navigator.platform + "</p>";
		nav_builtins+= "<p>User-agent header: " + navigator.userAgent + "</p>";

		console.log("nav builtins ~ \n" + nav_builtins.toString())
		sg_plat.set(nav_builtins)

	onMount(() => {
		console.log("app onmount call")
		
		// set unique name to search for later
		store_val_0_writer.set("Silclouds SV0 Init")

		auth_cookie_login()    

			return () => {
    	
	};
  });


		
</script>

<!-- <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css'> -->
<link rel='stylesheet' href='http://localhost:1110/sc_fs/Vhjc_src/sc_g_css/'>
<link rel='stylesheet' href='http://localhost:1110/sc_fs/Vhjc_src/sv_sc_nav_css/'>
<link rel='stylesheet' href='http://localhost:1110/sc_fs/Vhjc_src/sv_auth_css/'>
<link rel='stylesheet' href='http://localhost:1110/sc_fs/Vhjc_src/sv_acc_css/'>
<link rel='stylesheet' href='http://localhost:1110/sc_fs/Vhjc_src/sv_prod_css/'>



<div class="sv_dev_head">
	<div > {$sg_plat} </div>
	<div>
 	~ StoreVal 0: { $store_val_0_writer }
	~ Location { $sg_loc }
	</div>
	<div class="sv_head">
		<div class="ad_dev">Username: { JSON.parse($sg_auth)["uname"] }</div>
	</div>
</div>

<div class="sv_sc_app_cont">
		
<div class="sv_auth_tab">

		<div class="ad_login">
			<input type="text" value="username" id="ad_log_un">
			<button on:click={ auth_header_login_click }> Test gStore Username </button>
		</div>

		<button on:click={ remove_auth_cookie }>Remove Cookie</button>
		<button on:click={ redirect_no_auth }>Log out</button>
	</div>

<div class="nav_ham_btn_mbar">
	<div class="nav_ham_btn" >	
		<div class="nav_ham_btn_fwrap" on:click={ sv_ham_menu_click }>
			<img id="ham_img" src="http://localhost:1110/si_media/sm_ham_black_trans_png/" alt="scalt_HAM">
		</div>
	</div>
</div>

	<div id="sv_nav_row" class="navcolor sv_nav_row">
	
		<div class="nav_logo">
	             	<img class="logo_box_cont" id="si_drip_logo" 
		src="http://localhost:1110/si_media/si_drip_logo_png/" alt="scalt">
		</div>

		<!-- <div class="nav_ham_btn" on:click={ sv_ham_menu_click }>	
			<div class="nav_ham_btn_fwrap">
				<img src="http://localhost:1110/si_media/sm_ham_black_trans/" alt="scalt_HAM">
			</div>
		</div> -->

		<!-- <div id="sv_nav_item_wrap" class="navcolor"> -->
		{#each navOptions as option, i}
			<div class="nav-item">
				<button 
				class={intSelected==i ? 
				"nav-link active" : "nav-link"}
				on:click={changeComponent} 
				id={i} role="tab">{option.page}
				</button>
			</div>
			{/each}
		<!-- </div> -->

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


