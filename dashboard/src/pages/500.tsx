import Head from "next/head";
import Header from "../components/Header";
import Footer from "../components/Footer";

const _500 = () => {
    return (
        <div className="flex h-screen flex-col">
            <Head>
                <title>JAK Discord Bot | 500 Error</title>
            </Head>
            <Header />
            <main className="flex-1 overflow-y-auto px-2 scrollbar-hide md:px-4 lg:px-6 xl:px-10">
                <div className="flex justify-center">
                    <p className="text-2xl font-bold text-white">500 Error!!</p>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default _500;
