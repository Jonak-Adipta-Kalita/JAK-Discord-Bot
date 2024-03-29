import disnake
import src.core.embeds as embeds
import src.core.functions as funcs
from src.core.bot import JAKDiscordBot
from disnake.ext import commands


class Music(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
        self.bot = bot

    @commands.group(invoke_without_command=True, description="Connect/Leave VC")
    @commands.has_guild_permissions(connect=True)
    async def vc(self, ctx: commands.Context, command: str):
        await ctx.reply("Command not Found!!")

    @commands.group(
        invoke_without_command=True, description="Play, Pause, Resume, Stop Music"
    )
    @commands.has_guild_permissions(connect=True)
    async def music(self, ctx: commands.Context, command: str):
        await ctx.reply("Command not Found!!")

    @vc.command(
        description="Joins the VC you are currently in", aliases=["connect", "c"]
    )
    @commands.has_guild_permissions(connect=True)
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

    @vc.command(description="Leaves VC", aliases=["disconnect", "dc"])
    @commands.has_guild_permissions(connect=True)
    async def leave(self, ctx: commands.Context):
        if ctx.voice_client:
            await ctx.reply("Disconnected!!")
            await ctx.voice_client.disconnect()
        else:
            await ctx.reply("I am not Connected to any Voice Channel!!")

    @music.command(description="Plays the Music")
    @commands.has_guild_permissions(connect=True)
    async def play(self, ctx: commands.Context, *, music_name: str):
        if (
            not music_name.startswith("https://")
            and music_name in self.bot.bad_words
            and not ctx.channel.is_nsfw
        ):
            return

        vc: disnake.VoiceClient = ctx.voice_client

        if vc:
            if vc.is_playing():
                await ctx.reply("One song is already playing!!")
                return

            info, source = await funcs.get_music_info(music_name)

            if info and source:
                self.bot.music_name = music_name
                await ctx.reply(embed=embeds.music_playing_embed(info))
                vc.play(source)

        else:
            await ctx.reply("I am not Connected to any Voice Channel!!")

    @music.command(description="Pauses the Music")
    @commands.has_guild_permissions(connect=True)
    async def pause(self, ctx: commands.Context):
        vc: disnake.VoiceClient = ctx.voice_client

        if vc:
            if vc.is_playing():
                await ctx.reply("Song Paused!!")
                vc.pause()
            else:
                await ctx.reply("No Song is Playing!!")
        else:
            await ctx.reply("I am not Connected to any Voice Channel!!")

    @music.command(description="Resumes the Music")
    @commands.has_guild_permissions(connect=True)
    async def resume(self, ctx: commands.Context):
        vc: disnake.VoiceClient = ctx.voice_client

        if vc:
            if vc.is_paused():
                await ctx.reply("Song Resumed!!")
                vc.resume()
            else:
                await ctx.reply("No Song is Paused!!")
        else:
            await ctx.reply(" I am not Connected to any Voice Channel!!")

    @music.command(description="Adjusts the Volume as per given amount")
    @commands.has_guild_permissions(connect=True)
    async def volume(self, ctx: commands.Context, volume: int):
        vc: disnake.VoiceClient = ctx.voice_client

        if vc:
            if not 0 > volume > 100:
                volume = volume / 100
                vc.source = disnake.PCMVolumeTransformer(original=vc.source, volume=1.0)
                vc.source.volume = volume

                await ctx.reply(f"Changed volume to {volume * 100}%")
            else:
                await ctx.reply("Volume must be between 0 to 100 (Inclusive)")
        else:
            await ctx.reply("I am not Connected to any Voice Channel!!")

    @music.command(description="Stops the Music")
    @commands.has_guild_permissions(connect=True)
    async def stop(self, ctx: commands.Context):
        vc: disnake.VoiceClient = ctx.voice_client

        if vc:
            if vc.is_playing() or vc.is_paused():
                await ctx.reply("Song Stopped!!")
                self.name = ""
                vc.stop()
            else:
                await ctx.reply("No Song is Playing")
        else:
            await ctx.reply("I am not Connected to any Voice Channel!!")

    @music.command(description="Get the Lyrics of the playing Music")
    @commands.has_guild_permissions(connect=True)
    async def lyrics(self, ctx: commands.Context):
        vc: disnake.VoiceClient = ctx.voice_client

        if not (vc.is_playing() or vc.is_paused()):
            await ctx.reply("No Song is Playing!!")
            return

        if self.name.startswith("https://"):
            await ctx.reply("Links are not allowed to get Lyrics")
            return

        try:
            lyrics = (await funcs.get_lyrics(name=self.name.replace(" ", "+")))[
                "lyrics"
            ]
            await ctx.reply(embed=embeds.music_lyrics_embed(lyrics=lyrics))
        except KeyError:
            await ctx.reply(embed=embeds.error_embed("Lyrics not Found!!"))


def setup(bot: JAKDiscordBot):
    bot.add_cog(Music(bot))
