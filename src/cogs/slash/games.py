import disnake, random
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
    async def _8ball_(
        self, inter: disnake.ApplicationCommandInteraction, question: str
    ):
        await inter.response.send_message(
            f"Question: {question}\nAnswer: {random.choice(self._8ball_responses)}"
        )


def setup(bot: commands.Bot):
    with open("resources/8ball_responses.txt") as txt:
        _8ball_responses = txt.readlines()

    bot.add_cog(Games_(bot, _8ball_responses))
