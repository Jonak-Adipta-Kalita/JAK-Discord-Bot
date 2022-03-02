import disnake, os, googletrans, asyncio, itertools
import src.core.functions as funcs
import src.core.embeds as embeds
import src.core.emojis as emojis
from disnake.ext import commands

class JAKDiscordBot(commands.Bot):
    def __init__(self, command_prefix: any, intents: disnake.Intents):
        self.prefix = funcs.get_prefixes()
        self.servers = None

        super().__init__(
            command_prefix=command_prefix, intents=intents, help_command=None
        )

        self.load_extension("src.cogs.help")
        self.load_extension("jishaku")

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
        self.servers = self.guilds
        statuses = [
            ("listening", f"{self.prefix[0]}help"),
            (
                "watching",
                f"{len(self.servers)} {'Servers' if len(self.servers) != 1 else 'Server'}!!",
            ),
        ]
        for type, message in itertools.cycle(statuses):
            await self.change_presence(
                status=disnake.Status.online,
                activity=disnake.Activity(
                    type=disnake.ActivityType.listening
                    if type == "listening" and type != "watching"
                    else disnake.ActivityType.watching,
                    name=message,
                ),
            )
            await asyncio.sleep(60)

    async def on_message(self, message: disnake.Message):
        member = message.author

        if member == self.user:
            return

        msg = message.content
        channel = message.channel

        if msg in [f"<@!{self.user.id}>", f"<@{self.user.id}>"]:
            await message.reply(
                embed=embeds.ping_bot_embed(
                    bot_name=self.user.name,
                    bot_avatar_url=self.user.avatar.url,
                    servers=len(self.servers),
                )
            )

        if len(msg) >= 3 and not (
            msg.startswith(funcs.get_prefixes()[0])
            or msg.startswith(funcs.get_prefixes()[1])
        ):
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
                        await channel.send(
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
                    await channel.send(
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

    async def on_member_join(self, member: disnake.Member):
        perms = member.guild.me.guild_permissions
        if perms.manage_guild and perms.manage_messages:
            try:
                await member.send(f"Welcome to **{member.guild.name}**!!")
            except disnake.HTTPException:
                pass

    async def on_member_remove(self, member: disnake.Member):
        perms = member.guild.me.guild_permissions
        if perms.manage_guild and perms.manage_messages:
            try:
                await member.send(
                    f"You just left **{member.guild.name}**, What a Shame!!"
                )
            except disnake.HTTPException:
                pass

    async def on_command_error(
        self, ctx: commands.Context, error: commands.CommandError
    ):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply(
                "You don't have the Appropriate Permissions to run this command!!"
            )
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply(
                "Bot doesn't have the Appropriate Permissions to run this command!!"
            )
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Please make sure to provide all the required Arguments!!")
        elif isinstance(error, commands.BadArgument):
            await ctx.reply("Please make sure to provide the Arguments correctly!!")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(
                f"This Command is currently in Cooldown for you!! Try again in {int(error.retry_after)} seconds!!"
            )
        else:
            print(error)

    async def on_slash_command_error(
        self, inter: disnake.ApplicationCommandInteraction, error: commands.CommandError
    ):
        if isinstance(error, commands.MissingPermissions):
            await inter.response.send_message(
                "You don't have the Appropriate Permissions to run this command!!"
            )
        elif isinstance(error, commands.MissingRequiredArgument):
            await inter.response.send_message(
                "Please make sure to provide all the required Arguments!!"
            )
        elif isinstance(error, commands.BadArgument):
            await inter.response.send_message(
                "Please make sure to provide the Arguments correctly!!"
            )
        elif isinstance(error, commands.CommandOnCooldown):
            await inter.response.send_message(
                f"This Command is currently in Cooldown for you!! Try again in {int(error.retry_after)} seconds!!"
            )
        else:
            print(error)
