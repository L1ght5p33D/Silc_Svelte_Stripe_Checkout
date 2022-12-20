
console.log("INIT create_account.js" ) 

console.log("get auth for pre input ~ " + cua_resp)



document.addEventListener('keyup', logAccFormKey);


function ca_back_click(){
    console.log("ca back click")
    window.location.href="/shop_client/";
}


const validateEmail = (email) => {
    console.log("validate em called email ~ " + email)
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var ret= re.test(email.toLowerCase());
      console.log("Ret rs ~ " + ret)
      return ret
  };

function validate_ac_form(){ // all inputs valid
    console.log("validate ac form called")

            var unin = document.getElementById("username_input").value;
            var emin = document.getElementById("email_input").value;
            var pin = document.getElementById("pass_input").value;

            console.log("validate form input vals ~ ")
            console.log("user input ~ " + unin)
            console.log("email input ~ " + emin)
            var sub_but_elem = document.getElementById("ca_but")
            
            var ret_err = "init_ret_err"
            if (unin == "new_username"  ){
                    console.log("new username in ")
                    ret_err = "please choose a unique username"
                    document.getElementById("err_out_un").innerHTML= ret_err
            }

                    else{document.getElementById("err_out_un").innerHTML= ""}
                
                if (unin.length < 8   ){
                    console.log("username too short")
                ret_err = "username too short"
                document.getElementById("err_out_un").innerHTML= ret_err    
            }
                else{ console.log("username pass") 
                document.getElementById("err_out_un").innerHTML=""}


            if (emin=="your@email.com" || emin == ""){
                ret_err = "You need to enter your email";
                document.getElementById("err_out_em").innerHTML=  ret_err;
            }
                else{
                document.getElementById("err_out_em").innerHTML= ""
            }

            console.log("call validate email emin ~ " + emin)
            var em_valid = validateEmail(emin)

            if (em_valid== false){
                ret_err = "Email address is not valid"
                document.getElementById("err_out_em").innerHTML= ret_err
                
            }
                else{
                document.getElementById("err_out_em").innerHTML= ""
            }

            if (pin.length < 8){
                ret_err = "Password less than 8 characters"
                console.log("pass length" + pin.length.toString())
                document.getElementById("err_out_pass").innerHTML = ret_err
            }
                else{
                document.getElementById("err_out_pass").innerHTML= ""
            }


            if (ret_err == "init_ret_err"){
                console.log("sub active error null")
                sub_but_elem.classList.add("sub_active")
                return true;
            }
            else{
                console.log("create acc validate found err button disabled")
                sub_but_elem.classList.remove("sub_active")
                return false;
                }

}

function logAccFormKey(e) {
    console.log("KEYUP EVENT FIRE ~~~~~~ ")

    validate_ac_form()
}



async function create_acc_click(){

	console.log("create acc sub click, call validate ac")

    var vac = validate_ac_form();
    if (vac == false){
        console.log("form not valid, disp err")
        return;
}

	const location = window.location.hostname;
const purl = window.scs_host + `/post_create_silc_account/`

var un = document.getElementById("username_input").value
var em = document.getElementById("email_input").value
var pi = document.getElementById("pass_input").value


var user_reg_data = {"uname": un, "email": em, "key": pi}

console.log("call post creat account async")

console.log("send create account POST w scs host " + window.scs_host)
    const settings = {
        method: 'POST',
        mode: 'no-cors',
        cache: 'no-cache',
        body: JSON.stringify( user_reg_data ),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
    };
    try {
        const fetchResponse = await fetch( purl , settings);
        const data = await fetchResponse.json();
       
        console.log( "await register response ~ " , data )
        
        if (data["cas"] == "cas"){
            console.log("HAVING TROUBLE PASSING DATA")
        }
        
      if (data["account create success"] == "success"){
        console.log("got register success ~ ")
	      window.location.href = window.scs_host + "/driver_dashboard/"
      }

    //   if(data["account create success"] == "username already exists"){
    //   console.log("got register fail.. username exist")
	//       window.alert("register fail... account exists or something went wrong. Try again later")
    //   }
      if( JSON.parse(data)["account create success"] == "username already exists"){
        console.log("got register fail.. username exist")
            window.alert("Username already taken. Choose a new username and try again.")
        }
        if( JSON.parse(data)["account create success"] == "email already exists"){
            console.log("got register fail.. username exist")
                window.alert("Email already taken. Choose a new username and try again.")
            }
    
        //Fri Feb 11 20:47:16 PST 2022 return data;
    } catch (e) {
        return e;
    }    

}


