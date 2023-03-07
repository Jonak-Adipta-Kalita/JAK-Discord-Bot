import axios from "axios";

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
                timestamp: new Date().toISOString(),
            },
        ],
    };

    const sent_message = await (
        await axios.post(
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
