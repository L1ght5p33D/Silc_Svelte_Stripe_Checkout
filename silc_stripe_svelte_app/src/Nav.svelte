
<script context="module">

import SilcPage_1 from './Silc_Page_1.svelte';
import SilcPage_2 from './Silc_Page_2.svelte';
import SilcPage_3 from './Silc_Page_3.svelte';
import SilcPage_4 from './Silc_Page_4.svelte';
import SilcPage_5 from './Silc_Page_5.svelte';

export const navOptions = [
		{ page: 'Home',   component: SilcPage_1 },
    { page: 'Product',   component: SilcPage_2 },
    { page: 'Messages',   component: SilcPage_3 },
    { page: 'PayGate',   component: SilcPage_4 },
    { page: 'Pending',   component: SilcPage_5 },

];
</script>