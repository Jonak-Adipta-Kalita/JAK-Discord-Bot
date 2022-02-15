import { getProviders, signIn } from "next-auth/react";
import Head from "next/head";
import Header from "../components/Header";
import Footer from "../components/Footer";
import { GetServerSideProps } from "next";
import { Provider } from "next-auth/providers";

interface Props {
    providers: Provider[];
}

const Login = ({ providers }: Props) => {
    const provider = Object.values(providers).map((provider) => provider);

    return (
        <div className="flex flex-col h-screen">
            <Head>
                <title>JAK Discord Bot | Login</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Header />
            <main className="flex-1 overflow-y-auto scrollbar-hide">
                <div className="flex justify-center mt-20">
                    <button
                        className="bodyBtn text-gray-400 cursor-pointer border-[0.1px] border-white"
                        onClick={() =>
                            signIn(provider[0].id, { callbackUrl: "/" })
                        }
                    >
                        Login with Discord
                    </button>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default Login;

export const getServerSideProps: GetServerSideProps = async () => {
    const providers = await getProviders();

    return {
        props: {
            providers: providers,
        },
    };
};
