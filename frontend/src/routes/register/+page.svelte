<script lang="ts">
	import axios, { AxiosError } from 'axios'
	import { goto } from '$app/navigation'
	import { PUBLIC_API_URL } from '$env/static/public'

	let email = ''
	let password = ''
	let firstName = ''
	let lastName = ''
	let error = ''
	let loading = false
	
	$: valid = !!email && !!password && !!firstName && !!lastName

	async function signUp() {
		try {
			loading = true

			const response = await axios.post(
				`${PUBLIC_API_URL}/auth/signup/`, 
				{ 
					email, 
					password, 
					firstName, 
					lastName 
				})
			console.log('Sign up successful:', response.data)
			goto('/')
		} catch (err) {
			if (err instanceof AxiosError) error = err.response?.data.message
			else error = 'Something went wrong. Please try again'

			loading = false
		}
	}
</script>

<svelte:head>
	<title>Register | Jobmate</title>
	<meta name="description" content="Register for Jobmate" />
</svelte:head>

<main>
	<h1>Register</h1>
	{#if error}
		<p style="color: red;">{error}</p>
	{/if}
	<form 
		class={`${loading ? 'loading' : ''}`}
		on:submit|preventDefault={signUp}>
		<label>
			First Name:
			<input type="text" bind:value={firstName} required />
		</label>
		<label>
			Last Name:
			<input type="text" bind:value={lastName} required />
		</label>
		<label>
			Email:
			<input type="email" bind:value={email} required />
		</label>
		<label>
			Password:
			<input type="password" bind:value={password} required />
		</label>
		<button type="submit" disabled={!valid}>Sign Up</button>
	</form>
</main>

<style>
	main {
		max-width: 400px;
		margin: 0 auto;
		padding: 2rem;
	}

	h1 {
		text-align: center;
	}

	form {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.loading {
		opacity: 0.75;
		pointer-events: none;
	}

	label {
		display: flex;
		flex-direction: column;
	}

	input {
		padding: 0.5rem;
	}

	button {
		padding: 0.5rem 1rem;
		background-color: #007bff;
		color: #fff;
		border: none;
		cursor: pointer;
	}

	button:disabled {
		background-color: #ccc;
		cursor: not-allowed;
	}
</style>
