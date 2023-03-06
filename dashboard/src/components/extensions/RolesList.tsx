import { Dispatch, SetStateAction } from "react";
import { Role } from "../../types/typings";

type Props = {
    roles: Role[];
    selectedRole?: Role;
    setSelectedRole?: Dispatch<SetStateAction<Role>>;
};

const RolesList = ({ roles, selectedRole, setSelectedRole }: Props) => {
    return <div></div>;
};

export default RolesList;
