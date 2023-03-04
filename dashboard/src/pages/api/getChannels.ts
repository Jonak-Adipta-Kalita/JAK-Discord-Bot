import axios from "axios";
import { NextApiRequest, NextApiResponse } from "next";
import { getGuild } from "../../../utils/getGuild";
import { Channel, Guild } from "../../types/typings";

const getChannels = async (guild: Guild): Promise<Channel[]> => {
    const res = await axios.get<Channel[]>(
        `${process.env.DISCORD_API_BASE_URL}/guilds/${guild.id}/channels`,
        {
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bot ${process.env.TOKEN}`,
            },
        }
    );

    return res.data;
};

export default async (
    req: NextApiRequest,
    res: NextApiResponse<Channel[] | { error: string }>
) => {
    if (!(req.method === "POST")) {
        res.setHeader("Allow", ["POST"]);
        return res
            .status(405)
            .json({ error: `Method ${req.method} now allowed` });
    }

    const { guild_id } = req.body;

    const guild: Guild = await getGuild(guild_id as string);
    const channels = await getChannels(guild);

    res.status(200).json(channels);
};
