export interface Command {
    id: number;
    name: string;
    usage: string;
    has_slash_command: boolean;
    description: string;
}

export interface Role {
    id: string;
    name: string;
    color: number;
    hoist: boolean;
    icon?: string;
    unicode_emoji?: string;
    position: string;
    permission: string;
    managed: boolean;
    mentionable: boolean;
}

export interface Guild {
    id: string;
    name: string;
    icon: string;
    owner: boolean;
    permissions: string;
    features: string[];
    roles: Role[];
}

export type SelectedSiderbarOptions =
    | "general"
    | "welcome"
    | "moderation"
    | "rules"
    | "reaction roles"
    | "translation and pronunciation"
    | "poll"
    | "experience"
    | "reputation"
    | "chatbot"
    | "giveaway";

export type SelectedSiderbarOptionsTitleCase =
    | "General"
    | "Welcome"
    | "Moderation"
    | "Rules"
    | "Reaction Roles"
    | "Translation and Pronunciation"
    | "Poll"
    | "Experience"
    | "Reputation"
    | "Chatbot"
    | "Giveaway";

export type ChatbotAIChoices = "Alexis" | "Chat-GPT";
