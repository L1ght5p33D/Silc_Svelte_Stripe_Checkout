
<script context="module">

    import msg_ibx from '../smsg/msg_ibx.svelte';
    import msg_block from '../smsg/msg_block.svelte';
    // message settings and options
    import msg_so from '../smsg/msg_so.svelte';
    
    export const msgNavOptions = [
            { page: 'Inbox',   component: msg_ibx },
        { page: 'Block List',   component: msg_block },
        { page: 'Settings',   component: msg_so }
    
    ];
    </script>