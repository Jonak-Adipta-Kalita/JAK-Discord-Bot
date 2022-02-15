import Head from "next/head";
import Header from "../components/Header";
import Footer from "../components/Footer";

const _500 = () => {
    return (
        <div className="flex flex-col h-screen">
            <Head>
                <title>JAK Discord Bot | 500 Error</title>
            </Head>
            <Header />
            <main className="flex-1 overflow-y-auto scrollbar-hide px-2 md:px-4 lg:px-6 xl:px-10">
                <div className="flex justify-center">
                    <p className="text-white font-bold text-2xl">500 Error!!</p>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default _500;
