import disnake
import src.core.functions as funcs
import src.core.emojis as emojis
from disnake.ext import commands

prefix = funcs.get_prefix()


def ping_bot_embed(bot_name: str, bot_avatar_url: str, servers: int):
    embed = disnake.Embed(
        title=f"Hello Buddy!!",
        description=f"My Prefix is `{prefix}`\nUse `{prefix}help` to see the Help Embed!!\n\nTotal Servers = {servers}",
        color=disnake.Color.blue(),
    )
    embed.set_author(name=bot_name, icon_url=bot_avatar_url)

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
    embed.add_field(
        name=f"{prefix}help misc",
        value="Show the Misc Commands",
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
    embed.add_field(
        name=f"{prefix}remove_channel #<channel> [reason]",
        value="Remove a Channe;",
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
        name=f"{prefix}tictactoe @<1st Player> @<2nd Player>",
        value="Play Tic-Tac-Toe Game",
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
    embed.add_field(
        name=f"{prefix}hangman",
        value="Play Hangman Game",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}hangman guess <word/letter>",
        value="Guess Word in Hangman Game",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}hangman stop",
        value="Stops Hangman Game",
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
    embed.add_field(
        name=f"{prefix}fact",
        value="Display a Fact",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}together <activity>",
        value="Use Discord Together Activities",
        inline=False,
    )
    embed.set_footer(
        text=f"Information Requested by: {ctx.author.display_name}",
        icon_url=ctx.author.avatar.url,
    )

    return embed


def misc_help_embed(ctx: commands.Context, bot_name: str, bot_avatar_url: str):
    embed = disnake.Embed(
        color=disnake.Color.blue(),
    )
    embed.set_author(name=f"{bot_name} - Misc Help Menu", icon_url=bot_avatar_url)
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
    embed.add_field(
        name=f'{prefix}poll "<question>" <option1> <option2> [option3]',
        value="Show the Server Information",
        inline=False,
    )
    embed.set_footer(
        text=f"Information Requested by: {ctx.author.display_name}",
        icon_url=ctx.author.avatar.url,
    )

    return embed


def moderation_embed(title: str, status: str, message: str):
    embed = disnake.Embed(
        title=f"{title} HAVE BEEN {status}!!",
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


def member_details_embed(member: disnake.Member, fetched_member: disnake.User):
    roles_list = [role.mention for role in member.roles if role.name != "@everyone"]

    embed = disnake.Embed(color=disnake.Color.blue())
    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(
        name="Name:",
        value=f"{member.display_name}#{member.discriminator}",
        inline=False,
    )
    embed.add_field(
        name="Created At:",
        value=f"<t:{int(member.created_at.timestamp())}:F>",
        inline=False,
    )
    embed.add_field(
        name="Joined At:",
        value=f"<t:{int(member.joined_at.timestamp())}:F>",
        inline=False,
    )
    embed.add_field(
        name=f"Roles: ({len(roles_list)})",
        value="".join([",".join(roles_list)]),
        inline=False,
    )
    embed.add_field(name="Top Role:", value=member.top_role.mention, inline=False)
    embed.add_field(name="Is Bot:", value=member.bot, inline=False)
    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.display_avatar.url)
    if fetched_member.banner:
        embed.set_image(url=fetched_member.banner.url)

    return embed


def server_stats_embed(guild: disnake.Guild):
    emojis_list = [f"<:{emoji.name}:{emoji.id}>" for emoji in guild.emojis]
    roles_list = [role.mention for role in guild.roles if role.name != "@everyone"]

    embed = disnake.Embed(
        title=f"{guild.name}'s Stats",
        description=guild.description if guild.description else "",
        color=disnake.Color.blue(),
    )
    embed.set_thumbnail(url=guild.icon.url)
    embed.add_field(name="Owner", value=guild.owner, inline=False)
    embed.add_field(name="Server ID", value=guild.id, inline=False)
    embed.add_field(
        name="Created At:",
        value=f"<t:{int(guild.created_at.timestamp())}:F>",
        inline=False,
    )
    embed.add_field(name="Member Count", value=guild.member_count, inline=False)
    embed.add_field(
        name="Text Channels Count", value=len(guild.text_channels), inline=False
    )
    embed.add_field(
        name="Voice Channels Count", value=len(guild.voice_channels), inline=False
    )
    embed.add_field(
        name=f"Emojis ({len(emojis_list)})",
        value="".join([", ".join(emojis_list)]),
        inline=False,
    )
    embed.add_field(
        name=f"Roles ({len(roles_list)})",
        value=f'{"".join([", ".join(roles_list[::-1][:20])])}, etc',
        inline=False,
    )
    if guild.banner:
        embed.set_image(url=guild.banner.url)

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


def poll_embed(question: str, option1: str, option2: str, option3: str):
    desc = f"{emojis.alphabets['regional_indicator_a']} {option1}\n\n{emojis.alphabets['regional_indicator_b']} {option2}"
    if option3:
        desc += f"\n\n{emojis.alphabets['regional_indicator_c']} {option3}"

    embed = disnake.Embed(title=question, description=desc, color=disnake.Color.blue())

    return embed


def hangman_embed(guesses_left: int, word: str, guesses: list):
    desc = " ".join([i if i in guesses else "__" for i in word])

    embed = disnake.Embed(
        description=f"`{desc}`\n\n**{guesses_left} guesses left!!**",
        color=disnake.Color.blue(),
    )

    return embed
