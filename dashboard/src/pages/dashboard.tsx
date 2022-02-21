import { useSession } from "next-auth/react";
import Head from "next/head";
import Header from "../components/Header";
import Footer from "../components/Footer";

const Dashboard = () => {
    const { data: session } = useSession();

    return (
        <div className="flex h-screen flex-col  text-gray-300">
            <Head>
                <title>JAK Website | Dashboard</title>
            </Head>
            <Header />
            {session ? (
                <div className="mx-auto mb-5 mt-3 space-y-4 md:mt-10 md:max-w-3xl lg:mt-[50px] lg:max-w-5xl">
                    <p className="mb-[30px] text-3xl font-bold">Your Servers</p>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
                        {session?.user!.guilds?.map((guild) => (
                            <div
                                className="m-4 flex transform cursor-pointer flex-col items-center justify-center border-[0.2px] py-5 px-5 transition duration-100 ease-out hover:scale-105"
                                key={guild.id}
                            >
                                {guild.icon ? (
                                    <img
                                        src={`https://cdn.discordapp.com/icons/${guild.id}/${guild.icon}.png`}
                                        alt=""
                                        className="rounded-full"
                                    />
                                ) : (
                                    <img
                                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUieWGY_3xYwtl4SWwfXzYpppzYVftnJKa_Q&usqp=CAU"
                                        alt=""
                                        className="rounded-full"
                                    />
                                )}
                                <p className="mt-4 cursor-pointer">
                                    {guild.name}
                                </p>
                            </div>
                        ))}
                    </div>
                </div>
            ) : (
                <div className="mx-auto mt-5 flex justify-center md:mt-10 md:max-w-3xl lg:mt-[50px] lg:max-w-5xl">
                    <p className="font-2xl font-bold">
                        You need to Sign Up or Login first!!
                    </p>
                </div>
            )}
            <Footer />
        </div>
    );
};

export default Dashboard;
