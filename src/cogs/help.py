import disnake
import src.core.embeds as embeds
import src.core.functions as funcs
from disnake.ext import commands

prefix = funcs.get_prefix()


class Dropdown(disnake.ui.Select):
    def __init__(self, ctx: commands.Context, bot: commands.Bot):
        self.ctx = ctx
        self.bot = bot

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
            await interaction.response.send_message(
                embed=embeds.moderation_help_embed(
                    ctx=self.ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar.url,
                )
            )
        elif label == "games_help_embed":
            await interaction.response.send_message(
                embed=embeds.games_help_embed(
                    ctx=self.ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar.url,
                )
            )
        elif label == "music_help_embed":
            await interaction.response.send_message(
                embed=embeds.music_help_embed(
                    ctx=self.ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar.url,
                )
            )
        elif label == "fun_help_embed":
            await interaction.response.send_message(
                embed=embeds.fun_help_embed(
                    ctx=self.ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar.url,
                )
            )
        elif label == "misc_help_embed":
            await interaction.response.send_message(
                embed=embeds.misc_help_embed(
                    ctx=self.ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar.url,
                )
            )


class DropdownView(disnake.ui.View):
    def __init__(self, ctx: commands.Context, bot: commands.Bot):
        super().__init__(timeout=None)
        self.add_item(Dropdown(ctx, bot))


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, description="Show the Help Menu")
    async def help(self, ctx: commands.Context):
        await ctx.reply(
            embed=embeds.help_embed(
                ctx=ctx,
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar.url,
            ),
            view=DropdownView(ctx=ctx, bot=self.bot),
        )

    @help.command(description="Show the Moderation Commands", aliases=["mod"])
    async def moderation(self, ctx: commands.Context):
        await ctx.reply(
            embed=embeds.moderation_help_embed(
                ctx=ctx,
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar.url,
            )
        )

    @help.command(description="Show the Game Commands")
    async def games(self, ctx: commands.Context):
        await ctx.reply(
            embed=embeds.games_help_embed(
                ctx=ctx,
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar.url,
            )
        )

    @help.command(description="Show the Music Commands")
    async def music(self, ctx: commands.Context):
        await ctx.reply(
            embed=embeds.music_help_embed(
                ctx=ctx,
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar.url,
            )
        )

    @help.command(description="Show the Fun Commands")
    async def fun(self, ctx: commands.Context):
        await ctx.reply(
            embed=embeds.fun_help_embed(
                ctx=ctx,
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar.url,
            )
        )

    @help.command(description="Show the Misc Commands")
    async def misc(self, ctx: commands.Context):
        await ctx.reply(
            embed=embeds.misc_help_embed(
                ctx=ctx,
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar.url,
            )
        )


def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
