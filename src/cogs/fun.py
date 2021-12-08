from discord.ext import commands
from src.functions import get_joke
from src.embeds import fun_help_embed, meme_embed
import aiohttp


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help_fun(self, ctx: commands.Context):
        await ctx.send(embed=fun_help_embed(ctx))

    @commands.command()
    async def joke(self, ctx: commands.Context):
        joke = get_joke()

        await ctx.send(joke)

    @commands.command()
    async def meme(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as client:
            async with client.get("https://some-random-api.ml/meme") as resp:
                response = await resp.json()
                await ctx.send(
                    embed=meme_embed(label=response["caption"], image=response["image"])
                )

    @commands.command()
    async def emojify(self, ctx: commands.Context, *, text):
        emojis = []
        punc_to_emo = {"!": "grey_exclamation"}

        for word in text.lower():
            if word.isdecimal():
                num_to_emo = {
                    "0": "zero",
                    "1": "one",
                    "2": "two",
                    "3": "three",
                    "4": "four",
                    "5": "five",
                    "6": "six",
                    "7": "seven",
                    "8": "eight",
                    "9": "nine",
                }
                emojis.append(f":{num_to_emo.get(word)}:")
            if word.isalpha():
                emojis.append(f":regional_indicator_{word}:")
            elif word in punc_to_emo:
                print("punc found")
                emojis.append(f":{punc_to_emo.get(word)}:")

        await ctx.send("".join(emojis))


def setup(bot):
    bot.add_cog(Meme(bot))
