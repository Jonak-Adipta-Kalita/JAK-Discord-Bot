import asyncio, disnake, random, os
import src.core.embeds as embeds
import src.core.files as files
import src.core.functions as funcs
from disnake.ext import commands
from PIL import Image, ImageDraw, ImageFont


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
                name="action",
                description="The Action (Encode or Decode)!!",
                type=disnake.OptionType.string,
                required=True,
            ),
            disnake.Option(
                name="text",
                description="The Text to Encode/Decode!!",
                type=disnake.OptionType.string,
                required=True,
            ),
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def morse(
        self, inter: disnake.ApplicationCommandInteraction, action: str, text: str
    ):
        if action in ["encode", "decode"]:
            try:
                title, converted = funcs.morse_code_encode_decode(
                    text=text, action=action
                )
                await inter.response.send_message(
                    embed=embeds.morse_code_embed(title=title, converted=converted)
                )
            except ValueError:
                await inter.response.send_message(
                    "The String contains some characters which cannot be converted into Morse!!"
                )
        else:
            await inter.response.send_message('Action must be "encode" or "decode"')

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

    @commands.command(
        description="Choose between 2 Options",
        options=[
            disnake.Option(
                name="option1",
                description="First Option",
                type=disnake.OptionType.string,
                required=True,
            ),
            disnake.Option(
                name="option2",
                description="Second Option",
                type=disnake.OptionType.string,
                required=True,
            ),
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def choose_between(
        self, inter: disnake.ApplicationCommandInteraction, option1: str, option2: str
    ):
        choice = random.choice([option1, option2])

        await inter.response.send_message(
            f"Choices: **{option1}**, **{option2}**\nChoice: {choice}"
        )

    @commands.slash_command(
        description="Generate Name Fact Image",
        options=[
            disnake.Option(
                name="name",
                description="Your Name",
                type=disnake.OptionType.string,
                required=True,
            ),
            disnake.Option(
                name="gender",
                description="Your Gender",
                type=disnake.OptionType.string,
                required=True,
            ),
        ],
    )
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def name_fact_generator(
        self, inter: disnake.ApplicationCommandInteraction, name: str, gender: str
    ):
        await inter.response.defer()

        member = inter.author
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
            await inter.edit_original_message("Incorrect Gender Entered!!")
            return

        lines = funcs.generate_name_fact(name, heshe, hisher, guygirl, himher, girlguy)

        image = Image.new("RGB", (1000, 1000), (255, 255, 255))
        lines_font = ImageFont.truetype("resources/bahnschrift.ttf", size=38)
        name_font = ImageFont.truetype("resources/theboldfont.ttf", size=72)
        watermark_font = ImageFont.truetype("resources/arial.ttf", size=24)

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

        await inter.edit_original_message(
            file=files.name_fact_file(
                file=os.path.realpath(f"name_fact/{author_id}.png"),
                author_id=author_id,
            )
        )

        await asyncio.sleep(60)

        if os.path.isfile(f"name_fact/{author_id}.png"):
            os.remove(f"name_fact/{author_id}.png")


def setup(bot: commands.Bot):
    bot.add_cog(Fun_(bot))
