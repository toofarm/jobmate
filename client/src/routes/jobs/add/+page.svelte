<script lang="ts">
    import axios, { AxiosError } from 'axios'
    import { PUBLIC_API_URL } from '$env/static/public'
    import { addError } from '$stores/error'
    import { DateInput } from 'date-picker-svelte'
    import Button from '$components/Button.svelte'

    let title = ''
    let company = ''
    let description = ''
    let successful = false
    let applied = new Date()

    async function handleAddJob(): Promise<void> {
        console.log('Adding job...')
        try {
            const response = await axios.post(`${PUBLIC_API_URL}/jobs/`, {
                title,
                company,
                description
            })
            console.log('Job added:', response.data)
            successful = true
        } catch (err) {
            console.error('Job add failed:', err)
            if (err instanceof AxiosError) addError(err.message)
        }
    }

</script>

<section>
    <h2>Add Job</h2>
    {#if successful}
        <p>Job added successfully!</p>
    {/if}
    <form on:submit|preventDefault={handleAddJob}>
        <label for="title">Title:</label>
        <input type="text" id="title" bind:value={title} />

        <label for="company">Company:</label>
        <input type="text" id="company" bind:value={company} />

        <label for="description">Description:</label>
        <textarea id="description" bind:value={description}></textarea>

        <label for="date">Applied Date:</label>
        <DateInput id="date" bind:value={applied} />

        <Button 
            type="submit"
            disabled={!title || !company || !description}>Add Job</Button>
    </form>
</section>