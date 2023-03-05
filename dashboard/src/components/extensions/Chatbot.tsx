/* eslint-disable react/prop-types */

import { Listbox, Transition } from "@headlessui/react";
import { CheckIcon, ChevronDownIcon } from "@heroicons/react/solid";
import { child, ref } from "firebase/database";
import { Fragment, useEffect, useState } from "react";
import { useObjectVal } from "react-firebase-hooks/database";
import { db } from "../../firebase";
import { ExtensionProps } from "../../types/typings";
import ModifyButtons from "../ModifyButtons";
import Switch from "../Switch";

const Chatbot = ({ guild, ...guildProps }: ExtensionProps) => {
    const aiChoices = [{ id: 0, name: "alexis", unavailable: false }];

    const [enabled, setEnabled] = useState<boolean>(false);
    const [selectedAI, setSelectedAI] = useState(aiChoices[0]);

    const chatbotRef = child(child(ref(db, `guilds`), guild?.id!), "chatbot");
    const [chatbotData, chatbotDataLoading, chatbotDataError] =
        useObjectVal<[]>(chatbotRef);

    useEffect(() => {
        if (chatbotData) {
            setEnabled(true);
            setSelectedAI(
                aiChoices[
                    aiChoices.findIndex(
                        ({ name }) => name === chatbotData[0][1]
                    )
                ]
            );
        }
    }, [chatbotData]);

    if (!guild || chatbotDataLoading || chatbotDataError)
        return (
            <div className="guildBodyContainer">
                <p className="">Loading...</p>
            </div>
        );

    const save = () => {};

    const cancel = () => {};

    return (
        <div className="guildBodyContainer">
            <Switch enabled={enabled} setEnabled={setEnabled} />

            {enabled ? (
                <>
                    <hr className="mt-10 -mb-10 text-gray-600" />
                    <div className="my-20 flex flex-col items-center justify-center">
                        <div className="flex items-center space-x-5">
                            <p className="text-xl">Select AI : </p>
                            <div className="relative w-52">
                                <Listbox
                                    value={selectedAI}
                                    onChange={setSelectedAI}
                                >
                                    <Listbox.Button className="relative w-full cursor-default rounded-lg bg-white py-2 pl-3 pr-10 text-left shadow-md focus:outline-none focus-visible:border-indigo-500 focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75 focus-visible:ring-offset-2 focus-visible:ring-offset-orange-300 sm:text-sm">
                                        <span className="block truncate text-gray-900">
                                            {selectedAI.name}
                                        </span>
                                        <span className="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2">
                                            <ChevronDownIcon
                                                className="h-5 w-5 text-gray-400"
                                                aria-hidden="true"
                                            />
                                        </span>
                                    </Listbox.Button>
                                    <Transition
                                        as={Fragment}
                                        leave="transition ease-in duration-100"
                                        leaveFrom="opacity-100"
                                        leaveTo="opacity-0"
                                    >
                                        <Listbox.Options className="absolute z-50 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
                                            {aiChoices.map((ai) => (
                                                <Listbox.Option
                                                    key={ai.id}
                                                    className={({ active }) =>
                                                        `relative cursor-default select-none py-2 pl-10 pr-4 ${
                                                            active
                                                                ? "bg-amber-100 text-amber-900"
                                                                : "text-gray-900"
                                                        }`
                                                    }
                                                    value={ai}
                                                    disabled={ai.unavailable}
                                                >
                                                    {({
                                                        selected,
                                                    }: {
                                                        selected: boolean;
                                                    }) => (
                                                        <>
                                                            <span
                                                                className={`block truncate ${
                                                                    selected
                                                                        ? "font-medium"
                                                                        : "font-normal"
                                                                }`}
                                                            >
                                                                {ai.name}
                                                            </span>
                                                            {selected ? (
                                                                <span className="absolute inset-y-0 left-0 flex items-center pl-3 text-amber-600">
                                                                    <CheckIcon
                                                                        className="h-5 w-5"
                                                                        aria-hidden="true"
                                                                    />
                                                                </span>
                                                            ) : null}
                                                        </>
                                                    )}
                                                </Listbox.Option>
                                            ))}
                                        </Listbox.Options>
                                    </Transition>
                                </Listbox>
                            </div>
                        </div>
                    </div>
                </>
            ) : (
                <div className="mb-10" />
            )}

            <ModifyButtons cancelFunc={cancel} saveFunc={save} disabled />
        </div>
    );
};

export default Chatbot;
