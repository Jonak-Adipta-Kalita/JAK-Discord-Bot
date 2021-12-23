import discord, dislash, credentials, os, googletrans, asyncio, itertools
import src.functions as funcs
import src.embeds as embeds
import src.emojis as emojis
from discord.ext import commands


class JAKDiscordBot(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents, bad_words: list):
        self.bad_words = bad_words
        self.prefix = command_prefix
        self.servers = 0
        super().__init__(
            command_prefix=command_prefix, intents=intents, help_command=None
        )

        self.load_extension("src.cogs.help")

        for files in os.listdir(f"./src/cogs/commands/"):
            if files.endswith(".py"):
                self.load_extension(f"src.cogs.commands.{files[:-3]}")

        for files in os.listdir(f"./src/cogs/slash/"):
            if files.endswith(".py"):
                self.load_extension(f"src.cogs.slash.{files[:-3]}")

    async def on_connect(self):
        print("Bot is Connected!!")

    async def on_disconnect(self):
        print("Bot is Disconnected!!")

    async def on_ready(self):
        self.slash = dislash.SlashClient(self)
        self.servers = len(self.guilds)
        statuses = [
            ("listening", f"{self.prefix}help"),
            (
                "watching",
                f"{self.servers} {'Servers' if self.servers != 1 else 'Server'}!!",
            ),
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
            await message.add_reaction(emojis.broom)
            return

        msg = message.content
        perms = message.channel.permissions_for(message.guild.me)

        if msg == f"<@!{self.user.id}>" or msg == f"<@{self.user.id}>":
            await message.reply(
                embed=embeds.ping_bot_embed(
                    bot_name=self.user.name,
                    bot_avatar_url=self.user.avatar_url,
                    servers=self.servers,
                )
            )

        if perms.manage_messages:
            for word in self.bad_words:
                if word in msg.lower().split(" "):
                    try:
                        await member.send(
                            embed=embeds.warning_embed(
                                f"The word `{word}` is banned!! Watch your Language"
                            )
                        )
                        await message.delete()
                    except discord.HTTPException:
                        await message.delete()
                    break

        if len(msg) >= 3 and not msg.startswith(funcs.get_prefix()):
            translation = funcs.translate_text(msg)

            if translation.src != "en":
                language_name = ""
                languages_dict = googletrans.LANGUAGES

                def translation_check(reaction, user):
                    global author_reacted_translation
                    author_reacted_translation = user
                    return (
                        str(reaction.emoji) == emojis.abc
                        and reaction.message == message
                        and not user.bot
                    )

                if translation.src in languages_dict:
                    language_name = languages_dict[translation.src].title()

                    try:
                        await self.wait_for(
                            "reaction_add", check=translation_check, timeout=60.0
                        )
                        await message.channel.send(
                            embed=embeds.translation_embed(
                                text=msg,
                                translated_text=translation.text,
                                language_name=language_name,
                                language_iso=translation.src,
                                author=member,
                                author_reacted=author_reacted_translation,
                            )
                        )
                    except asyncio.TimeoutError:
                        pass

            else:

                def pronunciation_check(reaction, user):
                    global author_reacted_pronunciation
                    author_reacted_pronunciation = user
                    return (
                        str(reaction.emoji) == emojis.abc
                        and reaction.message == message
                        and not user.bot
                    )

                try:
                    await self.wait_for(
                        "reaction_add", check=pronunciation_check, timeout=60.0
                    )
                    await message.channel.send(
                        embed=embeds.pronunciation_embed(
                            text=msg,
                            pronunciation=funcs.pronunciation(msg),
                            author=member,
                            author_reacted=author_reacted_pronunciation,
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
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply("Its not a valid Command!!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply(
                "You don't have the Appropriate Permissions to run this command!!"
            )
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Please make sure to provide all the required Arguments!!")
        elif isinstance(error, commands.BadArgument):
            await ctx.reply("Please make sure to provide the Arguments correctly!!")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply("This Command is currently in Cooldown for you!!")
        else:
            print(error)


if __name__ == "__main__":
    bad_words = []
    with open("src/filters/profanity.txt", "r") as f:
        bad_words = f.read().splitlines()

    bot = JAKDiscordBot(
        command_prefix=funcs.get_prefix(),
        intents=discord.Intents.all(),
        bad_words=bad_words,
    )

    bot.run(credentials.TOKEN)
