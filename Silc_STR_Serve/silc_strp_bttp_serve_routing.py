


from pymongo import MongoClient                                                                                                                      
import pprint
import json
import stripe

from silc_priv_api.create_prod import create_prod
from silc_priv_api.create_account import create_account
from silc_auth_api.check_auth import check_auth, san_lstr


def route_fs_get(get_path, get_cd_ctx):
    print("route_fs_get call ROUTE ~ " + str( get_path ))
    b_resp = ""
    c_resp = ""
    stat = 404

    fs_parse_get = ""
    fs_parse_get = get_path.split("/sc_fs/")[1]
    print("parse sc fs req path ~ " + str(fs_parse_get))
    # fpg = fs_parse_get.split("/")[0].split("/")[0]
    # print("get fpg ~ " + fpg)

    # DEV/PROD switch
    # sc_tsi_ssh 45.32.65.26:/silc_strpe_co_root/ <SI_src | Vhjc_src >
    # glob_stat_dir = "/silc_strpe_co_root/"
    glob_stat_dir = "/home/si/os_projects/3Trade_GIS/Silc_STR_Serve/"
    
    # any URLS with /sc_fs/ get routed into Silc_STR_Serve/ desired path
    sf_path = glob_stat_dir + fs_parse_get

    # Naming convention to replace underscore in URL to period for file exts
    sf_path_urlsan = sf_path.replace("_html",".html")
    sf_path_urlsan = sf_path_urlsan.replace("_js",".js")
    sf_path_urlsan = sf_path_urlsan.replace("_css",".css")
    sf_path_urlsan = sf_path_urlsan.replace("_png",".png")
    # Static file endpoint special path ~ search for filetypes in by dir auto
    sf_spath = sf_path_urlsan
    
    # Cut last slash for dir str lookup
    if sf_spath[ len(sf_spath) - 1] == "/":
        sf_spath = sf_spath[0:len(sf_spath) - 1] 
    
    # if fpg == "ht1":
    #     with open('SI_src/jhc_test.html', 'r') as jhct:
    #         b_resp = jhct.read().encode("utf-8")
    #     stat = 200
    #     c_resp = "text/html; charset=utf-8"

    print("open sf path ~ " + str(sf_spath))
    
    try:
        with open( sf_spath ) as sresp:
            b_resp = sresp.read()
    except:
        print("couldnt open sc static dir ... fail out")
        stat = 404
        with open('SI_src/si_notfound.html', 'r') as jhct:
            b_resp = jhct.read()
    
        c_resp = "text/html; charset=utf-8"
        return b_resp, c_resp, stat   
    # else:
    #     print("get not found call 404 resp")
        
    #     # Could return shop client for all urls but might increase robot traffic
    #     # with open('Vhjc_src/shop_client.html', 'r') as jhct:
    #     #    jhc_resp = jhct.read()
    #     with open('SI_src/si_notfound.html', 'r') as jhct:
    #         b_resp = jhct.read().encode("utf-8")
        
        # stat = 200
        # c_resp = "text/html; charset=utf-8"
    stat = 200

    return b_resp, c_resp, stat

def route_get(jhc_path):
    print("route_get call ROUTE ~ " + str( jhc_path ))
    jhc_resp = ""
    c_resp = ""
    stat = 404

    # if jhc_path == "/ht1/":
        # with open('SI_src/jhc_test.html', 'r') as jhct:
            # jhc_resp = jhct.read()
        # stat = 200
        # c_resp = "text/html; charset=utf-8"
    
    if jhc_path == "/sc_auth/":
        with open('Vhjc_src/sc_auth.js', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/html; charset=utf-8"
    # elif jhc_path == "/jt1/":
    #     with open("SI_src/jhc_test.js", "r") as jhcs:
    #         jhc_resp = jhcs.read()
    #     stat = 200
    #     c_resp = "text/javascript; charset=utf-8"
    elif jhc_path == "/login/":
        with open('SI_src/login.html', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/html; charset=utf-8"


    elif jhc_path == "/nav_home/":
        with open('Vhjc_src/nav_home.html', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/html; charset=utf-8"
    

    elif jhc_path == "/shop_client/":
        with open('Vhjc_src/shop_client.html', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/html; charset=utf-8"

    elif jhc_path == "/shop_client_js/":
        with open('Vhjc_src/shop_client.js', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/javascript; charset=utf-8"

    elif jhc_path == "/nav_home_js/":
        with open('Vhjc_src/nav_home_js', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/javascript; charset=utf-8"


    elif jhc_path == "/glob_1/":
        with open('Vhjc_src/glob_1.js', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/javascript; charset=utf-8"

    elif jhc_path == "/glob_2/":
        with open('Vhjc_src/glob_2.js', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/javascript; charset=utf-8"

    elif jhc_path == "/driver_dashboard/":
        with open('Vhjc_src/driver_dashboard.html', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/html; charset=utf-8"
    elif jhc_path == "/driver_dashboard_js/":
        with open('Vhjc_src/driver_dashboard.js', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/javascript; charset=utf-8"
    elif jhc_path == "/edit_product/":
        with open('Vhjc_src/edit_product.html', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/html; charset=utf-8"
    elif jhc_path == "/edit_product_js/":
        with open('Vhjc_src/edit_product.js', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/javascript; charset=utf-8"
    elif jhc_path == "/gird/":
        with open('Vhjc_src/gird_cal_tst.html', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/html; charset=utf-8"
    
    # GET create_account
    elif jhc_path == "/create_account/":
        with open('Vhjc_src/create_account.html', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/html; charset=utf-8"
    
    elif jhc_path == "/create_account_js/":
        with open('Vhjc_src/create_account.js', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/javascript; charset=utf-8"
    
    
    elif jhc_path == "/pay_info_tab/":
        with open('Vhjc_src/pay_info_tab.html', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/html; charset=utf-8"
    elif jhc_path == "/pay_info_tab_js/":
        with open('Vhjc_src/pay_info_tab.js', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/javascript; charset=utf-8"
    
    elif jhc_path == "/sttings_tab/":
        with open('Vhjc_src/settings_tab.html', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/html; charset=utf-8"
    elif jhc_path == "/settings_js/":
        with open('Vhjc_src/settings_tab.js', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/javascript; charset=utf-8"

    elif jhc_path == "/jquery_min_cr/":
        with open('Vhjc_src/jQuery_min_cr.js', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/javascript; charset=utf-8"
    
    
    # Globals and CSS
    # elif jhc_path== "/sc_g_css/":
    #     with open('Vhjc_src/sc_g_css.css', 'r') as jhct:
    #         jhc_resp = jhct.read()
    #     stat = 200
    #     c_resp = "text/css; charset=utf-8"
    elif jhc_path== "/driver_dashboard_css/":
        with open('Vhjc_src/driver_dashboard.css', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/css; charset=utf-8"
    elif jhc_path== "/sc_acc_css/":
        with open('Vhjc_src/sc_acc.css', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/css; charset=utf-8"
    elif jhc_path== "/sv_sc_nav_css/":
        with open('Vhjc_src/sv_sc_nav.css', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/css; charset=utf-8"

    elif jhc_path== "/sv_auth_css/":
        with open('Vhjc_src/sv_auth.css', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/css; charset=utf-8"
    elif jhc_path== "/sv_acc_css/":
        with open('Vhjc_src/sv_acc.css', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/css; charset=utf-8"

    elif jhc_path== "/sv_prod_css/":
        with open('Vhjc_src/sv_prod.css', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/css; charset=utf-8"

    elif jhc_path == "/sc_msg_nav_css/":
        with open('Vhjc_src/sc_msg_nav.css', 'r') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "text/css; charset=utf-8"

    #MEDIA
    elif jhc_path == "/si_media/si_drip_logo_png/":
        with open('si_media/sit.png', 'rb') as jhct:
            jhc_resp = jhct.read()
        
        print("PNG RESP SLIC LOGO")

        stat = 200
        c_resp = "image/png;"
    
    elif jhc_path == "/si_media/round_black_ham_trans_bg/":
        with open('si_media/round_black_ham_trans_bg.png', 'rb') as jhct:
            jhc_resp = jhct.read()
        stat = 200
        c_resp = "image/png;"
    
    # elif jhc_path == "/si_media/sm_ham_black_trans_png/":
    #     with open('si_media/sm_ham_black_trans.png', 'rb') as jhct:
    #         jhc_resp = jhct.read()
    #         stat = 200
    #     c_resp = "image/png;"

    elif jhc_path == "/favicon.ico":
        with open('si_media/sit.png', 'rb') as jhct:
            jhc_resp = jhct.read()
        
        print("PNG RESP SLIC LOGO")

        stat = 200
        c_resp = "image/png;"

    elif jhc_path == "/manifest.webmanifest":
        with open('/manifest.webmanifest', 'r') as jhct:
            jhc_resp = jhct.read()
        
        print("MANIFEST RESP prog app")

        stat = 200
        c_resp = "application/manifest+json"
    

    # else:
    #     print("page not found return 404")
    #     with open('SI_src/si_notfound.html', 'r') as nfr:
    #         jhc_resp = nfr.read()
    #     stat = 200
    #     c_resp = "text/html"   
    else:
        print("get NOT FOUND call 404 resp")
        
        # Could return shop client for all urls but might increase robot traffic
        # with open('Vhjc_src/shop_client.html', 'r') as jhct:
        #    jhc_resp = jhct.read()
        with open('SI_src/si_notfound.html', 'r') as jhct:
            jhc_resp = jhct.read()
        
        stat = 200
        c_resp = "text/html; charset=utf-8"
    return jhc_resp, c_resp, stat


def route_post(path, post_data):
    print("route_post called with path ~ " + str( path ))
    if str( path ) == "rp_test":
        print( "rp_test path route post called " )
        return "<html><head><title>TTrade</title></head><body><div>RP0</div></body></html>" 
    

    if str( path ) == "/dash_auth/":
        print("check dash auth cookie post data ~")
        print(str(post_data))
        # dpd = json.dumps{post_data}
        dpd = post_data
        posted_uname = dpd["uname"]
        dpds = str( post_data )
        da_succ = check_auth(dpds)
        # da_succ = True
        auth_data = {"rkey":"rollkey_test", "uname":"tuname"}
        da_res = {"success": da_succ, "auth_data": auth_data}
        return da_res
    
    if str( path ) == "/silc_auth_svck/":
        print("silc svck auth call")
        sas_pd = post_data
        print("get sas post data ~ " + str( sas_pd ))
        sas_succ = check_auth( sas_pd )
        print("sas succ ~ " + str( sas_succ))
        auth_data = {"uname":"stuff"}
        return {"success": sas_succ, "auth_data": auth_data}

    #PRIVATE
    if str( path ) == "/silc_product_create/":
        print("call create prod private w post data ~ " + str(post_data))
        cp_succ = create_prod(post_data)
        return {"create_product_success": cp_succ }

    # POST create
    if str(path) == "/post_create_silc_account/":
        print("call register w post data" + str(post_data))
        
        acc_create_succ = create_account(post_data)
        return json.dumps({"account create success": str(acc_create_succ), "cas":"cas"})

    if str(path) == "/create_account_user/":
        print("create account user called")

        auth_succ = check_auth(post_data)
        acc_data = get_account_data_priv(auth_succ)
        

    if str(path) == "/get_account_user/":
        print("get account user called")
        print("Get auth cookie post data ~" + str(post_data))
        auth_succ = check_auth(post_data)
        print("get account user auth ~" + str(auth_succ))
        if auth_succ == "fail":
            print("return success false")
            
            #not working
            return {"success":"not_succ"}

    if str(path) == "/create_si_silc_stripe_checkout_session/":
            print("start pyserve stripe checkout redirect")
            
            
            session = stripe.checkout.Session.create(
                        payment_method_types=['card'],
                        line_items=[{
                          'price_data': {
                            'currency': 'usd',
                            'product_data': {
                              'name': 'T-shirt',
                            },
                            'unit_amount': 2000,
                          },
                          'quantity': 1,
                        }],
                        mode='payment',
                        success_url='http://localhost:4242/success.html',
                        cancel_url='http://localhost:4242/cancel.html',
                      )
            
            self.send_response(303)
            #self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps( session ).encode('utf-8'))

    else:
        return {"silc_post_resp": "error, path not found"}
