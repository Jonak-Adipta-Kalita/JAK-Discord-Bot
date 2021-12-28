import src.emojis as emojis
import src.embeds as embeds
from disnake.ext import commands


class Poll(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def poll(
        self,
        ctx: commands.Context,
        question: str,
        option1: str,
        option2: str = None,
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
        if option2:
            await msg.add_reaction(emojis.alphabets["regional_indicator_b"])
        if option3:
            await msg.add_reaction(emojis.alphabets["regional_indicator_c"])


def setup(bot: commands.Bot):
    bot.add_cog(Poll(bot))
