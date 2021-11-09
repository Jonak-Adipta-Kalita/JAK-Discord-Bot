import discord
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help_music(self, ctx):
        embed = discord.Embed(
            title="!JAK help_music",
            description="Shows all the Music Commands!!",
            color=discord.Color.blue(),
        )
        embed.add_field(
            name="!JAK join_vc",
            value="Joins the VC you are currently in",
            inline=False,
        )
        embed.add_field(
            name="!JAK leave_vc",
            value="Leaves VC",
            inline=False,
        )
        embed.add_field(
            name="!JAK play_music <music_name>",
            value="Plays the Music",
            inline=False,
        )
        embed.add_field(
            name="!JAK pause_music",
            value="Pauses the Music",
            inline=False,
        )
        embed.add_field(
            name="!JAK resume_music",
            value="Resumes the Music",
            inline=False,
        )
        embed.add_field(
            name="!JAK stop_music",
            value="Stops the Music",
            inline=False,
        )
        embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def join_vc(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def leave_vc(self, ctx):
        await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(Music(bot))
