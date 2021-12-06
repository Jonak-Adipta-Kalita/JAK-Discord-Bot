from discord.ext import commands
from src.embeds import meme_embed


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(ctx: commands.Context):
        await ctx.send(embed=meme_embed())


def setup(bot):
    bot.add_cog(Meme(bot))
