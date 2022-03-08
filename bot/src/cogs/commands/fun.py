import asyncio, disnake, os, discord_together, credentials, random
import src.core.embeds as embeds
import src.core.functions as funcs
import src.core.files as files
import src.core.calculator as calc
from src.core.bot import JAKDiscordBot
from disnake.ext import commands
from PIL import Image, ImageDraw, ImageFont


class Fun(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
        self.bot = bot
        self.together_control: discord_together.DiscordTogether = None

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

            resp = await funcs.convert_to_snippet(code=code_edited)

            if os.path.isdir("snippets"):
                with open(f"snippets/{author_id}.png", "wb") as f:
                    f.write(resp)
                    carbon_file = f

                await ctx.reply(
                    file=files.code_snippet_file(
                        carbon_file=os.path.realpath(carbon_file.name),
                        author_id=author_id,
                    ),
                )

                await asyncio.sleep(60)

                if os.path.isfile(f"snippets/{author_id}.png"):
                    os.remove(f"snippets/{author_id}.png")
            else:
                os.mkdir("snippets")

                with open(f"snippets/{author_id}.png", "wb") as f:
                    f.write(resp)
                    carbon_file = f

                await ctx.reply(
                    file=files.code_snippet_file(
                        carbon_file=os.path.realpath(carbon_file.name),
                        author_id=author_id,
                    ),
                )

                await asyncio.sleep(60)

                if os.path.isfile(f"snippets/{author_id}.png"):
                    os.remove(f"snippets/{author_id}.png")
        else:
            await ctx.reply("Use a CodeBlock!!")

    @commands.group(
        invoke_without_command=True,
        aliases=["morse_code"],
        description="Encode or Decode PlainText/MorseCode into MorseCode/PlainText",
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def morse(self, ctx: commands.Context, action: str):
        if action:
            await ctx.reply('Action must be "encode" or "decode"')

    @morse.command(description="Encode PlainText into MorseCode", aliases=["en"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def encode(self, ctx: commands.Context, *, text):
        try:
            title, converted = funcs.morse_code_encode_decode(
                text=text, action="encode"
            )
            await ctx.reply(
                embed=embeds.morse_code_embed(title=title, converted=converted)
            )
        except ValueError:
            await ctx.reply(
                "The String contains some characters which cannot be converted into Morse!!"
            )

    @morse.command(description="Decode MorseCode into PlainText", aliases=["de"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def decode(self, ctx: commands.Context, *, text):
        try:
            title, converted = funcs.morse_code_encode_decode(
                text=text, action="decode"
            )
            await ctx.reply(
                embed=embeds.morse_code_embed(title=title, converted=converted)
            )
        except ValueError:
            await ctx.reply(
                "The String contains some characters which cannot be converted into Morse!!"
            )

    @commands.command(description="Display a Fact")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def fact(self, ctx: commands.Context):
        fact = funcs.fact()

        await ctx.reply(fact)

    @commands.group(
        invoke_without_command=True,
        description="Use Discord Together Activities",
        aliases=["discord_together"],
    )
    async def together(self, ctx: commands.Context, activity: str):
        await ctx.reply("Activity not Found!!")

    @together.command(description="Use `YouTube Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def youtube(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "youtube"
        )
        await ctx.reply(link, delete_after=60)
        await asyncio.sleep(60)
        await self.together_control.close()

    @together.command(description="Use `Poker Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def poker(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "poker"
        )
        await ctx.reply(link, delete_after=60)
        await asyncio.sleep(60)
        await self.together_control.close()

    @together.command(description="Use `Chess Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def chess(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "chess"
        )
        await ctx.reply(link, delete_after=60)
        await asyncio.sleep(60)
        await self.together_control.close()

    @together.command(description="Use `Betrayal Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def betrayal(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "betrayal"
        )
        await ctx.reply(link, delete_after=60)
        await asyncio.sleep(60)
        await self.together_control.close()

    @together.command(
        description="Use `Fishing Together` Activity", aliases=["fishington"]
    )
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def fishing(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "fishing"
        )
        await ctx.reply(link, delete_after=60)
        await asyncio.sleep(60)
        await self.together_control.close()

    @together.command(description="Use `Letter Tile Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def letter_tile(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "letter-tile"
        )
        await ctx.reply(link, delete_after=60)
        await asyncio.sleep(60)
        await self.together_control.close()

    @together.command(description="Use `Word Snack Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def word_snack(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "word-snack"
        )
        await ctx.reply(link, delete_after=60)
        await asyncio.sleep(60)
        await self.together_control.close()

    @together.command(description="Use `Doddle Crew Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def doodle_crew(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "doodle-crew"
        )
        await ctx.reply(link, delete_after=60)
        await asyncio.sleep(60)
        await self.together_control.close()

    @together.command(description="Use `Spell Cast Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def spell_cast(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "spellcast"
        )
        await ctx.reply(link, delete_after=60)
        await asyncio.sleep(60)
        await self.together_control.close()

    @together.command(description="Use `Awkword Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def awkword(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "awkword"
        )
        await ctx.reply(link, delete_after=60)
        await asyncio.sleep(60)
        await self.together_control.close()

    @together.command(description="Use `Checkers Together` Activity")
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def checkers(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.reply("You are not Connected to a Voice Channel!!")
            return
        link = await self.together_control.create_link(
            ctx.author.voice.channel.id, "checkers"
        )
        await ctx.reply(link, delete_after=60)
        await asyncio.sleep(60)
        await self.together_control.close()

    @commands.command(
        description="Use a Calculator to do Mathamatics", aliases=["calc"]
    )
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def calculator(self, ctx: commands.Context):
        embed = embeds.calculator_embed()

        await ctx.send(embed=embed, view=calc.CalculatorButtons(embed, ctx.author))

    @commands.command(description="Find a Pokemon by Name")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def find_pokemon(self, ctx: commands.Context, *, name: str):
        name: str = name.replace(" ", "-").lower()
        try:
            pokemon = await funcs.find_pokemon(name=name)
            await ctx.reply(embed=embeds.pokemon_embed(pokemon=pokemon))
        except Exception:
            await ctx.reply("Please provide a Valid Pokemon Name!!")

    @commands.command(description="Find a Pokemon Card by Name")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def find_pokemon_card(self, ctx: commands.Context, *, name: str):
        name: str = name.replace(" ", "-").lower()
        try:
            card = await funcs.find_pokemon_card(name=name)
            await ctx.reply(embed=embeds.pokemon_card_embed(card=card))
        except Exception:
            await ctx.reply("Please provide a Valid Pokemon Card Name!!")

    @commands.command(description="Choose between 2 Options")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def choose(self, ctx: commands.Context, option1: str, option2: str):
        choice = random.choice([option1, option2])

        await ctx.reply(f"Choices: **{option1}**, **{option2}**\nChoice: {choice}")

    @commands.command(description="Generate Name Fact Image")
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def name_fact_generator(self, ctx: commands.Context, name: str, gender: str):
        member = ctx.author
        author_id = member.id

        if not os.path.isdir("name_fact"):
            os.mkdir("name_fact")

        if gender == "f" or gender == "F" or gender == "female" or gender == "Female":
            heshe = "She"
            hisher = "Her"
            guygirl = "girl"
            himher = "her"
            girlguy = "guy"
        elif gender == "m" or gender == "M" or gender == "male" or gender == "Male":
            heshe = "He"
            hisher = "His"
            guygirl = "guy"
            himher = "him"
            girlguy = "girl"
        else:
            await ctx.reply("Incorrect Gender Entered!!")
            return

        lines = funcs.generate_name_fact(name, heshe, hisher, guygirl, himher, girlguy)

        image = Image.new("RGB", (1000, 1000), (255, 255, 255))
        lines_font = ImageFont.truetype("fonts/bahnschrift.ttf", size=38)
        name_font = ImageFont.truetype("fonts/theboldfont.ttf", size=72)
        watermark_font = ImageFont.truetype("fonts/arial.ttf", size=24)

        history = []
        y0, dy = 220, 40
        for i in range(6):
            y0 += 10
            text = random.choice(lines)
            try:
                history.index(text)
                continue
            except:
                history.append(text)
                for j, line in enumerate(text.split("\n")):
                    y0 += dy
                    ImageDraw.Draw(image).text(
                        (70, y0), line, fill="rgb(0,0,0)", font=lines_font
                    )

        ImageDraw.Draw(image).rectangle(
            [50, 150, 1000 - 50, y0 + 70], fill=None, outline=(0, 0, 0), width=5
        )
        ImageDraw.Draw(image).text(
            (70, 180), str(name), fill="rgb(0,0,0)", font=name_font
        )
        ImageDraw.Draw(image).text(
            (1000 - 400, 1000 - 30),
            "JAK Discord Bot",
            fill="rgb(0,0,0)",
            font=watermark_font,
        )

        image.save(f"name_fact/{author_id}.png")

        await ctx.reply(
            file=files.name_fact_file(
                file=os.path.realpath(f"name_fact/{author_id}.png"),
                author_id=author_id,
            )
        )

        await asyncio.sleep(60)

        if os.path.isfile(f"name_fact/{author_id}.png"):
            os.remove(f"name_fact/{author_id}.png")

    @commands.command(description="Convert Text to Ascii art")
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def ascii(self, ctx: commands.Context, *, text: str):
        art = funcs.convert_to_ascii(text=text)

        await ctx.reply(f"```{art}```")

    @commands.Cog.listener()
    async def on_ready(self):
        self.together_control = await discord_together.DiscordTogether(
            credentials.TOKEN
        )


def setup(bot: JAKDiscordBot):
    bot.add_cog(Fun(bot))
