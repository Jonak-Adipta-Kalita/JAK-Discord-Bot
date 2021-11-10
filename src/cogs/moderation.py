import discord
import src.variables as variables
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help_moderation(self, ctx):
        embed = discord.Embed(
            title=f"{variables.PREFIX} help_moderation",
            description="Shows all the Moderation Commands!!",
            color=discord.Color.blue(),
        )
        embed.add_field(
            name=f"{variables.PREFIX} clear <amount>",
            value="Delete messages as given amount",
            inline=False,
        )
        embed.add_field(
            name=f"{variables.PREFIX} kick @<member> reason=<reason>",
            value="Kick Member or Bot",
            inline=False,
        )
        embed.add_field(
            name=f"{variables.PREFIX} ban @<member> reason=<reason>",
            value="Ban Member or Bot",
            inline=False,
        )
        embed.add_field(
            name=f"{variables.PREFIX} unban <member, tag>",
            value="Unban Member or Bot",
            inline=False,
        )
        embed.add_field(
            name=f"{variables.PREFIX} mute @<member> reason=<reason>",
            value="Mute Member or Bot",
            inline=False,
        )
        embed.add_field(
            name=f"{variables.PREFIX} unmute @<member> reason=<reason>",
            value="UnMute Member or Bot",
            inline=False,
        )
        embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="Nothing"):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} is Kicked!! Reason: {reason}")

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="Nothing!!"):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} is Banned!! Reason: {reason}")

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def unban(self, ctx, *, member):
        banned_user = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_user:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{member.mention} is Unbanned!!")
                return

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def mute(ctx, member: discord.Member, *, reason=None):
        pass

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def unmute(ctx, member: discord.Member):
        pass


def setup(bot):
    bot.add_cog(Moderation(bot))
