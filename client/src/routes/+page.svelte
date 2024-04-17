<script lang="ts">
	import type { PageData } from './$types'
	export let data: PageData
</script>

<svelte:head>
	<title>Home | Jobmate</title>
	<meta name="description" content="Jobmate home" />
</svelte:head>

<section>
	<h1>
		Welcome
	</h1>
	{#if data}
	<ul>
		{#each data.jobs as item}
			<li>{item.title}</li>
		{/each}
	</ul>
	{:else}
	<p>No jobs yet! Better go <a href="/jobs/add">add some</a></p>
	{/if}
	<ul>
		<li><a href="/jobs/add">Add Job</a></li>
		<li><a href="/jobs">View Jobs</a></li>
	</ul>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}


</style>
