import discord, youtube_dl
from discord.ext import commands
from src.embeds import music_help_embed, music_playing_embed
from src.functions import get_prefix

prefix = get_prefix()


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def help_music(self, ctx: commands.Context):
        await ctx.send(embed=music_help_embed(ctx))

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def join_vc(self, ctx: commands.Context):
        member = ctx.message.author

        if ctx.author.voice is None:
            await ctx.send(
                f"{member.mention} You are not Connected to a Voice Channel!!"
            )
            return
        if ctx.voice_client is None:
            voice_channel = ctx.author.voice.channel
            try:
                await voice_channel.connect()
                await ctx.send(f"{member.mention} Connected!!")
            except discord.HTTPException:
                await ctx.send(
                    f"{member.mention} Can't Connect to this Voice Channel!!"
                )
        else:
            await ctx.send(f"{member.mention} I am already in a Voice Channel!!")

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def leave_vc(self, ctx: commands.Context):
        member = ctx.message.author

        if ctx.voice_client:
            await ctx.send(f"{member.mention} Disconnected!!")
            await ctx.voice_client.disconnect()
        else:
            await ctx.send(
                f"{member.mention} I am not Connected to any Voice Channel!!"
            )

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def play_music(self, ctx: commands.Context, music_name: str):
        member = ctx.message.author
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
                    await ctx.send(embed=music_playing_embed(info))

                source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
                vc.play(source)

        else:
            await ctx.send(
                f"{member.mention} I am not Connected to any Voice Channel!!"
            )

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def pause_music(self, ctx: commands.Context):
        member = ctx.message.author
        vc = ctx.voice_client

        if vc:
            if ctx.voice_client.is_playing():
                await ctx.send(f"{member.mention} Song Paused!!")
                await ctx.voice_client.pause()
            else:
                await ctx.send(f"{member.mention} No Song is Playing!!")
        else:
            await ctx.send(
                f"{member.mention} I am not Connected to any Voice Channel!!"
            )

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def resume_music(self, ctx: commands.Context):
        member = ctx.message.author
        vc = ctx.voice_client

        if vc:
            if ctx.voice_client.is_paused():
                await ctx.send(f"{member.mention} Song Resumed!!")
                await ctx.voice_client.resume()
            else:
                await ctx.send(f"{member.mention} No Song is Paused!!")
        else:
            await ctx.send(
                f"{member.mention} I am not Connected to any Voice Channel!!"
            )

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def volume_music(self, ctx: commands.Context, volume: int):
        member = ctx.message.author
        vc = ctx.voice_client

        if vc:
            vc.source.volume = volume / 100
            await ctx.send(f"{member.mention} Changed volume to {volume}%")
        else:
            await ctx.send(
                f"{member.mention} I am not Connected to any Voice Channel!!"
            )

    @commands.command()
    # @commands.has_permissions(connect=True)
    async def stop_music(self, ctx: commands.Context):
        member = ctx.message.author
        vc = ctx.voice_client

        if vc:
            if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                await ctx.send(f"{member.mention} Song Stopped!!")
                await ctx.voice_client.stop()
            else:
                await ctx.send(f"{member.mention} No Song is Playing")
        else:
            await ctx.send(
                f"{member.mention} I am not Connected to any Voice Channel!!"
            )


def setup(bot):
    bot.add_cog(Music(bot))
