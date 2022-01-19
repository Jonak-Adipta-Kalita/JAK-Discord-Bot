import { getProviders, signIn } from "next-auth/react";
import Head from "next/head";
import Header from "../components/Header";
import propTypes from "prop-types";

const Login = ({ providers }) => {
    const provider = Object.values(providers).map((provider) => provider);

    return (
        <div className="h-screen bg-[#272934]">
            <Head>
                <title>JAK Discord Bot | Login</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Header />
            <div className="flex justify-center mt-20">
                <button
                    className="body-btn text-gray-400 cursor-pointer border-[0.1px] border-white"
                    onClick={() => signIn(provider[0].id, { callbackUrl: "/" })}
                >
                    Login with Discord
                </button>
            </div>
        </div>
    );
};

Login.propTypes = {
    providers: propTypes.object.isRequired,
};

export default Login;

export async function getServerSideProps() {
    const providers = await getProviders();

    return {
        props: {
            providers: providers,
        },
    };
}
