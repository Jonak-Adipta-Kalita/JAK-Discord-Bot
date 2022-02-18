import Document, { Html, Head, Main, NextScript } from "next/document";

class MyDocument extends Document {
    render() {
        return (
            <Html lang="en">
                <Head>
                    <link rel="manifest" href="/manifest.json" />
                    <meta
                        name="description"
                        content="Jonak Adipta Kalita's Discord Bot's Dashboard"
                    />
                    <meta name="keywords" content="Discord, Bot, Dashboard" />
                    <meta name="author" content="Jonak Adipta Kalita" />
                    <meta name="publisher" content="Jonak Adipta Kalita" />
                    <meta name="copyright" content="Jonak Adipta Kalita" />
                    <meta name="theme-color" content="#272934" />
                    <link
                        rel="icon"
                        type="image/ico"
                        href="/images/favicon.ico"
                    />
                    <link
                        rel="apple-touch-icon"
                        type="image/ico"
                        href="/images/favicon.ico"
                    />
                    <meta name="apple-mobile-web-app-capable" content="yes" />
                    <meta
                        name="apple-mobile-web-app-title"
                        content="JAK Discord Bot"
                    />
                    <meta
                        name="apple-mobile-web-app-status-bar-style"
                        content="default"
                    />
                </Head>
                <body className="">
                    <Main />
                    <NextScript />
                </body>
            </Html>
        );
    }
}

export default MyDocument;
