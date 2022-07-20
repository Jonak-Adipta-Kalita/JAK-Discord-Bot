import disnake, typing
import src.core.functions as funcs
import src.core.emojis as emojis
from disnake.ext import commands


def ping_bot_embed(
    bot: commands.Bot, servers: int, prefixes: typing.List[str]
) -> disnake.Embed:
    embed = disnake.Embed(
        title=f"Hello Buddy!!",
        description=f"My Prefix is `{prefixes[0]}`\nUse `{prefixes[0]}help` to see the Help Embed!!\n\nTotal Servers = {servers}",
        color=0x3498DB,
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar.url)

    return embed


async def help_embed(
    bot: commands.Bot,
    prefixes: typing.List[str],
    author: disnake.Member,
    command_type: str = None,
) -> disnake.Embed:
    bot_commands = await funcs.get_commands()

    embed = disnake.Embed(color=0x3498DB)
    embed.set_author(
        name=f"{bot.user.name} - {command_type.title() if command_type else ''} Help Menu",
        icon_url=bot.user.avatar.url,
    )
    if command_type:
        for commands in bot_commands[command_type]:
            embed.add_field(
                name=commands["usage"],
                value=commands["description"],
                inline=False,
            )
    else:
        embed.add_field(
            name=f"{prefixes[0]}help moderation",
            value="Show the Moderation Commands",
            inline=False,
        )
        embed.add_field(
            name=f"{prefixes[0]}help games",
            value="Show the Game Commands",
            inline=False,
        )
        embed.add_field(
            name=f"{prefixes[0]}help music",
            value="Show the Music Commands",
            inline=False,
        )
        embed.add_field(
            name=f"{prefixes[0]}help fun",
            value="Show the Fun Commands",
            inline=False,
        )
        embed.add_field(
            name=f"{prefixes[0]}help misc",
            value="Show the Misc Commands",
            inline=False,
        )
    embed.set_footer(
        text=f"Information Requested by: {author.display_name}",
        icon_url=author.avatar.url,
    )

    return embed


def commands_help_embed(
    bot: commands.Bot,
    prefixes: typing.List[str],
    author: disnake.Member,
    command: commands.Command,
    sub_command: commands.Command = None,
) -> disnake.Embed:
    embed = disnake.Embed(color=0x3498DB)
    embed.set_author(
        name=f"{bot.user.name} - {command.name.replace('_', ' ').title()} {sub_command.name.replace('_', ' ').title() if sub_command else ''} Help Menu",
        icon_url=bot.user.avatar.url,
    )
    embed.add_field(
        name="Name:",
        value=f"`{command.name.replace('_', ' ').title()} {sub_command.name.replace('_', ' ').title() if sub_command else ''}`",
        inline=False,
    )
    embed.add_field(
        name="Alias:",
        value=(
            f"{', '.join([f'`{k}`' for k in sub_command.aliases if sub_command.aliases])} "
            if sub_command.aliases
            else f"`none`"
        )
        if sub_command
        else (
            f"{', '.join([f'`{k}`' for k in command.aliases if command.aliases])} "
            if command.aliases
            else f"`none`"
        ),
        inline=False,
    )
    embed.add_field(
        name="Usage:",
        value=(f"`{prefixes[0]}{command.name} {sub_command.name}`")
        if sub_command
        else (
            f"`{prefixes[0]}{command.name} {command.signature}`"
            if command.signature
            else f"`{prefixes[0]}{command.name}`"
        ),
        inline=False,
    )
    embed.add_field(
        name="Description:",
        value=sub_command.description if sub_command else command.description,
        inline=False,
    )
    embed.set_footer(
        text=f"Information Requested by: {author.display_name}",
        icon_url=author.avatar.url,
    )

    return embed


def error_embed(content: str) -> disnake.Embed:
    embed = disnake.Embed(title="Error Occured", description=content, color=0x3498DB)

    return embed


def rules_embed(bot: commands.Bot, rules: typing.List[dict]) -> disnake.Embed:
    embed = disnake.Embed(color=0x3498DB)
    embed.set_author(name=f"{bot.user.name} - Rules", icon_url=bot.user.avatar.url)
    embed.set_footer(text="Please Follow all the RULES!!")
    for rule in rules:
        embed.add_field(
            name=rule["name"],
            value=rule["description"],
            inline=False,
        )

    return embed


def moderation_embed(title: str, status: str, message: str) -> disnake.Embed:
    embed = disnake.Embed(
        title=f"{title} HAVE BEEN {status}!!",
        description=message,
        color=0x3498DB,
    )

    return embed


def music_playing_embed(info: dict) -> disnake.Embed:
    embed = disnake.Embed(
        title=info["title"],
        description=f"Channel: {info['channel']}",
        color=0x3498DB,
    )
    embed.set_image(url=info["thumbnail"])

    return embed


def music_lyrics_embed(lyrics: str) -> disnake.Embed:
    embed = disnake.Embed(description=lyrics, color=0x3498DB)

    return embed


def translation_embed(
    text: str,
    translated_text: str,
    language_name: str,
    language_iso: str,
    author: disnake.Member,
    author_reacted: disnake.Member = None,
) -> disnake.Embed:
    embed = disnake.Embed(color=0x3498DB)
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
) -> disnake.Embed:
    embed = disnake.Embed(color=0x3498DB)
    embed.set_author(name=f"Author: {author.display_name}")
    embed.add_field(name="Text", value=text, inline=True)
    embed.add_field(name=f"Pronunciation", value=pronunciation, inline=True)
    embed.set_footer(
        text=f"Request: {author_reacted.display_name}",
    )

    return embed


def meme_embed(label: str, image: str) -> disnake.Embed:
    embed = disnake.Embed(title=f"Caption: **{label}**", color=0x3498DB)
    embed.set_image(url=image)

    return embed


def member_details_embed(
    member: disnake.Member, fetched_member: disnake.User
) -> disnake.Embed:
    roles_list = [role.mention for role in member.roles if role.name != "@everyone"]

    embed = disnake.Embed(color=0x3498DB)
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


def server_stats_embed(guild: disnake.Guild) -> disnake.Embed:
    emojis_list = [f"<:{emoji.name}:{emoji.id}>" for emoji in guild.emojis]
    roles_list = [role.mention for role in guild.roles if role.name != "@everyone"]

    embed = disnake.Embed(
        title=f"{guild.name}'s Stats",
        description=guild.description if guild.description else "",
        color=0x3498DB,
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


def morse_code_embed(title: str, converted: str) -> disnake.Embed:
    embed = disnake.Embed(
        title=title, description=f"```yaml\n{converted}```", color=0x3498DB
    )

    return embed


def calculator_embed() -> disnake.Embed:
    embed = disnake.Embed(
        title="Calculator", description="```yaml\n0```", color=0x3498DB
    )
    embed.set_footer(
        text="To interact with your virtual calculator, click the shown buttons."
    )

    return embed


def poll_embed(
    question: str, option1: str, option2: str, option3: str
) -> disnake.Embed:
    desc = f"{emojis.alphabets['regional_indicator_a']} {option1}\n\n{emojis.alphabets['regional_indicator_b']} {option2}"
    if option3:
        desc += f"\n\n{emojis.alphabets['regional_indicator_c']} {option3}"

    embed = disnake.Embed(title=question, description=desc, color=0x3498DB)

    return embed


def hangman_embed(guesses_left: int, word: str, guesses: list) -> disnake.Embed:
    desc = " ".join([i if i in guesses else "__" for i in word])

    embed = disnake.Embed(
        description=f"`{desc}`\n\n**{guesses_left} guesses left!!**",
        color=0x3498DB,
    )

    return embed


def rock_paper_scissor_embed(
    player_move: str, comp_move: str, winner: str
) -> disnake.Embed:
    embed = disnake.Embed(color=0x3498DB)
    embed.add_field(name="Player's Move", value=player_move, inline=False)
    embed.add_field(name="CPU's Move", value=comp_move, inline=False)
    embed.add_field(name="Winner", value=winner if winner else "Draw", inline=False)

    return embed


def message_source_embed(msg: disnake.Message) -> disnake.Embed:
    embed = disnake.Embed(
        description=disnake.utils.escape_markdown(msg.content).replace(" ", "\u200B "),
        color=0x3498DB,
    )

    return embed


def pokemon_embed(pokemon: dict) -> disnake.Embed:
    name: str = pokemon["name"]
    description: str = pokemon["description"]
    sprite: str = pokemon["sprites"]["animated"]
    types: str = ", ".join(pokemon["type"])
    species: str = ", ".join(pokemon["species"])
    abilities: str = ", ".join(pokemon["abilities"])

    embed = disnake.Embed(
        title=name.replace("-", " ").title(),
        description=description,
        color=0x3498DB,
    )
    embed.add_field(name="Types:", value=types, inline=False)
    embed.add_field(name="Species:", value=species, inline=False)
    embed.add_field(name="Abilities:", value=abilities, inline=False)
    embed.set_thumbnail(url=sprite)

    return embed


def pokemon_card_embed(card: dict) -> disnake.Embed:
    embed = disnake.Embed(color=0x3498DB)
    embed.set_image(url=card["imageUrlHiRes"])

    return embed


def servers_in_embed(servers: typing.List[disnake.Guild]) -> disnake.Embed:
    servers_name = []
    number = 0
    for server in servers:
        number += 1
        servers_name.append(f"{number})  **{server.name}**")

    embed = disnake.Embed(
        title="Servers:",
        description="\n".join(servers_name),
        color=0x3498DB,
    )

    return embed


def place_details_embed(place: dict) -> disnake.Embed:
    name: str = place["name"]
    coordinates: dict = place["coord"]
    humidity: str = f"{place['main']['humidity']}%"
    temperature = int(place["main"]["temp"] - 273.15)
    weather_description: str = place["weather"][0]["description"]

    try:
        country = funcs.get_country(place["sys"]["country"])
    except KeyError:
        country = None

    embed = disnake.Embed(title=f"{name}'s Detail", color=0x3498DB)
    embed.add_field(
        name="Country",
        value=country["country"] if country else place["sys"]["country"],
        inline=False,
    )
    embed.add_field(name="Weather", value=weather_description.title(), inline=False)
    embed.add_field(name="Temperature", value=temperature, inline=False)
    embed.add_field(name="Humidity", value=humidity, inline=False)
    embed.add_field(
        name="Coordinates",
        value=f"Longitude: {coordinates['lon']}, Latitude: {coordinates['lat']}",
        inline=False,
    )

    return embed


def brawler_embed(brawler: dict) -> disnake.Embed:
    embed = disnake.Embed(title=f"{brawler['name']}'s Details", color=0x3498DB)
    embed.add_field(name="Category", value=brawler["category"], inline=False)
    embed.add_field(
        name="Gadgets",
        value=", ".join(brawler["gadget"])
        if brawler["gadget"][1]
        else brawler["gadget"][0],
        inline=False,
    )
    embed.add_field(
        name="Star Powers",
        value=", ".join(brawler["starpower"])
        if brawler["starpower"][1]
        else brawler["starpower"][0],
        inline=False,
    )
    embed.add_field(name="Total Pins", value=len(brawler["pins"]))
    if brawler["sprays"]:
        embed.add_field(name="Total Sprays", value=len(brawler["sprays"]))
    embed.set_thumbnail(url=f"https://jak-api.vercel.app{brawler['image']}")

    return embed


def akinator_embed(
    question: str = None, counter: int = None, guess=None
) -> disnake.Embed:
    if guess and not (question and counter):
        embed = disnake.Embed(title=f"My Guess", color=0x3498DB)
        embed.add_field("Name", guess["name"], inline=False)
        embed.add_field("Description", guess["description"], inline=False)
        embed.set_thumbnail(guess["absolute_picture_path"])
    else:
        embed = disnake.Embed(
            title=f"Question no. {counter}: {question}", color=0x3498DB
        )

    return embed
