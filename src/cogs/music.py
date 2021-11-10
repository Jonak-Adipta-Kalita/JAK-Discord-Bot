import discord, youtube_dl
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
        member = ctx.message.author

        if ctx.author.voice is None:
            await ctx.send(
                f"{member.mention} You are not Connected to a Voice Channel!!"
            )
            return
        if ctx.voice_client is None:
            voice_channel = ctx.author.voice.channel
            await ctx.send(f"{member.mention} Connected!!")
            await voice_channel.connect()
        else:
            await ctx.send(f"{member.mention} I am already in a Voice Channel!!")

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def leave_vc(self, ctx):
        member = ctx.message.author

        if ctx.voice_client:
            await ctx.send(f"{member.mention} Disconnected!!")
            await ctx.voice_client.disconnect()
        else:
            await ctx.send(
                f"{member.mention} I am not Connected to any Voice Channel!!"
            )

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def play_music(self, ctx, music_name):
        member = ctx.message.author
        vc = ctx.voice_client

        if vc:
            FFMPEG_OPTIONS = {
                "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                "options": "-vn",
            }
            YDL_OPTIONS = {"formats": "bestaudio"}
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(f"ytsearch:{music_name}", download=False)
                url = info["entries"][0]["webpage_url"]
                source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)

                vc.play(source)
        else:
            await ctx.send(
                f"{member.mention} I am not Connected to any Voice Channel!!"
            )

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def pause_music(self, ctx):
        member = ctx.message.author

        await ctx.send(f"{member.mention} Song Paused!!")
        await ctx.voice_client.pause()

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def resume_music(self, ctx):
        member = ctx.message.author

        await ctx.send(f"{member.mention} Song Resumed!!")
        await ctx.voice_client.resume()

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def stop_music(self, ctx):
        member = ctx.message.author

        await ctx.send(f"{member.mention} Song Stopped!!")
        await ctx.voice_client.stop()


def setup(bot):
    bot.add_cog(Music(bot))
