import aiohttp, asyncio, discord, os
import src.embeds as embeds
import src.functions as funcs
import src.files as files
from discord.ext import commands


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
            code_edited = discord.utils.remove_markdown(code.strip()).strip()

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

        TEXT_TO_MORSE = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----",
            ",": "--..--",
            ".": ".-.-.-",
            "?": "..--..",
            "/": "-..-.",
            "-": "-....-",
            "(": "-.--.",
            ")": "-.--.-",
            ":": "---...",
            "'": ".----.",
            "’": ".----.",
            '"': ".-..-.",
            " ": ".......",
            "!": "-.-.--",
            "@": ".--.-.",
            "$": "...-..-",
            "&": ".-...",
            ";": "-.-.-.",
            "=": "-...-",
            "+": ".-.-.",
            "_": "..--.-",
        }

        MORSE_TO_TEXT = {
            ".-": "A",
            "-...": "B",
            "-.-.": "C",
            "-..": "D",
            ".": "E",
            "..-.": "F",
            "--.": "G",
            "....": "H",
            "..": "I",
            ".---": "J",
            "-.-": "K",
            ".-..": "L",
            "--": "M",
            "-.": "N",
            "---": "O",
            ".--.": "P",
            "--.-": "Q",
            ".-.": "R",
            "...": "S",
            "-": "T",
            "..-": "U",
            "...-": "V",
            ".--": "W",
            "-..-": "X",
            "-.--": "Y",
            "--..": "Z",
            ".----": "1",
            "..---": "2",
            "...--": "3",
            "....-": "4",
            ".....": "5",
            "-....": "6",
            "--...": "7",
            "---..": "8",
            "----.": "9",
            "-----": "0",
            "--..--": ",",
            ".-.-.-": ".",
            "..--..": "?",
            "-..-.": "/",
            "-....-": "-",
            "-.--.": "(",
            "-.--.-": ")",
            "---...": ":",
            ".----.": "'",
            ".-..-.": '"',
            ".......": " ",
            "-.-.--": "!",
            ".--.-.": "@",
            "...-..-": "$",
            ".-...": "&",
            "-.-.-.": ";",
            "-...-": "=",
            ".-.-.": "+",
            "..--.-": "_",
        }

        _tempset = set(string)
        check = True
        for char in _tempset:
            if char not in [".", "-", " "]:
                check = False

        if check is True:
            _templist = str(string).split(" ")
            converted = "".join(MORSE_TO_TEXT[str(i)] for i in _templist)

            await ctx.reply(embed=embeds.morse_code_embed(
                ctx=ctx, title="Morse ---> Text", converted=converted
            ))
        else:
            _templist = []
            for char in str(string):
                _templist.append(char)
            try:
                converted = " ".join(TEXT_TO_MORSE[str(i).upper()] for i in _templist)
                await ctx.reply(embed=embeds.morse_code_embed(
                    ctx=ctx, title="Text ---> Morse", converted=converted
                ))
            except KeyError:
                await ctx.reply(
                    "The String contains some characters which cannot be converted into Morse!!"
                )


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
