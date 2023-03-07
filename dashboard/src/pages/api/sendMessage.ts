import axios from "axios";
import type { NextApiRequest, NextApiResponse } from "next";

export default async (req: NextApiRequest, res: NextApiResponse) => {
    if (!(req.method === "POST")) {
        res.setHeader("Allow", ["POST"]);
        return res
            .status(405)
            .json({ error: `Method ${req.method} now allowed` });
    }

    const { message, channel_id } = req.body;

    const sent_message = await axios.post(
        `${process.env.DISCORD_API_BASE_URL}/channels/${channel_id}/messages`,
        message,
        {
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bot ${process.env.TOKEN}`,
            },
        }
    );

    res.status(200).json(sent_message.data);
};
