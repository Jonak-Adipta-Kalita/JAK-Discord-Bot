import Image from "next/image";
import { useRouter } from "next/router";

const Header = () => {
    const router = useRouter();

    const login = (e) => {};

    return (
        <header className="flex items-center bg-[#272934] sticky top-0 text-gray-400 p-4 py-5 justify-between shadow-xl">
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
            <div className="mr-4">
                <button
                    className="cursor-pointer border-[0.1px] border-gray-400 p-4 px-10 rounded-lg hover:scale-125 transition transform duration-100 ease-out focus:outline-none focus:ring-2"
                    onClick={login}
                >
                    Login
                </button>
            </div>
        </header>
    );
};

export default Header;
