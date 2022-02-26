import { GetServerSideProps } from "next";
import { getSession } from "next-auth/react";
import Head from "next/head";
import Header from "../components/Header";
import Footer from "../components/Footer";
import { useSession } from "next-auth/react";
import { useState, useEffect } from "react";
import { editMessage } from "@xxjonakadiptaxx/jak_javascript_package";
import { Command } from "../types/typings";
import axios from "axios";

interface Props {
    commandsData: object;
}

const Home = ({ commandsData }: Props) => {
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
        <div className="flex h-screen flex-col">
            <Head>
                <title>JAK Discord Bot | Home</title>
            </Head>
            <Header />
            <main className="flex-1 overflow-y-auto px-2 scrollbar-hide md:px-4 lg:px-6 xl:px-10">
                <div className="mx-auto mt-28 mb-5 space-y-4 text-gray-300 md:max-w-3xl lg:mt-20 lg:max-w-5xl">
                    {session && (
                        <div className="flex justify-center pb-[50px]">
                            <a
                                href="https://discord.com/api/oauth2/authorize?client_id=756402881913028689&permissions=8&redirect_uri=https%3A%2F%2Fjak-discord-bot.vercel.app%2Fapi%2Fauth%2Fcallback%2Fdiscord&response_type=code&scope=bot%20applications.commands"
                                target="_blank"
                                className="bodyBtn cursor-pointer bg-[#3994ff] text-white active:bg-[#3572a5]"
                                rel="noreferrer"
                            >
                                Add to Server
                            </a>
                        </div>
                    )}
                    <div className="">
                        <p className="text-2xl font-bold">Commands</p>
                        <div className="mt-[20px] flex items-center justify-center space-x-4 rounded-xl border-[0.1px] p-4">
                            {categories.map((category) => (
                                <p
                                    className={`cursor-pointer text-lg ${
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
                        <div className="mt-[20px] space-y-4 rounded-xl border-[0.1px] p-4">
                            {commands?.map((command) => (
                                <div
                                    className="space-y-[10px] rounded-xl border-[0.1px] p-4"
                                    key={command.id}
                                >
                                    <p className="">
                                        Name:{" "}
                                        {new editMessage(
                                            command.name.replace("_", " ")
                                        ).toTitleCase()}
                                    </p>
                                    <p className="">Usage: {command.usage}</p>
                                    <p className="">
                                        {console.log(command.has_slash_command)}
                                        Has Slash Command:{" "}
                                        {command.has_slash_command
                                            ? "Yes"
                                            : "No"}
                                    </p>
                                    <p className="">
                                        Description: {command.description}
                                    </p>
                                </div>
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

    const commandsDataRes = await axios.get(
        "https://raw.githubusercontent.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/main/resources/commands.json",
        {
            headers: {
                "Content-Type": "application/json",
            },
        }
    );

    const commandsData = commandsDataRes.data;

    return {
        props: {
            session: session,
            commandsData,
        },
    };
};
