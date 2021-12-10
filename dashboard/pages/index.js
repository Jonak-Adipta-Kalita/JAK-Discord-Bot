import Head from "next/head";
import Header from "../components/Header";

const Home = () => {
    return (
        <div className="h-screen overflow-x-scroll scrollbar-hide">
            <Head>
                <title>JAK Discord Bot - Dashboard</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Header />
            <main className=""></main>
        </div>
    );
};

export default Home;
