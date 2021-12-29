import disnake
import src.embeds as embeds
import src.functions as funcs
from disnake.ext import commands


prefix = funcs.get_prefix()


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embed_blank_value: str = "\u200b"

    @commands.command(description="Kick Member or Bot")
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def kick(
        self, ctx: commands.Context, member: disnake.Member, *, reason="Nothing"
    ):
        await member.kick(reason=reason)
        await ctx.reply(
            embed=embeds.moderation_embed(
                title=f"{member.display_name}#{member.discriminator}",
                status="KICKED",
                message=f"Reason: {reason}",
            )
        )

    @commands.command(description="Ban Member or Bot")
    @commands.has_permissions(kick_members=True, ban_members=True)
    @commands.bot_has_permissions(kick_members=True, ban_members=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def ban(
        self, ctx: commands.Context, member: disnake.Member, *, reason="Nothing!!"
    ):
        await member.ban(reason=reason)
        await ctx.reply(
            embed=embeds.moderation_embed(
                title=f"{member.display_name}#{member.discriminator}",
                status="BANNED",
                message=f"Reason: {reason}",
            )
        )

    @commands.command(description="Unban Member or Bot")
    @commands.has_permissions(kick_members=True, ban_members=True)
    @commands.bot_has_permissions(kick_members=True, ban_members=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def unban(self, ctx: commands.Context, *, member: str):
        banned_user = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_user:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.reply(
                    embed=embeds.moderation_embed(
                        title=f"{member_name}#{member_discriminator}",
                        status="UN Banned",
                        message="",
                    )
                )
                return

    @commands.command(description="Delete messages as given amount")
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def clear(self, ctx: commands.Context, amount: int):
        await ctx.channel.purge(limit=amount)


def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))
