import { NextResponse } from "next/server";
import { getToken } from "next-auth/jwt";

export const middleware: any = async (req: any) => {
    const token = await getToken({ req, secret: process.env.JWT_SECRET! });
    const { pathname } = req.nextUrl;

    if (!token && pathname.includes("/dashboard")) {
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
