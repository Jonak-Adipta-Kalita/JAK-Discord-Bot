import disnake
import src.embeds as embeds
import src.functions as funcs
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
                disnake.SelectOption(
                    label="Discord Together Help",
                    value="discord_together_help_embed",
                ),
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
        elif label == "discord_together_help_embed":
            await interaction.response.send_message(
                embed=embeds.discord_together_help_embed(
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

    @commands.command()
    async def help(self, ctx: commands.Context, type: str = "default"):
        if type == "moderation":
            await ctx.reply(
                embed=embeds.moderation_help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar.url,
                )
            )
        elif type == "games":
            await ctx.reply(
                embed=embeds.games_help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar.url,
                )
            )
        elif type == "music":
            await ctx.reply(
                embed=embeds.music_help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar.url,
                )
            )
        elif type == "fun":
            await ctx.reply(
                embed=embeds.fun_help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar.url,
                )
            )
        elif type == "discord_together":
            await ctx.reply(
                embed=embeds.discord_together_help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar.url,
                )
            )
        elif type == "default":
            await ctx.send(
                embed=embeds.help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar.url,
                ),
                view=DropdownView(ctx=ctx, bot=self.bot),
            )
        elif (
            type != "default"
            and type != "moderation"
            and type != "games"
            and type != "music"
            and type != "fun"
        ):
            return


def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
