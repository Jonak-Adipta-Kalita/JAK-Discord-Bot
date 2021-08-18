<div align='center'>

# JAK-Discord-Bot
[![Discord](https://img.shields.io/discord/752800104112717826?style=for-the-badge)](https://discord.gg/S3UfGkW)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg?style=for-the-badge)](https://github.com/psf/black)

</div>

- 	Note: [Formatting](#format-code) the Code before Pushing is Important!!

Invite [Bot](https://discord.com/oauth2/authorize?client_id=756402881913028689&scope=bot) to your Server

## Steps

### Clone the Repository
To Clone this Repository, open a terminal in a empty folder and type 
```bash
git clone https://github.com/Jonak-Adipta-Kalita/JAK-Discord-Bot.git
```

### Installing The Required Modules
To install the required modules, just open a terminal in the directory where this project is cloned. Now type: 
```bash
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
pip install -r .\requirements.txt
``` 
and hit enter.

### Enabling Intents
Go to [Discord Developers Portal](https://discord.com/developers/applications) and Click on your Application. Now got to Bot 
Section and Enable `PRESENCE INTENT` and `SERVER MEMBERS INTENT` in `Privileged Gateway Intents`.

### Starting the Bot:
Create `.env`. Now go to [Discord Developers Portal](https://discord.com/developers/applications) and create a new application. Now go to the Bot 
section and create a new Bot. Now copy the Token given in the redirected page and paste it in 
the `.env` file 
```env
TOKEN=<YOUR_BOT_TOKEN>
```
like this. Now go to the OAuth2 section and copy the CLIENT ID. Now open a new tab 
in your browser and type `https://discord.com/api/oauth2/authorize?client_id=<YOUR_CLIENT_ID>&scope=bot` 
and hit enter. Now add the Bot to your server. After you added the bot, open any terminal in the 
directory and type 
```bash
python main.py
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

-   Language: [Python](https://python.org/)
-   Hosted: [Heroku](https://heroku.com/)

## Contributors
<a href = "https://github.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/graphs/contributors">
	<img src = "https://contrib.rocks/image?repo=Jonak-Adipta-Kalita/JAK-Discord-Bot"/>
</a>
