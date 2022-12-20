<script context="module">

import{ lcoord_list } from '..//us_loc_cord_json.svelte';

import { sg_loc } from '../silc_store';

    export const min_dist_state_from_pos =
    
    function min_dist_state_from_pos(position){
        //console.log(position) 
        // >> GeolocationPosition {coords: GeolocationCoordinates, timestamp: 1643504191737}
//coords: GeolocationCoordinates {latitude: 33.4659584, longitude: -117.6403968, altitude: null, accuracy: 1400.625166814183, altitudeAccuracy: null, …} timestamp: 1643504191737

    
    console.log("start lookup w lcoord_list")
  
    var user_plat = position.coords.latitude
    var user_plong = position.coords.longitude
    
    var min_dist_state = "not_found_min_state"
    var min_dist = 99999999
   
    var loc_writer_obj = {"lat":0, "long": 0, "mds": "notset"}

    for (var st_v in lcoord_list){
      // console.log("looping sv" + st_v)
        var st_lat = lcoord_list[st_v]["latitude"]
        var st_long = lcoord_list[st_v]["longitude"]
        loc_writer_obj["lat"] = st_lat;
        loc_writer_obj["long"] = st_long;
        var ydistsq = ( st_lat - user_plat )**2
        // console.log("calc sq y ~ " + ydistsq.toString())
        var xdistsq = ( st_long - user_plong ) **2
        var dist_c = ( xdistsq + ydistsq )** .5 

      // console.log("dist c = " +dist_c.toString())
   if (dist_c < min_dist){
     min_dist = dist_c
     min_dist_state = lcoord_list[st_v]["state"]
   }
  }
   console.log("found min dist state ~ " + min_dist_state.toString())
    loc_writer_obj["mds"] = min_dist_state;
   sg_loc.set(JSON.stringify(loc_writer_obj))

   return min_dist_state
}

export const getPosition = function getPostition(options) {
  return new Promise(function (resolve, reject) {
    navigator.geolocation.getCurrentPosition(resolve, reject, options);
  });
}


</script>