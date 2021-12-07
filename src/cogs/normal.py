from discord.ext import commands
from dislash import SlashClient, SelectMenu, SelectOption
from src.embeds import games_help_embed, help_embed, moderation_help_embed, music_help_embed, rules_embed
from src.functions import get_prefix

prefix = get_prefix()


class Normal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_blank_value = "\u200b"

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def help(self, ctx: commands.Context):
        msg = await ctx.send(
            embed=help_embed(ctx),
            components=[
                SelectMenu(
                    custom_id="help_command",
                    placeholder="Choose a Category",
                    max_values=1,
                    options=[
                        SelectOption("Moderation Help", "moderation_help_embed"),
                        SelectOption("Games Help", "games_help_embed"),
                        SelectOption("Music Help", "music_help_embed"),
                    ],
                )
            ],
        )

        inter = await msg.wait_for_dropdown()

        if inter.select_menu.selected_options[0].value == "moderation_help_embed":
            await inter.reply(embed=moderation_help_embed(ctx))
        elif inter.select_menu.selected_options[0].value == "games_help_embed":
            await inter.reply(embed=games_help_embed(ctx))
        elif inter.select_menu.selected_options[0].value == "music_help_embed":
            await inter.reply(embed=music_help_embed(ctx))

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def help_games(self, ctx: commands.Context):
        await ctx.send(embed=games_help_embed(ctx))

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def show_rules(self, ctx: commands.Context):
        await ctx.send(embed=rules_embed(self.embed_blank_value))

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Ping: {round(self.bot.latency * 1000)}")


def setup(bot):
    bot.add_cog(Normal(bot))
