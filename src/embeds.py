import disnake
import src.functions as funcs
from disnake.ext import commands

prefix = funcs.get_prefix()


def ping_bot_embed(bot_name: str, bot_avatar_url: str, servers: int):
    body_text = f"""
        Use `{prefix}help` to see the Help Embed!!

        Total Servers = {servers}
    """

    embed = disnake.Embed(
        title=f"Hello Buddy!!", description=body_text, color=disnake.Color.blue()
    )
    embed.set_author(name=f"{bot_name}", icon_url=bot_avatar_url)

    return embed


def rules_embed(bot_name: str, bot_avatar_url: str, rules: str):
    embed = disnake.Embed(
        color=disnake.Color.blue(),
    )
    embed.set_author(name=f"{bot_name} - Rules", icon_url=bot_avatar_url)
    embed.set_footer(text="Please Follow all the RULES!!")
    for rule in rules:
        embed.add_field(
            name=rule[0],
            value=rule[1],
            inline=False,
        )

    return embed


def help_embed(ctx: commands.Context, bot_name: str, bot_avatar_url: str):
    embed = disnake.Embed(
        color=disnake.Color.blue(),
    )
    embed.set_author(name=f"{bot_name} - Help Menu", icon_url=bot_avatar_url)
    embed.add_field(
        name=f"{prefix}help moderation",
        value="Show the Moderation Commands",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}help games",
        value="Show the Game Commands",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}help music",
        value="Show the Music Commands",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}help fun",
        value="Show the Fun Commands",
        inline=False,
    )
    embed.set_footer(
        text=f"Information Requested by: {ctx.author.display_name}",
        icon_url=ctx.author.avatar.url,
    )

    return embed


def moderation_help_embed(ctx: commands.Context, bot_name: str, bot_avatar_url: str):
    embed = disnake.Embed(
        color=disnake.Color.blue(),
    )
    embed.set_author(
        name=f"{bot_name} - Moderation Help Menu",
        icon_url=bot_avatar_url,
    )
    embed.add_field(
        name=f"{prefix}clear <amount>",
        value="Delete messages as given amount",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}kick @<member> [reason]",
        value="Kick Member or Bot",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}ban @<member> [reason]",
        value="Ban Member or Bot",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}unban <member,tag>",
        value="Unban Member or Bot",
        inline=False,
    )
    embed.add_field(name=f"{prefix}show_rules", value="Show the Rules", inline=False)
    embed.add_field(name=f"{prefix}latency", value="Show the Latency", inline=False)
    embed.add_field(
        name=f"{prefix}user_details [member]",
        value="Show the Details of a Member",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}server_stats",
        value="Show the Server Information",
        inline=False,
    )
    embed.set_footer(
        text=f"Information Requested by: {ctx.author.display_name}",
        icon_url=ctx.author.avatar.url,
    )

    return embed


def games_help_embed(ctx: commands.Context, bot_name: str, bot_avatar_url: str):
    embed = disnake.Embed(
        color=disnake.Color.blue(),
    )
    embed.set_author(name=f"{bot_name} - Games Help Menu", icon_url=bot_avatar_url)
    embed.add_field(
        name=f"{prefix}8ball <question>",
        value="Play 8ball Game",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}help tictactoe",
        value="Show Help Menu for Tic-Tac-Toe",
        inline=False,
    )
    embed.set_footer(
        text=f"Information Requested by: {ctx.author.display_name}",
        icon_url=ctx.author.avatar.url,
    )

    return embed


def music_help_embed(ctx: commands.Context, bot_name: str, bot_avatar_url: str):
    embed = disnake.Embed(
        color=disnake.Color.blue(),
    )
    embed.set_author(name=f"{bot_name} - Music Help Menu", icon_url=bot_avatar_url)
    embed.add_field(
        name=f"{prefix}vc join",
        value="Joins the VC you are currently in",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}vc leave",
        value="Leaves VC",
        inline=False,
    )
    embed.add_field(
        name=f'{prefix}music play "<music_name>"/<url>',
        value="Plays the Music",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}music pause",
        value="Pauses the Music",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}music resume",
        value="Resumes the Music",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}music volume <volume>",
        value="Adjusts the Volume as per given amount",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}music stop",
        value="Stops the Music",
        inline=False,
    )
    embed.set_footer(
        text=f"Information Requested by: {ctx.author.display_name}",
        icon_url=ctx.author.avatar.url,
    )

    return embed


def fun_help_embed(ctx: commands.Context, bot_name: str, bot_avatar_url: str):
    embed = disnake.Embed(
        color=disnake.Color.blue(),
    )
    embed.set_author(name=f"{bot_name} - Fun Help Menu", icon_url=bot_avatar_url)
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
    embed.add_field(
        name=f"{prefix}code_snippet <code>",
        value="Convert Code Block to Snippet",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}morse <text>",
        value="Encode or Decode PlainText/MorseCode into MorseCode/PlainText",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}calculator",
        value="Use a Calculator to do Mathamatics",
        inline=False,
    )
    embed.set_footer(
        text=f"Information Requested by: {ctx.author.display_name}",
        icon_url=ctx.author.avatar.url,
    )

    return embed


def tictactoe_help_embed(ctx: commands.Context, bot_name: str, bot_avatar_url: str):
    embed = disnake.Embed(
        color=disnake.Color.blue(),
    )
    embed.set_author(
        name=f"{bot_name} - TicTacToe Help Menu",
        icon_url=bot_avatar_url,
    )
    embed.add_field(
        name=f"{prefix}tictactoe @<1st Player> @<2nd Player>",
        value="Start Tic-Tac-Toe Game",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}tictactoe place <Position in Integer>",
        value="Place your position for Tic-Tac-Toe Game",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}tictactoe stop",
        value="Stops Tic-Tac-Toe Game",
        inline=False,
    )
    embed.set_footer(
        text=f"Information Requested by: {ctx.author.display_name}",
        icon_url=ctx.author.avatar.url,
    )

    return embed


def discord_together_help_embed(
    ctx: commands.Context, bot_name: str, bot_avatar_url: str
):
    embed = disnake.Embed(
        color=disnake.Color.blue(),
    )
    embed.set_author(
        name=f"{bot_name} - Discord Together Help Menu", icon_url=bot_avatar_url
    )
    embed.add_field(
        name=f"{prefix}together youtube",
        value="Use `YouTube Together` Activity",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}together chess",
        value="Use `Chess Together` Activity",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}together poker",
        value="Use `Poker Together` Activity",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}together betrayal",
        value="Use `Betrayal Together` Activity",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}together fishing",
        value="Use `Fishing Together` Activity",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}together letter_tile",
        value="Use `Letter Tile Together` Activity",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}together word_snack",
        value="Use `Word Snack Together` Activity",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}together doodle_crew",
        value="Use `Doddle Crew Together` Activity",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}together spell_cast",
        value="Use `Spell Cast Together` Activity",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}together awkword",
        value="Use `Awkword Together` Activity",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}together checkers",
        value="Use `Checkers Together` Activity",
        inline=False,
    )
    embed.set_footer(
        text=f"Information Requested by: {ctx.author.display_name}",
        icon_url=ctx.author.avatar.url,
    )

    return embed


def warning_embed(message: str):
    embed = disnake.Embed(
        title="YOU HAVE BEEN WARNED!!",
        description=message,
        color=disnake.Color.blue(),
    )

    return embed


def music_playing_embed(info: dict):
    embed = disnake.Embed(
        title=info["title"],
        description=f"Channel: {info['channel']}",
        color=disnake.Color.blue(),
    )
    embed.set_image(url=info["thumbnail"])

    return embed


def translation_embed(
    text: str,
    translated_text: str,
    language_name: str,
    language_iso: str,
    author: disnake.Member,
    author_reacted: disnake.Member = None,
):
    embed = disnake.Embed(
        color=disnake.Color.blue(),
    )
    embed.set_author(name=f"Author: {author.display_name}")
    embed.add_field(name="Translation (en)", value=translated_text, inline=True)
    embed.add_field(
        name=f"Original ({language_iso} - {language_name})", value=text, inline=True
    )
    if author_reacted:
        embed.set_footer(
            text=f"Request: {author_reacted.display_name}",
        )

    return embed


def pronunciation_embed(
    text: str,
    pronunciation: str,
    author: disnake.Member,
    author_reacted: disnake.Member,
):
    embed = disnake.Embed(color=disnake.Color.blue())
    embed.set_author(name=f"Author: {author.display_name}")
    embed.add_field(name="Text", value=text, inline=True)
    embed.add_field(name=f"Pronunciation", value=pronunciation, inline=True)
    embed.set_footer(
        text=f"Request: {author_reacted.display_name}",
    )

    return embed


def meme_embed(label: str, image: str):
    embed = disnake.Embed(title=f"Caption: **{label}**", color=disnake.Color.blue())
    embed.set_image(url=image)

    return embed


def user_details_embed(member: disnake.Member):
    embed = disnake.Embed(color=disnake.Color.blue())
    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(name="Name:", value=member.display_name, inline=False)
    embed.add_field(name="Created At:", value=member.created_at, inline=False)
    embed.add_field(name="Joined At:", value=member.joined_at, inline=False)
    embed.add_field(name="Is Bot:", value=member.bot, inline=False)

    return embed


def server_stats_embed(
    name: str,
    description: str,
    icon: disnake.Asset,
    owner: str,
    guild_id: int,
    member_count: int,
    banner: disnake.Asset = None,
):
    embed = disnake.Embed(
        description=description if description else "", color=disnake.Color.blue()
    )
    embed.set_author(name=f"{name}'s Stats", icon_url=icon.url)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=guild_id, inline=True)
    embed.add_field(name="Member Count", value=member_count, inline=True)
    if banner:
        embed.set_thumbnail(url=banner.url)

    return embed


def morse_code_embed(title: str, converted: str):
    embed = disnake.Embed(
        title=title, description=f"```yaml\n{converted}```", color=disnake.Color.blue()
    )

    return embed


def calculator_embed():
    embed = disnake.Embed(
        title="Calculator", description="```yaml\n0```", color=disnake.Color.blue()
    )
    embed.set_footer(
        text="To interact with your virtual calculator, click the shown buttons."
    )

    return embed
