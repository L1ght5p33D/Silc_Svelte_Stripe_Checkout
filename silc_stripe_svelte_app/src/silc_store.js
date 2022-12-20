

import { writable} from 'svelte/store';

// Ex store val. Type doesn't matter for init
export const store_val_0_writer =
 writable(0)

 // export const store_val_0_writer = writable(0)
export const store_val_1_writer =
 writable("Test store val 1")


 // platform info
 var init_plat = {"uplat":"init plat"}
    
export const sg_plat = writable( JSON.stringify(init_plat))

// auth
var init_auth_writer = {"uname":"init auth"}

export const sg_auth =
 writable( JSON.stringify(init_auth_writer ))


 // location
var init_loc_writer = {"uloc":"init loc"}

export const sg_loc =
 writable( JSON.stringify(init_loc_writer ))


