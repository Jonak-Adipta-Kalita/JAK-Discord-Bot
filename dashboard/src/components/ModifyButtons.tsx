type Props = {
    saveFunc: () => void;
    cancelFunc: () => void;
    disabled?: boolean;
};

const ModifyButtons = ({ saveFunc, cancelFunc, disabled }: Props) => {
    return (
        <div className="mt-5 flex justify-end space-x-10">
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
                Save
            </button>
        </div>
    );
};

export default ModifyButtons;
