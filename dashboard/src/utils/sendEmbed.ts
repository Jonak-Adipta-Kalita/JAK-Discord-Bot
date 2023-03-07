import axios from "axios";
import { Message } from "../types/typings";

export const sendEmbed = async (
    channel_id: string,
    embedTitle: string,
    embedDescription: string
) => {
    const message = {
        embeds: [
            {
                title: embedTitle,
                description: embedDescription,
                color: 0x3498db,
            },
        ],
    };

    const sent_message = (
        await axios.post<Message>(
            "/api/sendMessage",
            { message, channel_id },
            {
                headers: {
                    "Content-Type": "application/json",
                },
            }
        )
    ).data;

    return sent_message;
};
