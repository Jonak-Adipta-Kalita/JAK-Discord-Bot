import disnake
import src.core.embeds as embeds
import src.core.functions as funcs
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

    @commands.slash_command(
        description="Encode or Decode PlainText/MorseCode into MorseCode/PlainText",
        options=[
            disnake.Option(
                name="text",
                description="The Text to Encode/Decode!!",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def morse(self, inter: disnake.ApplicationCommandInteraction, text: str):
        try:
            title, converted = funcs.morse_code_encode_decode(text=text)
            await inter.response.send_message(
                embed=embeds.morse_code_embed(title=title, converted=converted)
            )
        except KeyError:
            await inter.response.send_message(
                "The String contains some characters which cannot be converted into Morse!!"
            )

    @commands.slash_command(description="Display a Fact")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def fact(self, inter: disnake.ApplicationCommandInteraction):
        fact = funcs.fact()

        await inter.response.send_message(fact)

    @commands.slash_command(
        description="Find a Pokemon by Name",
        options=[
            disnake.Option(
                name="name",
                description="Name of the Pokemon",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.guild)
    async def find_pokemon(
        self, inter: disnake.ApplicationCommandInteraction, name: str
    ):
        name: str = name.replace(" ", "-").lower()
        try:
            pokemon = await funcs.find_pokemon(name=name)
            await inter.response.send_message(
                embed=embeds.pokemon_embed(pokemon=pokemon)
            )
        except Exception:
            await inter.response.send_message("Please provide a Valid Pokemon Name!!")


def setup(bot: commands.Bot):
    bot.add_cog(Fun_(bot))
