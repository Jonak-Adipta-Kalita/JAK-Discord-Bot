import {
    BackspaceIcon,
    PlusCircleIcon,
    XCircleIcon,
} from "@heroicons/react/solid";
import axios from "axios";
import EmojiPicker, { Theme, EmojiClickData } from "emoji-picker-react";
import { child, ref, set } from "firebase/database";
import { useEffect, useState } from "react";
import { useObjectVal } from "react-firebase-hooks/database";
import { toast } from "react-hot-toast";
import { useRecoilState } from "recoil";
import { reactionRolesState } from "../../atoms/reactionRoles";
import { db } from "../../firebase";
import {
    Channel,
    ExtensionProps,
    ReactionRole,
    Role,
} from "../../types/typings";
import { sendEmbed } from "../../utils/sendEmbed";
import toastDefaultOptions from "../../utils/toastDefaultOptions";
import ChannelsList from "../ChannelsList";
import ModifyButtons from "../ModifyButtons";
import RolesList from "./RolesList";

const ReactionRole_ = ({
    roles,
    reactionRole,
    id,
}: {
    roles: Role[];
    reactionRole: ReactionRole;
    id: number;
}) => {
    const [showEmojiPicker, setShowEmojiPicker] = useState<boolean>(false);
    const [reactionRoles, setReactionRoles] =
        useRecoilState(reactionRolesState);
    const [selectedRole, setSelectedRole] = useState<Role>(roles[0]);
    const [selectedEmoji, setSelectedEmoji] = useState<EmojiClickData | null>(
        null
    );

    const onEmojiClick = (emoji: EmojiClickData) => {
        setSelectedEmoji(emoji);
        setShowEmojiPicker(false);
    };

    useEffect(() => {
        if (Array(reactionRoles.keys()).length === 0) return;

        setSelectedRole(reactionRoles[id].role);
        setSelectedEmoji(reactionRoles[id].emoji);
    }, []);

    useEffect(() => {
        setReactionRoles((prev) => {
            const newReactionRoles = [...prev];
            const index = newReactionRoles.findIndex(
                (rr: ReactionRole) => rr.emoji === reactionRole.emoji
            );
            newReactionRoles[index] = {
                emoji: selectedEmoji,
                role: selectedRole,
            };
            return newReactionRoles;
        });
    }, [selectedRole, selectedEmoji]);

    return (
        <div className="flex space-x-4">
            <XCircleIcon
                className="mt-1 h-7 w-7 cursor-pointer hover:opacity-60"
                onClick={() => {
                    setReactionRoles((prev) => {
                        const newReactionRoles = [...prev];
                        delete newReactionRoles[id];
                        return newReactionRoles;
                    });
                }}
            />
            <p className="mt-1">
                {"#"}
                {id + 1}
            </p>
            <div className="space-y-4">
                <div className="flex items-center space-x-5">
                    <p className="text-sm md:text-xl">Emoji : </p>
                    <div className="relative">
                        {showEmojiPicker && (
                            <div className="absolute z-50">
                                <EmojiPicker
                                    lazyLoadEmojis
                                    theme={Theme.DARK}
                                    onEmojiClick={onEmojiClick}
                                />
                            </div>
                        )}
                        {reactionRole.emoji ? (
                            <p
                                onClick={() => setShowEmojiPicker(true)}
                                className="cursor-pointer text-2xl"
                            >
                                {reactionRole.emoji.emoji}
                            </p>
                        ) : (
                            <button
                                onClick={() => setShowEmojiPicker(true)}
                                className="rounded-xl border-[0.8px] p-2 text-xs"
                            >
                                Show Emoji Picker
                            </button>
                        )}
                    </div>
                </div>
                <div className="flex items-center space-x-5">
                    <p className="text-sm md:text-xl">Role : </p>
                    <RolesList
                        roles={roles}
                        selectedRole={selectedRole}
                        setSelectedRole={setSelectedRole}
                    />
                </div>
            </div>
        </div>
    );
};

const ReactionRoles = ({ guild, ...guildProps }: ExtensionProps) => {
    const [reactionRoles, setReactionRoles] =
        useRecoilState(reactionRolesState);

    const [selectedChannel, setSelectedChannel] = useState<Channel>(
        guildProps.channels[0]
    );

    const [addMore, setAddMore] = useState<boolean>(false);

    const reactionRolesRef = child(
        child(ref(db, `guilds`), guild?.id!),
        "reactionRoles"
    );
    const [
        reactionRolesData,
        reactionRolesDataLoading,
        reactionRolesDataError,
    ] = useObjectVal<[]>(reactionRolesRef);

    const [embedTitle, setEmbedTitle] = useState<string>("");
    const [embedDescription, setEmbedDescription] = useState<string>("");

    if (!guild || reactionRolesDataLoading || reactionRolesDataError)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );

    const addReactionRole = () => {
        setReactionRoles((prev) => [
            ...prev,
            { emoji: null, role: guildProps.roles[0] },
        ]);
    };

    const cancel = () => {
        const notification = toast("Cancelling...", {
            ...toastDefaultOptions,
        });

        setSelectedChannel(guildProps.channels[0]);
        setReactionRoles([]);
        setEmbedDescription("");
        setEmbedTitle("");

        toast.success("Cancelled!", {
            ...toastDefaultOptions,
            id: notification,
        });
    };

    const send = async () => {
        const notification = toast("Sending...", {
            ...toastDefaultOptions,
        });

        const msg = await sendEmbed(
            selectedChannel.id,
            embedTitle,
            embedDescription
        );

        await axios.post("/api/reactToMessage", {
            message_id: msg.id,
            channel_id: selectedChannel.id,
            reactionRoles,
        });

        const reactionRoleData = reactionRoles.map((reactionRole) => ({
            ...reactionRole,
            emoji: {
                activeSkinTone: reactionRole.emoji!.activeSkinTone,
                emoji: reactionRole.emoji!.emoji,
                names: reactionRole.emoji!.names,
                unified: reactionRole.emoji!.unified,
                unifiedWithoutSkinTone:
                    reactionRole.emoji!.unifiedWithoutSkinTone,
            },
        }));

        const modifiedData = {
            channel_id: selectedChannel.id,
            message_id: msg.id,
            reactionRoles: reactionRoleData,
        };

        const newData = reactionRolesData
            ? [...reactionRolesData, modifiedData]
            : [modifiedData];

        set(reactionRolesRef, newData);

        toast.success("Sent!", {
            ...toastDefaultOptions,
            id: notification,
        });

        setSelectedChannel(guildProps.channels[0]);
        setReactionRoles([]);
        setEmbedDescription("");
        setEmbedTitle("");
    };

    const checkForDisabled = () => {
        return (
            !embedTitle ||
            !embedDescription ||
            reactionRoles.length === 0 ||
            reactionRoles.some((rr) => !rr.emoji)
        );
    };

    return (
        <div className="guildBodyContainer">
            {!reactionRolesData || addMore ? (
                <div className="relative flex flex-col items-center justify-center space-y-4">
                    {addMore && (
                        <BackspaceIcon
                            className="absolute -top-5 left-10 h-12 cursor-pointer hover:opacity-60 md:top-0 md:left-0 md:h-16"
                            onClick={() => setAddMore(false)}
                        />
                    )}
                    <div className="flex items-center space-x-5">
                        <p className="text-sm md:text-xl">Select channel :</p>
                        <ChannelsList
                            channels={guildProps.channels}
                            selectedChannel={selectedChannel}
                            setSelectedChannel={setSelectedChannel}
                        />
                    </div>
                    <div className="flex items-center space-x-5">
                        <p className="text-sm md:text-xl">Embed Title :</p>
                        <input
                            type="text"
                            value={embedTitle}
                            maxLength={256}
                            onChange={(e) => setEmbedTitle(e.target.value)}
                            placeholder="Your Embed Title"
                            className="rounded-lg bg-[#17181e] py-2 px-4 text-xs text-gray-100 outline-none md:text-base"
                        />
                    </div>
                    <div className="flex items-center space-x-3 md:space-x-5">
                        <p className="text-sm md:text-xl">
                            Embed <span className="truncate">Description</span>{" "}
                            :
                        </p>
                        <textarea
                            value={embedDescription}
                            maxLength={1024}
                            onChange={(e) =>
                                setEmbedDescription(e.target.value)
                            }
                            placeholder="Embed Description"
                            className="w-[200px] rounded-lg bg-[#17181e] py-2 px-4 text-xs text-gray-100 outline-none md:w-[350px] md:text-base"
                        />
                    </div>
                    <div className="mt-10" />

                    <div className="space-y-8">
                        {reactionRoles.length > 0 &&
                            reactionRoles.map((reactionRole, i) => (
                                <ReactionRole_
                                    key={i}
                                    reactionRole={reactionRole}
                                    roles={guildProps.roles}
                                    id={i}
                                />
                            ))}
                    </div>

                    <PlusCircleIcon
                        className="h-16 w-16 cursor-pointer hover:opacity-60"
                        onClick={addReactionRole}
                    />

                    <div className="mb-5" />

                    <ModifyButtons
                        cancelFunc={cancel}
                        saveFunc={send}
                        disabled={checkForDisabled()}
                        send
                    />

                    <div className="mb-5" />
                </div>
            ) : (
                <div className="flex flex-col items-center">
                    <div className="">
                        {reactionRoles.map((reactionRole, i) => (
                            <div className="" key={i}></div>
                        ))}
                    </div>
                    <PlusCircleIcon
                        className="h-16 w-16 cursor-pointer hover:opacity-60"
                        onClick={() => setAddMore(true)}
                    />
                </div>
            )}
        </div>
    );
};

export default ReactionRoles;
