import dislash, random
from discord.ext import commands


class _8Ball(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.responses = [
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

    @dislash.slash_command(
        name="8ball",
        description="Play 8Ball Game!!",
        options=[
            dislash.Option(
                name="question",
                description="The Question you want to ask!!",
                type=dislash.Type.STRING,
                required=True,
            )
        ],
    )
    @dislash.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def _8ball_(self, inter: dislash.SlashInteraction, question: str):
        await inter.respond(
            f"Question: {question}\nAnswer: {random.choice(self.responses)} :relieved:"
        )


def setup(bot: commands.Bot):
    bot.add_cog(_8Ball(bot))
