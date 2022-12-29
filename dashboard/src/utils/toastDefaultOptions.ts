import { Toast } from "react-hot-toast";

const toastDefaultOptions: Partial<
    Pick<
        Toast,
        | "id"
        | "icon"
        | "duration"
        | "ariaProps"
        | "className"
        | "style"
        | "position"
        | "iconTheme"
    >
> = {
    style: {
        borderRadius: "10px",
        background: "#333",
        color: "#fff",
    },
};

export default toastDefaultOptions;
