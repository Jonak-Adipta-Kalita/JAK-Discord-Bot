import { getSession } from "next-auth/react";
import Head from "next/head";
import Body from "../components/Body";
import Footer from "../components/Footer";
import Header from "../components/Header";

const Home = () => {
    return (
        <div className="flex flex-col h-screen bg-[#272934]">
            <Head>
                <title>JAK Discord Bot</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Header />
            <Body />
            <Footer />
        </div>
    );
};

export default Home;

export async function getServerSideProps(context) {
    const session = await getSession(context);

    return {
        props: {
            session: session,
        },
    };
}
