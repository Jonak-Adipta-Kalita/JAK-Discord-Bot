export interface Command {
    id: number;
    name: string;
    usage: string;
    has_slash_command: boolean;
    description: string;
}

export interface Guild {
    id: string;
    name: string;
    icon: string;
    owner: boolean;
    permissions: string;
    features: string[];
}
