


console.log("init driverdashboard js")


// already call from auth set glob
//var auth = check_user_auth()
var auth = window.sc_g_auth;
console.log("g auth ~ " + auth.toString())


async function send_auth_prod_post_click(prod_data){
    
    console.log("call send_auth_prod_post_click")
const location = window.location.hostname;
// const purl = `http://${location}:1110/silc_product_create_pf/`
const purl = `http://${location}:1110/get_account_user/`
console.log(" init ptest call ")
    const settings = {
        method: 'POST',
        // mode: 'no-cors',
        cache: 'no-cache',
        body: JSON.stringify( prod_data ),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
    };
    // try {
        console.log("init post prod fetch")
        const fetchResponse = await fetch( purl , settings);
        console.log("get post prod data")
        console.log("parse dd")
        const data = await fetchResponse.json();
        console.log("parse dd ~ " + data.toString())
        console.log("str again")
        var ddata = JSON.parse(JSON.stringify(data)       )
        console.log("st data")
        console.log(ddata.toString())

        for (var k in ddata){
            console.log("loop data" + k.toString())
            console.log("loop data v ~" + ddata[k])
        }
        return data;
    // } catch (e) {
    //     console.log("catch create pf err " + e.message)
    //     return e;
    // }    
}

async function post_create_prod_click(prod_data) {
	if (auth != "init_auth"){
		var prod_name = document.getElementById("prod_in").value
		var prod_desc = document.getElementById("desc_in").value
		var prod_price = document.getElementById("price_in").value
	}



console.log("init async create product post")

//var create_prod_url = "localhost:1110/silc_product_create_pf/"
	    
const location = window.location.hostname;
const purl = `http://${location}:1110/silc_product_create_pf/`

console.log(" init ptest call ")
    const settings = {
        method: 'POST',
        mode: 'no-cors',
        cache: 'no-cache',
        body: JSON.stringify( prod_data ),
        headers: {
            'Accept': 'application/json',
            // 'Content-Type': 'application/json',
        },
    }
    try {
        const fetchResponse = await fetch( purl , settings);
        const data = await fetchResponse.json();
       
        console.log( "await post fetch data ~ " , data )
        // return data;
    } catch (e) {
        console.log("catch create pf err " + e.toString())
        return e;
    }    

    console.log("Ready state Create Product response ~ ")
console.log("send create prod post ~~~ >>>>>> ")
console.log("post crprod post")

}


// username from auth and product json data

function edit_prod(uname, js_cpa){
    console.log("edit prod called")
    // window.location.href = "/edit_product/"
    console.log("edit prod json data" + js_cpa.toString())
    var dec_cpa = JSON.parse(js_cpa)
    console.log("get dec cpa ~ " + dec_cpa.toString())
}

// function edit_prod(uname){
//     console.log("edit prod called")
//     //window.location.href = "/edit_product/"
//     //console.log("edit prod json data" + pjd.toString())
// }

function insert_prod_node(){
	console.log("call insert prod node")
	//var ins_prod_node_parent = document.getElementById("insert_prod_node_parent")
var ins_prod_menu = document.getElementById("menu")
	var lic = document.createElement("li")
	//var ins_node = document.createElement("div")
	//ins_node.textContent = "Set cont from node"
    var pname = document.getElementById("prod_in_ui").value
    var pdesc = document.getElementById("desc_in_ui").value
    var pprice = document.getElementById("price_in_ui").value

lic.className += "prod_hov"
lic.className += " "
lic.className += "x-scroll-card"

lic.addEventListener("click", function() {
  console.log("LIC class listener fire ~")
});

console.log("set pins user from auth ~ " + auth)

/*
Cant do any of this
console.log("parse auth user ~ " + puvp)
console.log("parse auth user string ~ " + puvp.toString())
var uname_val = puvp["silc_auth"]
console.log("get obj val ~ " + uname_val)
var puval = JSON.parse(JSON.stringify(uname_val))
console.log("get silc obj parse val ~ " + puval)

var puvs = JSON.stringify(auth)
console.log("get auth stringify ~ " + puvs)
console.log("get auth stringify stri" + puvs.toString())
var get_auth = JSON.parse(JSON.stringify(auth))
console.log("get obj auth ~ " + get_auth)
*/

var auth_uname = JSON.parse(auth)["silc_auth"]["uname"]
console.log("get gauth cookie uname for prod ~" + auth_uname)
var auth_key = JSON.parse(auth)["silc_auth"]["key"]
console.log("get auth key ~ " + auth_key)

var cre_prod = {"pname":pname,"powner":auth_uname,"pprice":pprice}
var cre_prod_arg = JSON.parse(JSON.stringify(cre_prod))

console.log("make prod obj ~ " + cre_prod_arg.toString())
console.log("create prod json ~ " + cre_prod_arg)

var js_cpa = JSON.stringify(cre_prod_arg)

send_auth_prod_post_click(cre_prod_arg)
console.log("send auth click complete")

var ap_div_child = `<div onclick="edit_prod( '${auth_uname}', '${cre_prod_arg}' )" class="ap-child-div"> 

<div class="prodname">${pname}</div>
<div class="prodowner">${auth_uname} </div>
<div class="proddesc">${pdesc}</div>
<div class="prodprice"> $ ${pprice}</div>
</div>`

lic.innerHTML = ap_div_child 
//lic.textContent =  pname + "\n Description : \n" + pdesc + " Price: \n " + pprice 

ins_prod_menu.insertBefore(lic, ins_prod_menu.firstElementChild.nextSibling )
}


