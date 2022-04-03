import disnake
import src.core.embeds as embeds
from src.core.bot import JAKDiscordBot
from disnake.ext import commands


class Dropdown(disnake.ui.Select):
    def __init__(self, bot: JAKDiscordBot, author: disnake.Member):
        self.bot = bot
        self.author = author

        super().__init__(
            placeholder="Choose a category!!",
            min_values=1,
            max_values=1,
            options=[
                disnake.SelectOption(
                    label="Moderation Help",
                    value="moderation_help_embed",
                ),
                disnake.SelectOption(label="Games Help", value="games_help_embed"),
                disnake.SelectOption(label="Music Help", value="music_help_embed"),
                disnake.SelectOption(label="Fun Help", value="fun_help_embed"),
                disnake.SelectOption(label="Misc Help", value="misc_help_embed"),
            ],
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        label = interaction.values[0]

        if label == "moderation_help_embed":
            await interaction.response.edit_message(
                embed=await embeds.help_embed(
                    bot=self.bot,
                    author=self.author,
                    command_type="moderation",
                )
            )
        elif label == "games_help_embed":
            await interaction.response.edit_message(
                embed=await embeds.help_embed(
                    bot=self.bot,
                    author=self.author,
                    command_type="games",
                )
            )
        elif label == "music_help_embed":
            await interaction.response.edit_message(
                embed=await embeds.help_embed(
                    bot=self.bot,
                    author=self.author,
                    command_type="music",
                )
            )
        elif label == "fun_help_embed":
            await interaction.response.edit_message(
                embed=await embeds.help_embed(
                    bot=self.bot,
                    author=self.author,
                    command_type="fun",
                )
            )
        elif label == "misc_help_embed":
            await interaction.response.edit_message(
                embed=await embeds.help_embed(
                    bot=self.bot,
                    author=self.author,
                    command_type="misc",
                )
            )


class DropdownView(disnake.ui.View):
    def __init__(self, bot: JAKDiscordBot, author: disnake.Member):
        super().__init__(timeout=300)

        self.bot = bot
        self.author = author

        self.add_item(Dropdown(self.bot, self.author))

    async def interaction_check(self, interaction: disnake.MessageInteraction) -> bool:
        if interaction.author == self.author:
            return True

        await interaction.response.send_message(
            "This is not your Help Menu!!", ephemeral=True
        )
        return False


class Help(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
        self.bot = bot

    @commands.group(invoke_without_command=True, description="Show the Help Menu")
    async def help(
        self, ctx: commands.Context, command: str = None, sub_command: str = None
    ):
        if command:
            cmd = self.bot.get_command(command)
            if cmd:
                if sub_command:
                    sub_cmd = self.bot.get_command(f"{command} {sub_command}")

                    if sub_cmd:
                        await ctx.reply(
                            embed=embeds.commands_help_embed(
                                bot=self.bot,
                                prefixes=self.bot.prefixes,
                                author=ctx.author,
                                command=cmd,
                                sub_command=sub_cmd,
                            )
                        )
                    else:
                        await ctx.reply("Sub Command not found!!")
                else:
                    await ctx.reply(
                        embed=embeds.commands_help_embed(
                            bot=self.bot,
                            prefixes=self.bot.prefixes,
                            author=ctx.author,
                            command=cmd,
                        )
                    )
            else:
                await ctx.reply("Command not found!!")
        else:
            await ctx.reply(
                embed=await embeds.help_embed(
                    bot=self.bot, prefixes=self.bot.prefixes, author=ctx.author
                ),
                view=DropdownView(bot=self.bot, author=ctx.author),
            )

    @help.command(description="Show the Moderation Commands", aliases=["mod"])
    async def moderation(self, ctx: commands.Context):
        await ctx.reply(
            embed=await embeds.help_embed(
                bot=self.bot,
                prefixes=self.bot.prefixes,
                author=ctx.author,
                command_type="moderation",
            )
        )

    @help.command(description="Show the Game Commands")
    async def games(self, ctx: commands.Context):
        await ctx.reply(
            embed=await embeds.help_embed(
                bot=self.bot,
                prefixes=self.bot.prefixes,
                author=ctx.author,
                command_type="games",
            )
        )

    @help.command(description="Show the Music Commands")
    async def music(self, ctx: commands.Context):
        await ctx.reply(
            embed=await embeds.help_embed(
                bot=self.bot,
                prefixes=self.bot.prefixes,
                author=ctx.author,
                command_type="music",
            )
        )

    @help.command(description="Show the Fun Commands")
    async def fun(self, ctx: commands.Context):
        await ctx.reply(
            embed=await embeds.help_embed(
                bot=self.bot,
                prefixes=self.bot.prefixes,
                author=ctx.author,
                command_type="fun",
            )
        )

    @help.command(description="Show the Misc Commands")
    async def misc(self, ctx: commands.Context):
        await ctx.reply(
            embed=await embeds.help_embed(
                bot=self.bot,
                prefixes=self.bot.prefixes,
                author=ctx.author,
                command_type="misc",
            )
        )


def setup(bot: JAKDiscordBot):
    bot.add_cog(Help(bot))
