<script lang="ts">
	import axios, { AxiosError } from 'axios';

	let email = '';
	let password = '';
	let firstName = '';
	let lastName = '';
	let error = '';

	async function signUp() {
		try {
			const response = await axios.post('/api/sign-up', { email, password, firstName, lastName });
			console.log('Sign up successful:', response.data);
		} catch (err) {
			if (err instanceof AxiosError) error = err.response?.data.message;
		}
	}
</script>

<main>
	<h1>Sign Up</h1>
	{#if error}
		<p style="color: red;">{error}</p>
	{/if}
	<form on:submit|preventDefault={signUp}>
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
		<button type="submit">Sign Up</button>
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
</style>
