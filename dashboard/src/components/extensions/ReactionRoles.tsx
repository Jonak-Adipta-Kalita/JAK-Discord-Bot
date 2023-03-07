import { PlusCircleIcon } from "@heroicons/react/solid";
import EmojiPicker, { Theme, EmojiClickData } from "emoji-picker-react";
import { useState } from "react";
import { toast } from "react-hot-toast";
import { useRecoilState, useSetRecoilState } from "recoil";
import { reactionRolesState } from "../../atoms/reactionRoles";
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
    const [selectedRole, setSelectedRole] = useState<Role>(roles[0]);
    const setReactionRoles = useSetRecoilState(reactionRolesState);

    const onEmojiClick = (emoji: EmojiClickData) => {
        setReactionRoles((prev) => {
            const newReactionRoles = [...prev];
            const index = newReactionRoles.findIndex(
                (rr: ReactionRole) => rr.emoji === reactionRole.emoji
            );
            newReactionRoles[index] = {
                emoji,
                role: selectedRole,
            };
            return newReactionRoles;
        });

        setShowEmojiPicker(false);
    };

    return (
        <div className="flex space-x-4">
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

    const [embedTitle, setEmbedTitle] = useState<string>("");
    const [embedDescription, setEmbedDescription] = useState<string>("");

    if (!guild)
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

        toast.success("Sent!", {
            ...toastDefaultOptions,
            id: notification,
        });
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
        <div className="guildBodyContainer flex flex-col items-center justify-center space-y-4">
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
                    Embed <span className="truncate">Description</span> :
                </p>
                <textarea
                    value={embedDescription}
                    maxLength={1024}
                    onChange={(e) => setEmbedDescription(e.target.value)}
                    placeholder="Embed Description"
                    className="w-[200px] rounded-lg bg-[#17181e] py-2 px-4 text-xs text-gray-100 outline-none md:w-[350px] md:text-base"
                />
            </div>
            <div className="mt-10" />

            <div className="space-y-8">
                {reactionRoles.map((reactionRole, i) => (
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
    );
};

export default ReactionRoles;
