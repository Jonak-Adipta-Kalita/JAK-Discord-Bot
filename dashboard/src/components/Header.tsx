import { signIn, signOut, useSession } from "next-auth/react";
import Image from "next/image";
import { useRouter } from "next/router";
import { ChevronDownIcon } from "@heroicons/react/solid";
import { Fragment, useState } from "react";
import { Menu, Transition } from "@headlessui/react";

const Header = () => {
    const router = useRouter();
    const { data: session } = useSession();
    const [dropdownOpen, setDropdownOpen] = useState(false);

    return (
        <header className="flex items-center justify-between p-4 py-5 text-gray-400 shadow-xl md:px-10 lg:px-20">
            <div
                onClick={() => router.push("/")}
                className="flex cursor-pointer items-center space-x-4"
            >
                <Image
                    src="/images/favicon.ico"
                    alt="logo"
                    height={60}
                    width={60}
                    className=""
                />
                <p className="cursor-pointer text-sm font-bold text-white md:text-base">
                    JAK Discord Bot
                </p>
            </div>
            <div className="">
                {!session ? (
                    <div className="mr-4">
                        <button
                            className="transform cursor-pointer rounded-xl border-[0.1px] border-gray-400 p-4 px-10 transition duration-100 ease-out hover:scale-125 focus:outline-none focus:ring-2"
                            onClick={() => signIn()}
                        >
                            Login
                        </button>
                    </div>
                ) : (
                    <div
                        className="flex cursor-pointer items-center space-x-3"
                        onClick={() => setDropdownOpen(!dropdownOpen)}
                    >
                        <img
                            className="hidden h-10 w-10 rounded-full md:inline"
                            src={session?.user?.image!}
                            alt="avatar"
                        />

                        <Menu
                            as="div"
                            className="relative inline-block text-left"
                        >
                            <div className="">
                                <Menu.Button className="flex items-center text-gray-400 hover:text-white">
                                    {session?.user?.name}
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
                                <Menu.Items className="absolute right-0 mt-6 w-56 origin-top-right divide-y divide-gray-100 rounded-md border-[0.1px] bg-bg-color text-white shadow-lg">
                                    <div className="py-1">
                                        <Menu.Item>
                                            {() => (
                                                <p
                                                    onClick={() =>
                                                        router.push(
                                                            "/dashboard"
                                                        )
                                                    }
                                                    className="menuItem"
                                                >
                                                    Dashboard
                                                </p>
                                            )}
                                        </Menu.Item>
                                    </div>
                                    <div className="py-1">
                                        <Menu.Item>
                                            {() => (
                                                <p
                                                    onClick={() => signOut()}
                                                    className="block cursor-pointer px-4 py-2 text-sm font-semibold text-red-700 hover:text-red-500"
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
