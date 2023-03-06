import discordEmojis from "discord-emoji";

const convertToArray = (emojies: any) => {
    return Object.entries(emojies) as [string, string][];
};

export const people = convertToArray(discordEmojis.people);
export const nature = convertToArray(discordEmojis.nature);
export const food = convertToArray(discordEmojis.food);
export const activity = convertToArray(discordEmojis.activity);
export const travel = convertToArray(discordEmojis.travel);
export const objects = convertToArray(discordEmojis.objects);
export const symbols = convertToArray(discordEmojis.symbols);
export const flags = convertToArray(discordEmojis.flags);
