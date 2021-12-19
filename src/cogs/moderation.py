import discord
import src.embeds as embeds
import src.functions as funcs
from discord.ext import commands

prefix = funcs.get_prefix()


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embed_blank_value = "\u200b"

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(
        self, ctx: commands.Context, member: discord.Member, *, reason="Nothing"
    ):
        await member.kick(reason=reason)
        await ctx.reply(f"{member.mention} is Kicked!! Reason: {reason}")

    @commands.command()
    @commands.has_permissions(kick_members=True, ban_members=True)
    @commands.bot_has_permissions(kick_members=True, ban_members=True)
    async def ban(
        self, ctx: commands.Context, member: discord.Member, *, reason="Nothing!!"
    ):
        await member.ban(reason=reason)
        await ctx.reply(f"{member.mention} is Banned!! Reason: {reason}")

    @commands.command()
    @commands.has_permissions(kick_members=True, ban_members=True)
    @commands.bot_has_permissions(kick_members=True, ban_members=True)
    async def unban(self, ctx: commands.Context, *, member):
        banned_user = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_user:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.reply(f"{member} is Unbanned!!")
                return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx: commands.Context, amount: int):
        await ctx.channel.purge(limit=amount)

    @commands.command(aliases=["rules"])
    async def show_rules(self, ctx: commands.Context):
        await ctx.reply(
            embed=embeds.rules_embed(
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar_url,
                embed_blank_value=self.embed_blank_value,
            )
        )

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.reply(f"Ping: {round(self.bot.latency * 1000)}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def mute(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        pass

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def unmute(self, ctx: commands.Context, member: discord.Member):
        pass


def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))
