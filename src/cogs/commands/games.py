import disnake, random
import src.core.emojis as emojis
from disnake.ext import commands


class Games(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self._8ball_responses: list = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes definitely.",
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

        self.tictactoe_players: list = []
        self.tictactoe_player1: str = ""
        self.tictactoe_player2: str = ""
        self.tictactoe_turn: str = ""
        self.tictactoe_game_over: bool = True
        self.tictactoe_board: list = []
        self.tictactoe_winning_conditions: list = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

    @commands.command(name="8ball", description="Play 8Ball Game")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def _8ball(self, ctx: commands.Context, *, question):
        await ctx.reply(
            f"Question: {question}\nAnswer: {random.choice(self._8ball_responses)} :relieved:"
        )

    @commands.group(invoke_without_command=True, description="Start Tic-Tac-Toe Game")
    async def tictactoe(
        self, ctx: commands.Context, p1: disnake.Member, p2: disnake.Member
    ):
        global count

        if self.tictactoe_game_over:
            self.tictactoe_board = [
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
            self.tictactoe_turn = ""
            self.tictactoe_game_over = False
            count = 0
            self.tictactoe_player1 = p1
            self.tictactoe_player2 = p2
            self.tictactoe_players = [p1, p2]
            line = ""
            for x in range(len(self.tictactoe_board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + self.tictactoe_board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + self.tictactoe_board[x]
            num = random.randint(1, 2)
            if num == 1:
                self.tictactoe_turn = self.tictactoe_player1
                await ctx.send(f"Its {self.tictactoe_player1.mention}'s turn!!")
            elif num == 2:
                self.tictactoe_turn = self.tictactoe_player2
                await ctx.send(f"Its {self.tictactoe_player2.mention}'s turn!!")
        else:
            await ctx.reply("A game is already in progress!! Finish it or Stop it!!")

    @tictactoe.command(description="Place your position for Tic-Tac-Toe Game")
    async def place(self, ctx: commands.Context, pos: int):
        global count

        if not self.tictactoe_game_over:
            mark = ""
            if self.tictactoe_turn == ctx.author:
                if ctx.author in self.tictactoe_players:
                    if self.tictactoe_turn == self.tictactoe_player1:
                        mark = emojis.alphabets["regional_indicator_x"]
                    elif self.tictactoe_turn == self.tictactoe_player2:
                        mark = emojis.o2
                    if (
                        0 < pos < 10
                        and self.tictactoe_board[pos - 1] == emojis.white_large_square
                    ):
                        self.tictactoe_board[pos - 1] = mark
                        count += 1
                        line = ""
                        for x in range(len(self.tictactoe_board)):
                            if x == 2 or x == 5 or x == 8:
                                line += " " + self.tictactoe_board[x]
                                await ctx.send(line)
                                line = ""
                            else:
                                line += " " + self.tictactoe_board[x]
                        self.tictactoe_check_winner(
                            self.tictactoe_winning_conditions, mark
                        )
                        if self.tictactoe_game_over == True:
                            await ctx.send(f"{mark} WINS!!")
                        elif count >= 9:
                            self.tictactoe_game_over = True
                            await ctx.send("It's a TIE!!")

                        if not self.tictactoe_game_over:
                            if self.tictactoe_turn == self.tictactoe_player1:
                                self.tictactoe_turn = self.tictactoe_player2
                                await ctx.send(
                                    f"Its {self.tictactoe_player2.mention}'s turn!!"
                                )
                            elif self.tictactoe_turn == self.tictactoe_player2:
                                self.tictactoe_turn = self.tictactoe_player1
                                await ctx.send(
                                    f"Its {self.tictactoe_player1.mention}'s turn!!"
                                )
                    else:
                        await ctx.reply(
                            "Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile!!"
                        )
                else:
                    await ctx.reply("It is not your turn!!")
            else:
                await ctx.reply("You are not a Player of the Current Game!!")
        else:
            await ctx.reply("Please start a new game!!")

    @tictactoe.command(description="Stops Tic-Tac-Toe Game")
    async def stop(self, ctx: commands.Context):
        if not self.tictactoe_game_over:
            if ctx.author in self.tictactoe_players:
                self.tictactoe_game_over = True
                await ctx.reply("Stopped the Game!!")
            else:
                await ctx.reply("You are not a Player of the Current Game!!")
        else:
            await ctx.reply("No game is currently running!!")

    def tictactoe_check_winner(self, winning_conditions, mark):
        for condition in winning_conditions:
            if (
                self.tictactoe_board[condition[0]] == mark
                and self.tictactoe_board[condition[1]] == mark
                and self.tictactoe_board[condition[2]] == mark
            ):
                self.tictactoe_game_over = True


def setup(bot: commands.Bot):
    bot.add_cog(Games(bot))
