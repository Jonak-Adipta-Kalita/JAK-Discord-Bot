import discord, random
from discord.ext import commands
from src.functions import get_prefix

prefix = get_prefix()

class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.player1 = ""
        self.player2 = ""
        self.turn = ""
        self.count = 0
        self.game_over = True
        self.board = []
        self.winning_conditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

    @commands.command()
    async def help_tictactoe(self, ctx: commands.Context):
        embed = discord.Embed(
            title=f"{prefix} help_tictactoe",
            description="Shows all the Tic-Tac-Toe Game Commands!!",
            color=discord.Color.blue(),
        )
        embed.add_field(
            name=f"{prefix} tictactoe @<1st Player> @<2nd Player>",
            value="Start Tic-Tac-Toe",
            inline=False,
        )
        embed.add_field(
            name=f"{prefix} tictactoe_place <Position in Integer>",
            value="Place your position for Tic-Tac-Toe",
            inline=False,
        )
        embed.add_field(
            name=f"{prefix} tictactoe_stop",
            value="Stops Tic-Tac-Toe",
            inline=False,
        )
        embed.set_footer(text=f"Information Requested by: {ctx.author.display_name}")

        await ctx.send(embed=embed)

    @commands.command()
    async def tictactoe(
        self, ctx: commands.Context, p1: discord.Member, p2: discord.Member
    ):
        member = ctx.message.author

        if self.game_over:
            self.board = [
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
            self.turn = ""
            self.game_over = False
            count = 0
            self.player1 = p1
            self.player2 = p2
            line = ""
            for x in range(len(self.board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + self.board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + self.board[x]
            num = random.randint(1, 2)
            if num == 1:
                self.turn = self.player1
                await ctx.send("Its <@" + str(self.player1.id) + ">'s turn!!")
            elif num == 2:
                self.turn = self.player2
                await ctx.send("Its <@" + str(self.player2.id) + ">'s turn!!")
        else:
            await ctx.send(
                f"{member.mention} A game is already in progress!! Finish it before starting a new one!!"
            )

    @commands.command()
    async def tictactoe_place(self, ctx: commands.Context, pos: int):
        member = ctx.message.author

        if not self.game_over:
            mark = ""
            if self.turn == ctx.author:
                if self.turn == self.player1:
                    mark = ":regional_indicator_x:"
                elif self.turn == self.player2:
                    mark = ":o2:"
                if 0 < pos < 10 and self.board[pos - 1] == ":white_large_square:":
                    self.board[pos - 1] = mark
                    self.count += 1
                    line = ""
                    for x in range(len(self.board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + self.board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + self.board[x]
                    self.tictactoe_check_winner(self.winning_conditions, mark)
                    if self.game_over == True:
                        await ctx.send(mark + " WINS!!")
                    elif self.count >= 9:
                        self.game_over = True
                        await ctx.send("It's a TIE!!")
                    if self.turn == self.player1:
                        self.turn = self.player2
                    elif self.turn == self.player2:
                        self.turn = self.player1
                else:
                    await ctx.send(
                        f"{member.mention} Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile!!"
                    )
            else:
                await ctx.send(f"{member.mention} It is not your turn!!")
        else:
            await ctx.send(
                f"{member.mention} Please start a new game using the `{prefix} tictactoe @<1st Member> @<2nd Member>` command!!"
            )

    @commands.command()
    async def tictactoe_stop(self, ctx: commands.Context):
        member = ctx.message.author
        if not self.game_over:
            self.game_over = True
            await ctx.send(f"{member.mention} Stopped Game!!")
        else:
            await ctx.send(f"{member.mention} No game is currently running!!")

    def tictactoe_check_winner(self, winning_conditions, mark):
        for condition in winning_conditions:
            if (
                self.board[condition[0]] == mark
                and self.board[condition[1]] == mark
                and self.board[condition[2]] == mark
            ):
                self.game_over = True


def setup(bot):
    bot.add_cog(TicTacToe(bot))
