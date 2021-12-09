import discord, credentials, os, googletrans, asyncio, itertools
from discord.ext import commands
from dislash import *
from src.functions import get_prefix, translate_text
from src.embeds import translation_embed, warning_embed


class JAKDiscordBot(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents, bad_words):
        self.bad_words = bad_words
        self.prefix = command_prefix
        super().__init__(
            command_prefix=command_prefix, intents=intents, help_command=None
        )

        for files in os.listdir(f"./src/cogs/"):
            if files.endswith(".py"):
                self.load_extension(f"src.cogs.{files[:-3]}")

    async def on_connect(self):
        print("Bot is Connected!!")

    async def on_disconnect(self):
        print("Bot is Disconnected!!")

    async def on_ready(self):
        self.slash = SlashClient(self)
        servers = len(self.guilds)
        statuses = [
            ("listening", f"{self.prefix}help"),
            ("watching", f"{servers} {'Servers' if servers != 1 else 'Server'}!!"),
        ]
        for type, message in itertools.cycle(statuses):
            await self.change_presence(
                status=discord.Status.online,
                activity=discord.Activity(
                    type=discord.ActivityType.listening
                    if type == "listening" and type != "watching"
                    else discord.ActivityType.watching,
                    name=message,
                ),
            )
            await asyncio.sleep(60)

    async def on_message(self, message: discord.Message):
        member = message.author

        if member == self.user:
            return

        msg = message.content
        perms = message.channel.permissions_for(message.guild.me)

        if perms.manage_messages:
            for word in self.bad_words:
                if word in msg.lower().split(" "):
                    try:
                        await member.send(
                            embed=warning_embed(
                                f"The word `{word}` is banned!! Watch your Language"
                            )
                        )
                        await message.delete()
                    except discord.HTTPException:
                        await message.delete()
                    break

        if len(msg) >= 3:
            translation = translate_text(msg)
            if translation.src != "en":
                language_name = ""
                languages_dict = googletrans.LANGUAGES

                if translation.src in languages_dict:
                    language_name = languages_dict[translation.src].title()

                    if message.channel.id == 918028426353455116:
                        await message.channel.send(
                            embed=translation_embed(
                                text=msg,
                                translated_text=translation.text,
                                language_name=language_name,
                                language_iso=translation.src,
                                author=member,
                            )
                        )
                    else:

                        def translation_check(reaction, user):
                            global author_reacted
                            author_reacted = user
                            return (
                                str(reaction.emoji) == "🔤"
                                and reaction.message == message
                                and not user.bot
                            )

                        try:
                            await self.wait_for(
                                "reaction_add", check=translation_check, timeout=60.0
                            )
                            await message.channel.send(
                                embed=translation_embed(
                                    text=msg,
                                    translated_text=translation.text,
                                    language_name=language_name,
                                    language_iso=translation.src,
                                    author=member,
                                    author_reacted=author_reacted,
                                )
                            )
                        except asyncio.TimeoutError:
                            pass

        await self.process_commands(message)

    async def on_member_join(self, member: discord.Member):
        perms = member.guild.me.guild_permissions
        if perms.manage_guild and perms.manage_messages:
            try:
                await member.send(f"Welcome to **{member.guild}**!!")
            except discord.HTTPException:
                pass

    async def on_member_remove(self, member: discord.Member):
        perms = member.guild.me.guild_permissions
        if perms.manage_guild and perms.manage_messages:
            try:
                await member.send(f"You just left **{member.guild}**, What a Shame!!")
            except discord.HTTPException:
                pass

    async def on_command_error(
        self, ctx: commands.Context, error: discord.HTTPException
    ):
        print(error)
        member = ctx.message.author

        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"{member.mention} Its not a valid Command!!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(
                f"{member.mention} You don't have the Appropriate Permissions to run this command!!"
            )
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"{member.mention} Please make sure to provide all the required Arguments!!"
            )
        elif isinstance(error, commands.BadArgument):
            await ctx.send(
                f"{member.mention} Please make sure to provide the Arguments correctly!!"
            )


if __name__ == "__main__":
    bad_words = []
    with open("src/filters/profanity.txt", "r") as f:
        bad_words = f.read().splitlines()

    bot = JAKDiscordBot(
        command_prefix=get_prefix(), intents=discord.Intents.all(), bad_words=bad_words
    )

    bot.run(credentials.TOKEN)
