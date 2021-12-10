import { getProviders, getSession } from "next-auth/react";
import Head from "next/head";
import Header from "../components/Header";

const Home = ({ providers, session }) => {
    return (
        <div className="h-screen overflow-x-scroll scrollbar-hide">
            <Head>
                <title>JAK Discord Bot - Dashboard</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Header providers={providers} />
            <main className=""></main>
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
