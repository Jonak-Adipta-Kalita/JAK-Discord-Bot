from discord.ext import commands
from src.embeds import help_embed, rules_embed
from src.functions import get_prefix

prefix = get_prefix()


class Normal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_blank_value = "\u200b"

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def help(self, ctx: commands.Context):
        await ctx.send(embed=help_embed(ctx))

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def show_rules(self, ctx: commands.Context):
        await ctx.send(embed=rules_embed(self.embed_blank_value))

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Ping: {round(self.bot.latency * 1000)}")


def setup(bot):
    bot.add_cog(Normal(bot))
