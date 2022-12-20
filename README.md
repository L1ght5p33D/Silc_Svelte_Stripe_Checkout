

# Silclouds Stripe Svelte

a test environment for Stripe checkout API and a demo of Svelte app components

### startup 
$ source ../env_silc_mdb/bin/activate                 
(env_silc_mdb)  python ./silc_strp_bttp_serve.py 

### Stunnel startup
stunnel4 /etc/stunnel/silc_stunnel_0.conf python ./silc_strp_bttp_serve.py


### DB Config
 SILC_STR_SERVE/silc_str_conf.py



### Start with filewatch reload


python silc_strp_bttp_serve.py & ./sr_recsha_sreload.sh



#### Env vars
STRIPE_API_KEY  = 'your secret key'




