import discord
from discord.ext import commands

default_applications = {
    "youtube": "755600276941176913",
    "poker": "755827207812677713",
    "betrayal": "773336526917861400",
    "fishing": "814288819477020702",
    "chess": "832012586023256104",
}


class DiscordTogetherUrlGen:
    def __init__(self, bot):
        self.bot = bot

    async def create_link(self, voice_channel_id: int, option: str) -> str:
        if option and (
            str(option).lower().replace(" ", "") in default_applications.keys()
        ):
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": default_applications[
                    str(option).lower().replace(" ", "")
                ],
                "target_type": 2,
                "temporary": False,
                "validate": None,
            }

            try:
                result = await self.bot.http.request(
                    discord.http.Route("POST", f"/channels/{voice_channel_id}/invites"),
                    json=data,
                )
            except Exception:
                pass

            return f"https://discord.com/invite/{result['code']}"

        elif (
            option
            and (str(option).replace(" ", "") not in default_applications.keys())
            and str(option).replace(" ", "").isnumeric()
        ):
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": str(option).replace(" ", ""),
                "target_type": 2,
                "temporary": False,
                "validate": None,
            }

            try:
                result = await self.bot.http.request(
                    discord.http.Route("POST", f"/channels/{voice_channel_id}/invites"),
                    json=data,
                )
            except Exception:
                pass

            return f"https://discord.com/invite/{result['code']}"
        else:
            pass


class DiscordTogether(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.together_control = DiscordTogetherUrlGen(bot)

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
