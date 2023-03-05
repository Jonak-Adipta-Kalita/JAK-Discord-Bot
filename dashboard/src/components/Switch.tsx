import { Switch as Switch_ } from "@headlessui/react";
import { Dispatch, SetStateAction } from "react";

const Switch = ({
    enabled,
    setEnabled,
}: {
    enabled: boolean;
    setEnabled: Dispatch<SetStateAction<boolean>>;
}) => {
    return (
        <Switch_.Group>
            <div className="flex items-center justify-center space-x-10">
                <Switch_.Label className="-mt-2 text-3xl">
                    Enable :
                </Switch_.Label>
                <Switch_
                    checked={enabled}
                    onChange={setEnabled}
                    className={`${
                        enabled ? "bg-blue-600" : "bg-gray-200"
                    } relative inline-flex h-6 w-11 items-center rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2`}
                >
                    <span
                        className={`${
                            enabled ? "translate-x-6" : "translate-x-1"
                        } inline-block h-4 w-4 transform rounded-full bg-white transition-transform`}
                    />
                </Switch_>
            </div>
        </Switch_.Group>
    );
};

export default Switch;
