import disnake, pytimeparse
import src.core.embeds as embeds
from src.core.bot import JAKDiscordBot
from disnake.ext import commands


class Moderation_(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
        self.bot = bot

    @commands.slash_command(
        description="Kick Member or Bot",
        options=[
            disnake.Option(
                name="member",
                description="The Member/Bot you want to Kick",
                type=disnake.OptionType.user,
                required=True,
            ),
            disnake.Option(
                name="reason",
                description="The Reason",
                type=disnake.OptionType.string,
                required=False,
            ),
        ],
    )
    @commands.has_guild_permissions(kick_members=True)
    @commands.bot_has_guild_permissions(kick_members=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def kick(
        self,
        inter: disnake.ApplicationCommandInteraction,
        member: disnake.Member,
        reason="Nothing",
    ):
        await member.kick(reason=reason)
        await inter.response.send_message(
            embed=embeds.moderation_embed(
                title=f"{member.display_name}#{member.discriminator}",
                status="KICKED",
                message=f"Reason: {reason}",
            )
        )

    @commands.slash_command(
        description="Ban Member or Bot",
        options=[
            disnake.Option(
                name="member",
                description="The Member/Bot you want to Ban",
                type=disnake.OptionType.user,
                required=True,
            ),
            disnake.Option(
                name="reason",
                description="The Reason",
                type=disnake.OptionType.string,
                required=False,
            ),
        ],
    )
    @commands.has_guild_permissions(kick_members=True, ban_members=True)
    @commands.bot_has_guild_permissions(kick_members=True, ban_members=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def ban(
        self,
        inter: disnake.ApplicationCommandInteraction,
        member: disnake.Member,
        reason="Nothing!!",
    ):
        await member.ban(reason=reason)
        await inter.response.send_message(
            embed=embeds.moderation_embed(
                title=f"{member.display_name}#{member.discriminator}",
                status="BANNED",
                message=f"Reason: {reason}",
            )
        )

    @commands.slash_command(
        description="Unban Member or Bot",
        options=[
            disnake.Option(
                name="member",
                description="The <name#discrimination> of the Member/Bot you want to Unban",
                type=disnake.OptionType.string,
                required=True,
            ),
        ],
    )
    @commands.has_guild_permissions(kick_members=True, ban_members=True)
    @commands.bot_has_guild_permissions(kick_members=True, ban_members=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def unban(self, inter: disnake.ApplicationCommandInteraction, member: str):
        banned_user = await inter.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_user:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await inter.guild.unban(user)
                await inter.response.send_message(
                    embed=embeds.moderation_embed(
                        title=f"{member_name}#{member_discriminator}",
                        status="UNBANNED",
                        message="Reason: Nothing",
                    )
                )
                return

    @commands.slash_command(
        description="Delete messages as given amount",
        options=[
            disnake.Option(
                name="amount",
                description="Amount of Messages you want to delete",
                type=disnake.OptionType.integer,
                required=True,
            ),
        ],
    )
    @commands.has_guild_permissions(manage_messages=True)
    @commands.bot_has_guild_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def clear(self, inter: disnake.ApplicationCommandInteraction, amount: int):
        await inter.channel.purge(limit=amount)

    @commands.slash_command(
        description="Remove a Channel",
        options=[
            disnake.Option(
                name="channel",
                description="The Text Channel you want to delete",
                type=disnake.OptionType.channel,
                required=True,
            ),
        ],
    )
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def remove_channel(
        self,
        inter: disnake.ApplicationCommandInteraction,
        channel: disnake.TextChannel,
        *,
        reason: str = "Nothing",
    ):
        await channel.delete(reason=reason)

    @commands.slash_command(
        description="Remove a Message",
        options=[
            disnake.Option(
                name="message_id",
                description="ID of the Message",
                type=disnake.OptionType.string,
                required=True,
            ),
            disnake.Option(
                name="reason",
                description="Reason for the deletion of the message",
                type=disnake.OptionType.string,
                required=False,
            ),
        ],
    )
    @commands.bot_has_guild_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def remove_message(
        self,
        inter: disnake.ApplicationCommandInteraction,
        message_id: str,
        reason: str = "Nothing",
    ):
        message = self.bot.get_message(int(message_id))

        inter.response.send_message(
            embed=embeds.moderation_embed(
                title=f"{message.author.display_name}#{message.author.discriminator}",
                status="WARNED and REMOVED MESSAGE",
                message=f"Reason: {reason}",
            )
        )
        await message.delete()

    @commands.slash_command(
        description="Timeout Member or Bot",
        options=[
            disnake.Option(
                name="member",
                description="The Member/Bot you want to Timeout",
                type=disnake.OptionType.user,
                required=True,
            ),
            disnake.Option(
                name="reason",
                description="The Reason",
                type=disnake.OptionType.string,
                required=False,
            ),
        ],
    )
    @commands.has_guild_permissions(moderate_members=True)
    @commands.bot_has_guild_permissions(moderate_members=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def timeout(
        self,
        inter: disnake.ApplicationCommandInteraction,
        member: disnake.Member,
        duration: str,
        *,
        reason="Nothing",
    ):
        seconds = pytimeparse.parse(duration)
        if seconds:
            await member.timeout(duration=seconds, reason=reason)
            await inter.response.send_message(
                embed=embeds.moderation_embed(
                    title=f"{member.display_name}#{member.discriminator}",
                    status="TIMED OUT",
                    message=f"For: {int(duration)}\nReason: {reason}",
                )
            )
        else:
            await inter.response.send_message(
                "Time specified incorrectly!!", ephemeral=True
            )


def setup(bot: JAKDiscordBot):
    bot.add_cog(Moderation_(bot))
