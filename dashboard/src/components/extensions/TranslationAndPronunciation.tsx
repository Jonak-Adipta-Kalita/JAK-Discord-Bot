import { child, ref, set } from "firebase/database";
import { useEffect, useState } from "react";
import { useObjectVal } from "react-firebase-hooks/database";
import { toast } from "react-hot-toast";
import { db } from "../../firebase";
import { Channel, ExtensionProps } from "../../types/typings";
import toastDefaultOptions from "../../utils/toastDefaultOptions";
import ChannelsList from "../ChannelsList";
import ModifyButtons from "../ModifyButtons";
import Switch from "../Switch";

const TranslationAndPronunciation = ({
    guild,
    ...guildProps
}: ExtensionProps) => {
    const [enabled, setEnabled] = useState<boolean>(false);

    const [selectedChannelTranslation, setSelectedChannelTranslation] =
        useState<Channel>(guildProps.channels[0]);
    const [selectedChannelPronunciation, setSelectedChannelPronunciation] =
        useState<Channel>(guildProps.channels[0]);

    const translationRef = child(
        child(ref(db, `guilds`), guild?.id!),
        "translation"
    );
    const [translationData, translationDataLoading, translationDataError] =
        useObjectVal<Channel>(translationRef);

    const pronunciationRef = child(
        child(ref(db, `guilds`), guild?.id!),
        "pronunciation"
    );
    const [
        pronunciationData,
        pronunciationDataLoading,
        pronunciationDataError,
    ] = useObjectVal<Channel>(pronunciationRef);

    useEffect(() => {
        if (translationData && pronunciationData) {
            setEnabled(true);
            setSelectedChannelTranslation(translationData);
            setSelectedChannelPronunciation(pronunciationData);
        }
    }, [translationData, pronunciationData]);

    if (
        !guild ||
        translationDataLoading ||
        pronunciationDataLoading ||
        translationDataError ||
        pronunciationDataError
    )
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );

    const save = () => {
        const notification = toast.loading("Saving...", {
            ...toastDefaultOptions,
        });

        set(translationRef, selectedChannelTranslation);
        set(pronunciationRef, selectedChannelPronunciation);

        toast.success("Saved!", {
            id: notification,
            ...toastDefaultOptions,
        });
    };

    const cancel = () => {
        const notification = toast.loading("Cancelling...", {
            ...toastDefaultOptions,
        });

        if (translationData && pronunciationData) {
            setEnabled(true);
            setSelectedChannelTranslation(translationData!);
            setSelectedChannelPronunciation(pronunciationData!);
        } else {
            setSelectedChannelTranslation(guildProps.channels[0]);
            setSelectedChannelPronunciation(guildProps.channels[0]);
            setEnabled(false);
        }

        toast.success("Cancelled!!", {
            ...toastDefaultOptions,
            id: notification,
        });
    };

    const checkForDisabled = () => {
        if (!translationData && !pronunciationData && !enabled) return true;
        if (translationData && pronunciationData && enabled) {
            if (
                translationData.id === selectedChannelTranslation.id &&
                pronunciationData.id === selectedChannelPronunciation.id
            )
                return true;
        }
        return false;
    };

    return (
        <div className="guildBodyContainer space-y-10">
            <Switch enabled={enabled} setEnabled={setEnabled} />
            {enabled && (
                <>
                    <hr className="mt-10 -mb-10 text-gray-600" />
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
                                    setSelectedChannel={
                                        setSelectedChannelTranslation
                                    }
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
                                    selectedChannel={
                                        selectedChannelPronunciation
                                    }
                                    setSelectedChannel={
                                        setSelectedChannelPronunciation
                                    }
                                />
                            </div>
                        </div>
                    </div>
                </>
            )}

            <ModifyButtons
                saveFunc={save}
                cancelFunc={cancel}
                disabled={checkForDisabled()}
            />
        </div>
    );
};

export default TranslationAndPronunciation;
