from discord.ext import commands
import discord, credentials
import src.variables as variables


class JAKDiscordBot(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)


if __name__ == "__main__":
    extensions = ["normal", "events", "moderation", "tictactoe", "8ball", "music"]

    bot = JAKDiscordBot(command_prefix=variables.PREFIX, intents=discord.Intents.all())
    bot.remove_command("help")

    for extension in extensions:
        try:
            bot.load_extension(f"src.cogs.{extension}")
        except Exception as e:
            print(f"Error: {e}")

    bot.run(credentials.TOKEN)
