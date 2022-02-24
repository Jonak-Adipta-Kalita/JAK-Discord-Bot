import disnake, random
import src.core.embeds as embeds
from disnake.ext import commands


class Games_(commands.Cog):
    def __init__(self, bot: commands.Bot, _8ball_responses: list):
        self.bot = bot
        self._8ball_responses = _8ball_responses

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
            f"Question: **{question}**\nAnswer: **{random.choice(self._8ball_responses)}**"
        )

    @commands.slash_command(
        description="Play Rock Paper Scissor",
        options=[
            disnake.Option(
                name="move",
                description="The Move!!",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    async def rock_paper_scissor(
        self, inter: disnake.ApplicationCommandInteraction, move: str
    ):
        moves = ["rock", "paper", "scissor"]

        if move in moves:
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
        else:
            await inter.response.send_message(
                "The Move must be `rock` `paper` or `scissor`"
            )


def setup(bot: commands.Bot):
    with open("../resources/8ballResponses.txt") as txt:
        _8ball_responses = txt.readlines()

    bot.add_cog(Games_(bot, _8ball_responses))
