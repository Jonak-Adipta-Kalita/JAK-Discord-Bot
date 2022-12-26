export interface Command {
    id: number;
    name: string;
    usage: string;
    has_slash_command: boolean;
    description: string;
}

export interface Overwrite {
    id: string;
    type: number;
    allow: string;
    deny: string;
}

export interface User {
    id: string;
    username: string;
    discriminator: string;
    avatar: string;
    bot: boolean;
    system: boolean;
    mfa_enabled: boolean;
    banner: string;
    accent_color: number;
    locale: string;
    verified: boolean;
    email: string;
    flags: number;
    premium_type: number;
    public_flags: number;
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
    channels: Channel[];
}

export interface Channel {
    id: string;
    type: number;
    guild_id: string;
    position: string;
    permission_overwrites: Overwrite[];
    name: string;
    topic: string;
    nsfw: boolean;
    last_message_id: string;
    bitrate: string;
    user_limit: string;
    rate_limit_per_user: string;
    recipients: User[];
    icon: string;
    owner_id: string;
    application_id: string;
    parent_id: string;
    last_pin_timestamp: string;
    rtc_region: string;
    video_quality_mode: string;
    message_count: string;
    member_count: string;
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
