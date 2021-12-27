import aiohttp, asyncio, disnake, os
import src.embeds as embeds
import src.functions as funcs
import src.files as files
from disnake.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description="Display a Joke")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def joke(self, ctx: commands.Context):
        joke = funcs.get_joke()

        await ctx.reply(joke)

    @commands.command(description="Display a Meme")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def meme(self, ctx: commands.Context):
        response = await funcs.get_meme()
        await ctx.reply(
            embed=embeds.meme_embed(label=response["caption"], image=response["image"])
        )

    @commands.command(description="Display a Meme")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def emojify(self, ctx: commands.Context, *, text):
        await ctx.reply(" ".join(funcs.emojify_text(text)))

    @commands.command(description="Covert Code Block to Snippet")
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def code_snippet(self, ctx: commands.Context, *, code: str):
        member = ctx.author

        if code.startswith("```") and code.endswith("```"):
            author_id = member.id
            code_edited = disnake.utils.remove_markdown(code.strip()).strip()

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

            await ctx.reply(
                file=files.code_snippet_file(
                    carbon_file=os.path.realpath(carbon_file.name), author_id=author_id
                ),
            )

            await asyncio.sleep(60)

            if os.path.isfile(f"snippets/{author_id}.png"):
                os.remove(f"snippets/{author_id}.png")
        else:
            await ctx.reply("Use a CodeBlock!!")

    @commands.command(
        aliases=["morse_code"],
        description="Encode or Decode PlainText/MorseCode into MorseCode/PlainText",
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def morse(self, ctx: commands.Context, *, string):
        try:
            title, converted = funcs.morse_code_encode_decode(text=string)
            await ctx.reply(
                embed=embeds.morse_code_embed(title=title, converted=converted)
            )
        except KeyError:
            await ctx.reply(
                "The String contains some characters which cannot be converted into Morse!!"
            )

    @commands.command(description="Display a Fact")
    async def fact(self, ctx: commands.Context):
        fact = funcs.fact()

        await ctx.send(fact)


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
