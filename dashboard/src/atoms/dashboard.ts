import { atom } from "recoil";

export const selectedSidebarOptionState = atom<string>({
    key: "selectedSidebarOptionState",
    default: "general",
});
