import { error } from '@sveltejs/kit'
import type { PageLoad } from './$types'
import axios from 'axios'
import { PUBLIC_API_URL } from '$env/static/public'

export const load: PageLoad = async ({ params }) => {	
    if (params.slug) {
        try {
            const job = await axios.get(`${PUBLIC_API_URL}/jobs/${params.slug}`)
            return { job: job.data }
        } catch (error) {
            console.error(error)
        }
    }


	error(404, 'Not found')
}