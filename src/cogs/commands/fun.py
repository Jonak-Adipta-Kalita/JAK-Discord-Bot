import aiohttp, asyncio, disnake, os, discord_together, credentials, simpleeval, re
import src.embeds as embeds
import src.functions as funcs
import src.files as files
from disnake.ext import commands


class buttons(disnake.ui.View):
    def __init__(self, embed: disnake.Embed, ctx: commands.Context):
        self.super().__init__()

        self.embed = embed
        self.ctx = ctx

        self.operations: list = ["/", "*", "+", "-"]
        self.sup = {
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
        self.norm = {
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
            return f"```yaml\n{content[:-1]}{self.sup[label]}```"
        if content[-1] in self.norm:
            return f"```yaml\n{content}{self.sup[label]}```"
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

        if content[-1] == " " and content[-2] in self.operations:
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
        equation = "".join(
            [k if k not in self.norm else f"**{self.norm[k]}" for k in display]
        )
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

    @commands.Cog.listener()
    async def on_ready(self):
        self.together_control = await discord_together.DiscordTogether(
            credentials.TOKEN
        )

    @commands.group(
        invoke_without_command=True,
        description="Use Discord Together Activities",
        aliases=["discord_together"],
    )
    async def together(self, ctx: commands.Context):
        pass

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

    @together.command(description="Use `Fishing Together` Activity")
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
    async def calculator(self, ctx: commands.Context):
        embed = embeds.calculator_embed()

        await ctx.send(embed=embed, view=buttons(embed, ctx))


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
