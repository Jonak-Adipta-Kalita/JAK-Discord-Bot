import asyncio, disnake, random, os, art
import src.core.embeds as embeds
import src.core.files as files
import src.core.functions as funcs
import src.core.buttons as buttons
import src.core.modals as modals
from src.core.bot import JAKDiscordBot
from disnake.ext import commands
from PIL import Image, ImageDraw, ImageFont


class Fun_(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
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
                choices=["encode", "decode"],
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
        try:
            title, converted = funcs.morse_code_encode_decode(text=text, action=action)
            await inter.response.send_message(
                embed=embeds.morse_code_embed(title=title, converted=converted)
            )
        except ValueError:
            await inter.response.send_message(
                "The String contains some characters which cannot be converted into Morse!!",
                ephemeral=True,
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
            await inter.response.send_message(
                "Please provide a Valid Pokemon Name!!", ephemeral=True
            )

    @commands.slash_command(
        description="Find a Pokemon Card by Name",
        options=[
            disnake.Option(
                name="name",
                description="Name of the Pokemon Card",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def find_pokemon_card(
        self, inter: disnake.ApplicationCommandInteraction, name: str
    ):
        name: str = name.replace(" ", "-").lower()
        try:
            card = await funcs.find_pokemon_card(name=name)
            await inter.response.send_message(
                embed=embeds.pokemon_card_embed(card=card)
            )
        except Exception:
            await inter.response.send_message(
                "Please provide a Valid Pokemon Card Name!!", ephemeral=True
            )

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
            await inter.edit_original_message(content="Incorrect Gender Entered!!")
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

        await inter.edit_original_message(
            file=files.name_fact_file(
                file=os.path.realpath(f"name_fact/{author_id}.png"),
                author_id=author_id,
            )
        )

        await asyncio.sleep(60)

        if os.path.isfile(f"name_fact/{author_id}.png"):
            os.remove(f"name_fact/{author_id}.png")

    @commands.slash_command(description="Use a Calculator to do Mathamatics")
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def calculator(self, inter: disnake.ApplicationCommandInteraction):
        embed = embeds.calculator_embed()

        await inter.response.send_message(
            embed=embed, view=buttons.CalculatorButtons(embed, inter.author)
        )

    @commands.slash_command(
        description="Convert Text to Ascii art",
        options=[
            disnake.Option(
                name="text",
                description="Text to convert to Ascii",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def ascii(self, inter: disnake.ApplicationCommandInteraction, text: str):
        if len(text) > 10:
            await inter.response.send_message(
                "Length of Text cannot be more than 10 Characters!!", ephemeral=True
            )
            return

        asciiart = art.text2art(text)

        if len(asciiart) > 1990:
            await inter.response.send_message(
                "ASCII Art crossed more than 2000 Words!! Please try a smaller Text!!",
                ephemeral=True,
            )
            return

        await inter.response.send_message(f"```{asciiart}```")

    @commands.slash_command(
        description="Use Discord Together Activities",
        options=[
            disnake.Option(
                name="activity",
                description="The Activity you want to use",
                type=disnake.OptionType.string,
                required=True,
                choices=JAKDiscordBot.together_choices,
            )
        ],
    )
    @commands.bot_has_permissions(create_instant_invite=True)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    async def together(
        self, inter: disnake.ApplicationCommandInteraction, activity: str
    ):
        if inter.author.voice is None:
            await inter.response.send_message(
                "You are not Connected to a Voice Channel!!", ephemeral=True
            )
            return
        link = await self.bot.together_control.create_link(
            inter.author.voice.channel.id, activity, max_age=60
        )
        await inter.response.send_message(link, delete_after=60)

    @commands.slash_command(
        description="Find a Brawler by Name",
        options=[
            disnake.Option(
                name="name",
                description="Name of the Brawler",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def find_brawler(
        self, inter: disnake.ApplicationCommandInteraction, name: str
    ):
        await inter.response.defer()

        try:
            brawlstars_data = await funcs.get_brawlstars()
            brawlers_names = [
                brawler["name"] for brawler in brawlstars_data["brawlers"]
            ]

            for i, brawler_name in enumerate(brawlers_names):
                if brawler_name.lower() == name.lower():
                    brawler: dict = brawlstars_data["brawlers"][i]
                    break

            await inter.edit_original_message(
                embed=embeds.brawler_embed(brawler=brawler)
            )

        except UnboundLocalError:
            await inter.edit_original_message(
                content="Please provide a Valid Brawler Name!!"
            )

    @commands.slash_command(description="Covert Code Block to Snippet")
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def code_snippet(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_modal(
            modal=modals.CodeSnippetModal(author=inter.author)
        )

    @commands.slash_command(description="Generate ambigram with two words")
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def ambigram(
        self, inter: disnake.ApplicationCommandInteraction, word_1: str, word_2: str
    ):
        await inter.response.defer()

        if not os.path.isdir("ambigrams"):
            os.mkdir("ambigrams")

        file_name = funcs.generate_ambigram(
            word1=word_1, word2=word_2, author_id=inter.author.id
        )

        await inter.edit_original_message(
            file=files.ambigram_file(file=file_name, author_id=inter.author.id)
        )

        await asyncio.sleep(60)

        if os.path.isfile(file_name):
            os.remove(file_name)


def setup(bot: JAKDiscordBot):
    bot.add_cog(Fun_(bot))
