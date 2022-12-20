<script>
    import { onDestroy } from 'svelte';
    import {onMount} from 'svelte';
    import{sleep} from './sc_util/gen_util.svelte';
    
    import { ss_jq } from './sc_util/ss_jq.svelte';  
    import { min_dist_state_from_pos, getPosition } from './sc_util/location_util.svelte';
    
    import {  sg_loc  } from './silc_store.js';
    import { sg_auth } from './silc_store';    


  
    

    function log_comp_destroy(){
        console.log("LOG SilcAccComp destroy called")
    }
    

  onDestroy(() => log_comp_destroy()); 
    console.log("Set destroy store_val sub")
        

      

var def_pos_str = "location unknown";
var def_bn_str = "business name not set"

// Toggle to "Done"
var cardPreviewBtnName="Card Preview";

// card name gets set to username or Public Business Name
var acc_user_name = "init_acc_data"


// for card preview click
var load_card_vals = {"bname":"Default BName", "bloc":"initbloc"}

function load_user_card_vals(){
  console.log("load user card preview called")
  
  return load_card_vals
}

function update_account_submit(){
  console.log("update accoutn submit called sub vals~ ")
  
}


function loc_sot_onchange(){
  var get_in_val = document.getElementById("loc_sot_input")
  console.log("loc sot change fire ~ ")
  load_card_vals["bloc"] = get_in_val
}




  onMount(async function() {
    console.log("silc acc comp onmount")
    getPosition()
  .then((position) => {
    console.log("set default position str from min dist loc call")
       def_pos_str = min_dist_state_from_pos(position) 
       sg_loc.set(JSON.stringify( {"uloc": def_pos_str } ))
  })
  .catch((err) => {
    console.error(err.message);
  });
  });


  function toggle_acc_but_disp_html(el){
    if (el.innerHTML == "⛻"){
      el.innerHTML = "✓" 
      }else{el.innerHTML="⛻"}
  }




  function card_bn_diff_click(){
    console.log("bn diff name chck click call ")
    var cl_elem = document.getElementById("card_bn_diff_wrap")
    cl_elem.classList.toggle("check_active")
    var bn_elem = document.getElementById("bn_diff_but")
    bn_elem.classList.toggle("check_active")
      toggle_acc_but_disp_html(bn_elem)
    var muf_bn_elem = document.getElementById("mb_card_bn_tog")
      // toggle_acc_tog_disp_html(muf_bn_elem)
      // muf_bn_elem.classList.toggle("checked")
      muf_bn_elem.classList.toggle("test_check")
      
      // muf_bn_elem.click()
    }


  function card_loc_show_click(){
    console.log("card loc  click")
    var clw_elem = document.getElementById("card_loc_show_wrap")
    clw_elem.classList.toggle("check_active")
  var cl_b_elem = document.getElementById("card_loc_show_but")
    cl_b_elem.classList.toggle("check_active")
      toggle_acc_but_disp_html(cl_b_elem)
    var muf_ls_elem = document.getElementById("mb_card_loc_tog")
    muf_ls_elem.classList.toggle("check_active")
  }

  function card_loc_diff_click(){
    console.log("card loc wrap check click")
    var cl_elem = document.getElementById("card_loc_diff_wrap")
    cl_elem.classList.toggle("check_active")
    var clb_elem = document.getElementById("card_loc_diff_but")
    clb_elem.classList.toggle("check_active")
     toggle_acc_but_disp_html(clb_elem)
    
     var luf_ls_elem = document.getElementById("loc_diff_tog")
    luf_ls_elem.classList.toggle("check_active")
  }

  function card_desc_click(){
    console.log("card desc check click")
    var cl_elem = document.getElementById("card_desc_wrap")
    cl_elem.classList.toggle("check_active")
    var cl_elem = document.getElementById("card_desc_but")
    cl_elem.classList.toggle("check_active")
    toggle_acc_but_disp_html(cl_elem)

    var duf_ls_elem = document.getElementById("desc_tog")
    duf_ls_elem.classList.toggle("check_active")
  }

  


function set_def_loc_press(){
  console.log("Set def loc press")
  var blocout=document.getElementById("bloc_out");
blocout.innerHTML = def_pos_str;
}

function tst_set_tog_from_js(){
  console.log("tst set call")
}

// Symbols  
//  mountiain ⛰ 
// confirm check ✓
//  japanese bank ⛻

</script>



      <!-- business name and username shown on user card to add stuff  -->

      <!-- <div id="dev_debug_test">
        def pos string : { def_pos_str }<br>
        G loc writer : { JSON.parse($sg_loc)["uloc"] } 
      </div> -->



      <div class="acc_card_update_wrap">
        
        <div class="card_bn_un_wrap">  
            <div class="ac_def_label"> { JSON.parse($sg_auth)["uname"] } </div>
        </div>
            
            <div class="card_item_wrap">
            
              <div id="card_bn_diff_wrap" class="user_card_field_wrap">
                <div id="bn_diff_but" class="dt_card_but" on:click={ card_bn_diff_click } >
                ⛻
              </div>

              <input type="checkbox" on:click={ card_bn_diff_click }
               id="mb_card_bn_tog" class="mb_card_tog toggle_switch">

                <div class="ai_cont">
                  <p>Show a different display name</p>   
                  <small>Default is Username</small>
                  <br>  <br>
                  Display Name:
                  <input id="bn_input" type="text" value={JSON.parse($sg_auth)["uname"] }>
                </div>
              </div>
            </div>


          {#await def_pos_str }
           <p>...waiting</p>
            {:then res}

          <div class="card_item_wrap">
            <div id="card_loc_wrap">
            <div id="card_loc_show_wrap" >  
              <div class="ac_def_label">
                {res}
              </div>
              <div class="user_card_field_wrap">        
                <div id="card_loc_show_but" class="dt_card_but"   on:click={ card_loc_show_click }>
                  ⛻
                </div>
                
                  <input type="checkbox" on:click= { card_loc_show_click }
                  id="mb_card_loc_tog" class="mb_card_tog toggle_switch">
              

                    <div class="ai_cont">
                      <p>Show Location on User Card</p>
                      <small>Default is location not shown</small>    
        
                    <div class="geo_def_out_wrap">
                     ~ {def_pos_str}  
                    <button on:click={ set_def_loc_press }>Use Default</button>        
                  </div>
                </div>
                </div>
                </div>
                </div>
              </div>

              <div class="card_item_wrap">
                <div id="card_loc_diff_wrap">
               <div id="loc_ucfw" class="user_card_field_wrap">
                  
                      <div id="card_loc_diff_but" class="dt_card_but"  
                       on:click={ card_loc_diff_click }>
                       ⛻
                      </div>

                      <input type="checkbox" id="loc_diff_tog"
                      class="mb_card_tog toggle_switch"
                      on:click={ card_loc_diff_click } >
                     
                      <div class="ai_cont">
                        <div class="sca_label loc_diff_label">
                 
                        <p>Set a Different Location on Card</p>
                          <small>Setting a location restricts the visibilty of your post.</small>
                      
                      </div>
                        
                      <input id="loc_sot_input" value={ res} type="text" on:keyup={ loc_sot_onchange }>
                      <div id="loc_sot_out">

                      </div>
                   </div>
                  </div>
                 </div>
                </div>
                  {:catch error}
                    <p style="color: red">{error.message}</p>
          {/await}

                   <div class="ac_def_label">
                                           Description
                   </div>

          <div id="card_desc_wrap" class="user_card_field_wrap">
            
                    <div id="card_desc_but" class="dt_card_but"   on:click={ card_desc_click }>
                      ⛻
                    </div>
                    <input type="checkbox" id="desc_tog" 
                    class="mb_card_tog toggle_switch"
                          on:click={ card_desc_click }
                            name="bdesc_check" value="bdesc_check_val">

                    <div class="ai_cont">
                      <div class="sca_label bdesc_label">
                      <p>Description on Card </p>
                        <textarea cols="40" rows="0" id="bdesc_input" >    </textarea>
                      </div>
                    </div>
         
                  </div>
                  
                  <!-- <div id="acc_wrap_end"></div> -->
                  
                  <!--
                        File upload images
                        <br>
                      <form action="/action_page.php">
                        <input type="file" id="myFile" name="filename">
                        <input type="submit">
                      </form> -->


            <!-- <div id="load_user_card_preview">

                      {#await load_user_card_vals() }
                      <p>...waiting</p>
                      {:then res}
                    
                      <div id="acc_card_out_wrap">
                        <div id="card_out_cont">
                        <div class="ucWrap">
                              <div class="ucBNameWrap">
                                <div class="ucBNameWrap ucFWrap">
                                  <div class="bn_ucd">{res["bname"]}</div>
                                </div>
                                <div class="ucBlocWrap ucFWrap">
                                  <div class="bl_ucd">{res["bloc"]}</div>
                                </div>
                                <div class="ucDescWrap ucFWrap">
                                  <div class="bd_ucd">{res["bdesc"]}</div>
                                </div>
                              </div>            
                            </div>             
                          </div>
                     </div>
                
                {:catch error}
                <p style="color: red">{error.message}</p>
         {/await}
        </div> -->
                              
</div>