import Head from "next/head";
import Header from "../../components/Header";
import Footer from "../../components/Footer";
import { getSession, useSession } from "next-auth/react";
import { useState, useEffect, FormEvent, MouseEvent } from "react";
import {
    Channel,
    Guild,
    Role,
    SelectedSiderbarOptions,
    SelectedSiderbarOptionsTitleCase,
} from "../../types/typings";
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
    XIcon,
} from "@heroicons/react/outline";
import { useRecoilState, useRecoilValue } from "recoil";
import { selectedSidebarOptionState } from "../../atoms/dashboard";
import TrophyIcon from "../../components/icons/TrophyIcon";
import BotIcon from "../../components/icons/BotIcon";
import { child, ref, set } from "firebase/database";
import { db } from "../../firebase";
import { useObjectVal } from "react-firebase-hooks/database";
import toast from "react-hot-toast";
import toastDefaultOptions from "../../utils/toastDefaultOptions";
import axios from "axios";
import { Session } from "next-auth";

interface Props {
    id: string;
    roles: Role[];
    channels: Channel[];
    session: Session | null | undefined;
}

interface ExtensionProps {
    guild: Guild | null | undefined;
    roles: Role[];
    channels: Channel[];
    session: Session | null | undefined;
}

const SidebarOption = ({
    name,
    Icon,
}: {
    name: SelectedSiderbarOptionsTitleCase;
    Icon: any;
}) => {
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
            onClick={() =>
                setSelectedSidebarOption(
                    name.toLowerCase() as SelectedSiderbarOptions
                )
            }
        >
            <Icon className="h-7 w-7 text-gray-300"></Icon>
            <p className="text-md flex-end hidden cursor-pointer font-semibold lg:inline">
                {name}
            </p>
        </div>
    );
};

const General = ({ guild }: ExtensionProps) => {
    const [customPrefix, setCustomPrefix] = useState<string>("");
    const prefixRef = child(child(ref(db, `guilds`), guild?.id!), "prefix");
    const [currentPrefix, currentPrefixLoading, currentPrefixError] =
        useObjectVal<string>(prefixRef);

    if (!guild || currentPrefixLoading || currentPrefixError)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );

    const addCustomPrefix = (e: FormEvent) => {
        e.preventDefault();

        const notification = toast.loading("Adding Custom Prefix...");

        if (customPrefix === "") {
            toast.error("Please fill in the Data properly!!", {
                ...toastDefaultOptions,
                id: notification,
            });
            return;
        }
        set(prefixRef, customPrefix);

        toast.success("Successfully Added Custom Prefix!!", {
            ...toastDefaultOptions,
            id: notification,
        });

        setCustomPrefix("");
    };

    return (
        <div className="guildBodyContainer">
            <div className="pt-[60px]" />
            <div className="flex flex-col">
                <form
                    onSubmit={(e) => addCustomPrefix(e)}
                    className="justify-center space-y-4 md:flex md:items-center md:space-y-0 md:space-x-6"
                >
                    <p className="text-xl">Prefix</p>
                    <input
                        type="text"
                        className="guildBodyInput"
                        placeholder={
                            currentPrefix
                                ? `Current Prefix: ${currentPrefix}`
                                : "Your Custom Prefix"
                        }
                        value={customPrefix}
                        onChange={(e) => setCustomPrefix(e.target.value)}
                    />
                    <button
                        className="ml-[120px] mt-4 transform rounded-xl border-[4px] p-4 transition duration-100 ease-out hover:scale-125 md:mt-0 md:ml-0"
                        type="submit"
                    >
                        Submit
                    </button>
                </form>
            </div>
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
    const [name, setName] = useState<string>("");
    const [description, setDescription] = useState<string>("");

    const rulesRef = child(child(ref(db, `guilds`), guild?.id!), "rules");
    const [existingRules, existingRulesLoading, existingRulesError] =
        useObjectVal<[]>(rulesRef);

    const removeRule = (
        e: MouseEvent<SVGSVGElement, globalThis.MouseEvent>,
        index: number
    ) => {
        e.preventDefault();

        const notification = toast.loading("Removing Rule...");

        const modifiedRules = existingRules;
        delete modifiedRules?.[index];
        set(rulesRef, modifiedRules);

        toast.success("Rule Removed!", {
            ...toastDefaultOptions,
            id: notification,
        });
    };

    if (!guild || existingRulesLoading || existingRulesError)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );

    const showExistingRules = () => {
        if (!existingRules) return <div className=""></div>;

        return (
            <div className="mt-[70px]">
                {existingRules.map((rule: string[], i) => (
                    <div
                        className="flex items-center justify-between rounded-xl bg-gray-700 px-6 py-3"
                        key={i}
                    >
                        <div className="space-y-2">
                            <p className="">Name: {rule[0]}</p>
                            <p className="">Description: {rule[1]}</p>
                        </div>
                        <XIcon
                            className="h-10 w-10 cursor-pointer"
                            onClick={(e) => removeRule(e, i)}
                        />
                    </div>
                ))}
            </div>
        );
    };

    const addRule = (e: FormEvent) => {
        e.preventDefault();

        const notification = toast("Adding Rule...");

        if (name === "" || description === "") {
            toast.error("Please fill in the Data properly!!", {
                ...toastDefaultOptions,
                id: notification,
            });
            return;
        }
        const newRules = existingRules
            ? [...existingRules, [name, description]]
            : [[name, description]];
        set(rulesRef, newRules);

        toast.success("Rule Added!", {
            ...toastDefaultOptions,
            id: notification,
        });

        setName("");
        setDescription("");
    };

    return (
        <div className="guildBodyContainer">
            <form
                className="flex flex-col items-center space-y-5"
                onSubmit={(e) => addRule(e)}
            >
                <input
                    type="text"
                    className="guildBodyInput"
                    placeholder="Body"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <input
                    type="text"
                    className="guildBodyInput"
                    placeholder="Description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                />
                <button
                    className="transform rounded-lg border-[5px] border-gray-300 p-4 transition duration-100 ease-out hover:scale-125"
                    aria-label="add-rule"
                    type="submit"
                >
                    Add Rule
                </button>
            </form>
            {showExistingRules()}
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

const Chatbot = ({ guild, ...guildProps }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );

    return (
        <div className="guildBodyContainer">
            <div className="flex justify-center space-x-10">
                <p className="text-2xl">Enable :</p>
                {/* Switch */}
            </div>
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

const Guild = ({ id, ...guildProps }: Props) => {
    const { data: session } = useSession();
    const [dbGuild, dbGuildLoading, dbGuildError] = useObjectVal(
        child(ref(db, `guilds`), id)
    );
    const [guild, setGuild] = useState<Guild | undefined | null>(null);
    const selectedSidebarOption = useRecoilValue(selectedSidebarOptionState);

    useEffect(() => {
        setGuild(session?.user?.guilds?.filter((guild) => guild.id === id)[0]);
    }, [session]);

    const body = () => {
        if (dbGuildLoading || dbGuildError) {
            return (
                <div className="guildBodyContainer">
                    <p className="">Loading...</p>
                </div>
            );
        }
        if (!dbGuild) {
            return (
                <div className="guildBodyContainer">
                    <p className="">
                        Your Server is not in JAK Discord Bot&apos;s Database!!
                        Please re-invite the Bot when it is online!!
                    </p>
                </div>
            );
        }
        if (selectedSidebarOption === "general") {
            return <General guild={guild} {...guildProps} />;
        } else if (selectedSidebarOption === "welcome") {
            return <Welcome guild={guild} {...guildProps} />;
        } else if (selectedSidebarOption === "moderation") {
            return <Moderation guild={guild} {...guildProps} />;
        } else if (selectedSidebarOption === "rules") {
            return <Rules guild={guild} {...guildProps} />;
        } else if (selectedSidebarOption === "reaction roles") {
            return <ReactionRoles guild={guild} {...guildProps} />;
        } else if (selectedSidebarOption === "translation and pronunciation") {
            return (
                <TranslationAndPronunciation guild={guild} {...guildProps} />
            );
        } else if (selectedSidebarOption === "poll") {
            return <Poll guild={guild} {...guildProps} />;
        } else if (selectedSidebarOption === "experience") {
            return <Experience guild={guild} {...guildProps} />;
        } else if (selectedSidebarOption === "reputation") {
            return <Reputation guild={guild} {...guildProps} />;
        } else if (selectedSidebarOption === "chatbot") {
            return <Chatbot guild={guild} {...guildProps} />;
        } else if (selectedSidebarOption === "giveaway") {
            return <Giveaway guild={guild} {...guildProps} />;
        }
    };

    return (
        <div className="flex flex-col text-gray-300">
            <Head>
                <title>
                    JAK Discord Bot | Guild |{" "}
                    {guild?.name ? guild.name : "Loading"}
                </title>
            </Head>
            {session ? (
                <div className="overflow-y-hidden">
                    {guild ? (
                        <div className="flex">
                            <div
                                className="flex h-screen flex-col items-center overflow-y-auto border-r-[3px] pb-5 scrollbar-hide"
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
                                className="h-screen overflow-y-auto scrollbar-hide"
                                style={{ flex: 0.8 }}
                            >
                                <Header />
                                {body()}
                                <Footer />
                            </div>
                        </div>
                    ) : (
                        <>
                            <Header />
                            <div className="mx-auto mt-5 flex justify-center md:mt-10 md:max-w-3xl lg:mt-[50px] lg:max-w-5xl">
                                <p className="font-2xl font-bold">Loading...</p>
                            </div>
                        </>
                    )}
                </div>
            ) : (
                <>
                    <Header />
                    <div className="mx-auto mt-5 flex justify-center md:mt-10 md:max-w-3xl lg:mt-[50px] lg:max-w-5xl">
                        <p className="font-2xl font-bold">
                            You need to Sign Up or Login first!!
                        </p>
                    </div>
                </>
            )}
        </div>
    );
};

export default Guild;

export const getServerSideProps: GetServerSideProps = async (context) => {
    const session = await getSession(context);

    if (!context.query.id) {
        return {
            props: {},
        };
    }

    if (!session) {
        return {
            props: {
                session: session,
                id: context.query.id,
            },
        };
    }

    const roles = await (
        await axios.post<Role[]>(`${process.env.NEXTAUTH_URL}/api/getRoles`, {
            guild_id: context.query.id,
        })
    ).data;

    const channels = await (
        await axios.post<Channel[]>(
            `${process.env.NEXTAUTH_URL}/api/getChannels`,
            { guild_id: context.query.id }
        )
    ).data;

    return {
        props: {
            session: session,
            id: context.query.id,
            roles,
            channels,
        },
    };
};
