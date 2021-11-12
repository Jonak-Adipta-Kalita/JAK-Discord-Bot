import discord
from discord.ext import commands
from src.functions import get_prefix

prefix = get_prefix()


def rules_embed(embed_blank_value: str):
    embed = discord.Embed(
        title=f"{prefix}show_rules",
        description="Show all the Rules!!",
        color=discord.Color.blue(),
    )
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
        title=f"{prefix}help",
        description="Shows all the Commands!!",
        color=discord.Color.blue(),
    )
    embed.add_field(name=f"{prefix}help", value="Show Commands", inline=False)
    embed.add_field(name=f"{prefix}ping", value="Show the Ping", inline=False)
    embed.add_field(name=f"{prefix}show_rules", value="Show the Rules", inline=False)
    embed.add_field(
        name=f"{prefix}8ball <question>",
        value="Play 8ball Game",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}help_moderation",
        value="Show the Moderation Commands",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}help_music",
        value="Show the Music Commands",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}help_tictactoe",
        value="Show the commands for Tic-Tac-Toe Game",
        inline=False,
    )
    embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

    return embed


def moderation_embed(ctx: commands.Context):
    embed = discord.Embed(
        title=f"{prefix}help_moderation",
        description="Shows all the Moderation Commands!!",
        color=discord.Color.blue(),
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


def tictactoe_embed(ctx: commands.Context):
    embed = discord.Embed(
        title=f"{prefix}help_tictactoe",
        description="Shows all the Tic-Tac-Toe Game Commands!!",
        color=discord.Color.blue(),
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


def music_embed(ctx: commands.Context):
    embed = discord.Embed(
        title=f"{prefix}help_music",
        description="Shows all the Music Commands!!",
        color=discord.Color.blue(),
    )
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
        name=f"{prefix}play_music <music_name>/<url>",
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


def warning_embed(word: str):
    embed = discord.Embed(
        title="YOU HAVE BEEN WARNED!!",
        description=f"The word `{word}` is banned!! Watch your Language",
        color=discord.Color.blue(),
    )

    return embed


def translation_embed(text: str, translated_text: str):
    embed = discord.Embed(
        title="Translation!!",
        description=f"Translated text!!",
        color=discord.Color.blue(),
    )
    embed.add_field(
        name=f"Text: {text}", value=f"Translated: {translated_text}", inline=False
    )

    return embed
