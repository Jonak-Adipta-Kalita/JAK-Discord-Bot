import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot, bad_words):
        self.bot = bot
        self.bad_words = bad_words

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot Started!!")
        await self.bot.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.listening, name="!JAK help"
            ),
        )

    @commands.Cog.listener()
    async def on_message(self, message):
        member = message.author

        if member == self.bot.user:
            return

        msg_list = []
        msg = message.content.lower()

        for msg_ in msg.split(" "):
            msg_list.append(msg_)

        for word in self.bad_words:
            if word in msg_list:
                embed = discord.Embed(
                    title="YOU HAVE BEEN WARNED!!",
                    description=f"The word `{word}` is banned!! Watch your Language",
                    color=discord.Color.blue(),
                )

                await member.send(embed=embed)
                await message.delete()
                break
                return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            await member.send(f"Welcome to **{member.guild}**!!")
        except Exception:
            pass

    @commands.Cog.listener()
    async def on_member_remove(member):
        try:
            await member.send(f"You just left **{member.guild}**, What a Shame!!")
        except Exception:
            pass

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
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

    with open("src/bad_words.txt", "r") as f:
        bad_words = f.read().splitlines()

    bot.add_cog(Events(bot, bad_words))
