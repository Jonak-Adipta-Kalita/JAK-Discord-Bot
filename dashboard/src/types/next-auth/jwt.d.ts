import { Guild } from "../typings";

declare module "next-auth/jwt" {
    interface JWT {
        guilds: Guild[];
    }
}
