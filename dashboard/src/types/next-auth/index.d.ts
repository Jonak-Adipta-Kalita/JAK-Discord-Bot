import { DefaultSession } from "next-auth";
import { Guild } from "../typings";

declare module "next-auth" {
    interface Session {
        user: {
            guilds: Guild[];
        } & DefaultSession["user"];
    }
}
