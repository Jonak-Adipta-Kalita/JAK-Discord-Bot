import { Guild } from "../typings";

declare module "next-auth/jwt" {
    interface JWT {
        accessToken: string | null | undefined;
        refreshToken: string | null | undefined;
        accessTokenExpires: number | null | undefined;
        guilds: Guild[] | null | undefined;
    }
}
