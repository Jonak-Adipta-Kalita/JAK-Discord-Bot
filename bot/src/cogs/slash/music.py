import disnake, youtube_dl
import src.core.embeds as embeds
import src.core.functions as funcs
from src.core.bot import JAKDiscordBot
from disnake.ext import commands


class Music_(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
        self.bot = bot

        self.name: str = ""

    @commands.slash_command(description="Connect/Leave VC")
    @commands.has_guild_permissions(connect=True)
    async def vc(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @commands.slash_command(description="Play, Pause, Resume, Stop Music")
    @commands.has_guild_permissions(connect=True)
    async def music(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @vc.sub_command(name="join", description="Joins the VC you are currently in")
    @commands.has_guild_permissions(connect=True)
    async def vc_join(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        if inter.author.voice is None:
            await inter.edit_original_message(
                "You are not Connected to a Voice Channel!!"
            )
            return
        vc: disnake.VoiceClient = inter.voice_client
        if vc is None:
            voice_channel = inter.author.voice.channel
            try:
                await voice_channel.connect()
                await inter.edit_original_message("Connected!!")
            except disnake.HTTPException:
                await inter.edit_original_message(
                    "Can't Connect to this Voice Channel!!"
                )
        else:
            await inter.edit_original_message("I am already in a Voice Channel!!")

    @vc.sub_command(name="leave", description="Leaves VC")
    @commands.has_guild_permissions(connect=True)
    async def vc_leave(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        vc: disnake.VoiceClient = inter.voice_client
        if vc:
            await inter.edit_original_message("Disconnected!!")
            await vc.disconnect()
        else:
            await inter.edit_original_message(
                "I am not Connected to any Voice Channel!!"
            )

    @music.sub_command(
        name="play",
        description="Plays the Music",
        options=[
            disnake.Option(
                name="music_name",
                description="Name or YouTube Link of the Song",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    @commands.has_guild_permissions(connect=True)
    async def music_play(
        self, inter: disnake.ApplicationCommandInteraction, music_name: str
    ):
        await inter.response.defer()

        if (
            not music_name.startswith("https://")
            and music_name in self.bot.bad_words
            and not inter.channel.is_nsfw
        ):
            return

        vc: disnake.VoiceClient = inter.voice_client

        if vc:
            if vc.is_playing():
                await inter.edit_original_message("One song is already playing!!")
                return

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
                    await inter.edit_original_message(
                        embed=embeds.music_playing_embed(info)
                    )
                    self.name = music_name

                source = disnake.FFmpegPCMAudio(url, **FFMPEG_OPTIONS)
                vc.play(source)

        else:
            await inter.edit_original_message(
                "I am not Connected to any Voice Channel!!"
            )

    @music.sub_command(name="pause", description="Pauses the Music")
    @commands.has_guild_permissions(connect=True)
    async def music_pause(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        vc: disnake.VoiceClient = inter.voice_client

        if vc:
            if vc.is_playing():
                await inter.edit_original_message("Song Paused!!")
                vc.pause()
            else:
                await inter.edit_original_message("No Song is Playing!!")
        else:
            await inter.edit_original_message(
                "I am not Connected to any Voice Channel!!"
            )

    @music.sub_command(name="resumt", description="Resumes the Music")
    @commands.has_guild_permissions(connect=True)
    async def music_resume(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        vc: disnake.VoiceClient = inter.voice_client

        if vc:
            if vc.is_paused():
                await inter.edit_original_message("Song Resumed!!")
                vc.resume()
            else:
                await inter.edit_original_message("No Song is Paused!!")
        else:
            await inter.edit_original_message(
                " I am not Connected to any Voice Channel!!"
            )

    @music.sub_command(
        name="volume",
        description="Adjusts the Volume as per given amount",
        options=[
            disnake.Option(
                name="volume",
                description="Volume of the Song",
                type=disnake.OptionType.integer,
                required=True,
            )
        ],
    )
    @commands.has_guild_permissions(connect=True)
    async def music_volume(
        self, inter: disnake.ApplicationCommandInteraction, volume: int
    ):
        await inter.response.defer()

        vc: disnake.VoiceClient = inter.voice_client

        if vc:
            if not 0 > volume > 100:
                volume = volume / 100
                vc.source = disnake.PCMVolumeTransformer(original=vc.source, volume=1.0)
                vc.source.volume = volume

                await inter.edit_original_message(f"Changed volume to {volume * 100}%")
            else:
                await inter.edit_original_message(
                    "Volume must be between 0 to 100 (Inclusive)"
                )
        else:
            await inter.edit_original_message(
                "I am not Connected to any Voice Channel!!"
            )

    @music.sub_command(name="stop", description="Stops the Music")
    @commands.has_guild_permissions(connect=True)
    async def music_stop(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        vc: disnake.VoiceClient = inter.voice_client

        if vc:
            if vc.is_playing() or vc.is_paused():
                await inter.edit_original_message("Song Stopped!!")
                self.name = ""
                vc.stop()
            else:
                await inter.edit_original_message("No Song is Playing")
        else:
            await inter.edit_original_message(
                "I am not Connected to any Voice Channel!!"
            )

    @music.sub_command(name="lyrics", description="Get the Lyrics of the playing Music")
    @commands.has_guild_permissions(connect=True)
    async def music_lyrics(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        vc: disnake.VoiceClient = inter.voice_client

        if not (vc.is_playing() or vc.is_paused()):
            await inter.edit_original_message("No Song is Playing!!")
            return

        if self.name.startswith("https://"):
            await inter.edit_original_message("Links are not allowed to get Lyrics")
            return

        try:
            lyrics = (await funcs.get_lyrics(name=self.name.replace(" ", "+")))[
                "lyrics"
            ]
            await inter.edit_original_message(
                embed=embeds.music_lyrics_embed(lyrics=lyrics)
            )
        except KeyError:
            await inter.edit_original_message(
                embed=embeds.error_embed("Lyrics not Found!!")
            )


def setup(bot: JAKDiscordBot):
    bot.add_cog(Music_(bot))
