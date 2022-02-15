module.exports = {
    content: [
        "./src/pages/**/*.{js,ts,jsx,tsx}",
        "./src/components/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            fontFamily: {
                "otomanopee-one": ["OtomanopeeOne", "sans-serif"],
            },
            colors: {
                "bg-color": {
                    DEFAULT: "#272934",
                },
            },
        },
    },
    plugins: [require("tailwind-scrollbar-hide")],
};
