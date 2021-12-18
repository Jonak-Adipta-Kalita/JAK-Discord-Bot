import aiohttp, os
import src.embeds as embeds
import src.functions as funcs
import src.emojis as emojis_list
import src.files as files
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help_fun(self, ctx: commands.Context):
        await ctx.send(
            embed=embeds.fun_help_embed(
                ctx=ctx,
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar_url,
            )
        )

    @commands.command()
    async def joke(self, ctx: commands.Context):
        joke = funcs.get_joke()

        await ctx.send(joke)

    @commands.command()
    async def meme(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as client:
            async with client.get("https://some-random-api.ml/meme") as resp:
                response = await resp.json()
                await ctx.send(
                    embed=embeds.meme_embed(
                        label=response["caption"], image=response["image"]
                    )
                )

    @commands.command()
    async def emojify(self, ctx: commands.Context, *, text):
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

        await ctx.send(" ".join(emojis))

    @commands.command()
    async def code_snippet(self, ctx: commands.Context, *, code: str):
        member = ctx.author

        if code.startswith("```") and code.endswith("```"):
            author_id = member.id
            code_edited = "\n".join(code.split("\n")[1:-1])

            async with aiohttp.ClientSession(
                headers={"Content-Type": "application/json"},
            ) as ses:
                try:
                    request = await ses.post(
                        f"https://carbonara-42.herokuapp.com/api/cook",
                        json={
                            "code": code_edited,
                        },
                    )
                except Exception as e:
                    print(f"Exception: {e}")

                resp = await request.read()

            with open(f"snippets/{author_id}.png", "wb") as f:
                f.write(resp)
                carbon_file = f

            await ctx.send(
                file=files.code_snippet_file(
                    carbon_file=os.path.realpath(carbon_file.name), author_id=author_id
                ),
            )
        else:
            await ctx.send(f"{member.mention}!! Use a CodeBlock!!")


def setup(bot):
    bot.add_cog(Fun(bot))
