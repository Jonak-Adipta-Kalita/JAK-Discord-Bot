import type { NextApiRequest, NextApiResponse } from "next";
import NextAuth from "next-auth";
import DiscordProvider from "next-auth/providers/discord";
import axios from "axios";
import { Guild, Role } from "../../../types/typings";

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
            async jwt({ token, account, user }) {
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
                    botGuildsRes.data.map(async (botGuild: Guild) => {
                        if (userGuild.id === botGuild.id && userGuild.owner) {
                            const allowedRoles: Role[] = [];

                            // const rolesRes = await axios.get(
                            //     `https://discord.com/api/v8/guilds/${userGuild.id}/roles`,
                            //     {
                            //         headers: {
                            //             "Content-Type": "application/json",
                            //             Authorization: `Bot ${process.env.TOKEN}`,
                            //         },
                            //     }
                            // );

                            // rolesRes.data.map((role: Role) => {
                            //     if (
                            //         role.name !== "@everyone" &&
                            //         !role.managed
                            //     ) {
                            //         allowedRoles.push(role);
                            //     }
                            // });

                            commonGuilds.push({
                                ...userGuild,
                                roles: allowedRoles,
                            });
                        }
                    });
                });

                if (account && user) {
                    return {
                        ...token,
                        guilds: commonGuilds,
                        accessToken: account.access_token,
                        refreshToken: account.refresh_token,
                        accessTokenExpires:
                            account?.expires_at && account.expires_at * 1000,
                    };
                }

                if (Date.now() < token.accessTokenExpires!) return token;

                return token;
            },
            async session({ session, token }) {
                session.user.accessToken = token.accessToken;
                session.user.refreshToken = token.refreshToken;
                session.user.guilds = token.guilds;

                return session;
            },
        },
    });
};
