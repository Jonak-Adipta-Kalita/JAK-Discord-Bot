import { useSession } from "next-auth/react";
import Head from "next/head";
import Header from "../components/Header";
import Footer from "../components/Footer";
import { useRouter } from "next/router";

const Dashboard = () => {
    const { data: session } = useSession();
    const router = useRouter();

    return (
        <div className="flex h-screen flex-col text-gray-300">
            <Head>
                <title>JAK Website | Dashboard</title>
            </Head>
            <Header />
            {session ? (
                <div className="mx-auto mb-5 mt-3 space-y-4 md:mt-10 md:max-w-3xl lg:mt-[50px] lg:max-w-5xl">
                    {session?.user!.guilds?.length !== 0 ? (
                        <>
                            <div className="flex justify-center">
                                <p className="my-[30px] text-3xl font-bold md:mt-0">
                                    Select a Server
                                </p>
                            </div>

                            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
                                {session?.user!.guilds?.map((guild) => (
                                    <div
                                        className="m-4 flex w-[250px] transform cursor-pointer flex-col items-center justify-center rounded-xl border-[0.2px] p-5 transition duration-100 ease-out hover:scale-105"
                                        key={guild.id}
                                        onClick={() =>
                                            router.push(`/guild/${guild.id}`)
                                        }
                                    >
                                        {guild.icon ? (
                                            <img
                                                src={`https://cdn.discordapp.com/icons/${guild.id}/${guild.icon}.png`}
                                                alt=""
                                                className="rounded-full"
                                            />
                                        ) : (
                                            <div className="rounded-full border-[0.2px] py-[46px] px-14">
                                                <p className="text-4xl">
                                                    {guild.name[0]}
                                                </p>
                                            </div>
                                        )}
                                        <p className="mt-4 cursor-pointer">
                                            {guild.name}
                                        </p>
                                    </div>
                                ))}
                            </div>
                        </>
                    ) : (
                        <div className="mx-auto mt-5 flex justify-center md:mt-10 md:max-w-3xl lg:mt-[50px] lg:max-w-5xl">
                            <p className="font-2xl font-bold">
                                You are not a Owner of any Server, which have
                                JAK Discord Bot in it!!
                            </p>
                        </div>
                    )}
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
