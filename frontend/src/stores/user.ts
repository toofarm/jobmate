import { writable } from 'svelte/store'

// Define the initial user profile data
const initialUserProfile = null

// Create a writable store to hold the user profile data
export const userProfile = writable(initialUserProfile)