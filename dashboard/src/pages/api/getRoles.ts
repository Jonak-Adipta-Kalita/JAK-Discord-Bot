import axios from "axios";
import { NextApiRequest, NextApiResponse } from "next";
import { getGuild } from "../../../utils/getGuild";
import { Guild, Role } from "../../types/typings";

const getRoles = async (guild: Guild): Promise<Role[]> => {
    const res = await axios.get<Role[]>(
        `https://discord.com/api/v8/guilds/${guild.id}/roles`,
        {
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bot ${process.env.TOKEN}`,
            },
        }
    );

    return res.data.filter(
        (role) => role.name !== "@everyone" && !role.managed
    );
};

export default async (
    req: NextApiRequest,
    res: NextApiResponse<Role[] | { error: string }>
) => {
    if (!(req.method === "POST")) {
        res.setHeader("Allow", ["POST"]);
        return res
            .status(405)
            .json({ error: `Method ${req.method} now allowed` });
    }

    const { guild_id } = req.body;

    const guild: Guild = await getGuild(guild_id as string);
    const roles = await getRoles(guild);

    res.status(200).json(roles);
};
