import disnake
import src.embeds as embeds
import src.emojis as emojis
import src.functions as funcs
from disnake.ext import commands


prefix = funcs.get_prefix()


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embed_blank_value = "\u200b"

    @commands.command(description="Kick Member or Bot")
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def kick(
        self, ctx: commands.Context, member: disnake.Member, *, reason="Nothing"
    ):
        await member.kick(reason=reason)
        await ctx.reply(f"{member.mention} is Kicked!! Reason: {reason}")

    @commands.command(description="Ban Member or Bot")
    @commands.has_permissions(kick_members=True, ban_members=True)
    @commands.bot_has_permissions(kick_members=True, ban_members=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def ban(
        self, ctx: commands.Context, member: disnake.Member, *, reason="Nothing!!"
    ):
        await member.ban(reason=reason)
        await ctx.reply(f"{member.mention} is Banned!! Reason: {reason}")

    @commands.command(description="Unban Member or Bot")
    @commands.has_permissions(kick_members=True, ban_members=True)
    @commands.bot_has_permissions(kick_members=True, ban_members=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def unban(self, ctx: commands.Context, *, member):
        banned_user = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_user:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.reply(f"{member} is Unbanned!!")
                return

    @commands.command(description="Delete messages as given amount")
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def clear(self, ctx: commands.Context, amount: int):
        await ctx.channel.purge(limit=amount)

    @commands.command(aliases=["rules"], description="Show the Rules")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def show_rules(self, ctx: commands.Context):
        rules = [
            (f"{emojis.numbers['one']}   No Negativity", self.embed_blank_value),
            (f"{emojis.numbers['two']}   No Spamming", self.embed_blank_value),
            (f"{emojis.numbers['three']}   No Swearing", self.embed_blank_value),
            (
                f"{emojis.numbers['four']}   No Discriminatory Or Hate Speech",
                self.embed_blank_value,
            ),
            (f"{emojis.numbers['five']}   No NSFW Content", self.embed_blank_value),
            (
                f"{emojis.numbers['six']}   No Potentially Harmful Content",
                self.embed_blank_value,
            ),
        ]

        await ctx.reply(
            embed=embeds.rules_embed(
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar.url,
                rules=rules,
            )
        )

    @commands.command(description="Show the Latency", aliases=["ping", "ms"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def latency(self, ctx: commands.Context):
        await ctx.reply(f"Ping: {round(self.bot.latency * 1000)}")

    @commands.command(description="Show the Details of a Member")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def member_details(
        self, ctx: commands.Context, member: disnake.Member = None
    ):
        if not member:
            member = ctx.author
            fetched_member = await self.bot.fetch_user(ctx.author.id)
        else:
            fetched_member = await self.bot.fetch_user(member.id)
        await ctx.reply(
            embed=embeds.member_details_embed(
                member=member, fetched_member=fetched_member
            )
        )

    @commands.command(description="Show the Server Information")
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def server_stats(self, ctx: commands.Context):
        name = ctx.guild.name
        description = ctx.guild.description
        icon = ctx.guild.icon
        owner = ctx.guild.owner
        guild_id = ctx.guild.id
        member_count = ctx.guild.member_count
        banner = ctx.guild.banner

        await ctx.reply(
            embed=embeds.server_stats_embed(
                name=name,
                description=description,
                icon=icon,
                owner=owner,
                guild_id=guild_id,
                member_count=member_count,
                banner=banner,
            )
        )


def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))
