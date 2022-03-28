import Head from "next/head";
import Header from "../components/Header";
import Footer from "../components/Footer";
import { GetServerSideProps } from "next";
import { getSession } from "next-auth/react";

const _404 = () => {
    return (
        <div className="flex h-screen flex-col">
            <Head>
                <title>JAK Discord Bot | Page Not Found</title>
            </Head>
            <Header />
            <main className="flex-1 overflow-y-auto px-2 scrollbar-hide md:px-4 lg:px-6 xl:px-10">
                <div className="mt-10 flex justify-center lg:mt-[50px]">
                    <p className="text-2xl font-bold text-white">
                        Page Not Found!!
                    </p>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default _404;

export const getServerSideProps: GetServerSideProps = async (context) => {
    const session = await getSession(context);

    return {
        props: {
            session: session,
        },
    };
};
