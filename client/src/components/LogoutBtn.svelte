<script lang="ts">
    import { goto } from '$app/navigation'
    import { PUBLIC_API_URL } from '$env/static/public'
    import { userProfile } from '$stores/user'

    async function handleLogout(): Promise<void> {
        try {
            await fetch(`${PUBLIC_API_URL}/auth/logout/`, { method: 'POST' })
            await userProfile.set(null)
            localStorage.removeItem('access_token')
            goto('/login')
        } catch (err) {
            console.error('Logout failed:', err)
        }
    }
</script>

<button on:click={handleLogout}>Logout</button>
