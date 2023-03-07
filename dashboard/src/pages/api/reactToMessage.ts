import axios from "axios";
import type { NextApiRequest, NextApiResponse } from "next";
import { ReactionRole } from "../../types/typings";

export default async (req: NextApiRequest, res: NextApiResponse) => {
    if (!(req.method === "POST")) {
        res.setHeader("Allow", ["POST"]);
        return res
            .status(405)
            .json({ error: `Method ${req.method} now allowed` });
    }

    const { message_id, channel_id, reactionRoles } = req.body;

    reactionRoles.map(async (reactionRole: ReactionRole) => {
        await axios.put(
            encodeURI(
                `${
                    process.env.DISCORD_API_BASE_URL
                }/channels/${channel_id}/messages/${message_id}/reactions/${
                    reactionRole.emoji!.emoji
                }/@me`
            ),
            {},
            {
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bot ${process.env.TOKEN}`,
                },
            }
        );
        await new Promise((resolve) => {
            setTimeout(resolve, 3000);
        });
    });
};
