import { atom } from "recoil";
import { ReactionRole } from "../types/typings";

export const reactionRolesState = atom<ReactionRole[]>({
    key: "reactionRolesState",
    default: [],
});
