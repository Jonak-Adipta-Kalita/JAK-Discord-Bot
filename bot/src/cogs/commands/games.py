import disnake, random, asyncio, requests, akinator as aki_
import src.core.emojis as emojis
import src.core.embeds as embeds
import src.core.buttons as buttons
from src.core.bot import JAKDiscordBot
from disnake.ext import commands


class Games(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
        self.bot = bot

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

        self.hangman_game_over: bool = True
        self.hangman_player: disnake.Member = None
        self.hangman_guesses: list = []
        self.hangman_guesses_left: int = 0
        self.hangman_word: str = None

    def tictactoe_check_winner(self, winning_conditions, mark):
        for condition in winning_conditions:
            if (
                self.tictactoe_board[condition[0]] == mark
                and self.tictactoe_board[condition[1]] == mark
                and self.tictactoe_board[condition[2]] == mark
            ):
                self.tictactoe_game_over = True

    @commands.command(name="8ball", description="Play 8Ball Game")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def _8ball(self, ctx: commands.Context, *, question):
        await ctx.reply(
            f"Question: **{question}**\nAnswer: **{random.choice(self.bot._8ball_responses)}**"
        )

    @commands.group(invoke_without_command=True, description="Play Tic-Tac-Toe Game")
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def tictactoe(
        self, ctx: commands.Context, p1: disnake.Member, p2: disnake.Member
    ):
        global tictactoe_count

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
            tictactoe_count = 0
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
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def place(self, ctx: commands.Context, pos: int):
        global tictactoe_count

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
                        tictactoe_count += 1
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
                        elif tictactoe_count >= 9:
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
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def stop(self, ctx: commands.Context):
        if not self.tictactoe_game_over:
            if ctx.author in self.tictactoe_players:
                self.tictactoe_game_over = True
                await ctx.reply("Stopped the Game!!")
            else:
                await ctx.reply("You are not a Player of the Current Game!!")
        else:
            await ctx.reply("No game is currently running!!")

    @commands.group(invoke_without_command=True, description="Play Hangman Game")
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def hangman(self, ctx: commands.Context):
        if self.hangman_game_over:
            self.hangman_player = ctx.author
            self.hangman_guesses_left = 7
            self.hangman_game_over = False
            self.hangman_word = random.choice(self.bot.hangman_words).strip()
            self.hangman_guesses = []

            await ctx.reply(
                embed=embeds.hangman_embed(
                    guesses_left=7, word=self.hangman_word, guesses=self.hangman_guesses
                )
            )

            await asyncio.sleep(300)

            if not self.hangman_game_over:
                self.hangman_guesses = []
                self.hangman_game_over = True

                await ctx.reply("Time Out!!")
        else:
            await ctx.reply("One game is already running!!")

    @hangman.command(description="Guess Word in Hangman Game")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def guess(self, ctx: commands.Context, letter: str):
        if not self.hangman_game_over:
            if ctx.author == self.hangman_player:
                WORD_WAS = f"The word was `{self.hangman_word}`"

                content = letter.lower()
                self.hangman_guesses.append(content)

                if content == self.hangman_word:
                    self.hangman_game_over = True
                    self.hangman_guesses = []
                    await ctx.reply(f"That is the word! {WORD_WAS}")
                    return
                if all([w in self.hangman_guesses for w in list(self.hangman_word)]):
                    self.hangman_game_over = True
                    self.hangman_guesses = []
                    await ctx.reply(f"Well done! You got the word. {WORD_WAS}")
                    return
                if self.hangman_guesses_left == 1:
                    self.hangman_game_over = True
                    self.hangman_guesses = []
                    await ctx.reply(f"Unlucky, you ran out of guesses! {WORD_WAS}")
                    return
                if len(content) >= 2:
                    await ctx.reply(
                        f"`{content}` is not the word! Try sending letters one at a time"
                    )

                if content not in self.hangman_guesses[:-1]:
                    if content not in self.hangman_word:
                        self.hangman_guesses_left -= 1

                await ctx.reply(
                    embed=embeds.hangman_embed(
                        guesses_left=self.hangman_guesses_left,
                        word=self.hangman_word,
                        guesses=self.hangman_guesses,
                    )
                )
            else:
                await ctx.reply("You are not Playing!!")
        else:
            await ctx.reply("No game is currently running!!")

    @hangman.command(description="Stops Hangman Game")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def stop(self, ctx: commands.Context):
        if not self.hangman_game_over:
            if ctx.author == self.hangman_player:
                self.hangman_game_over = True
                self.hangman_guesses = []
                await ctx.reply("Stopped the Game!!")
            else:
                await ctx.reply("You are not Playing!!")
        else:
            await ctx.reply("No game is currently running!!")

    @commands.command(
        aliases=["rps", "rock_paper_scissor"], description="Play Rock Paper Scissor"
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def rock_paper_scissors(self, ctx: commands.Context, move: str):
        moves = ["rock", "paper", "scissor"]

        if move in moves:
            winner = None
            author = ctx.author
            comp_choice = random.choice(moves)

            if move == "rock":
                if comp_choice == "rock":
                    winner = None
                elif comp_choice == "paper":
                    winner = "CPU"
                elif comp_choice == "scissor":
                    winner = f"{author.display_name}#{author.discriminator}"
            elif move == "paper":
                if comp_choice == "paper":
                    winner = None
                elif comp_choice == "scissor":
                    winner = "CPU"
                elif comp_choice == "rock":
                    winner = f"{author.display_name}#{author.discriminator}"
            elif move == "scissor":
                if comp_choice == "scissor":
                    winner = None
                elif comp_choice == "rock":
                    winner = "CPU"
                elif comp_choice == "paper":
                    winner = f"{author.display_name}#{author.discriminator}"

            await ctx.reply(
                embed=embeds.rock_paper_scissor_embed(
                    player_move=move, comp_move=comp_choice, winner=winner
                )
            )
        else:
            await ctx.reply("The Move must be `rock` `paper` or `scissor`")

    @commands.command(description="Play Akinator Game", aliases=["aki"])
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def akinator(self, ctx: commands.Context):
        async with ctx.typing():
            aki = aki_.Akinator()
            question = aki.start_game()

        counter = 1
        embed = embeds.akinator_embed(question, counter)
        await ctx.reply(
            embed=embed,
            view=buttons.AkinatorButtons(
                author=ctx.author, aki=aki, embed=embed, counter=counter
            ),
        )


def setup(bot: JAKDiscordBot):
    bot.add_cog(Games(bot))
