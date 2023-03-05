import { child, ref, set } from "firebase/database";
import { FormEvent, useState } from "react";
import { useObjectVal } from "react-firebase-hooks/database";
import { toast } from "react-hot-toast";
import { db } from "../../firebase";
import { ExtensionProps } from "../../types/typings";
import toastDefaultOptions from "../../utils/toastDefaultOptions";

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
            <div className="flex flex-col items-center justify-center">
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

export default General;
