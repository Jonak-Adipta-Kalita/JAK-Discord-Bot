import { editMessage } from "@xxjonakadiptaxx/jak_javascript_package";
import { Command } from "../typings";

interface Props {
    command: Command;
}

const Command = ({ command }: Props) => {
    return (
        <div className="p-4 border-[0.1px] rounded-xl">
            <p className="">
                Name:{" "}
                {new editMessage(command.name.replace("_", " ")).toTitleCase()}
            </p>
            <p className="">Usage: {command.usage}</p>
            <p className="">Description: {command.description}</p>
        </div>
    );
};

export default Command;
