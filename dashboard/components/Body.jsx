const Body = () => {
    return (
        <main className="flex-1 overflow-y-auto scrollbar-hide bg-[#272934]">
            <div>
                <div className="flex mt-10 justify-center lg:mt-20">
                    <a
                        href="https://discord.com/api/oauth2/authorize?client_id=756402881913028689&permissions=8&scope=bot"
                        target="_blank"
                        className="body-btn text-white bg-[#3994ff] active:bg-[#3572a5] cursor-pointer"
                    >
                        Add to Server
                    </a>
                </div>
            </div>
        </main>
    );
};

export default Body;
