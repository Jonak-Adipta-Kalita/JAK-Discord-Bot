import Head from "next/head";
import Header from "../../components/Header";
import Footer from "../../components/Footer";
import { useSession } from "next-auth/react";
import { useState, useEffect } from "react";
import { Guild } from "../../types/typings";
import { GetServerSideProps } from "next";

interface Props {
    id: string;
}

const Guild = ({ id }: Props) => {
    const { data: session } = useSession();
    const [guild, setGuild] = useState<Guild | undefined | null>(null);

    useEffect(() => {
        setGuild(session?.user?.guilds?.filter((guild) => guild.id === id)[0]);
    }, [session]);

    return (
        <div className="flex h-screen flex-col text-gray-300">
            <Head>
                <title>
                    JAK Discord Bot | Guild |{" "}
                    {guild?.name ? guild.name : "Loading"}
                </title>
            </Head>
            <Header />
            <main className="flex-1 overflow-y-auto px-2 scrollbar-hide md:px-4 lg:px-6 xl:px-10">
                {session ? (
                    <div className="">
                        {guild ? (
                            <div className=""></div>
                        ) : (
                            <div className="mx-auto mt-5 flex justify-center md:mt-10 md:max-w-3xl lg:mt-[50px] lg:max-w-5xl">
                                <p className="font-2xl font-bold">Loading...</p>
                            </div>
                        )}
                    </div>
                ) : (
                    <div className="mx-auto mt-5 flex justify-center md:mt-10 md:max-w-3xl lg:mt-[50px] lg:max-w-5xl">
                        <p className="font-2xl font-bold">
                            You need to Sign Up or Login first!!
                        </p>
                    </div>
                )}
            </main>
            <Footer />
        </div>
    );
};

export default Guild;

export const getServerSideProps: GetServerSideProps = async (context) => {
    return {
        props: {
            id: context.query.id,
        },
    };
};
