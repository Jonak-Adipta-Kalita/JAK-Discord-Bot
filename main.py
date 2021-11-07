from discord.ext import commands
import discord, random, credentials
import src.variables as variables

prefix = variables.PREFIX
embed_blank_value = variables.EMBED_BLANK_VALUE

### Tic-Tac-Toe Varialbles ###
player1 = variables.player1
player2 = variables.player2
turn = variables.turn
gameOver = variables.gameOver
board = variables.board
winningConditions = variables.winningConditions
##############################

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")

with open("src/bad_words.txt", "r") as f:
    global bad_words
    bad_words = f.read().splitlines()


@bot.event
async def on_ready():
    print("Bot Started!!")
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="!JAK help"
        ),
    )


@bot.event
async def on_message(message):
    msg = message.content.lower()
    member = message.author

    if member == bot.user:
        return

    for word in bad_words:
        if word in msg:
            embed = discord.Embed(
                title="YOU HAVE BEEN WARNED!!",
                description=f"The word `{word}` is banned!! Watch your Language",
                color=discord.Color.blue(),
            )

            await member.send(embed=embed)
            await message.delete()
            break
            return

    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    try:
        await member.send(f"Welcome to **{member.guild}**!!")
    except Exception:
        pass


@bot.event
async def on_member_remove(member):
    try:
        await member.send(f"You just left **{member.guild}**, What a Shame!!")
    except Exception:
        pass


@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        title="!JAK help",
        description="Shows all the Commands!!",
        color=discord.Color.blue(),
    )
    embed.add_field(name="!JAK help", value="Show Commands", inline=False)
    embed.add_field(name="!JAK ping", value="Show the Ping", inline=False)
    embed.add_field(name="!JAK 8ball <question>", value="Play 8ball Game", inline=False)
    embed.add_field(
        name="!JAK help_moderation", value="Show the Moderation Commands", inline=False
    )
    embed.add_field(
        name="!JAK help_tictactoe",
        value="Show the commands for Tic-Tac-Toe Game",
        inline=False,
    )
    embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def show_rules(ctx):
    embed = discord.Embed(
        title="!JAK show_rules",
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

    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def help_moderation(ctx):
    embed = discord.Embed(
        title="!JAK help_moderation",
        description="Shows all the Moderation Commands!!",
        color=discord.Color.blue(),
    )
    embed.add_field(
        name="!JAK clear <amount>",
        value="Delete messages as given amount",
        inline=False,
    )
    embed.add_field(
        name="!JAK kick @<member> reason=<reason>",
        value="Kick Member or Bot",
        inline=False,
    )
    embed.add_field(
        name="!JAK ban @<member> reason=<reason>",
        value="Ban Member or Bot",
        inline=False,
    )
    embed.add_field(
        name="!JAK unban <member, tag>", value="Unban Member or Bot", inline=False
    )
    embed.add_field(name="!JAK show_rules", value="Show the Rules", inline=False)
    embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def help_tictactoe(ctx):
    embed = discord.Embed(
        title="!JAK help_tictactoe",
        description="Shows all the Tic-Tac-Toe Game Commands!!",
        color=discord.Color.blue(),
    )
    embed.add_field(
        name="!JAK tictactoe @<1st Player> @<2nd Player>",
        value="Start Tic-Tac-Toe",
        inline=False,
    )
    embed.add_field(
        name="!JAK tictactoe_place <Position in Integer>",
        value="Place your position for Tic-Tac-Toe",
        inline=False,
    )
    embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

    await ctx.send(embed=embed)


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Nothing"):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} is Kicked!! Reason: {reason}")


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True, ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Nothing!!"):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} is Banned!! Reason: {reason}")


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True, ban_members=True)
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_user:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{member.mention} is Unbanned!!")
            return


@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f"Ping: {round(bot.latency * 1000)}")


@bot.command(pass_context=True, aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtfut.",
        "Kinda Lazy to answer.",
    ]

    await ctx.send(
        f"Question: {question}\nAnswer: {random.choice(responses)} :relieved:"
    )


@bot.command(pass_context=True)
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
        ]
        turn = ""
        gameOver = False
        count = 0
        player1 = p1
        player2 = p2
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("Its <@" + str(player1.id) + ">'s turn!!")
        elif num == 2:
            turn = player2
            await ctx.send("Its <@" + str(player2.id) + ">'s turn!!")
    else:
        await ctx.send(
            "A game is already in progress!! Finish it before starting a new one!!"
        )


@bot.command(pass_context=True)
async def tictactoe_place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver
    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]
                tictactoe_checkWinner(winningConditions, mark)
                if gameOver == True:
                    await ctx.send(mark + " WINS!!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a TIE!!")
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send(
                    "Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile!!"
                )
        else:
            await ctx.send("It is not your turn!!")
    else:
        await ctx.send(
            "Please start a new game using the `!JAK tictactoe @<1st Member> @<2nd Member>` command!!"
        )


def tictactoe_checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if (
            board[condition[0]] == mark
            and board[condition[1]] == mark
            and board[condition[2]] == mark
        ):
            gameOver = True


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "You don't have the Appropriate Permissions to run this command!!"
        )
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide the required Arguments!!")


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "You don't have the Appropriate Permissions to run this command!!"
        )
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide the required Arguments!!")


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "You don't have the Appropriate Permissions to run this command!!"
        )
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide the required Arguments!!")


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "You don't have the Appropriate Permissions to run this command!!"
        )
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide the required Arguments!!")


@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide your Question!!")


@tictactoe.error
async def tictactoe_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command!!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players!!")


@tictactoe_place.error
async def tictactoe_place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark!!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer!!")


bot.run(credentials.TOKEN)
