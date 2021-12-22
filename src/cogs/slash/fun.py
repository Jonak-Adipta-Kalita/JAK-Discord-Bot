import dislash
import src.embeds as embeds
import src.functions as funcs
import src.emojis as emojis_list
import src.files as files
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @dislash.slash_command(
        description="Display a Joke",
    )
    async def joke(self, inter):
        joke = funcs.get_joke()

        await inter.respond(joke)

    @dislash.slash_command(
        description="Display a Meme",
    )
    async def meme(self, inter):
        response = funcs.get_meme()
        await inter.respond(
            embed=embeds.meme_embed(label=response["caption"], image=response["image"])
        )

    @dislash.slash_command(
        description="Convert Text to Emoji",
        options=[
            dislash.Option(
                name="text",
                description="The Text to Emojify!!",
                type=dislash.Type.STRING,
                required=True,
            )
        ],
    )
    async def emojify(self, inter, text):
        await inter.respond(" ".join(funcs.emojify_text(text)))


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
