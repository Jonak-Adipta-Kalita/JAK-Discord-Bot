import type { NextApiRequest, NextApiResponse } from "next";
import NextAuth from "next-auth";
import DiscordProvider from "next-auth/providers/discord";
import axios from "axios";
import { Guild, Role } from "../../../types/typings";

const getRoles = async (botGuild: Guild): Promise<Role[]> => {
    const res = await axios.get<Role[]>(
        `https://discord.com/api/v8/guilds/${botGuild.id}/roles`,
        {
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bot ${process.env.TOKEN}`,
            },
        }
    );

    return res.data.filter(
        (role: Role) => role.name !== "@everyone" && !role.managed
    );
};

export default async (req: NextApiRequest, res: NextApiResponse) => {
    return await NextAuth(req, res, {
        providers: [
            DiscordProvider({
                clientId: process.env.DISCORD_CLIENT_ID!,
                clientSecret: process.env.DISCORD_CLIENT_SECRET!,
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

                if (account && user) {
                    const commonGuilds: Guild[] = [];

                    const userGuildsRes = await axios.get<Guild[]>(
                        "https://discord.com/api/v8/users/@me/guilds",
                        {
                            headers: {
                                "Content-Type": "application/json",
                                Authorization: `Bearer ${token.accessToken}`,
                            },
                        }
                    );

                    const botGuildsRes = await axios.get<Guild[]>(
                        "https://discord.com/api/v8/users/@me/guilds",
                        {
                            headers: {
                                "Content-Type": "application/json",
                                Authorization: `Bot ${process.env.TOKEN}`,
                            },
                        }
                    );

                    const pushPromises = userGuildsRes.data.map(
                        async (userGuild: Guild) => {
                            return Promise.all(
                                botGuildsRes.data.map(
                                    async (botGuild: Guild) => {
                                        if (
                                            userGuild.id === botGuild.id &&
                                            userGuild.owner
                                        ) {
                                            const roles = await getRoles(
                                                botGuild
                                            );
                                            return new Promise<void>(
                                                (resolve) => {
                                                    commonGuilds.push({
                                                        ...botGuild,
                                                        roles,
                                                    });
                                                    resolve();
                                                }
                                            );
                                        }
                                    }
                                )
                            );
                        }
                    );

                    await Promise.all(pushPromises);

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
