import asyncio, disnake, os, discord_together, credentials, simpleeval, re, random
import src.core.embeds as embeds
import src.core.functions as funcs
import src.core.files as files
from disnake.ext import commands
from PIL import Image, ImageDraw, ImageFont


sup = {
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
    "-": "⁻",
}
norm = {
    "⁰": "0",
    "¹": "1",
    "²": "2",
    "³": "3",
    "⁴": "4",
    "⁵": "5",
    "⁶": "6",
    "⁷": "7",
    "⁸": "8",
    "⁹": "9",
}
operations = ["/", "*", "+", "-"]


class buttons(disnake.ui.View):
    def __init__(self, embed: disnake.Embed, ctx: commands.Context):
        super().__init__()

        self.embed = embed
        self.ctx = ctx

    async def interaction_check(self, interaction: disnake.MessageInteraction) -> bool:
        if interaction.author == self.ctx.author:
            return True

        await interaction.response.send_message(
            "This is not your calculator!", ephemeral=True
        )
        return False

    def get_description(self) -> str:
        return self.embed.description[8:-3]

    def edit_embed(self, label) -> str:
        content = self.get_description()
        if content == "0":
            return f"```yaml\n{label}```"

        if "Out" in content:
            return f"```yaml\n{label}```"
        if content[-1] == "ˣ":
            return f"```yaml\n{content[:-1]}{sup[label]}```"
        if content[-1] in norm:
            return f"```yaml\n{content}{sup[label]}```"
        return f"```yaml\n{content}{label}```"

    @disnake.ui.button(label="1", style=disnake.ButtonStyle.grey, row=0)
    async def first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="2", style=disnake.ButtonStyle.grey, row=0)
    async def second_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="3", style=disnake.ButtonStyle.grey, row=0)
    async def third_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="*", style=disnake.ButtonStyle.green, row=0)
    async def fourth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):

        self.embed.description = self.edit_embed(" * ")
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="√", style=disnake.ButtonStyle.green, row=0)
    async def fifth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="4", style=disnake.ButtonStyle.grey, row=1)
    async def row_two_first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="5", style=disnake.ButtonStyle.grey, row=1)
    async def row_two_second_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="6", style=disnake.ButtonStyle.grey, row=1)
    async def row_two_third_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="-", style=disnake.ButtonStyle.green, row=1)
    async def row_two_fourth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(" - ")
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="ˣ", style=disnake.ButtonStyle.green, row=1)
    async def row_two_fifth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="7", style=disnake.ButtonStyle.grey, row=2)
    async def row_three_first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="8", style=disnake.ButtonStyle.grey, row=2)
    async def row_three_second_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="9", style=disnake.ButtonStyle.grey, row=2)
    async def row_three_third_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="+", style=disnake.ButtonStyle.green, row=2)
    async def row_three_fourth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(" + ")
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="⌫", style=disnake.ButtonStyle.red, row=2)
    async def row_three_fifth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        content = self.get_description()
        display = f"```yaml\n{self.get_description()[:-1] if self.get_description() != '0' else '0'}```"

        if content[-1] == " " and content[-2] in operations:
            print(".")
            display = f"```yaml\n{content[:-3]}```"

        self.embed.description = display
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label=".", style=disnake.ButtonStyle.grey, row=3)
    async def row_four_first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="0", style=disnake.ButtonStyle.grey, row=3)
    async def row_four_second_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="=", style=disnake.ButtonStyle.grey, row=3)
    async def row_four_third_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        display = self.get_description()
        equation = "".join([k if k not in norm else f"**{norm[k]}" for k in display])
        pattern = re.compile("^√(\d+)")
        equation = pattern.sub("\\1 ** 0.5 ", equation)

        try:
            result = simpleeval.simple_eval(equation)
        except Exception as e:
            print(e)
            result = "Error! Something went wrong"

        self.embed.description = f"```yaml\nIn ❯❯ {display} \nOut ❯❯ {result}```"
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="/", style=disnake.ButtonStyle.green, row=3)
    async def row_four_fourth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(" / ")
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="Clear", style=disnake.ButtonStyle.red, row=3)
    async def row_four_fifth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = "```yaml\n0```"
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="(", style=disnake.ButtonStyle.blurple, row=4)
    async def row_five_first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label=")", style=disnake.ButtonStyle.blurple, row=4)
    async def row_five_second_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(button.label)
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="Space", style=disnake.ButtonStyle.red, row=4)
    async def row_five_third_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        self.embed.description = self.edit_embed(" ")
        await interaction.response.edit_message(embed=self.embed)

    @disnake.ui.button(label="Sci", style=disnake.ButtonStyle.red, row=4)
    async def row_five_fourth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("Soon to come...", ephemeral=True)

    @disnake.ui.button(label="Exit", style=disnake.ButtonStyle.red, row=4)
    async def row_five_fifth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.edit_message()
        self.stop()


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.together_control: discord_together.DiscordTogether = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.together_control = await discord_together.DiscordTogether(
            credentials.TOKEN
        )

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

    @together.command(description="Use `Chess Together` Activity")
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

    @together.command(description="Use `Poker Together` Activity")
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

    @commands.command(description="Use a Calculator to do Mathamatics")
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def calculator(self, ctx: commands.Context):
        embed = embeds.calculator_embed()

        await ctx.send(embed=embed, view=buttons(embed, ctx))

    @commands.command(description="Find a Pokemon by Name")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def find_pokemon(self, ctx: commands.Context, *, name: str):
        name: str = name.replace(" ", "-").lower()
        try:
            pokemon = await funcs.find_pokemon(name=name)
            await ctx.reply(embed=embeds.pokemon_embed(pokemon=pokemon))
        except Exception:
            await ctx.reply("Please provide a Valid Pokemon Name!!")

    @commands.command(description="Choose between 2 Options")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def choose(self, ctx: commands.Context, option1: str, option2: str):
        choice = random.choice([option1, option2])

        await ctx.reply(f"Choices: **{option1}**, **{option2}**\nChoice: {choice}")

    @commands.command(description="Generate Name Fact Image")
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def name_fact_generator(self, ctx: commands.Context, member: disnake.Member, gender: str):
        member = ctx.author
        author_id = member.id
        name = member.display_name

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

        lines = [
            f"{heshe} is fun and playful, but has a serious side.",
            f"A smart, talented and humorous {guygirl}, who likes\nto take charge.",
            f"A {guygirl} with a big heart.",
            f"Very rare though, {heshe} is usually a very sweet\nperson and is protective when it comes to {hisher}\nfriends.",
            "A perfect blend of brains and strength.",
            "Someone who has many dreams and desires.",
            f"{str(name)} is a great listener and you can always\ntrust {himher} with anything.",
            f"{str(name)}, a fun energetic {guygirl}, this {guygirl} just\noozes charisma.",
            f"A nice {guygirl}, who respect the feelings of {girlguy}s,\ngood looking personality, charming, smart.",
            f"Many people find {str(name)} rude and arrogant but\n {heshe} is the best and thus has many enemies.",
            f"An attractive, charming {guygirl}, full of joy.",
            f"{heshe} is a great person who will be the best friend\nyou ever had once you crack {hisher} hard outer\nshell.",
            "Romantic and charming.",
            f"One of the sweetest {guygirl}s you will come across\nalthough\nkeep {himher} in your life when {heshe} comes across\nyou. You might regret leaving {himher}.",
            f"{str(name)} is a very unique and interesting person.",
            f"{str(name)} is an amazing friend and {heshe} will always\nbe there for you.",
            f"{str(name)}'s have elegance, charm and good taste,\nare naturally kind, very gentle, and lovers of\nbeauty.",
            f"{heshe} notices when your down and always brings\nyou back up.",
            f"{heshe} is a kind and caring person.",
            f"{str(name)} is overall funny, kind, a savage,\nintelligent and just overall an amazing person.",
            f"{hisher} beauty over powers all the other {guygirl}s and\nnot only is {heshe} smoking hot but {hisher} style is so\ncool.",
            f"Not a fan of romantic commitments but deeply\ncommitted to {hisher} fail out and friends.",
            f"{str(name)} is extremely smart, loving and\nknowledgeable person.",
            "The epitome of cool. Often used to denote\nsomeone whose very understanfing.",
            f"Everyone likes {himher}.",
            f"{heshe} has big dreams, and {heshe} can make them\ncome true.",
            f"You want to be like this {guygirl}, {heshe}'s just too good\nto be true. A true legend.",
            f"Keep {himher} in your life when {heshe} comes across\nyou. You might regret leaving {himher}.",
            f"{str(name)} is a healer of hearts.",
            "The Kind of person who is one in million",
            f"{str(name)} is smart,funny and beautiful.",
            f"{heshe}'s smart beautiful kind and caring.",
            f"Time files with a {str(name)}, as they are simply\nmesmerizing.",
            f"{str(name)} has an amazing personality. Also\nfunny and fun to be around.",
            f"{heshe} is very funny, smart, and good at event the\nnew things {heshe} tries.",
            f"{str(name)} thinks {heshe}'s unattractive but every {girlguy}\n{heshe} walks past just stops and stares.",
            "Strong opinions but has an open mind.",
            "Usually loves hugs and respects people a lot.",
            f"{heshe}'s adorable, {heshe}'s hot, {heshe}'s everything a {girlguy}\ncraves for.",
            f"A good looking {guygirl} with a perfect smile.",
            "Cuddly like a teddy bear but strong like\na soldier.",
            f"{heshe} is loveable, caring, but also tough and\nprotective.",
            f"{girlguy}s really dig a {guygirl} like {himher} cuz {heshe}'s got most\nof the skills..",
            "Will make you laugh a lot.",
            "This person is always well dressed and very\nloved.",
            f"{heshe} is a perfectionist.",
            "The most beautiful eyes in the whole wide\nworld. They Look like stars and if you look too\ndeep you'll get lost in them.",
            "Diplomatic and urbane.",
            "Always genuine and will try and help out if\nyou're in need.",
            f"{str(name)}'s Run the world, and always get what they\ndesire.",
            f"A beautiful {guygirl} who makes people laugh\nall the time.",
            f"{str(name)}'s funny as hell.",
            f"Quite with the ones {heshe} is unfamiliar with, and\necstatic with those {heshe} prizes.",
            f"{str(name)} is an amazing person.",
            f"{str(name)} is a very smart and caring person.",
            "When they need to talk and gives great advice to\nany and everyone.",
            f"{str(name)} is a very smart, sweet, good looking\nand extremely intelligent {guygirl}.",
            "Easygoing and sociable.",
            f"{heshe} can talk to basically anything or anyone for\nhours.",
            "One of the most wonderful person you will ever\nmeet in your life.",
            "Will do anything for friends.",
            f"{heshe} is dutiful and will never put {hisher} own thoughts\nand feelings before {hisher} loved ones.",
            "Wise enough to overcome every situation.",
            f"{heshe} makes you smile with all your heart and you\nlove {himher} and never want to loose {himher}.",
            "Very passionate and romantic and emotional\ntoo!",
            f"If u r {hisher} {girlguy} he'll take care of u like a little\ndiamond of {hisher}.",
            f"{str(name)} has a kind heart, and is family oriented.",
            f"Will insist that {heshe} is a piece of hard candy, but\nif you dig deep enough {heshe}'s got a soft chewy\ncenter.",
            f"{heshe} is likesd by everyone and also has a great\ntaste in fashion.",
            "A very awesome person who is well rounded\nand good at everything.",
            f"{str(name)} can't be wholly defined in few words\nbecause {heshe}'s so close to perfection that any\nwords for {hisher} just won't be good enough.",
            "Helps everyone, great friend, crazy about many\nthings.",
            f"{str(name)} is a {guygirl} you will want to hold close\nforever.",
            "Loves to party and have fun, and can always\nmake you smile.",
            f"{hisher} smile is infectious and {heshe} laughs all the\ntime which everyone loves about {himher}.",
            f"{str(name)} is completely down to earth and sweet\nand kind. {heshe} is the best friend anybody could\never wish for!",
            f"{str(name)} might come off as indifferent and\nimpatient occasionally but it's only because\nthey are working for greater good which takes a\nlot of effort.",
            "Cute and caring. One of the nicest people you'll\nmeet.",
            f"Stunning long legs, hazel eyes, perfect smile,\ndimples, freckles, and every {girlguy} dream.",
            f"Everything {heshe} does is so sexy and appealing,\nwhen you see {himher}..",
            f"{heshe} thinks only about only the lucky {girlguy} {heshe} loves and\nno one else.",
            "Someone you can talk to and trust.",
            f"{str(name)} is funny and {heshe} will make you laugh in\nthe hardest times beacuase {heshe} loves to see\npeople smile.",
            f"The most perfect {guygirl} in the universe.",
            f"{heshe} is a strong hearted charming person.",
            f"{heshe} is good looking, polite, and just all round\nplain awesome.",
            f"{heshe} holds {hisher} emotions and true feelings back\n{heshe}'s very protective of what {heshe} cares for.",
            f"Everyone likes {himher}.",
            "Destined to become a person who does not\nhave an average job.",
            f"One of the most unique {guygirl} you'll every meet.",
            f"{str(name)}'s are extremely caring, affable, and they\nare very sensititve but tend to hide it.",
            f"{heshe}'s the kind of {guygirl}who's so loveable that\neveryone likes her.",
            "Black hair, brown eyes, falls in love hard and\nfast but won't admit it.",
            f"You are really lucky if you have a {str(name)} in your\nlife especially if you are dating her.",
            f"{str(name)} is and achiever and the best person you turn\nto when you need a shoulder to cry on.",
            f"{str(name)} is the definition of compassion.",
            f"The best person ever. {heshe} is one of a kind.",
            f"{heshe}'s beautiful, lovely body and lovely\npersonality.",
            f"A {str(name)} is worthy of being a friend for quite\na long time.",
            f"{heshe} doesn't know how valuable {heshe} really is so\nmake {himher} realise {hisher} worth.",
            f"{heshe} is unique in every way starting from {hisher}\nname to {hisher} looks and personality.",
            f"Always will have your back no matter who you\nare unless you get on {hisher} bad; once you on {hisher}\nbad side there's no coming back.",
            f"{heshe} is loyal to people and won't back stab you.",
            "Really beautiful, has an amazing body.",
            "The ruler of real goon nation and one of a kind.",
            "Never less than awesome.",
            f"{str(name)}'s are the model type, loved by {girlguy}, and\nhated by some {guygirl}s who are jealous.",
            f"{str(name)} can do whatever {heshe} puts {hisher} mind to and\n{heshe} is not quitter, {heshe} does not give up easily\non anything or anyone.",
            f"{heshe} loves music.",
            f"{str(name)} is a very smart and caring person.",
            f"{heshe} has a rocken model body that makes other\n{guygirl} jealous, but {heshe} is very modest.",
            "They are logical, understanding, and see\nthrough any trick or gig you try to pull on them.",
            "The person who radiates happiness.",
            f"{str(name)} is a {guygirl} who is not really insecure and is\nquite protective sometimes.",
            "They have trouble expressing their\nemotions in real life, but it takes the right person\nto see through this barrier and into their true\nhearts.",
            f"{str(name)} has beautiful hairs.",
            f"{heshe} is really funny and sarcastic but really\nsweet and kindhearted at the same time.",
            f"If you ever come across a {str(name)} never let {himher}\ngo because {heshe}'ll be the best thing that you've\never had.",
            f"{str(name)} have a lot of talent in the arts and\nperformance arts and have quite a lot of sports\npotential that they may/may not put to use.",
            "Someone who loves and cares for everyone.",
            f"Modest, but also speak {hisher} mind in a way that\nothers can't.",
            f"Sometimes you need to have patience with {himher}\nbecause {heshe} has anger issues but {heshe}'ll get\nover it very fast.",
            f"{heshe}'s beautiful, talented and intelligent af You\ncan not ignore a {str(name)}, If you do, you have\nforgotten it till you die.",
            "Smart and out to prove the world wrong.",
            f"It's like a drug! Your heart races and you can't\nget enough of {str(name)}'s gorgeousness.",
            f"If you ever find {himher} just hold on tight and never\nlet go cause {heshe} is a gem.",
            f"{str(name)}s are the best!",
            f"{str(name)}'s are absolutely stunning, gorgeous, and\nallurging.",
            f"{heshe} cares about {hisher} family and {hisher} friends and\nis a person who is trustworthy.",
            f"{heshe} is not only unique but one of a kind.",
            f"{str(name)} is too perfect to describe.",
            f"{str(name)} likes to keep {hisher} circle tight and small,{heshe}\n is picky about who {heshe} trusts, and isn't fond of\nlarge circles.",
            f"{girlguy} really wish to have a man who is protective\nenough and secure enough.",
            f"{heshe}'ll leave you coming back for more; wanted\nby many.",
            "Their eyes, eyebrows, and overall facial\nstructure are striking.",
            "Idealistic and peaceable."
        ]

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
            (1000 - 400, 1000 - 30), "JAK Discord Bot", fill="rgb(0,0,0)", font=watermark_font
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


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
