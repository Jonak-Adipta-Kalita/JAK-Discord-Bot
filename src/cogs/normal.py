import discord
from discord.ext import commands
from src.functions import get_prefix

prefix = get_prefix()

class Normal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_blank_value = "\u200b"

    @commands.command()
    async def help(self, ctx: commands.Context):
        embed = discord.Embed(
            title=f"{prefix} help",
            description="Shows all the Commands!!",
            color=discord.Color.blue(),
        )
        embed.add_field(name=f"{prefix} help", value="Show Commands", inline=False)
        embed.add_field(name=f"{prefix} ping", value="Show the Ping", inline=False)
        embed.add_field(
            name=f"{prefix} show_rules", value="Show the Rules", inline=False
        )
        embed.add_field(
            name=f"{prefix} 8ball <question>",
            value="Play 8ball Game",
            inline=False,
        )
        embed.add_field(
            name=f"{prefix} help_moderation",
            value="Show the Moderation Commands",
            inline=False,
        )
        embed.add_field(
            name=f"{prefix} help_music",
            value="Show the Music Commands",
            inline=False,
        )
        embed.add_field(
            name=f"{prefix} help_tictactoe",
            value="Show the commands for Tic-Tac-Toe Game",
            inline=False,
        )
        embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

        await ctx.send(embed=embed)

    @commands.command()
    async def show_rules(self, ctx: commands.Context):
        embed = discord.Embed(
            title=f"{prefix} show_rules",
            description="Show all the Rules!!",
            color=discord.Color.blue(),
        )
        embed.add_field(
            name="Be respectful, civil, and welcoming.",
            value=self.embed_blank_value,
            inline=False,
        )
        embed.add_field(
            name="No inappropriate or unsafe content.",
            value=self.embed_blank_value,
            inline=False,
        )
        embed.add_field(
            name="Do not misuse or spam in any of the channels.",
            value=self.embed_blank_value,
            inline=False,
        )
        embed.add_field(
            name="Any content that is NSFW is not allowed under any circumstances.",
            value=self.embed_blank_value,
            inline=False,
        )
        embed.add_field(
            name="The primary language of this server is English.",
            value=self.embed_blank_value,
            inline=False,
        )
        embed.add_field(
            name="Discord names and avatars must be appropriate.",
            value=self.embed_blank_value,
            inline=False,
        )
        embed.add_field(
            name="Controversial topics such as religion or politics are not allowed.",
            value=self.embed_blank_value,
            inline=False,
        )
        embed.add_field(
            name="Do not attempt to bypass any blocked words.",
            value=self.embed_blank_value,
            inline=False,
        )
        embed.add_field(
            name="Don’t ping without legitimate reasoning behind them.",
            value=self.embed_blank_value,
            inline=False,
        )
        embed.add_field(
            name="Catfishing and any sort of fake identities are forbidden.",
            value=self.embed_blank_value,
            inline=False,
        )
        embed.add_field(
            name="Do not advertise without permission.",
            value=self.embed_blank_value,
            inline=False,
        )
        embed.add_field(
            name="Raiding is not allowed.", value=self.embed_blank_value, inline=False
        )
        embed.set_footer(text="Please Follow all the RULES!!")

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Ping: {round(self.bot.latency * 1000)}")


def setup(bot):
    bot.add_cog(Normal(bot))
