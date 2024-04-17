<script lang="ts">
    export let onClick = () => console.log('Button clicked!')
    export let disabled = false
    export let type: 'button' | 'reset' | 'submit' = 'button'
</script>

<button 
    on:click={() => onClick()}
    disabled={disabled}
    type={type}>
    <slot />
</button>

<style>
    button {
        background-color: #007bff;
        border: none;
        border-radius: 0.25rem;
        color: white;
        cursor: pointer;
        font-size: 1rem;
        margin: 0.5rem;
        padding: 0.5rem 1rem;
    }

    button:disabled {
        background-color: #6c757d;
        cursor: not-allowed;
    }

    button:hover {
        background-color: #0056b3;
    }

    button:active {
        background-color: #0056b3;
        transform: translateY(1px);
    }

    button:focus {
        outline: none;
    }

    button:active:focus {
        box-shadow: 0 0 0 0.2rem rgba(38, 143, 255, 0.5);
    }

    button:disabled {
        background-color: #6c757d;
        cursor: not-allowed;
    }

    button:disabled:hover {
        background-color: #6c757d;
    }

    button:disabled:active {
        background-color: #6c757d;
    }

    button:disabled:focus {
        outline: none;
    }

    button:disabled:active:focus {
        box-shadow: none;
    }

</style>