import { XIcon } from "@heroicons/react/outline";
import { child, ref, set } from "firebase/database";
import { FormEvent, MouseEvent, useState } from "react";
import { useObjectVal } from "react-firebase-hooks/database";
import { toast } from "react-hot-toast";
import { db } from "../../firebase";
import { ExtensionProps } from "../../types/typings";
import toastDefaultOptions from "../../utils/toastDefaultOptions";

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

export default Rules;
