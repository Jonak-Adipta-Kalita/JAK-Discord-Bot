import { atom } from "recoil";
import { SelectedSiderbarOptions } from "../types/typings";

export const selectedSidebarOptionState = atom<SelectedSiderbarOptions>({
    key: "selectedSidebarOptionState",
    default: "general",
});
