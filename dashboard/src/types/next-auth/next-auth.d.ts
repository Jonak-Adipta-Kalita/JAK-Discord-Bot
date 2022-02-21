import { DefaultSession } from "next-auth";
import { Guild } from "../typings";

declare module "next-auth" {
    interface Session {
        user: {
            guilds?: Guild[] | null | undefined;
            accessToken?: string | null | undefined;
            refreshToken?: string | null | undefined;
        } & DefaultSession["user"];
    }
}
