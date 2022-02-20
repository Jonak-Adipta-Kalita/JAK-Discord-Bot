import type { NextApiRequest, NextApiResponse } from "next";
import NextAuth from "next-auth";
import DiscordProvider from "next-auth/providers/discord";
import axios from "axios";

export default async (req: NextApiRequest, res: NextApiResponse) => {
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
        callbacks: {
            async jwt({ token, account }) {
                if (account) token.accessToken = account.access_token;

                const apiRes = await axios.get(
                    "https://discord.com/api/v8/users/@me/guilds",
                    {
                        headers: {
                            "Content-Type": "application/json",
                            Authorization: `Bot ${process.env.TOKEN}`,
                        },
                    }
                );

                token.guilds = apiRes.data;

                return token;
            },
            async session({ session, token }) {
                session.user!.guilds = token.guilds;

                return session;
            },
        },
    });
};
