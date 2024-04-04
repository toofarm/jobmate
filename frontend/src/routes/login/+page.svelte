<script lang="ts">
	import axios, { AxiosError } from 'axios'
	import { goto } from '$app/navigation'
	import { PUBLIC_API_URL } from '$env/static/public'
	import { userProfile } from '$stores/user'
	import { addError } from '$stores/error'

	let username = ''
	let password = ''

	async function handleLogin(): Promise<void> {
		console.log('Logging in...')
		try {
			const response = await axios.post(`${PUBLIC_API_URL}/auth/`, { 
				username, 
				password })
			console.log('Login successful:', response.data)
			await userProfile.set(response.data)
			goto('/')
		} catch (err) {
			console.error('Login failed:', err)
			if (err instanceof AxiosError) addError(err.message)
		}
	}
</script>

<main>
	<h1>Login</h1>
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
