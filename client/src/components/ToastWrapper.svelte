<script lang="ts">
</script>

<ul class="toast-wrapper">
    <slot></slot>
</ul>

<style>
    .toast-wrapper {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        list-style: none;
        max-width: 100%;
        position: fixed;
        right: 0;
        top: 0;
        width: 100%;
        z-index: 1000;
    }
</style>    