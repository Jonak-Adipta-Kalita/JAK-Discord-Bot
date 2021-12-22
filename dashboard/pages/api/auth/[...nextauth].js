import NextAuth from "next-auth";
import DiscordProvider from "next-auth/providers/discord";

export default async function auth(req, res) {
    return await NextAuth(req, res, {
        providers: [
            DiscordProvider({
                clientId: process.env.DISCORD_CLIENT_ID,
                clientSecret: process.env.DISCORD_CLIENT_SECRET,
                authorization: {
                    params: {
                        scope: "identify guilds email",
                    },
                },
            }),
        ],
        secret: process.env.JWT_SECRET,
        pages: {
            signIn: "/login",
        },
    });
}
