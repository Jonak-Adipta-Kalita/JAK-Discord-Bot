import disnake, simpleeval, re, akinator.async_aki as akinator
import src.core.emojis as emojis
import src.core.embeds as embeds

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


class CalculatorButtons(disnake.ui.View):
    def __init__(self, embed: disnake.Embed, author: disnake.Member):
        super().__init__(timeout=300)

        self.embed = embed
        self.author = author

    async def interaction_check(self, interaction: disnake.MessageInteraction) -> bool:
        if interaction.author == self.author:
            return True

        await interaction.response.send_message(
            "This is not your calculator!!", ephemeral=True
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


class AkinatorButtons(disnake.ui.View):
    def __init__(
        self,
        author: disnake.Member,
        aki: akinator.Akinator,
        embed: disnake.Embed,
        counter: int,
    ):
        super().__init__(timeout=300)

        self.author = author
        self.aki = aki
        self.embed = embed
        self.counter = counter

    async def interaction_check(self, interaction: disnake.MessageInteraction) -> bool:
        if interaction.author == self.author:
            return True

        await interaction.response.send_message(
            "This is not your Akinator Game!!", ephemeral=True
        )
        return False

    async def check_for_progression(self, interaction: disnake.MessageInteraction):
        if self.aki.progression >= 85:
            await self.aki.win()
            await interaction.edit_original_message(
                embed=embeds.akinator_embed(guess=self.aki.first_guess), view=None
            )

    @disnake.ui.button(
        label="Yes", style=disnake.ButtonStyle.blurple, emoji=emojis.thumbs["up"]
    )
    async def yes(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        question = await self.aki.answer("yes")
        self.counter += 1
        self.embed.title = f"Question no. {self.counter}: {question}"
        await interaction.edit_original_message(
            embed=self.embed,
        )

        await self.check_for_progression(interaction=interaction)

    @disnake.ui.button(
        label="No", style=disnake.ButtonStyle.blurple, emoji=emojis.thumbs["down"]
    )
    async def no(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        question = await self.aki.answer("no")
        self.counter += 1
        self.embed.title = f"Question no. {self.counter}: {question}"
        await interaction.edit_original_message(
            embed=self.embed,
        )

        await self.check_for_progression(interaction=interaction)

    @disnake.ui.button(
        label="Don't Know",
        style=disnake.ButtonStyle.blurple,
        emoji=emojis.punctuation["question"],
    )
    async def dont_know(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        question = await self.aki.answer("idk")
        self.counter += 1
        self.embed.title = f"Question no. {self.counter}: {question}"
        await interaction.edit_original_message(
            embed=self.embed,
        )

        await self.check_for_progression(interaction=interaction)

    @disnake.ui.button(
        label="Probably",
        style=disnake.ButtonStyle.blurple,
        emoji=emojis.faces["thinking"],
    )
    async def probably(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        question = await self.aki.answer("probably")
        self.counter += 1
        self.embed.title = f"Question no. {self.counter}: {question}"
        await interaction.edit_original_message(
            embed=self.embed,
        )

        await self.check_for_progression(interaction=interaction)

    @disnake.ui.button(
        label="Probably Not",
        style=disnake.ButtonStyle.blurple,
        emoji=emojis.faces["rolling_eyes"],
        row=2,
    )
    async def probably_not(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        question = await self.aki.answer("probably not")
        self.counter += 1
        self.embed.title = f"Question no. {self.counter}: {question}"
        await interaction.edit_original_message(
            embed=self.embed,
        )

        await self.check_for_progression(interaction=interaction)

    @disnake.ui.button(
        label="Back",
        style=disnake.ButtonStyle.blurple,
        emoji=emojis.arrows["backward"],
        row=2,
    )
    async def back(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        try:
            question = await self.aki.back()
            self.counter -= 1
            self.embed.title = f"Question no. {self.counter}: {question}"
            await interaction.edit_original_message(
                embed=self.embed,
            )
        except akinator.CantGoBackAnyFurther:
            pass

    @disnake.ui.button(
        label="Stop", style=disnake.ButtonStyle.blurple, emoji=emojis.rejected, row=2
    )
    async def stop_(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        await interaction.edit_original_message(
            content="Game Stopped!!", embed=None, view=None
        )
        self.stop()
