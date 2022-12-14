import { NextResponse, NextRequest } from "next/server";
import { getToken } from "next-auth/jwt";

export const middleware = async (req: any) => {
    const token = await getToken({ req, secret: process.env.JWT_SECRET! });
    const { pathname }: NextRequest["nextUrl"] = req.nextUrl;

    if (
        !token &&
        (pathname.includes("/dashboard") ||
            pathname.includes("/guild") ||
            pathname.includes("/suggestion"))
    ) {
        const url = req.nextUrl.clone();
        url.pathname = "/login";

        return NextResponse.rewrite(url);
    }

    if (token && pathname.includes("/login")) {
        const url = req.nextUrl.clone();
        url.pathname = "/";

        return NextResponse.rewrite(url);
    }
};
