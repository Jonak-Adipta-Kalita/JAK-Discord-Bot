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
            await voice_channel.connect()
        else:
            await ctx.send(f"{member.mention} I am already in a Voice Channel!!")

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def leave_vc(self, ctx):
        member = ctx.message.author

        if ctx.voice_client:
            await ctx.voice_client.disconnect()
        else:
            await ctx.send(
                f"{member.mention} I am not Connected to any Voice Channel!!"
            )

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def play_music(self, ctx, music_name):
        vc = ctx.voice_client

        if vc:
            url = music_name

            FFMPEG_OPTIONS = {
                "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                "options": "-vn",
            }
            YDL_OPTIONS = {"formats": "bestaudio"}
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url_ = info["formats"][0]["url"]
                source = await discord.FFmpegOpusAudio.from_probe(
                    url_, **FFMPEG_OPTIONS
                )

                vc.play(source)
        else:
            print(f"{member.mention} I am not Connected to any Voice Channel!!")

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def pause_music(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Song Paused!!")

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def resume_music(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Song Paused!!")

    @commands.command(pass_context=True)
    # @commands.has_permissions(connect=True)
    async def stop_music(self, ctx):
        await ctx.voice_client.stop()
        await ctx.send("Song Stopped!!")


def setup(bot):
    bot.add_cog(Music(bot))
