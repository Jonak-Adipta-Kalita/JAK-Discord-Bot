import disnake, random, requests, asyncio, akinator as aki_
import src.core.embeds as embeds
import src.core.buttons as buttons
import src.core.emojis as emojis
from src.core.bot import JAKDiscordBot
from disnake.ext import commands


class Games_(commands.Cog):
    def __init__(self, bot: JAKDiscordBot, _8ball_responses: list):
        self.bot = bot
        self.bot._8ball_responses = _8ball_responses

    @commands.slash_command(
        name="8ball",
        description="Play 8Ball Game!!",
        options=[
            disnake.Option(
                name="question",
                description="The Question you want to ask!!",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def _8ball(self, inter: disnake.ApplicationCommandInteraction, question: str):
        await inter.response.send_message(
            f"Question: **{question}**\nAnswer: **{random.choice(self.bot._8ball_responses)}**"
        )

    @commands.slash_command(
        description="Play Rock Paper Scissor",
        options=[
            disnake.Option(
                name="move",
                description="The Move!!",
                type=disnake.OptionType.string,
                required=True,
                choices=["rock", "paper", "scissor"],
            )
        ],
    )
    async def rock_paper_scissors(
        self, inter: disnake.ApplicationCommandInteraction, move: str
    ):
        moves = ["rock", "paper", "scissor"]

        winner = None
        author = inter.author
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

        await inter.response.send_message(
            embed=embeds.rock_paper_scissor_embed(
                player_move=move, comp_move=comp_choice, winner=winner
            )
        )

    @commands.slash_command(description="Play Akinator Game")
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def akinator(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        aki = aki_.Akinator()
        question = aki.start_game()
        counter = 1

        embed = embeds.akinator_embed(question, counter)
        await inter.edit_original_message(
            embed=embed,
            view=buttons.AkinatorButtons(
                author=inter.author, aki=aki, embed=embed, counter=counter
            ),
        )

    @commands.slash_command(description="Use Hangman Game Commands")
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def hangman(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @hangman.sub_command(description="Play Hangman Game")
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def start(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        if self.bot.hangman_game_over:
            self.bot.hangman_player = inter.author
            self.bot.hangman_guesses_left = 7
            self.bot.hangman_game_over = False
            self.bot.hangman_word = random.choice(self.bot.hangman_words).strip()
            self.bot.hangman_guesses = []

            await inter.edit_original_message(
                embed=embeds.hangman_embed(
                    guesses_left=7,
                    word=self.bot.hangman_word,
                    guesses=self.bot.hangman_guesses,
                )
            )

            await asyncio.sleep(300)

            if not self.bot.hangman_game_over:
                self.bot.hangman_guesses = []
                self.bot.hangman_game_over = True

                await inter.edit_original_message("Time Out!!")
        else:
            await inter.edit_original_message("One game is already running!!")

    @hangman.sub_command(description="Guess Word in Hangman Game")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def guess(self, inter: disnake.ApplicationCommandInteraction, letter: str):
        await inter.response.defer()

        if not self.bot.hangman_game_over:
            if inter.author == self.bot.hangman_player:
                WORD_WAS = f"The word was `{self.bot.hangman_word}`"

                content = letter.lower()
                self.bot.hangman_guesses.append(content)

                if content == self.bot.hangman_word:
                    self.bot.hangman_game_over = True
                    self.bot.hangman_guesses = []
                    await inter.edit_original_message(f"That is the word! {WORD_WAS}")
                    return
                if all(
                    [w in self.bot.hangman_guesses for w in list(self.bot.hangman_word)]
                ):
                    self.bot.hangman_game_over = True
                    self.bot.hangman_guesses = []
                    await inter.edit_original_message(
                        f"Well done! You got the word. {WORD_WAS}"
                    )
                    return
                if self.bot.hangman_guesses_left == 1:
                    self.bot.hangman_game_over = True
                    self.bot.hangman_guesses = []
                    await inter.edit_original_message(
                        f"Unlucky, you ran out of guesses! {WORD_WAS}"
                    )
                    return
                if len(content) >= 2:
                    await inter.edit_original_message(
                        f"`{content}` is not the word! Try sending letters one at a time"
                    )

                if content not in self.bot.hangman_guesses[:-1]:
                    if content not in self.bot.hangman_word:
                        self.bot.hangman_guesses_left -= 1

                await inter.edit_original_message(
                    embed=embeds.hangman_embed(
                        guesses_left=self.bot.hangman_guesses_left,
                        word=self.bot.hangman_word,
                        guesses=self.bot.hangman_guesses,
                    )
                )
            else:
                await inter.edit_original_message("You are not Playing!!")
        else:
            await inter.edit_original_message("No game is currently running!!")

    @hangman.sub_command(description="Stops Hangman Game")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def stop(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        if not self.bot.hangman_game_over:
            if inter.author == self.bot.hangman_player:
                self.bot.hangman_game_over = True
                self.bot.hangman_guesses = []
                await inter.edit_original_message("Stopped the Game!!")
            else:
                await inter.edit_original_message("You are not Playing!!")
        else:
            await inter.edit_original_message("No game is currently running!!")

    @commands.slash_command(description="Use Tic-Tac-Toe Game Commands")
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def tictactoe(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @tictactoe.sub_command(
        description="Play Tic-Tac-Toe Game",
        options=[
            disnake.Option(
                name="p1",
                description="Player 1",
                type=disnake.OptionType.user,
                required=True,
            ),
            disnake.Option(
                name="p2",
                description="Player 2",
                type=disnake.OptionType.user,
                required=True,
            ),
        ],
    )
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def start(
        self,
        inter: disnake.ApplicationCommandInteraction,
        p1: disnake.Member,
        p2: disnake.Member,
    ):
        await inter.response.defer()

        if self.bot.tictactoe_game_over:
            self.bot.tictactoe_board = [
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
            self.bot.tictactoe_turn = ""
            self.bot.tictactoe_game_over = False
            self.bot.tictactoe_count = 0
            self.bot.tictactoe_player1 = p1
            self.bot.tictactoe_player2 = p2
            self.bot.tictactoe_players = [p1, p2]
            line = ""
            for x in range(len(self.bot.tictactoe_board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + self.bot.tictactoe_board[x]
                    await inter.edit_original_message(line)
                    line = ""
                else:
                    line += " " + self.bot.tictactoe_board[x]
            num = random.randint(1, 2)
            if num == 1:
                self.bot.tictactoe_turn = self.bot.tictactoe_player1
                await inter.edit_original_message(
                    f"Its {self.bot.tictactoe_player1.mention}'s turn!!"
                )
            elif num == 2:
                self.bot.tictactoe_turn = self.bot.tictactoe_player2
                await inter.edit_original_message(
                    f"Its {self.bot.tictactoe_player2.mention}'s turn!!"
                )
        else:
            await inter.edit_original_message(
                "A game is already in progress!! Finish it or Stop it!!"
            )

    @tictactoe.sub_command(
        description="Place your position for Tic-Tac-Toe Game",
        options=[
            disnake.Option(
                name="pos",
                description="Position for your next move",
                type=disnake.OptionType.integer,
                required=True,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def place(self, inter: disnake.ApplicationCommandInteraction, pos: int):
        await inter.response.defer()

        if not self.bot.tictactoe_game_over:
            mark = ""
            if self.bot.tictactoe_turn == inter.author:
                if inter.author in self.bot.tictactoe_players:
                    if self.bot.tictactoe_turn == self.bot.tictactoe_player1:
                        mark = emojis.alphabets["regional_indicator_x"]
                    elif self.bot.tictactoe_turn == self.bot.tictactoe_player2:
                        mark = emojis.o2
                    if (
                        0 < pos < 10
                        and self.bot.tictactoe_board[pos - 1]
                        == emojis.white_large_square
                    ):
                        self.bot.tictactoe_board[pos - 1] = mark
                        self.bot.tictactoe_count += 1
                        line = ""
                        for x in range(len(self.bot.tictactoe_board)):
                            if x == 2 or x == 5 or x == 8:
                                line += " " + self.bot.tictactoe_board[x]
                                await inter.edit_original_message(line)
                                line = ""
                            else:
                                line += " " + self.bot.tictactoe_board[x]
                        self.bot.tictactoe_check_winner(
                            self.bot.tictactoe_winning_conditions, mark
                        )
                        if self.bot.tictactoe_game_over == True:
                            await inter.edit_original_message(f"{mark} WINS!!")
                        elif self.bot.tictactoe_count >= 9:
                            self.bot.tictactoe_game_over = True
                            await inter.edit_original_message("It's a TIE!!")

                        if not self.bot.tictactoe_game_over:
                            if self.bot.tictactoe_turn == self.bot.tictactoe_player1:
                                self.bot.tictactoe_turn = self.bot.tictactoe_player2
                                await inter.edit_original_message(
                                    f"Its {self.bot.tictactoe_player2.mention}'s turn!!"
                                )
                            elif self.bot.tictactoe_turn == self.bot.tictactoe_player2:
                                self.bot.tictactoe_turn = self.bot.tictactoe_player1
                                await inter.edit_original_message(
                                    f"Its {self.bot.tictactoe_player1.mention}'s turn!!"
                                )
                    else:
                        await inter.edit_original_message(
                            "Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile!!"
                        )
                else:
                    await inter.edit_original_message("It is not your turn!!")
            else:
                await inter.edit_original_message(
                    "You are not a Player of the Current Game!!"
                )
        else:
            await inter.edit_original_message("Please start a new game!!")

    @tictactoe.sub_command(description="Stops Tic-Tac-Toe Game")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def stop(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        if not self.bot.tictactoe_game_over:
            if inter.author in self.bot.tictactoe_players:
                self.bot.tictactoe_game_over = True
                await inter.edit_original_message("Stopped the Game!!")
            else:
                await inter.edit_original_message(
                    "You are not a Player of the Current Game!!"
                )
        else:
            await inter.edit_original_message("No game is currently running!!")


def setup(bot: JAKDiscordBot):
    _8ball_responses = requests.get(
        "https://raw.githubusercontent.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/main/resources/8ballResponses.txt"
    ).text.splitlines()

    bot.add_cog(Games_(bot, _8ball_responses))
