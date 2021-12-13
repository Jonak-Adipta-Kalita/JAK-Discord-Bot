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

[Invite Bot to your Server](https://discord.com/api/oauth2/authorize?client_id=756402881913028689&permissions=8&scope=bot),
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

### Creating the Bot:

Create `.env` and `dashboard/.env.local`. Now go to [Discord Developers Portal](https://discord.com/developers/applications) and create a new application.
Now go to the Bot section and create a new Bot. Now copy the Token given in the redirected page. Now go to the OAuth Section and
copy the `CLIENT ID` and the `CLIENT SECRET` under `Client Information`.
Paste all Credentials the `.env` and the `dashboard/.env.local` file

For `.env`

```env
TOKEN=<YOUR_BOT_TOKEN>
```

For `dashboard/.env.local`

```env
DISCORD_CLIENT_ID=<YOUR_DISCORD_CLIENT_ID>
DISCORD_CLIENT_SECRET=<YOUR_DISCORD_CLIENT_SECRET>
JWT_SECRET=<YOUR_JWT_STRING>
NEXTAUTH_URL=http://localhost:3000
```

like this. In the OAuth > URL Generator Section, in scopes click on `bot`. This will reveal the `Bot Permissions` select your
Permissions from `Bot Permissions`. After that open the `GENERATED URL` in a new tab. Now add the Bot to your server.

### Enabling Intents

Go to [Discord Developers Portal](https://discord.com/developers/applications) and Click on your Application. Now got to Bot
Section and Enable Everything under `Privileged Gateway Intents`.

### Starting the Bot:

Open any terminal in the directory and type

```bash
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

-   Language: [Python](https://python.org/), [JavaScript]()
-   Frameworks: [discord.py](), [NextJS]()
-   Hosted: [Heroku](https://heroku.com/)

## Contributors

<a href = "https://github.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/graphs/contributors">
	<img src = "https://contrib.rocks/image?repo=Jonak-Adipta-Kalita/JAK-Discord-Bot"/>
</a>
