import "../styles/globals.css";
import { RecoilRoot } from "recoil";
import { Session } from "next-auth";
import { SessionProvider } from "next-auth/react";
import Progressbar from "@badrap/bar-of-progress";
import Router from "next/router";
import type { AppProps } from "next/app";

const progress = new Progressbar({
    size: 4,
    color: "#FD5B61",
    className: "z-50",
    delay: 100,
});

Router.events.on("routeChangeStart", progress.start);
Router.events.on("routeChangeComplete", progress.finish);
Router.events.on("routeChangeError", progress.finish);

const MyApp = ({
    Component,
    pageProps: { session, ...pageProps },
}: AppProps<{
    session: Session;
}>) => {
    return (
        <SessionProvider session={session}>
            <RecoilRoot>
                <Component {...pageProps} />
            </RecoilRoot>
        </SessionProvider>
    );
};

export default MyApp;
