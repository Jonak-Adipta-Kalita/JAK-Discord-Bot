from disnake.ext import commands
import discord_together
import credentials


class DiscordTogether(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.together_control = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.together_control = await discord_together.DiscordTogether(
            credentials.TOKEN
        )

    @commands.group(
        invoke_without_command=True, description="Use Discord Together Activities"
    )
    async def together(self, ctx: commands.Context):
        pass

    @together.command(description="Use `YouTube Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def youtube(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "youtube"
        )
        await ctx.reply(link, delete_after=60)

    @together.command(description="Use `Chess Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def poker(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "poker"
        )
        await ctx.reply(link, delete_after=60)

    @together.command(description="Use `Poker Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def chess(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "chess"
        )
        await ctx.reply(link, delete_after=60)

    @together.command(description="Use `Betrayal Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def betrayal(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "betrayal"
        )
        await ctx.reply(link, delete_after=60)

    @together.command(description="Use `Fishing Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def fishing(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "fishing"
        )
        await ctx.reply(link, delete_after=60)

    @together.command(description="Use `Letter Tile Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def letter_tile(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "letter-tile"
        )
        await ctx.reply(link, delete_after=60)

    @together.command(description="Use `Word Snack Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def word_snack(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "word-snack"
        )
        await ctx.reply(link, delete_after=60)

    @together.command(description="Use `Doddle Crew Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def doodle_crew(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "doodle-crew"
        )
        await ctx.reply(link, delete_after=60)

    @together.command(description="Use `Spell Cast Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def spell_cast(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "spellcast"
        )
        await ctx.reply(link, delete_after=60)

    @together.command(description="Use `Awkword Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def awkword(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "awkword"
        )
        await ctx.reply(link, delete_after=60)

    @together.command(description="Use `Checkers Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def checkers(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "checkers"
        )
        await ctx.reply(link, delete_after=60)


def setup(bot):
    bot.add_cog(DiscordTogether(bot))
