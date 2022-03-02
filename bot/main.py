import credentials
from src.core.bot import JAKDiscordBot

if __name__ == "__main__":
    try:
        bot = JAKDiscordBot()

        bot.run(credentials.TOKEN)
    except KeyboardInterrupt:
        print("Bot Exited!!")
