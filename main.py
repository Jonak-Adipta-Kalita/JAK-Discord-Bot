from discord.ext import commands
import discord, random, credentials
import src.tictactoe_variables as tictactoe_variables

### Tic-Tac-Toe Varialbles ###
player1 = tictactoe_variables.player1
player2 = tictactoe_variables.player2
turn = tictactoe_variables.turn
gameOver = tictactoe_variables.gameOver
board = tictactoe_variables.board
winningConditions = tictactoe_variables.winningConditions
##############################

prefix = "!JAK "
intents = discord.Intents()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")


@client.event
async def on_ready():
    print("Bot Started!!")
    await client.change_presence(
        status=discord.Status.online, activity=discord.Game("!JAK help")
    )


@client.command()
async def help(ctx):
    await ctx.send(
        r"""1. `!JAK `: Default Prefix
2. `!JAK help`: Show Commands
3. `!JAK ping`: Show the PING
4. `!JAK help_moderation`: Show the Moderation Commands
5. `!JAK help_8ball`: Show the commands for 8Ball Game
6. `!JAK help_tictactoe`: Show the commands for Tic-Tac-Toe Game"""
    )


@client.command()
async def help_moderation(ctx):
    await ctx.send(
        r"""1. `!JAK clear <amount>`: Delete messages as given amount
2. `!JAK kick @<member> reason=<reason>`: Kick Member/Bot
3. `!JAK ban @<member> reason=<reason>`: Ban Member/Bot
4. `!JAK unban <member, tag>`: Unban Member/Bot
5. `!JAK show_rules`: Show the Rules """
    )


@client.command()
async def help_8ball(ctx):
    await ctx.send(r"""4. `!JAK 8ball <question>`: Play 8ball Game """)


@client.command()
async def help_tictactoe(ctx):
    await ctx.send(
        r""" 1. `!JAK tictactoe @<1st Player> @<2nd Player>`: Start Tic-Tac-Toe
2. `!JAK tictactoe_place <Position in Integer>`: Place your position for Tic-Tac-Toe """
    )


@client.command()
async def show_rules(ctx):
    await ctx.send(
        r"""1. Be Cool!!
2. Be Awesome!!
3. Support Each Other!!
4. Don't Betray Anybody!!
5. Always Support YOUTUBE not TIKTOK!!
6. Dont Ask For Roles!! """
    )


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} is Banned!!")


@client.command()
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_user:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{member.mention} is Unbanned!!")
            return


@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@client.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)}")


@client.event
async def on_member_join(member):
    await member.send(f"Welcome to {member.server}!!")


@client.event
async def on_member_remove(member):
    await member.send(f"You just left {member.server}, What a Shame!!")


@client.command(aliases=["8ball"])
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
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}\n:)")


@client.command()
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


@client.command()
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


client.run(credentials.TOKEN)
