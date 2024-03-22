<script lang="ts">
	import axios, { AxiosError } from 'axios'

	let username = ''
	let password = ''
	let error = ''

	async function handleLogin(): Promise<void> {
		console.log('Logging in...')
		try {
			const response = await axios.post('/api/login', { username, password })
			console.log('Login successful:', response.data)
		} catch (err) {
			if (err instanceof AxiosError) error = err.response?.data.message
			console.error('Login failed:', error)
		}
	}
</script>

<main>
	<h1>Login</h1>
	{#if error}
		<p style="color: red;">{error}</p>
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
	/* Add your custom styles here */
</style>
