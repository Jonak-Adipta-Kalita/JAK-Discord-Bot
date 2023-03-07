type Props = {
    saveFunc: () => void;
    cancelFunc: () => void;
    disabled?: boolean;
    send?: boolean;
};

const ModifyButtons = ({ saveFunc, cancelFunc, disabled, send }: Props) => {
    return (
        <div className="mt-5 flex justify-center space-x-10">
            <button
                onClick={cancelFunc}
                disabled={disabled}
                className={`pluginModifyButton ${
                    disabled
                        ? "cursor-not-allowed bg-gray-500"
                        : "bg-red-500 hover:opacity-80"
                }`}
            >
                Cancel
            </button>
            <button
                onClick={saveFunc}
                disabled={disabled}
                className={`pluginModifyButton ${
                    disabled
                        ? "cursor-not-allowed bg-gray-500"
                        : "bg-blue-500 hover:opacity-80"
                }`}
            >
                {send ? "Send" : "Save"}
            </button>
        </div>
    );
};

export default ModifyButtons;
