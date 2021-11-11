import discord, credentials, os
from discord.ext import commands
from functions import get_prefix


class JAKDiscordBot(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents):
        super().__init__(
            command_prefix=command_prefix, intents=intents, help_command=None
        )

        self.COGS: list = list()

        for files in os.listdir(f"./src/cogs/"):
            if files.endswith(".py"):
                self.load_extension(f"src.cogs.{files[:-3]}")


if __name__ == "__main__":
    bot = JAKDiscordBot(command_prefix=get_prefix, intents=discord.Intents.all())
    bot.run(credentials.TOKEN)
