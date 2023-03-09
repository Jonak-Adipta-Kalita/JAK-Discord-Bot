import { useState } from "react";
import { Channel, ExtensionProps } from "../../types/typings";
import ChannelsList from "../ChannelsList";
import ModifyButtons from "../ModifyButtons";

const TranslationAndPronunciation = ({
    guild,
    ...guildProps
}: ExtensionProps) => {
    const [selectedChannelTranslation, setSelectedChannelTranslation] =
        useState<Channel>(guildProps.channels[0]);
    const [selectedChannelPronunciation, setSelectedChannelPronunciation] =
        useState<Channel>(guildProps.channels[0]);

    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );

    const save = () => {};

    const cancel = () => {};

    const checkForDisabled = () => {
        return true;
    };

    return (
        <div className="guildBodyContainer space-y-10">
            <div className="flex flex-col justify-around space-y-10 lg:flex-row lg:space-y-0">
                <div className="flex flex-col items-center justify-center space-y-5">
                    <p className="text-2xl underline underline-offset-4">
                        Translation
                    </p>
                    <div className="flex items-center space-x-5">
                        <p className="text-sm md:text-xl">Channel :</p>
                        <ChannelsList
                            channels={guildProps.channels}
                            selectedChannel={selectedChannelTranslation}
                            setSelectedChannel={setSelectedChannelTranslation}
                        />
                    </div>
                </div>
                <div className="flex flex-col items-center justify-center space-y-5">
                    <p className="text-2xl underline underline-offset-4">
                        Pronunciation
                    </p>
                    <div className="flex items-center space-x-5">
                        <p className="text-sm md:text-xl">Channel :</p>
                        <ChannelsList
                            channels={guildProps.channels}
                            selectedChannel={selectedChannelPronunciation}
                            setSelectedChannel={setSelectedChannelPronunciation}
                        />
                    </div>
                </div>
            </div>
            <ModifyButtons
                saveFunc={save}
                cancelFunc={cancel}
                disabled={checkForDisabled()}
            />
        </div>
    );
};

export default TranslationAndPronunciation;
