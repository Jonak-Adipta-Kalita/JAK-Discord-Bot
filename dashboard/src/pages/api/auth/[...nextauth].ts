import type { NextApiRequest, NextApiResponse } from "next";
import NextAuth from "next-auth";
import DiscordProvider from "next-auth/providers/discord";
import axios from "axios";
import { Guild } from "../../../types/typings";

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
            async jwt({ token, account }: any) {
                if (account) token.accessToken = account.access_token;

                const commonGuilds: Guild[] = [];

                const userGuildsRes = await axios.get(
                    "https://discord.com/api/v8/users/@me/guilds",
                    {
                        headers: {
                            "Content-Type": "application/json",
                            Authorization: `Bearer ${token.accessToken}`,
                        },
                    }
                );

                const botGuildsRes = await axios.get(
                    "https://discord.com/api/v8/users/@me/guilds",
                    {
                        headers: {
                            "Content-Type": "application/json",
                            Authorization: `Bot ${process.env.TOKEN}`,
                        },
                    }
                );

                userGuildsRes.data.map((userGuild: Guild) => {
                    botGuildsRes.data.map((botGuild: Guild) => {
                        if (userGuild.id === botGuild.id && userGuild.owner) {
                            commonGuilds.push(userGuild);
                        }
                    });
                });

                token.guilds = commonGuilds;

                return token;
            },
            async session({ session, token }: any) {
                session.user!.guilds = token.guilds;

                return session;
            },
        },
    });
};
