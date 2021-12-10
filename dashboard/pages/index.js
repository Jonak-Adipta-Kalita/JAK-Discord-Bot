import { getProviders, getSession, useSession } from "next-auth/react";
import Head from "next/head";
import Body from "../components/Body";
import Header from "../components/Header";

const Home = ({ providers }) => {
    const { data: session } = useSession();

    return (
        <div className="h-screen overflow-x-scroll scrollbar-hide bg-[#272934]">
            <Head>
                <title>JAK Discord Bot</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Header providers={providers} />
            <Body />
        </div>
    );
};

export default Home;

export async function getServerSideProps(context) {
    const providers = await getProviders();
    const session = await getSession(context);

    return {
        props: {
            providers: providers,
            session: session,
        },
    };
}
