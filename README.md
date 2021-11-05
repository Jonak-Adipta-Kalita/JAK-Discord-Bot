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

- 	Note: [Formatting](#format-code) the Code before Pushing is Important!!

Invite [Bot](https://discord.com/api/oauth2/authorize?client_id=756402881913028689&permissions=8&scope=bot) 
to your Server

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

### Creating the Bot:
Create `.env`. Now go to [Discord Developers Portal](https://discord.com/developers/applications) and create a new application. Now go to the Bot 
section and create a new Bot. Now copy the Token given in the redirected page and paste it in 
the `.env` file 
```env
TOKEN=<YOUR_BOT_TOKEN>
```
like this. Now go to the OAuth2 section and copy the CLIENT ID. Now open a new tab 
in your browser and type `https://discord.com/api/oauth2/authorize?client_id=<YOUR_CLIENT_ID>&scope=bot` 
and hit enter. Now add the Bot to your server.

### Enabling Intents
Go to [Discord Developers Portal](https://discord.com/developers/applications) and Click on your Application. Now got to Bot 
Section and Enable Everything under `Privileged Gateway Intents`.

### Starting the Bot:
Open any terminal in the directory and type 
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
