import aiohttp, asyncio, dislash, os
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
        async with aiohttp.ClientSession() as client:
            async with client.get("https://some-random-api.ml/meme") as resp:
                response = await resp.json()
                await inter.respond(
                    embed=embeds.meme_embed(
                        label=response["caption"], image=response["image"]
                    )
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
        emojis = []
        puncs_to_emo = {
            "!": "exclamation",
            "+": "heavy_plus_sign",
            "-": "heavy_minus_sign",
            "*": "heavy_multiplication_x",
            "/": "heavy_division_sign",
            "$": "heavy_dollar_sign",
        }

        for word in text.lower():
            if word.isdecimal():
                num_to_emo = {
                    "0": emojis_list.numbers["zero"],
                    "1": emojis_list.numbers["one"],
                    "2": emojis_list.numbers["two"],
                    "3": emojis_list.numbers["three"],
                    "4": emojis_list.numbers["four"],
                    "5": emojis_list.numbers["five"],
                    "6": emojis_list.numbers["six"],
                    "7": emojis_list.numbers["seven"],
                    "8": emojis_list.numbers["eight"],
                    "9": emojis_list.numbers["nine"],
                }
                emojis.append(f"{num_to_emo.get(word)}")
            if word.isalpha():
                emojis.append(emojis_list.alphabets[f"regional_indicator_{word}"])
            elif word in puncs_to_emo:
                emojis.append(emojis_list.punctuation[puncs_to_emo.get(word)])

        await inter.respond(" ".join(emojis))


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
