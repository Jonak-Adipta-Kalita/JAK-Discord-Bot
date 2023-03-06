import { useState } from "react";
import { Channel, ExtensionProps } from "../../types/typings";
import ChannelsList from "./ChannelsList";

const ReactionRoles = ({ guild, ...guildProps }: ExtensionProps) => {
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
            {/* Roles */}
        </div>
    );
};

export default ReactionRoles;
