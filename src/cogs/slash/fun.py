import disnake
import src.embeds as embeds
import src.functions as funcs
from disnake.ext import commands


class Fun_(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        description="Display a Joke",
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def joke(self, inter: disnake.ApplicationCommandInteraction):
        joke = funcs.get_joke()

        await inter.response.send_message(joke)

    @commands.slash_command(
        description="Display a Meme",
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def meme(self, inter: disnake.ApplicationCommandInteraction):
        response = await funcs.get_meme()
        await inter.response.send_message(
            embed=embeds.meme_embed(label=response["caption"], image=response["image"])
        )

    @commands.slash_command(
        description="Convert Text to Emoji",
        options=[
            disnake.Option(
                name="text",
                description="The Text to Emojify!!",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def emojify(self, inter: disnake.ApplicationCommandInteraction, text: str):
        await inter.response.send_message(" ".join(funcs.emojify_text(text)))


def setup(bot: commands.Bot):
    bot.add_cog(Fun_(bot))
