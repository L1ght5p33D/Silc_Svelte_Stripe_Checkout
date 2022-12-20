from si_bttp import BaseHTTPRequestHandler, HTTPServer

import asyncio

import json
#import cgi
import logging
from sys import argv
#import stripe

from silc_login_reqs import login_post_handler

from silc_strp_bttp_serve_routing import route_get, route_fs_get, route_post

# Test Curl
# curl -X POST  -H "Accept: Application/json" -H "Content-Type: application/json" http://localhost:8888/test_post_curl_call -d '{"id":"si post key","name":"si post val"}'

## Start python with permissions and pipe output to null ~
#exec sudo -u www-data /usr/bin/python /data/examples/python_minimal_http/server.py 8009 >> /dev/null 2>> /dev/null


'''
Local Static File Server ( use to avoid writing urls for everything )

By default, server binds itself to all interfaces. The option -b/--bind specifies a specific address to which it should bind. Both IPv4 and IPv6 addresses are supported.
For example, the following command causes the server to bind to localhost only:
python -m http.server 8000 --bind 127.0.0.1
New in version 3.4: --bind argument was introduced.
New in version 3.8: --bind argument enhanced to support IPv6

By default, server uses the current directory. The option -d/--directory specifies a directory to which
 it should serve the files. For example, the following command uses a specific directory:
python -m http.server --directory /tmp/

import http.server
import socketserver

PORT = 7777
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

'''

#stripe.api_key = 'secret stripe api key' 


defcon_type = 'application/json'

dev_sc_auth_cookie = {"username": "no_auth",
                        "key": "no_key"
 }


g_user_time_cache = {"sig_admin": 0}

def check_ctypes_for_enc(c_resp):
    print("check for ctext type in c_resp ~ " + str(c_resp))
    encode_resp = False
    if  "application/xml" in c_resp or "text/html" in c_resp or "text/javascript"  in c_resp:
        encode_resp = True
    if  "text/css" in c_resp:
        encode_resp = True
    if "image/*" in c_resp or  "image/jpeg" in c_resp or "image/jpg" in c_resp or "image/png" in c_resp:
        encode_resp = False
    
    print("check ctypes return ~ " + str(encode_resp))
    return encode_resp

class SC_Root_Server(BaseHTTPRequestHandler):
   
    def __init__(self, *args, **kwargs):
        print("SI Server Init ~ ")
        print(" Server Methods ~~ " + str( dir(BaseHTTPRequestHandler) ))
        super().__init__(*args, **kwargs)

    def do_HEAD(self):
        print("Root HEAD")
        print("set head headers")
        self.send_header("Accept", "*/*") 
        self.send_header("Accept-Encoding", "*/*" )
        self.send_header("Allow", "GET, POST, HEAD, OPTIONS")
        
        self.send_header('Access-Control-Allow-Methods', 'GET,POST,HEAD,OPTIONS') 
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Access-Control-Allow-Origin', '*')
      
        self.send_header('Cache-Control', 'no-store')
        
        self.send_header('Sec-Fetch-Site', '')
        self.send_header('Sec-Fetch-Mode', '')

        self.send_response(200)
        self.end_headers()



    def do_OPTIONS(self):
        # Send allow-origin header for preflight POST XHRs.
        #self.send_response(HTTPStatus.NO_CONTENT.value)
        print("OPTIONS set headers") 
        self.send_header("Allow", "GET, POST, HEAD, OPTIONS")
        self.send_header('Access-Control-Allow-Methods', 'GET,POST,HEAD,OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.send_header('Cache-Control', 'no-store')
        self.send_response(200)
        self.end_headers()


    
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        gheaders = self.headers
        print("Root GET headers")
        print( str(gheaders ))

        cd_ctx = ""
        for h,v in gheaders.items():
            print("get head for hds ~ "+str(h)+" ::: " + str(v))
            if h =="Accept":
                print("cd accept ctx ~ " + str(v))
                cd_ctx = v

        # ~ With encoding response ~  
        #self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

        # ~ Refuse to receive non-json content ~
        #if ctype != 'application/json':
        #    self.send_response(400)
        #    self.end_headers()
        #    return

        get_path = str( self.path )   
        print("route path called with qpath ~ " + str(get_path))

        
        print("route get with ctype ~ " + str(cd_ctx) )
        # make static for paths with /sc_fs no content type needed
        
        g_stat = 555
        g_encresp = ""
        # Just use Accept header from request for gc_resp content type
        gc_resp = ""
        if "sc_fs" in get_path:
            print("static route path ~ " + str(get_path))
            g_encresp, gc_resp, g_stat = route_fs_get( get_path, cd_ctx )
            print("root get cresp ~ " + gc_resp)
        else:
            print("call root get route ~")
            g_encresp, gc_resp, g_stat = route_get( get_path )
            print("root get gcresp ~ " + str(gc_resp))
            print("Set repsonse stat ~ " + str(g_stat))
            
        print("check ctypes with content type gc_resp ~ " + str(gc_resp))
        need_encode_resp = check_ctypes_for_enc(cd_ctx)

        
        if need_encode_resp == True:
            g_encresp = g_encresp.encode("utf-8")
        
        print("go to send resp")
        self.send_response(g_stat)
        print("set resp headers contype ~ " + str( gc_resp ))
        self.send_header('Content-type', gc_resp)
        print("wfile encode resp")
        self.end_headers()
        self.wfile.write( g_encresp  )



#header options ~ 'Cache-Control', 'no-store') 'Accept-Ranges', 'bytes') 'Content-Encoding', 'br')
    def set_post_headers(self, contype, conlen):
        print("call set_headers")    
        
        self.send_header('Access-Control-Allow-Credentials', 'true') 
        self.send_header('Access-Control-Allow-Origin', '*')
        if len(contype) < 1:
            print("set_header contype not set ~ set def con type" )
            self.send_header('Content-type', defcon_type )
        else:
            print("setting contype ~ " + str( contype ))
            self.send_header('Content-type', contype )
        print("set content-length ") 
        self.send_header('Content-Length', str(conlen) )

    def do_POST(self):
        #contype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        ppath = str( self.path )
        print("Root POST REQ PATH ~ " + ppath )
        # print("call get headers ")
        pheaders = self.headers 
        print( "Root POST REQ HEADERS ~ " + str( pheaders ))
        print("call get address str")
        ads = str( self.address_string() )
        print("POST REQ ADDRESS str " + str( ads ))


        if ppath == "/create_si_silc_stripe_checkout_session/":
            print("start pyserve stripe checkout redirect")
            
            '''
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
            '''
            self.send_response(303)
            #self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps( session ).encode('utf-8'))


        length = int(self.headers['content-length'])

        post_data = self.rfile.read(length)

        print("POST data ")
        print( str(post_data))
        # return json to encode, or 404 if route not found
        resp = None
        resp = route_post( ppath, post_data )
        
        print("POST resp pre encode ", resp )
        # .encode('utf-8')
        # encode_resp = json.dumps(resp).encode("utf-8")
        encode_resp=json.dumps(resp)
        print("encoded resp ~ " + str(encode_resp))
        # send the message back if route_post returns not 404
        self.send_response(200)
        print("send post resp 2")
        ler = len(encode_resp)
        print("get len encode resp ~ " + str(ler))
        print("set post resp default content type ~" + defcon_type)

        self.set_post_headers(defcon_type, ler)
        print("set ph")
        self.end_headers()
        print("end headers write resp")
        self.wfile.write(encode_resp.encode("utf-8"))


       


def run_sc_root(server_class=HTTPServer, handler_class=SC_Root_Server, port=1110 ):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting root sc bttp daemon on port %d...' % port)
    httpd.serve_forever()

    
def scm_astart():
    logging.basicConfig(level=logging.DEBUG)
    logging.info(" silc strp bttp server INIT ")
    
    run_sc_root()
    

scm_astart()

