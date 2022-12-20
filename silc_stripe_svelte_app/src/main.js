import App from './App.svelte';


const app = new App({
	target: document.body,
	props: {
		rootProp1: 'App rootProp1 test val'
	}
});

export default app;

