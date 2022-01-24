import Head from "next/head";
import Footer from "../components/Footer";
import Header from "../components/Header";

const _404 = () => {
    return (
        <div className="flex flex-col h-screen bg-[#272934]">
            <Head>
                <title>JAK Discord Bot | Page Not Found</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Header />
            <main className="flex-1 overflow-y-auto scrollbar-hide bg-[#272934] px-2 md:px-4 lg:px-6 xl:px-10">
                <div className="flex justify-center">
                    <h1 className="text-white font-bold text-2xl">
                        Page Not Found!!
                    </h1>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default _404;
