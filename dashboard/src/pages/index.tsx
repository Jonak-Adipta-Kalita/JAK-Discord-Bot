import { GetServerSideProps } from "next";
import { getSession } from "next-auth/react";
import Head from "next/head";
import Header from "../components/Header";
import Footer from "../components/Footer";
import { useSession } from "next-auth/react";
import { useState, useEffect } from "react";
import { editMessage } from "@xxjonakadiptaxx/jak_javascript_package";
import commandsData from "../../public/data/commands.json";
import { Command } from "../typings";
import CommandComponent from "../components/Command";

const Home = () => {
    const { data: session } = useSession();
    const categories: string[] = Object.keys(commandsData);
    const [currentCategory, setCurrentCategory] = useState<string>(
        categories[0]
    );
    const [commands, setCommands] = useState<Command[]>();

    useEffect(() => {
        setCommands(
            (commandsData as Record<string, Command[]>)[currentCategory]
        );
    }, [currentCategory]);

    return (
        <div className="flex flex-col h-screen">
            <Head>
                <title>JAK Discord Bot | Home</title>
            </Head>
            <Header />
            <main className="flex-1 overflow-y-auto scrollbar-hide px-2 md:px-4 lg:px-6 xl:px-10">
                <div className="md:max-w-3xl lg:max-w-5xl mx-auto space-y-4 mb-5 mt-10 lg:mt-20 text-gray-300">
                    {session && (
                        <div className="flex justify-center">
                            <a
                                href="https://discord.com/api/oauth2/authorize?client_id=756402881913028689&permissions=8&redirect_uri=https%3A%2F%2Fjak-discord-bot.vercel.app%2Fapi%2Fauth%2Fcallback%2Fdiscord&response_type=code&scope=bot%20applications.commands"
                                target="_blank"
                                className="bodyBtn text-white bg-[#3994ff] active:bg-[#3572a5] cursor-pointer"
                                rel="noreferrer"
                            >
                                Add to Server
                            </a>
                        </div>
                    )}
                    <div className="pt-[50px]">
                        <p className="text-2xl font-bold">Commands</p>
                        <div className="flex items-center justify-center space-x-4 mt-[20px] p-4 border-[0.1px] rounded-xl">
                            {categories.map((category) => (
                                <p
                                    className={`text-lg cursor-pointer ${
                                        category === currentCategory
                                            ? "text-gray-500"
                                            : "text-gray-300"
                                    }`}
                                    key={category}
                                    onClick={() => setCurrentCategory(category)}
                                >
                                    {new editMessage(category).toTitleCase()}
                                </p>
                            ))}
                        </div>
                        <div className="mt-[20px] p-4 border-[0.1px] rounded-xl space-y-4">
                            {commands?.map((command) => (
                                <CommandComponent
                                    key={command.id}
                                    command={command}
                                />
                            ))}
                        </div>
                    </div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default Home;

export const getServerSideProps: GetServerSideProps = async (context) => {
    const session = await getSession(context);

    return {
        props: {
            session: session,
        },
    };
};
