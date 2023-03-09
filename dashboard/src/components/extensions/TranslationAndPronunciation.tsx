import { ExtensionProps } from "../../types/typings";

const TranslationAndPronunciation = ({ guild }: ExtensionProps) => {
    if (!guild)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );
    return <div className="guildBodyContainer"></div>;
};

export default TranslationAndPronunciation;
