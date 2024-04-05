export type TUser = {
    name: string;
    email: string;
}

export type TError = {
    message: string;
    index: number;
}

export type TJob = {
    id: number;
    title: string;
    description: string;
    company: string;
    active: boolean;
    link?: string;
    applied?: string;
    follow_up?: boolean;
    created: string;
    confidence?: number;
    resume?: boolean;
    cover_letter?: boolean;
}