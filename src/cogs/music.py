import discord, youtube_dl
import src.embeds as embeds
import src.functions as funcs
from discord.ext import commands

prefix = funcs.get_prefix()


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def join_vc(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.message.reply("You are not Connected to a Voice Channel!!")
            return
        if ctx.voice_client is None:
            voice_channel = ctx.author.voice.channel
            try:
                await voice_channel.connect()
                await ctx.message.reply("Connected!!")
            except discord.HTTPException:
                await ctx.message.reply("Can't Connect to this Voice Channel!!")
        else:
            await ctx.message.reply("I am already in a Voice Channel!!")

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def leave_vc(self, ctx: commands.Context):
        if ctx.voice_client:
            await ctx.message.reply("Disconnected!!")
            await ctx.voice_client.disconnect()
        else:
            await ctx.message.reply("I am not Connected to any Voice Channel!!")

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def play_music(self, ctx: commands.Context, *, music_name: str):
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
                    await ctx.message.reply(embed=embeds.music_playing_embed(info))

                source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
                vc.play(source)

        else:
            await ctx.message.reply("I am not Connected to any Voice Channel!!")

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def pause_music(self, ctx: commands.Context):
        vc = ctx.voice_client

        if vc:
            if ctx.voice_client.is_playing():
                await ctx.message.reply("Song Paused!!")
                await ctx.voice_client.pause()
            else:
                await ctx.message.reply("No Song is Playing!!")
        else:
            await ctx.message.reply("I am not Connected to any Voice Channel!!")

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def resume_music(self, ctx: commands.Context):
        member = ctx.author
        vc = ctx.voice_client

        if vc:
            if ctx.voice_client.is_paused():
                await ctx.message.reply("Song Resumed!!")
                await ctx.voice_client.resume()
            else:
                await ctx.message.reply("No Song is Paused!!")
        else:
            await ctx.message.reply(" I am not Connected to any Voice Channel!!")

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def volume_music(self, ctx: commands.Context, volume: int):
        vc = ctx.voice_client

        if vc:
            vc.source.volume = volume / 100
            await ctx.message.reply(f"Changed volume to {volume}%")
        else:
            await ctx.message.reply("I am not Connected to any Voice Channel!!")

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def stop_music(self, ctx: commands.Context):
        vc = ctx.voice_client

        if vc:
            if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                await ctx.message.reply("Song Stopped!!")
                await ctx.voice_client.stop()
            else:
                await ctx.message.reply("No Song is Playing")
        else:
            await ctx.message.reply("I am not Connected to any Voice Channel!!")


def setup(bot):
    bot.add_cog(Music(bot))
