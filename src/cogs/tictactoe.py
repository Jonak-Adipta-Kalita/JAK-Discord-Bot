import discord, random
import src.embeds as embeds
import src.functions as funcs
import src.emojis as emojis
from discord.ext import commands

prefix = funcs.get_prefix()


class TicTacToe(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.player1 = ""
        self.player2 = ""
        self.turn = ""
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
    async def tictactoe(
        self, ctx: commands.Context, p1: discord.Member, p2: discord.Member
    ):
        global count

        if self.game_over:
            self.board = [
                emojis.white_large_square,
                emojis.white_large_square,
                emojis.white_large_square,
                emojis.white_large_square,
                emojis.white_large_square,
                emojis.white_large_square,
                emojis.white_large_square,
                emojis.white_large_square,
                emojis.white_large_square,
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
                await ctx.send(f"Its {self.player1.mention}'s turn!!")
            elif num == 2:
                self.turn = self.player2
                await ctx.send(f"Its {self.player2.mention}'s turn!!")
        else:
            await ctx.reply("A game is already in progress!! Finish it or Stop it!!")

    @commands.command()
    async def tictactoe_place(self, ctx: commands.Context, pos: int):
        global count

        if not self.game_over:
            mark = ""
            if self.turn == ctx.author:
                if self.turn == self.player1:
                    mark = emojis.alphabets["regional_indicator_x"]
                elif self.turn == self.player2:
                    mark = emojis.o2
                if 0 < pos < 10 and self.board[pos - 1] == emojis.white_large_square:
                    self.board[pos - 1] = mark
                    count += 1
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
                    elif count >= 9:
                        self.game_over = True
                        await ctx.send("It's a TIE!!")

                    if self.turn == self.player1:
                        self.turn = self.player2
                        await ctx.send(f"Its {self.player2.mention}'s turn!!")
                    elif self.turn == self.player2:
                        self.turn = self.player1
                        await ctx.send(f"Its {self.player1.mention}'s turn!!")
                else:
                    await ctx.reply(
                        "Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile!!"
                    )
            else:
                await ctx.reply("It is not your turn!!")
        else:
            await ctx.reply("Please start a new game!!")

    @commands.command()
    async def tictactoe_stop(self, ctx: commands.Context):
        if not self.game_over:
            self.game_over = True
            await ctx.reply("Stopped the Game!!")
        else:
            await ctx.reply("No game is currently running!!")

    def tictactoe_check_winner(self, winning_conditions, mark):
        for condition in winning_conditions:
            if (
                self.board[condition[0]] == mark
                and self.board[condition[1]] == mark
                and self.board[condition[2]] == mark
            ):
                self.game_over = True


def setup(bot: commands.Bot):
    bot.add_cog(TicTacToe(bot))
