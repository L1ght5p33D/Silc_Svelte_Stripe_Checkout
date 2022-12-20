<script>

var msg_init = "none";

// EX Data get from POST
var msg_list = [{"msgid_randid33":{"sender":"bob",
                                    "to":"alice",
                                    "mb":"stuff to say",// message body
                                    "pd": "A94ga38AF", // product id (msg from product only)
                                    "ts":3423453453, //timestamp
                                    "db":"db_0", // separate messages db from app later 
                                },},
                                    
                                {"msgid_randid34":{"sender":"alice",
                                    "to":"bob",
                                    "mb":"stuff to say back",
                                    "pd": "A94ga38AF",
                                    "ts":3423453477, 
                                    "db":"db_0", 
                                },}
            ]
</script>

<div class="page_cnt">
    <h3> Messages</h3>
    <div class="msg_ibx_out_wrap">
    { #if msg_init == "none"}
        <div class="msg_ibx_list">Nothing yet</div>    
    { :else if msg_init != "none"}
    <div class="msg_ibx_list">{msg_list}</div>    
    {/if}

</div>

    
    </div>
