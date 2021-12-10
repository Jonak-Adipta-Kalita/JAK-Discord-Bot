import Head from "next/head";
import Header from "../components/Header";

const Home = () => {
    return (
        <div className="bg-[#272934] h-screen overflow-x-scroll scrollbar-hide">
            <Head>
                <title>JAK Discord Bot - Dashboard</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <div className="">
                <Header />
            </div>
        </div>
    );
};

export default Home;
