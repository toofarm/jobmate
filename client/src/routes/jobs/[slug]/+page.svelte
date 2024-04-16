<script lang="ts">
    import type { PageData } from './$types'
	
	export let data: PageData
</script>

<section>
    <h2>
        {data.job.title}
    </h2>
    <h3>
        {data.job.company}
    </h3>
    <h3>
        {data.job.description}
    </h3>
</section>