<div align='center'>

# JAK-Discord-Bot

[![Discord](https://img.shields.io/discord/752800104112717826?style=for-the-badge)](https://discord.gg/S3UfGkW)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg?style=for-the-badge)](https://github.com/psf/black)
![License](https://img.shields.io/github/license/Jonak-Adipta-Kalita/JAK-Discord-Bot?style=for-the-badge)
![GitHub Repo Stars](https://img.shields.io/github/stars/Jonak-Adipta-Kalita/JAK-Discord-Bot?style=for-the-badge)
![GitHub Forks](https://img.shields.io/github/forks/Jonak-Adipta-Kalita/JAK-Discord-Bot?style=for-the-badge)
![GitHub Watchers](https://img.shields.io/github/watchers/Jonak-Adipta-Kalita/JAK-Discord-Bot?style=for-the-badge)
![Made by JAK](https://img.shields.io/badge/BeastNight%20TV-Made%20by%20JAK-blue?style=for-the-badge)

</div>

-   Note: [Formatting](#format-code) the Code before Pushing is Important!!
-   Prefix: $

[Invite Bot to your Server](https://jak-discord-bot.vercel.app/),
[Vote in top.gg](https://top.gg/bot/756402881913028689)

## Steps

### Clone the Repository

To Clone this Repository, open a terminal in a empty folder and type

```bash
git clone https://github.com/Jonak-Adipta-Kalita/JAK-Discord-Bot.git
```

### Installing The Required Modules

To install the required modules, just open a terminal in the directory where this project is cloned. Now type:

#### For the Bot

```bash
cd bot
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
pip install -r .\requirements.txt
```

#### For the Dashboard

```bash
cd dashboard
npm i

# or

cd dashboard
yarn
```

and hit enter.

### Getting `CHATBOT_KEY`

Follow this: [https://some-random-api.ml/docs/Welcome/Keys](https://some-random-api.ml/docs/Welcome/Keys)

### Getting `JWT_SECRET`

Use the [passwordgenerator](https://passwordsgenerator.net/) website to generate your secret.

### Getting the `PLACE_API_KEY`

Go to [WeatherAPIMap](https://openweathermap.org/) and Login after that go to [ApiKeys](https://home.openweathermap.org/api_keys),
there you will find your key.

### Getting the `NASA_API_KEY`

Go to [NASA API](https://api.nasa.gov/#signUp) website, Sign Up, then you will get a key this is your `<NASA_API_KEY>`

### Getting the Firebase Credentials

Go to [Firebase Console](http://console.firebase.google.com/) and create a Project. Enable
Google Analytics. Now click on `Realtime Database` and setup a database. Now click on the Web Icon and create an app.
After you created an app click on the cog icon in the sidebar and click on `Project settings`. Scroll to the Bottom
where you will find your app now click on Config. Copy the Config. It will give some of the credentials,
to get the other credentials click on `Service accounts` in `Project settings`. After that click on
`Generate new private key`. This will download a JSON file, you will get the remaining Credentials from
that JSON file.

### Creating the Bot:

Create `bot/.env` and `dashboard/.env.local`. Now go to [Discord Developers Portal](https://discord.com/developers/applications) and create a new application.
Now go to the Bot section and create a new Bot. Now copy the Token given in the redirected page. Now go to the OAuth Section and
copy the `CLIENT ID` and the `CLIENT SECRET` under `Client Information`.
Paste all Credentials the `bot/.env` and the `dashboard/.env.local` file

For `bot/.env`

```env
TOKEN=<YOUR_BOT_TOKEN>
CHATBOT_KEY=<YOUR_CHATBOT_KEY>
PLACE_API_KEY=<YOUR_PLACE_API_KEY>
NASA_API_KEY=<YOUR_NASA_API_KEY>
LOCAL=true

# Firebase
FIREBASE_TYPE=<YOUR_FIREBASE_TYPE>
FIREBASE_PROJECT_ID=<YOUR_FIREBASE_PROJECT_ID>
FIREBASE_PRIVATE_KEY_ID=<YOUR_FIREBASE_PRIVATE_KEY_ID>
FIREBASE_PRIVATE_KEY=<YOUR_FIREBASE_PRIVATE_KEY>
FIREBASE_CLIENT_EMAIL=<YOUR_FIREBASE_CLIENT_EMAIL>
FIREBASE_CLIENT_ID=<YOUR_FIREBASE_CLIENT_ID>
FIREBASE_AUTH_URI=<YOUR_FIREBASE_AUTH_URI>
FIREBASE_TOKEN_URI=<YOUR_FIREBASE_TOKEN_URI>
FIREBASE_AUTH_PROVIDER_X509_CERT_URL=<YOUR_FIREBASE_AUTH_PROVIDER_X509_CERT_URL>
FIREBASE_CLIENT_X509_CERT_URL=<YOUR_FIREBASE_CLIENT_X509_CERT_URL>
FIREBASE_DATABASE_URL=<YOUR_FIREBASE_DATABASE_URL>
```

For `dashboard/.env.local`

```env
# Discord
DISCORD_CLIENT_ID=<YOUR_DISCORD_CLIENT_ID>
DISCORD_CLIENT_SECRET=<YOUR_DISCORD_CLIENT_SECRET>
TOKEN=<YOUR_BOT_TOKEN>

# Auth
JWT_SECRET=<YOUR_JWT_STRING>
NEXTAUTH_URL=http://localhost:3000

# Firebase
NEXT_PUBLIC_FIREBASE_API_KEY=<YOUR_FIREBASE_API_KEY>
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=<YOUR_FIREBASE_AUTH_DOMAIN>
NEXT_PUBLIC_FIREBASE_PROJECT_ID=<YOUR_FIREBASE_PROJECT_ID>
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=<YOUR_FIREBASE_STORAGE_BUCKET>
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=<YOUR_FIREBASE_MESSAGE_SENDER_ID>
NEXT_PUBLIC_FIREBASE_APP_ID=<YOUR_FIREBASE_APP_ID>
NEXT_PUBLIC_FIREBASE_MEASUREMENT_ID=<YOUR_FIREBASE_MEASUREMENT_ID>
NEXT_PUBLIC_FIREBASE_DATABASE_URL=<YOUR_FIREBASE_DATABASE_URL>
```

like this. In the OAuth > URL Generator Section, in scopes click on `bot`. This will reveal the `Bot Permissions` select your
Permissions from `Bot Permissions`. After that open the `GENERATED URL` in a new tab. Now add the Bot to your server.

### Enabling Intents

Go to [Discord Developers Portal](https://discord.com/developers/applications) and Click on your Application. Now go to Bot
Section and Enable Everything under `Privileged Gateway Intents`.

### Adding Redirect URI

Go to [Discord Developers Portal](https://discord.com/developers/applications) and Click on your Application. Now go to OAuth
Section and in the Redirects Section click on `Add Another` now paste `http://localhost:3000/api/auth/callback/discord` in the
input field. Now click on `Save Changes`.

### Starting the Bot:

Open any terminal in the directory and type

```bash
cd bot
python main.py
```

### Starting the Dashboard

Open any terminal in the directory and type

```bash
cd dashboard
npm start

# or

cd dashboard
yarn start
```

## Format Code

In a terminal, type

```bash
.\venv\Scripts\activate
black .
deactivate
```

and press Enter.

## Technology(s) Used

-   Language: [Python](https://python.org/), [TypeScript](https://www.typescriptlang.org/)
-   Frameworks: [disnake](https://docs.disnake.dev/en/stable/), [NextJS](https://nextjs.org/)
-   Hosted: [Vercel](https://vercel.com/)

## Contributors

<a href = "https://github.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/graphs/contributors">
	<img src = "https://contrib.rocks/image?repo=Jonak-Adipta-Kalita/JAK-Discord-Bot"/>
</a>
