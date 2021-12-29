import disnake
import src.core.emojis as emojis
import src.core.embeds as embeds
from disnake.ext import commands


class Misc_(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        description="Create a Poll",
        options=[
            disnake.Option(
                name="question",
                description="The Question!!",
                type=disnake.OptionType.string,
                required=True,
            ),
            disnake.Option(
                name="option1",
                description="The First Option!!",
                type=disnake.OptionType.string,
                required=True,
            ),
            disnake.Option(
                name="option2",
                description="The Second Option!!",
                type=disnake.OptionType.string,
                required=True,
            ),
            disnake.Option(
                name="option3",
                description="The Third Option!!",
                type=disnake.OptionType.string,
                required=False,
            ),
        ],
    )
    async def poll(
        self,
        inter: disnake.ApplicationCommandInteraction,
        question: str,
        option1: str,
        option2: str,
        option3: str = None,
    ):
        await inter.response.send_message(
            embed=embeds.poll_embed(
                question=question,
                option1=option1,
                option2=option2,
                option3=option3,
            )
        )

        msg = await inter.original_message()

        await msg.add_reaction(emojis.alphabets["regional_indicator_a"])
        await msg.add_reaction(emojis.alphabets["regional_indicator_b"])
        if option3:
            await msg.add_reaction(emojis.alphabets["regional_indicator_c"])

    @commands.slash_command(description="Show the Rules")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def show_rules(self, inter: disnake.ApplicationCommandInteraction):
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

        await inter.response.send_message(
            embed=embeds.rules_embed(
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar.url,
                rules=rules,
            )
        )

    @commands.slash_command(description="Show the Latency")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def latency(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Ping: {round(self.bot.latency * 1000)}")

    @commands.slash_command(
        description="Show the Details of a Member",
        options=[
            disnake.Option(
                name="member",
                description="The Member!!",
                type=disnake.OptionType.mentionable,
                required=False,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def member_details(
        self,
        inter: disnake.ApplicationCommandInteraction,
        member: disnake.Member = None,
    ):
        if not member:
            member = inter.author
            fetched_member = await self.bot.fetch_user(inter.author.id)
        else:
            fetched_member = await self.bot.fetch_user(member.id)
        await inter.response.send_message(
            embed=embeds.member_details_embed(
                member=member, fetched_member=fetched_member
            )
        )

    @commands.slash_command(description="Show the Server Information")
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def server_stats(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            embed=embeds.server_stats_embed(guild=inter.guild)
        )


def setup(bot: commands.Bot):
    bot.add_cog(Misc_(bot))
