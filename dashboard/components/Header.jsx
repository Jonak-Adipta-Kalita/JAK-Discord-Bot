import { signIn, useSession } from "next-auth/react";
import Image from "next/image";
import { useRouter } from "next/router";
import { ChevronDownIcon } from "@heroicons/react/solid";

const Header = ({ providers }) => {
    const router = useRouter();
    const { data: session } = useSession();
    const provider = Object.values(providers).map((provider) => provider);

    return (
        <header className="flex items-center bg-[#272934] sticky top-0 text-gray-400 p-4 py-5 justify-between shadow-xl md:px-10 lg:px-20">
            <div
                onClick={() => router.push("/")}
                className="flex items-center space-x-4"
            >
                <Image
                    src="/favicon.ico"
                    alt="logo"
                    height={60}
                    width={60}
                    className="cursor-pointer"
                />
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
                    <div className="flex items-center space-x-3 cursor-pointer">
                        <img
                            className="w-10 h-10 rounded-full"
                            src={session?.user?.image}
                            alt="avatar"
                        />
                        <div className="flex items-center ml-2">
                            <p className="text-white font-semibold text-sm">
                                {session?.user?.name}
                            </p>
                            <ChevronDownIcon className="h-5 w-5 text-white" />
                        </div>
                    </div>
                )}
            </div>
        </header>
    );
};

export default Header;
