import discord
import src.embeds as embeds
from discord.ext import commands


class User(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def user_avatar(self, ctx: commands.Context, member: discord.Member):
        await ctx.reply(
            embed=embeds.user_avatar_embed(
                avatar_url=member.avatar_url, name=member.display_name
            )
        )


def setup(bot: commands.Bot):
    bot.add_cog(User(bot))
