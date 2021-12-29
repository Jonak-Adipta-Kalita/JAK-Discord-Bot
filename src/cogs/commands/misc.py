import disnake
import src.core.emojis as emojis
import src.core.embeds as embeds
from disnake.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description="Create a Poll")
    async def poll(
        self,
        ctx: commands.Context,
        question: str,
        option1: str,
        option2: str,
        option3: str = None,
    ):
        msg = await ctx.reply(
            embed=embeds.poll_embed(
                question=question,
                option1=option1,
                option2=option2,
                option3=option3,
            )
        )
        await msg.add_reaction(emojis.alphabets["regional_indicator_a"])
        await msg.add_reaction(emojis.alphabets["regional_indicator_b"])
        if option3:
            await msg.add_reaction(emojis.alphabets["regional_indicator_c"])

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
        await ctx.reply(embed=embeds.server_stats_embed(guild=ctx.guild))


def setup(bot: commands.Bot):
    bot.add_cog(Misc(bot))
