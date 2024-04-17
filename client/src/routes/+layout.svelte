<script>
	import './styles.css'
	import { goto } from '$app/navigation'
	import { page } from '$app/stores'
	import { errorStore, addError } from '$stores/error'
	import { loadingStore } from '$stores/loading'
	import { noAuthRoutes } from '$lib/images/client/constants'
	import { onMount } from 'svelte'
	import { PUBLIC_API_URL } from '$env/static/public'
	import axios from 'axios'

	// Components
	import ToastWrapper from '$components/ToastWrapper.svelte'
	import Error from '$components/Error.svelte'
	import Header from '$components/Header.svelte'


	onMount(async () => {
		loadingStore.set(true)

		const token = localStorage.getItem('access_token')

		if (token) {
			const response = await axios.get(`${PUBLIC_API_URL}/users/is_authenticated/`, {
				headers: {
					Authorization: `Bearer ${token}`
				}
			})

			console.log('Response:', response.data)
			if (response.data.authenticated && !noAuthRoutes.includes($page.url.pathname)) {
				console.log('User is authenticated')
				loadingStore.set(false)
			} else if (!response.data.authenticated && noAuthRoutes.includes($page.url.pathname)) {
				console.log('User is not authenticated, they can access this route.')
				loadingStore.set(false)
			} else {
				console.log('User is not authenticated, redirecting to /login')
				addError('You are not authenticated. Please log in.')
				goto('/login')
				loadingStore.set(false)
			}
		} else if (!noAuthRoutes.includes($page.url.pathname)) {
			console.log('No access token, redirecting to /login')
			goto('/login')
			loadingStore.set(false)
		}
	})

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
		{#if $loadingStore}
			<p>Loading...</p>
		{:else}
			<slot />
		{/if}
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
