from discord.ext import commands
import discord_together
import credentials

class DiscordTogether(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.together_control = None
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.together_control = await discord_together.DiscordTogether(credentials.TOKEN)

    @commands.command(aliases=["yt_together"])
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def youtube_together(self, ctx: commands.Context):
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "youtube"
        )
        await ctx.reply(link, delete_after=60)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def poker_together(self, ctx: commands.Context):
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "poker"
        )
        await ctx.reply(link, delete_after=60)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def chess_together(self, ctx: commands.Context):
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "chess"
        )
        await ctx.reply(link, delete_after=60)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def betrayal_together(self, ctx: commands.Context):
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "betrayal"
        )
        await ctx.reply(link, delete_after=60)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def fishing_together(self, ctx: commands.Context):
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "fishing"
        )
        await ctx.reply(link, delete_after=60)


def setup(bot):
    bot.add_cog(DiscordTogether(bot))
