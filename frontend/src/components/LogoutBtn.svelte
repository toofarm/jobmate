<script lang="ts">
    import { goto } from '$app/navigation'
    import { PUBLIC_API_URL } from '$env/static/public'

    async function handleLogout(): Promise<void> {
        console.log('Logging out...')
        await fetch(`${PUBLIC_API_URL}/logout`, { method: 'POST' })
        goto('/login')
    }
</script>

<button on:click={handleLogout}>Logout</button>
