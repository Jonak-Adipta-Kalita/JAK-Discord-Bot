import { signIn, signOut, useSession } from "next-auth/react";
import Image from "next/image";
import { useRouter } from "next/router";
import { ChevronDownIcon } from "@heroicons/react/solid";
import { Fragment, useState } from "react";
import { Menu, Transition } from "@headlessui/react";

const Header = ({ providers }) => {
    const router = useRouter();
    const { data: session } = useSession();
    const [dropdownOpen, setDropdownOpen] = useState(false);

    const provider = Object.values(providers).map((provider) => provider);

    return (
        <header className="flex items-center bg-[#272934] sticky top-0 text-gray-400 p-4 py-5 justify-between shadow-xl md:px-10 lg:px-20">
            <div
                onClick={() => router.push("/")}
                className="flex items-center space-x-4 cursor-pointer"
            >
                <Image src="/favicon.ico" alt="logo" height={60} width={60} />
                <h1 className="font-bold text-white">JAK Discord Bot</h1>
            </div>
            <div className="">
                {!session ? (
                    <div className="mr-4">
                        <button
                            className="cursor-pointer border-[0.1px] border-gray-400 p-4 px-10 rounded-xl hover:scale-125 transition transform duration-100 ease-out focus:outline-none focus:ring-2"
                            onClick={() =>
                                signIn(provider[0].id, { callbackUrl: "/" })
                            }
                        >
                            Login
                        </button>
                    </div>
                ) : (
                    <div
                        className="flex items-center space-x-3 cursor-pointer"
                        onClick={() => setDropdownOpen(!dropdownOpen)}
                    >
                        <img
                            className="w-10 h-10 rounded-full"
                            src={session.user.image}
                            alt="avatar"
                        />

                        <Menu
                            as="div"
                            className="relative inline-block text-left"
                        >
                            <div className="">
                                <Menu.Button className="flex items-center text-gray-400 hover:text-white">
                                    {session.user.name}
                                    <ChevronDownIcon
                                        className="-mr-1 ml-2 h-5 w-5"
                                        aria-hidden="true"
                                    />
                                </Menu.Button>
                            </div>

                            <Transition
                                as={Fragment}
                                enter="transition ease-out duration-100"
                                enterFrom="transform opacity-0 scale-95"
                                enterTo="transform opacity-100 scale-100"
                                leave="transition ease-in duration-75"
                                leaveFrom="transform opacity-100 scale-100"
                                leaveTo="transform opacity-0 scale-95"
                            >
                                <Menu.Items className="origin-top-right absolute right-0 mt-6 w-56 rounded-md shadow-lg bg-[#272934] divide-y divide-gray-100 text-white border-[0.1px]">
                                    <div className="py-1">
                                        <Menu.Item>
                                            {() => (
                                                <p
                                                    onClick={() =>
                                                        router.push(
                                                            "/dashboard"
                                                        )
                                                    }
                                                    className="menu-item"
                                                >
                                                    Dashboard
                                                </p>
                                            )}
                                        </Menu.Item>
                                        <Menu.Item>
                                            {() => (
                                                <p
                                                    onClick={() =>
                                                        router.push("/settings")
                                                    }
                                                    className="menu-item"
                                                >
                                                    Settings
                                                </p>
                                            )}
                                        </Menu.Item>
                                    </div>
                                    <div className="py-1">
                                        <Menu.Item>
                                            {() => (
                                                <p
                                                    onClick={signOut}
                                                    className="block px-4 py-2 text-sm text-red-700 font-semibold cursor-pointer hover:text-red-500"
                                                >
                                                    Logout
                                                </p>
                                            )}
                                        </Menu.Item>
                                    </div>
                                </Menu.Items>
                            </Transition>
                        </Menu>
                    </div>
                )}
            </div>
        </header>
    );
};

export default Header;
