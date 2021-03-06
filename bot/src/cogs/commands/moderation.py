import disnake, pytimeparse, requests
import src.core.embeds as embeds
from src.core.bot import JAKDiscordBot
from disnake.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
        self.bot = bot

    @commands.command(description="Kick Member or Bot")
    @commands.has_guild_permissions(kick_members=True)
    @commands.bot_has_guild_permissions(kick_members=True)
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
    @commands.has_guild_permissions(kick_members=True, ban_members=True)
    @commands.bot_has_guild_permissions(kick_members=True, ban_members=True)
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
    @commands.has_guild_permissions(kick_members=True, ban_members=True)
    @commands.bot_has_guild_permissions(kick_members=True, ban_members=True)
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
                        status="UNBANNED",
                        message="Reason: Nothing",
                    )
                )
                return

    @commands.command(description="Delete messages as given amount")
    @commands.has_guild_permissions(manage_messages=True)
    @commands.bot_has_guild_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def clear(self, ctx: commands.Context, amount: int):
        await ctx.channel.purge(limit=amount)

    @commands.command(description="Remove a Channel")
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def remove_channel(
        self,
        ctx: commands.Context,
        channel: disnake.TextChannel,
        *,
        reason: str = "Nothing",
    ):
        await channel.delete(reason=reason)

    @commands.command(description="Remove a Message")
    @commands.bot_has_guild_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def remove_message(
        self,
        ctx: commands.Context,
        message_id: str,
        *,
        reason: str = "Nothing",
    ):
        message = self.bot.get_message(int(message_id))

        await ctx.reply(
            embed=embeds.moderation_embed(
                title=f"{message.author.display_name}#{message.author.discriminator}",
                status="WARNED and REMOVED MESSAGE",
                message=f"Reason: {reason}",
            )
        )
        await message.delete()

    @commands.command(description="Timeout Member or Bot")
    @commands.has_guild_permissions(moderate_members=True)
    @commands.bot_has_guild_permissions(moderate_members=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def timeout(
        self,
        ctx: commands.Context,
        member: disnake.Member,
        duration: str,
        *,
        reason="Nothing",
    ):
        seconds = pytimeparse.parse(duration)
        if seconds:
            await member.timeout(duration=seconds, reason=reason)
            await ctx.reply(
                embed=embeds.moderation_embed(
                    title=f"{member.display_name}#{member.discriminator}",
                    status="TIMED OUT",
                    message=f"For: {int(duration)}\nReason: {reason}",
                )
            )
        else:
            await ctx.reply("Time specified incorrectly!!")

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        member = message.author

        if member == self.bot.user:
            return

        msg = message.content
        guild = message.guild
        channel = message.channel
        perms = channel.permissions_for(guild.me)

        if perms.manage_messages and not channel.is_nsfw():
            for word in self.bot.bad_words:
                if word in msg.lower().split(" "):
                    try:
                        await member.send(
                            embed=embeds.moderation_embed(
                                title="YOU",
                                status="WARNED",
                                message=f"The word `{word}` is banned!! Watch your Language",
                            )
                        )
                        await message.delete()
                    except disnake.HTTPException:
                        await message.delete()
                    break


def setup(bot: JAKDiscordBot):
    bot.add_cog(Moderation(bot))
