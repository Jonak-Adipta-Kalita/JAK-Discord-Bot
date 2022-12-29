import { addDoc, collection } from "firebase/firestore";
import { useSession } from "next-auth/react";
import Head from "next/head";
import { FormEvent, useState } from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";
import { firestoreDB } from "../firebase";
import toast from "react-hot-toast";
import toastDefaultOptions from "../utils/toastDefaultOptions";

const Suggestion = () => {
    const { data: session } = useSession();
    const [suggestion, setSuggestion] = useState("");

    const sendContact = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        const notification = toast.loading("Sending Suggestion...");

        const collectionRef = collection(firestoreDB, "suggestions");

        await addDoc(collectionRef, {
            username: session?.user.name,
            email: session?.user?.email,
            suggestion: suggestion,
        });

        toast.success("Suggestion Sent!", {
            ...toastDefaultOptions,
            id: notification,
        });

        setSuggestion("");
    };

    return (
        <div className="flex h-screen flex-col">
            <Head>
                <title>JAK Discord Bot | Suggestion</title>
            </Head>
            <Header />
            <main className="flex-1 overflow-y-auto scrollbar-hide">
                <form
                    onSubmit={sendContact}
                    className="mx-auto mt-5 flex flex-col items-center space-y-4 text-gray-300 md:mt-10 md:max-w-3xl lg:mt-[50px] lg:max-w-5xl"
                >
                    <textarea
                        required
                        value={suggestion}
                        onChange={(e) => setSuggestion(e.target.value)}
                        className="w-[400px] rounded-lg border-[5px] border-gray-300 bg-bg-color p-4 outline-none sm:w-[500px]"
                        placeholder="Your Suggestion"
                    />
                    <div className="py-[30px]">
                        <button
                            type="submit"
                            className="transform rounded-lg border-[0.1px] border-gray-300 p-4 transition duration-100 ease-out hover:scale-125"
                            aria-label="send-suggestion"
                        >
                            Send
                        </button>
                    </div>
                </form>
            </main>
            <Footer />
        </div>
    );
};

export default Suggestion;
