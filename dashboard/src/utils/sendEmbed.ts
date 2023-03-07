import axios from "axios";

export const sendEmbed = async (
    guild_id: string,
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

    await axios.post("/api/sendMessage", { message, channel_id });
};
