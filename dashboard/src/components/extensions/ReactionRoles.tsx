import { PlusCircleIcon } from "@heroicons/react/solid";
import EmojiPicker, { Theme } from "emoji-picker-react";
import { EmojiClickData } from "emoji-picker-react";
import { useState } from "react";
import { Channel, ExtensionProps, Role } from "../../types/typings";
import ChannelsList from "../ChannelsList";
import RolesList from "./RolesList";

interface ReactionRole {
    emoji: string | null;
    role: Role;
}

const ShowEmojiPickerButton = () => {
    const [showEmojiPicker, setShowEmojiPicker] = useState<boolean>(false);
    const [selectedEmoji, setSelectedEmoji] = useState<EmojiClickData | null>(
        null
    );

    const onEmojiClick = (emoji: EmojiClickData, e: MouseEvent) => {
        e.preventDefault();

        setSelectedEmoji(emoji);
        setShowEmojiPicker(false);
    };

    return (
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
            {console.log(selectedEmoji)}
            {selectedEmoji ? (
                <p
                    onClick={() => setShowEmojiPicker(true)}
                    className="cursor-pointer text-2xl"
                >
                    {selectedEmoji.emoji}
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
    );
};

const ReactionRoles = ({ guild, ...guildProps }: ExtensionProps) => {
    const [reactionRoles, setReactionRoles] = useState<ReactionRole[]>([]);

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

            {reactionRoles.map((reactionRole, i) => (
                <div key={i}>
                    <div className="flex items-center space-x-5">
                        <p className="text-sm md:text-xl">Emoji : </p>
                        <ShowEmojiPickerButton />
                    </div>
                    <div className="flex items-center space-x-5">
                        <p className="text-sm md:text-xl">Role : </p>
                        <RolesList roles={guildProps.roles} />
                    </div>
                </div>
            ))}

            <PlusCircleIcon
                className="h-16 w-16 cursor-pointer hover:opacity-60"
                onClick={addReactionRole}
            />
        </div>
    );
};

export default ReactionRoles;
