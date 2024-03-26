<script>
	import Header from '../components/Header.svelte'
	import './styles.css'
	import { userProfile } from '$stores/user'
	import { goto } from '$app/navigation'
	import { browser } from '$app/environment'
	import { page } from '$app/stores'

	$: console.log(`user profile: ${$userProfile}`)
	$: if (browser && !$userProfile) {
		console.log('No user profile, redirecting to /login')
		goto('/login')
	} else if (browser && $userProfile && $page.url.pathname === '/login') {
		console.log('User found, redirecting to /')
		goto('/')
	}

</script> 

<div class="app">
	<Header />

	<main>
		<slot />
	</main>

	<footer>
		<p>visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to learn SvelteKit</p>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
