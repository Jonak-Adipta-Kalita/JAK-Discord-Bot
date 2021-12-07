import discord
from discord.ext import commands
from src.functions import get_prefix

BOT_LOGO_URL = "https://avatars.githubusercontent.com/u/70377522?v=4"
prefix = get_prefix()


def rules_embed(embed_blank_value: str):
    embed = discord.Embed(
        color=discord.Color.blue(),
    )
    embed.set_author(name="JAK Discord Bot - Rules", icon_url=BOT_LOGO_URL)
    embed.add_field(
        name="Be respectful, civil, and welcoming.",
        value=embed_blank_value,
        inline=False,
    )
    embed.add_field(
        name="No inappropriate or unsafe content.",
        value=embed_blank_value,
        inline=False,
    )
    embed.add_field(
        name="Do not misuse or spam in any of the channels.",
        value=embed_blank_value,
        inline=False,
    )
    embed.add_field(
        name="Any content that is NSFW is not allowed under any circumstances.",
        value=embed_blank_value,
        inline=False,
    )
    embed.add_field(
        name="The primary language of this server is English.",
        value=embed_blank_value,
        inline=False,
    )
    embed.add_field(
        name="Discord names and avatars must be appropriate.",
        value=embed_blank_value,
        inline=False,
    )
    embed.add_field(
        name="Controversial topics such as religion or politics are not allowed.",
        value=embed_blank_value,
        inline=False,
    )
    embed.add_field(
        name="Do not attempt to bypass any blocked words.",
        value=embed_blank_value,
        inline=False,
    )
    embed.add_field(
        name="Don’t ping without legitimate reasoning behind them.",
        value=embed_blank_value,
        inline=False,
    )
    embed.add_field(
        name="Catfishing and any sort of fake identities are forbidden.",
        value=embed_blank_value,
        inline=False,
    )
    embed.add_field(
        name="Do not advertise without permission.",
        value=embed_blank_value,
        inline=False,
    )
    embed.add_field(
        name="Raiding is not allowed.", value=embed_blank_value, inline=False
    )
    embed.set_footer(text="Please Follow all the RULES!!")

    return embed


def help_embed(ctx):
    embed = discord.Embed(
        color=discord.Color.blue(),
    )
    embed.set_author(name="JAK Discord Bot - Help Menu", icon_url=BOT_LOGO_URL)
    embed.add_field(name=f"{prefix}ping", value="Show the Ping", inline=False)
    embed.add_field(name=f"{prefix}show_rules", value="Show the Rules", inline=False)
    embed.add_field(
        name=f"{prefix}help_moderation",
        value="Show the Moderation Commands",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}help_games",
        value="Show the Game Commands",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}help_music",
        value="Show the Music Commands",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}help_fun",
        value="Show the Fun Commands",
        inline=False,
    )
    embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

    return embed


def moderation_help_embed(ctx: commands.Context):
    embed = discord.Embed(
        color=discord.Color.blue(),
    )
    embed.set_author(
        name="JAK Discord Bot - Moderation Help Menu", icon_url=BOT_LOGO_URL
    )
    embed.add_field(
        name=f"{prefix}clear <amount>",
        value="Delete messages as given amount",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}kick @<member> reason=<reason>",
        value="Kick Member or Bot",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}ban @<member> reason=<reason>",
        value="Ban Member or Bot",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}unban <member, tag>",
        value="Unban Member or Bot",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}mute @<member> reason=<reason>",
        value="Mute Member or Bot",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}unmute @<member> reason=<reason>",
        value="UnMute Member or Bot",
        inline=False,
    )
    embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

    return embed


def games_help_embed(ctx: commands.Context):
    embed = discord.Embed(
        color=discord.Color.blue(),
    )
    embed.set_author(name="JAK Discord Bot - Games Help Menu", icon_url=BOT_LOGO_URL)
    embed.add_field(
        name=f"{prefix}8ball <question>",
        value="Play 8ball Game",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}tictactoe_help",
        value="Show Help Menu for Tic-Tac-Toe",
        inline=False,
    )
    embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

    return embed


def music_help_embed(ctx: commands.Context):
    embed = discord.Embed(
        color=discord.Color.blue(),
    )
    embed.set_author(name="JAK Discord Bot - Music Help Menu", icon_url=BOT_LOGO_URL)
    embed.add_field(
        name=f"{prefix}join_vc",
        value="Joins the VC you are currently in",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}leave_vc",
        value="Leaves VC",
        inline=False,
    )
    embed.add_field(
        name=f'{prefix}play_music "<music_name>"/<url>',
        value="Plays the Music",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}pause_music",
        value="Pauses the Music",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}resume_music",
        value="Resumes the Music",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}volume_music <volume>",
        value="Adjusts the Volume as per given amount",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}stop_music",
        value="Stops the Music",
        inline=False,
    )
    embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

    return embed


def fun_help_embed(ctx: commands.Context):
    embed = discord.Embed(
        color=discord.Color.blue(),
    )
    embed.set_author(name="JAK Discord Bot - Fun Help Menu", icon_url=BOT_LOGO_URL)
    embed.add_field(
        name=f"{prefix}joke",
        value="Display a Joke",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}meme",
        value="Display a Meme",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}emojify <text>",
        value="Convert Text to Emoji",
        inline=False,
    )
    embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

    return embed


def warning_embed(message: str):
    embed = discord.Embed(
        title="YOU HAVE BEEN WARNED!!",
        description=message,
        color=discord.Color.blue(),
    )

    return embed


def tictactoe_help_embed(ctx: commands.Context):
    embed = discord.Embed(
        color=discord.Color.blue(),
    )
    embed.set_author(
        name="JAK Discord Bot - TicTacToe Help Menu", icon_url=BOT_LOGO_URL
    )
    embed.add_field(
        name=f"{prefix}tictactoe @<1st Player> @<2nd Player>",
        value="Start Tic-Tac-Toe",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}tictactoe_place <Position in Integer>",
        value="Place your position for Tic-Tac-Toe",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}tictactoe_stop",
        value="Stops Tic-Tac-Toe",
        inline=False,
    )
    embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

    return embed


def music_playing_embed(info: dict):
    embed = discord.Embed(
        title=info["title"],
        description=f"Channel: {info['channel']}",
        color=discord.Color.blue(),
    )
    embed.set_image(url=info["thumbnail"])

    return embed


def translation_embed(
    text: str, translated_text: str, language_name: str, language_iso: str
):
    embed = discord.Embed(
        title="",
        description=f"{text} -> {translated_text}",
        color=discord.Color.blue(),
    )
    embed.set_footer(text=f"{language_name} ({language_iso}) -> English (en)")

    return embed


def meme_embed():
    embed = discord.Embed(color=discord.Color.blue())

    return embed
