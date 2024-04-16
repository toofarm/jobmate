import axios from 'axios'
import { PUBLIC_API_URL } from '$env/static/public'
import type { PageLoad } from './$types'
import type { TJob } from '$types/types'

type TReturn = {
    jobs: TJob[]
}

export const load: PageLoad = async (): Promise<TReturn> => {
    try {
        const jobs = await axios.get(`${PUBLIC_API_URL}/jobs/`)

        return {
            jobs: jobs.data,
        }
    } catch (error) {
        console.error(error)
    }
}
