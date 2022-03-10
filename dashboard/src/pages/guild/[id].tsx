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

interface ExtensionProps {
    guild: Guild | null | undefined;
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

const General = ({ guild }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );

    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Welcome = ({ guild }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );

    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Moderation = ({ guild }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );

    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Rules = ({ guild }: ExtensionProps) => {
    const [name, setName] = useState<string | null>(null);
    const [description, setDescription] = useState<string | null>(null);

    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );

    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const ReactionRoles = ({ guild }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const TranslationAndPronunciation = ({ guild }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Poll = ({ guild }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Experience = ({ guild }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Reputation = ({ guild }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Chatbot = ({ guild }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );
    return (
        <div className="guildBodyContainer">
            <p className="">Still in Development</p>
        </div>
    );
};

const Giveaway = ({ guild }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );
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

    useEffect(() => {
        setGuild(session?.user?.guilds?.filter((guild) => guild.id === id)[0]);
    }, [session]);

    const body = () => {
        if (selectedSidebarOption === "general") {
            return <General guild={guild} />;
        } else if (selectedSidebarOption === "welcome") {
            return <Welcome guild={guild} />;
        } else if (selectedSidebarOption === "moderation") {
            return <Moderation guild={guild} />;
        } else if (selectedSidebarOption === "rules") {
            return <Rules guild={guild} />;
        } else if (selectedSidebarOption === "reaction roles") {
            return <ReactionRoles guild={guild} />;
        } else if (selectedSidebarOption === "translation and pronunciation") {
            return <TranslationAndPronunciation guild={guild} />;
        } else if (selectedSidebarOption === "poll") {
            return <Poll guild={guild} />;
        } else if (selectedSidebarOption === "experience") {
            return <Experience guild={guild} />;
        } else if (selectedSidebarOption === "reputation") {
            return <Reputation guild={guild} />;
        } else if (selectedSidebarOption === "chatbot") {
            return <Chatbot guild={guild} />;
        } else if (selectedSidebarOption === "giveaway") {
            return <Giveaway guild={guild} />;
        }
    };

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
                                    className="flex flex-col items-center border-r-[3px]"
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
