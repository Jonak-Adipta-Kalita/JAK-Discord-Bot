import discord
from discord.ext import commands
from src.functions import get_prefix
from src.embeds import moderation_embed

prefix = get_prefix()


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def help_moderation(self, ctx: commands.Context):
        await ctx.send(embed=moderation_embed(ctx))

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(
        self, ctx: commands.Context, member: discord.Member, *, reason="Nothing"
    ):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} is Kicked!! Reason: {reason}")

    @commands.command()
    @commands.has_permissions(kick_members=True, ban_members=True)
    @commands.bot_has_permissions(kick_members=True, ban_members=True)
    async def ban(
        self, ctx: commands.Context, member: discord.Member, *, reason="Nothing!!"
    ):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} is Banned!! Reason: {reason}")

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
                await ctx.send(f"{member} is Unbanned!!")
                return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx: commands.Context, amount: int):
        await ctx.channel.purge(limit=amount)

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


def setup(bot):
    bot.add_cog(Moderation(bot))
