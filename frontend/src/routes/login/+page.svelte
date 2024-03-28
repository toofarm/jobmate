<script lang="ts">
	import axios, { AxiosError } from 'axios'
	import { goto } from '$app/navigation'
	import { PUBLIC_API_URL } from '$env/static/public'

	let username = ''
	let password = ''
	let error = ''

	async function handleLogin(): Promise<void> {
		console.log('Logging in...')
		try {
			const response = await axios.post(`${PUBLIC_API_URL}/auth/`, { username, password })
			console.log('Login successful:', response.data)
			goto('/')
		} catch (err) {
			console.error('Login failed:', err)
			if (err instanceof AxiosError) error = err.message
		}
	}
</script>

<main>
	<h1>Login</h1>
	{#if error}
		<p class="error">{error}</p>
	{/if}
	<form on:submit|preventDefault={handleLogin}>
		<label for="username">Username:</label>
		<input type="text" id="username" bind:value={username} />

		<label for="password">Password:</label>
		<input type="password" id="password" bind:value={password} />

		<button type="submit">Login</button>
	</form>
</main>

<style>
.error {
	color: red;
	font-style: italic;
}
</style>
