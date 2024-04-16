<script>
	import Header from '../components/Header.svelte'
	import './styles.css'
	import { userProfile } from '$stores/user'
	import { goto } from '$app/navigation'
	import { browser } from '$app/environment'
	import { page } from '$app/stores'
	import { errorStore } from '$stores/error'
	import ToastWrapper from '$components/ToastWrapper.svelte'
	import Error from '$components/Error.svelte'
	import { noAuthRoutes } from '$lib/images/client/constants'

	$: console.log(`user profile: ${$userProfile}`)
	$: if (browser && !$userProfile && !noAuthRoutes.includes($page.url.pathname)) {
		console.log('No user profile, redirecting to /login')
		goto('/login')
	} else if (browser && $userProfile && noAuthRoutes.includes($page.url.pathname)) {
		console.log('User found, redirecting to /')
		goto('/')
	}

</script> 

<div class="app">
	{#if $errorStore.length > 0}
		<ToastWrapper>
			{#each $errorStore as error, i}
				<Error 
				error={{
					'message': error,
					'index': i,
				}} />
			{/each}
		</ToastWrapper>
	{/if}

	<Header />

	<main>
		<slot />
	</main>

	<footer>
		<p>A modest job-search app from <a href="https://shanemadethat.com" target="_blank">Shane</a></p>
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
