<script lang="ts">
    import { clearOneError } from '$stores/error'
    import type { TError } from '$types/types'

    export let error: TError
</script>

<li class="error">
    <h4>{error.message}</h4>
    <button on:click={() => clearOneError(error.index)}>Clear</button>
</li>

<style>
    .error {
        align-items: center;
        background-color: red;
        color: white;
        display: flex;
        font-style: italic;
        justify-content: space-between;
        padding: 2rem;
        width: 100%;
    }

    .error h4 {
        margin: 0;
        padding: 0;
    }

    </style>