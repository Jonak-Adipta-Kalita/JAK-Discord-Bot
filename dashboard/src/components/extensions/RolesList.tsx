import { Listbox, Transition } from "@headlessui/react";
import { CheckIcon, ChevronDownIcon } from "@heroicons/react/solid";
import { Dispatch, Fragment, SetStateAction } from "react";
import { Role } from "../../types/typings";

type Props = {
    roles: Role[];
    selectedRole: Role;
    setSelectedRole: Dispatch<SetStateAction<Role>>;
};

const RolesList = ({ roles, selectedRole, setSelectedRole }: Props) => {
    return (
        <div className="relative w-52">
            <Listbox value={selectedRole} onChange={setSelectedRole}>
                <Listbox.Button className="relative w-full cursor-default rounded-lg bg-[#17181e] py-2 pl-3 pr-10 text-left shadow-md focus:outline-none focus-visible:border-indigo-500 focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75 focus-visible:ring-offset-2 focus-visible:ring-offset-orange-300 sm:text-sm">
                    <span
                        className={`block truncate text-[#${selectedRole.color
                            .toString(16)
                            .padStart(6, "0")}]`}
                    >
                        {selectedRole.name}
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
                    <Listbox.Options className="absolute z-50 mt-1 max-h-60 w-full overflow-auto rounded-md bg-[#17181e] py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
                        {roles.map((role) => (
                            <Listbox.Option
                                key={role.id}
                                className={({ active }) =>
                                    `relative cursor-default select-none py-2 pl-10 pr-4 ${
                                        active
                                            ? "rounded-md bg-gray-700"
                                            : "text-gray-300"
                                    }`
                                }
                                value={role}
                            >
                                {({ selected }: { selected: boolean }) => (
                                    <>
                                        <span
                                            className={`block truncate text-[#${role.color
                                                .toString(16)
                                                .padStart(6, "0")}] ${
                                                selected
                                                    ? "font-medium"
                                                    : "font-normal"
                                            }`}
                                        >
                                            {role.name}
                                        </span>
                                        {selected ? (
                                            <span className="absolute inset-y-0 left-0 flex items-center pl-3">
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
    );
};

export default RolesList;
