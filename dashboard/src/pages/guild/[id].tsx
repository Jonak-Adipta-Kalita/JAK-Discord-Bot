import Head from "next/head";
import Header from "../../components/Header";
import Footer from "../../components/Footer";
import { useSession } from "next-auth/react";
import { useState, useEffect } from "react";
import { Guild } from "../../types/typings";
import { GetServerSideProps } from "next";
import {
    HomeIcon,
    HandIcon,
    StopIcon,
    DocumentTextIcon,
    HeartIcon,
    StarIcon,
    TranslateIcon,
    SparklesIcon,
    ClipboardListIcon,
} from "@heroicons/react/outline";
import { useRecoilState, useRecoilValue } from "recoil";
import { selectedSidebarOptionState } from "../../atoms/dashboard";
import TrophyIcon from "../../components/icons/TrophyIcon";
import BotIcon from "../../components/icons/BotIcon";

interface Props {
    id: string;
}

const SidebarOption = ({ name, Icon }: { name: string; Icon: any }) => {
    const [selectedSidebarOption, setSelectedSidebarOption] = useRecoilState(
        selectedSidebarOptionState
    );

    return (
        <div
            className={`flex w-[50px] cursor-pointer items-center space-x-7 rounded-lg p-2 ${
                selectedSidebarOption === name.toLowerCase()
                    ? "bg-gray-700"
                    : "hover:bg-gray-700"
            } lg:w-[200px] xl:w-[240px]`}
            onClick={() => setSelectedSidebarOption(name.toLowerCase())}
        >
            <Icon className="h-7 w-7 text-gray-300"></Icon>
            <p className="text-md flex-end hidden cursor-pointer font-semibold lg:inline">
                {name}
            </p>
        </div>
    );
};

const General = () => {
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Welcome = () => {
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Moderation = () => {
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Rules = () => {
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const ReactionRoles = () => {
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const TranslationAndPronunciation = () => {
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Experience = () => {
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Reputation = () => {
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Chatbot = () => {
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Giveaway = () => {
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Guild = ({ id }: Props) => {
    const { data: session } = useSession();
    const [guild, setGuild] = useState<Guild | undefined | null>(null);
    const selectedSidebarOption = useRecoilValue(selectedSidebarOptionState);

    const body = () => {
        if (selectedSidebarOption === "general") {
            return <General />;
        } else if (selectedSidebarOption === "welcome") {
            return <Welcome />;
        } else if (selectedSidebarOption === "moderation") {
            return <Moderation />;
        } else if (selectedSidebarOption === "rules") {
            return <Rules />;
        } else if (selectedSidebarOption === "reaction roles") {
            return <ReactionRoles />;
        } else if (selectedSidebarOption === "translation and pronunciation") {
            return <TranslationAndPronunciation />;
        } else if (selectedSidebarOption === "experience") {
            return <Experience />;
        } else if (selectedSidebarOption === "reputation") {
            return <Reputation />;
        } else if (selectedSidebarOption === "chatbot") {
            return <Chatbot />;
        } else if (selectedSidebarOption === "giveaway") {
            return <Giveaway />;
        }
    };

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
            <main className="flex-1 overflow-y-auto scrollbar-hide">
                {session ? (
                    <div className="">
                        {guild ? (
                            <div className="flex">
                                <div
                                    className="flex h-screen flex-col items-center border-r-[3px]"
                                    style={{ flex: 0.2 }}
                                >
                                    <div className="mt-5" />
                                    <div className="">
                                        <SidebarOption
                                            name="General"
                                            Icon={HomeIcon}
                                        />
                                    </div>
                                    <div className="mt-7">
                                        <div className="flex justify-center">
                                            <p className="mb-4 hidden text-sm font-bold lg:inline">
                                                Server Management
                                            </p>
                                        </div>

                                        <div className="space-y-2">
                                            <SidebarOption
                                                name="Welcome"
                                                Icon={HandIcon}
                                            />
                                            <SidebarOption
                                                name="Moderation"
                                                Icon={StopIcon}
                                            />
                                            <SidebarOption
                                                name="Rules"
                                                Icon={DocumentTextIcon}
                                            />
                                            <SidebarOption
                                                name="Reaction Roles"
                                                Icon={HeartIcon}
                                            />
                                            <SidebarOption
                                                name="Translation and Pronunciation"
                                                Icon={TranslateIcon}
                                            />
                                            <SidebarOption
                                                name="Poll"
                                                Icon={ClipboardListIcon}
                                            />
                                        </div>
                                    </div>
                                    <div className="mt-7">
                                        <div className="flex justify-center">
                                            <p className="mb-4 hidden text-sm font-bold lg:inline">
                                                Fun
                                            </p>
                                        </div>

                                        <div className="space-y-2">
                                            <SidebarOption
                                                name="Experience"
                                                Icon={TrophyIcon}
                                            />
                                            <SidebarOption
                                                name="Reputation"
                                                Icon={StarIcon}
                                            />
                                            <SidebarOption
                                                name="Chatbot"
                                                Icon={BotIcon}
                                            />
                                            <SidebarOption
                                                name="Giveaway"
                                                Icon={SparklesIcon}
                                            />
                                        </div>
                                    </div>
                                </div>
                                <div
                                    className="mt-[10px]"
                                    style={{ flex: 0.8 }}
                                >
                                    {body()}
                                </div>
                            </div>
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
