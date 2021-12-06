import discord, googletrans, asyncio, itertools
from discord.ext import commands
from src.embeds import translation_embed, warning_embed
from src.functions import get_prefix, translate_text


prefix = get_prefix()


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot, bad_words):
        self.bot = bot
        self.bad_words = bad_words

    @commands.Cog.listener()
    async def on_connect(self):
        print("Bot is Connected!!")

    @commands.Cog.listener()
    async def on_disconnect(self):
        print("Bot is Disconnected!!")

    @commands.Cog.listener()
    async def on_ready(self):
        servers = len(self.bot.guilds)

        statuses = [
            ("listening", f"{prefix}help"),
            ("watching", f"{servers} {'Servers' if servers != 1 else 'Server'}!!"),
        ]

        for type, message in itertools.cycle(statuses):
            await self.bot.change_presence(
                status=discord.Status.online,
                activity=discord.Activity(
                    type=discord.ActivityType.listening
                    if type == "listening" and type != "watching"
                    else discord.ActivityType.watching,
                    name=message,
                ),
            )
            await asyncio.sleep(60)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        member = message.author

        if member == self.bot.user:
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

                def translation_check(reaction, user):
                    return (
                        str(reaction.emoji) == "🔤"
                        and reaction.message == message
                        and not user.bot
                    )

                language_name = ""
                languages_dict = googletrans.LANGUAGES

                if translation.src in languages_dict:
                    language_name = languages_dict[translation.src].title()

                    await self.bot.wait_for("reaction_add", check=translation_check)

                    await message.channel.send(
                        embed=translation_embed(
                            msg,
                            translation.text,
                            language_name,
                            translation.src,
                        )
                    )

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        perms = member.guild.me.guild_permissions
        if perms.manage_server:
            try:
                await member.send(f"Welcome to **{member.guild}**!!")
            except discord.HTTPException:
                pass

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        perms = member.guild.me.guild_permissions
        if perms.manage_server:
            try:
                await member.send(f"You just left **{member.guild}**, What a Shame!!")
            except discord.HTTPException:
                pass

    @commands.Cog.listener()
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


def setup(bot):
    bad_words = []

    with open("src/filters/profanity.txt", "r") as f:
        bad_words = f.read().splitlines()

    bot.add_cog(Events(bot, bad_words))
