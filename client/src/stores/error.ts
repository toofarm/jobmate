import { writable } from 'svelte/store'

export const errorStore = writable<string[]>([])

export function addError(message: string) {
    errorStore.update(errors => [...errors, message])
}

export function clearErrors() {
    errorStore.set([])
}

export function clearOneError(index: number) {
    errorStore.update(errors => errors.filter((_, i) => i !== index))
}