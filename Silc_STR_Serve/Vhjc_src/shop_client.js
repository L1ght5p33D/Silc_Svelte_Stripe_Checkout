

console.log(" INIT shop client JS " )


function shop_client_login_click(){
    console.log("shop_client_login_click call")
    var un_input = document.getElementById("shop_cli_un_input").value;
    console.log("get un input ~ "+un_input.toString())

    // key def for now
    var log_auth_cookie = JSON.stringify({"silc_auth": {"uname": un_input, "key": "HASHPASS"}})

    console.log("set cookie with un input")
    setCookie(log_auth_cookie, 1)
    console.log("run check user auth")
    check_user_auth()
    console.log("run uc auth tab")
    uc_auth_tab()

    //window.location.href = "/driver_dashboard/"

}