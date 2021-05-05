<div>

# JAK-Discord-Bot

</div>

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

### Starting the Bot:
Create `token.txt`. Now go to [Discord Developers Portal]
(https://discord.com/developers/applications) and create a new application. Now go to the Bot 
section and create a new Bot. Now copy the Token given in the redirected page and paste it in 
the `token.txt` file. Now go to the OAuth2 section and copy the CLIENT ID. Now open a new tab 
in your browser and type `https://discord.com/api/oauth2/authorize?client_id=<YOUR_CLIENT_ID>&scope=bot` 
and hit enter. Now add the Bot to your server. After you added the bot, open any terminal in the 
directory and type 
```bash
python main.py
```

## Contributors
<a href = "https://github.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=Jonak-Adipta-Kalita/JAK-Discord-Bot"/>
</a>
