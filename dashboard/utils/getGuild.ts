import axios from "axios";
import { Guild } from "../src/types/typings";

export const getGuild = async (guild_id: string) => {
    const res = await axios.get<Guild>(
        `${process.env.DISCORD_API_BASE_URL}/guilds/${guild_id}`,
        {
            headers: {
                "Content-Type": "application/json",
            },
        }
    );

    return res.data;
};
