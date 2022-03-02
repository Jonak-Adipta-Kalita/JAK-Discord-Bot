import disnake, credentials
import src.core.functions as funcs
from disnake.ext import commands
from src.core.bot import JAKDiscordBot

if __name__ == "__main__":
    try:
        bot = JAKDiscordBot(
            command_prefix=commands.bot.when_mentioned_or(*funcs.get_prefixes()),
            intents=disnake.Intents.all(),
        )

        bot.run(credentials.TOKEN)
    except KeyboardInterrupt:
        print("Bot Exited!!")
