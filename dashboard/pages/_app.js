import "../styles/globals.css";
import { RecoilRoot } from "recoil";
import { SessionProvider } from "next-auth/react";
import propTypes from "prop-types";

const MyApp = ({ Component, pageProps: { session, ...pageProps } }) => {
    return (
        <SessionProvider session={session}>
            <RecoilRoot>
                <Component {...pageProps} />
            </RecoilRoot>
        </SessionProvider>
    );
};

MyApp.propTypes = {
    Component: propTypes.any.isRequired,
    pageProps: propTypes.any.isRequired,
};

export default MyApp;
