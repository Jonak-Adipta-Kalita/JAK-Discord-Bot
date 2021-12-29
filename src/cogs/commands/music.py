import disnake, youtube_dl
import src.core.embeds as embeds
import src.core.functions as funcs
from disnake.ext import commands

prefix = funcs.get_prefix()


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, description="Connect/Leave VC")
    async def vc(self, ctx: commands.Context):
        pass

    @commands.group(
        invoke_without_command=True, description="Play, Pause, Resume, Stop Music"
    )
    async def music(self, ctx: commands.Context):
        pass

    @vc.command(description="Joins the VC you are currently in")
    # @commands.has_permissions(connect=True)
    async def join(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        if ctx.voice_client is None:
            voice_channel = ctx.author.voice.channel
            try:
                await voice_channel.connect()
                await ctx.reply("Connected!!")
            except disnake.HTTPException:
                await ctx.reply("Can't Connect to this Voice Channel!!")
        else:
            await ctx.reply("I am already in a Voice Channel!!")

    @vc.command(description="Leaves VC")
    # @commands.has_permissions(connect=True)
    async def leave(self, ctx: commands.Context):
        if ctx.voice_client:
            await ctx.reply("Disconnected!!")
            await ctx.voice_client.disconnect()
        else:
            await ctx.reply("I am not Connected to any Voice Channel!!")

    @music.command(description="Plays the Music")
    # @commands.has_permissions(connect=True)
    async def play(self, ctx: commands.Context, *, music_name: str):
        vc = ctx.voice_client

        if vc:
            FFMPEG_OPTIONS = {
                "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                "options": "-vn",
            }
            YDL_OPTIONS = {"formats": "bestaudio"}
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = {}
                url = ""

                if music_name.startswith("https://"):
                    info = ydl.extract_info(music_name, download=False)
                    url = info["formats"][0]["url"]
                else:
                    info_ = ydl.extract_info(f"ytsearch:{music_name}", download=False)
                    url_ = info_["entries"][0]["webpage_url"]
                    info = ydl.extract_info(url_, download=False)
                    url = info["formats"][0]["url"]

                if info:
                    await ctx.reply(embed=embeds.music_playing_embed(info))

                source = await disnake.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
                vc.play(source)

        else:
            await ctx.reply("I am not Connected to any Voice Channel!!")

    @music.command(description="Pauses the Music")
    # @commands.has_permissions(connect=True)
    async def pause(self, ctx: commands.Context):
        vc = ctx.voice_client

        if vc:
            if ctx.voice_client.is_playing():
                await ctx.reply("Song Paused!!")
                await ctx.voice_client.pause()
            else:
                await ctx.reply("No Song is Playing!!")
        else:
            await ctx.reply("I am not Connected to any Voice Channel!!")

    @music.command(description="Resumes the Music")
    # @commands.has_permissions(connect=True)
    async def resume(self, ctx: commands.Context):
        vc = ctx.voice_client

        if vc:
            if ctx.voice_client.is_paused():
                await ctx.reply("Song Resumed!!")
                await ctx.voice_client.resume()
            else:
                await ctx.reply("No Song is Paused!!")
        else:
            await ctx.reply(" I am not Connected to any Voice Channel!!")

    @music.command(description="Adjusts the Volume as per given amount")
    # @commands.has_permissions(connect=True)
    async def volume(self, ctx: commands.Context, volume: int):
        vc = ctx.voice_client

        if vc:
            vc.source.volume = volume / 100
            await ctx.reply(f"Changed volume to {volume}%")
        else:
            await ctx.reply("I am not Connected to any Voice Channel!!")

    @music.command(description="Stops the Music")
    # @commands.has_permissions(connect=True)
    async def stop(self, ctx: commands.Context):
        vc = ctx.voice_client

        if vc:
            if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                await ctx.reply("Song Stopped!!")
                await ctx.voice_client.stop()
            else:
                await ctx.reply("No Song is Playing")
        else:
            await ctx.reply("I am not Connected to any Voice Channel!!")


def setup(bot: commands.Bot):
    bot.add_cog(Music(bot))
