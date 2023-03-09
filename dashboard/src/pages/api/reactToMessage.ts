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

    const {
        message_id,
        channel_id,
        reactionRoles,
    }: {
        message_id: string;
        channel_id: string;
        reactionRoles: ReactionRole[];
    } = req.body;

    const delay = (ms: number) =>
        new Promise((resolve) => setTimeout(resolve, ms));

    async function sendRequests() {
        for (let i = 0; i < reactionRoles.length; i++) {
            await delay(3000);
            console.log(i);
            await axios.put(
                encodeURI(
                    `${
                        process.env.DISCORD_API_BASE_URL
                    }/channels/${channel_id}/messages/${message_id}/reactions/${
                        reactionRoles[i].emoji!.emoji
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
        }
    }

    sendRequests();

    res.status(200).json({ message: "Reacted!!" });
};
